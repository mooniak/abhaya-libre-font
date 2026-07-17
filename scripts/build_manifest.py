#!/usr/bin/env python3
"""build_manifest.py — emit ``fontstatus.json``, a per-build computed-fact manifest.

Part of Phase 2 of the tooling roadmap (``docs/tooling-roadmap.md``): the homebase
stops *scanning* 57 local checkouts to derive truth; instead each repo *publishes*
its own truth from CI, and the homebase only aggregates.

Two files, cleanly separated:
  - ``fontpackage.json``  — declared intent (hand-edited, tracked): name, license,
    designers, channels you *intend* to publish, maturity.
  - ``fontstatus.json``   — computed fact (this file, emitted per build, never
    committed): version, channel, commit sha, built files + hashes, QA verdict,
    glyphset coverage, timestamps.

Standalone by design: depends only on fontTools (already pinned in every repo's
``requirements.txt``) and the standard library, so it runs in CI without the mnik
homebase checked out. The canonical copy lives at
``font-directory/mnik/tools/manifest/build_manifest.py``; ``mnik manifest`` imports
and runs it for local/dev parity, and a copy is synced into each font repo's
``scripts/`` by the project template so CI can run it self-contained.

Reads (all relative to the repo root, the current directory by default):
  fontpackage.json                       -> id (the only declared field consumed)
  fonts/{variable,ttf,otf,webfonts}/*    -> built binaries (hash, size, names, axes)
  out/fontspector/fontspector-report.md  -> QA verdict, if a report is present
  environment (GITHUB_*)                  -> channel, commit, ref, run metadata

Writes:
  out/fontstatus.json  (path overridable with --out)

Usage:
  python3 scripts/build_manifest.py                 # in a repo root, after `make build test`
  python3 build_manifest.py --repo path/to/repo --channel dev --out /tmp/x.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "mooniak-fontstatus/v1"
FONT_EXTS = (".ttf", ".otf", ".woff2", ".woff")
# fontspector report severities, worst-first (matches mnik.tools.qa.SEVERITIES).
SEVERITIES = ["ERROR", "FAIL", "WARN", "SKIP", "INFO", "PASS", "DEBUG"]


# ── QA: parse the fontspector ghmarkdown summary the `make test` step already writes ──
def _parse_fontspector_md(md_path: Path) -> dict | None:
    """Parse fontspector's ghmarkdown summary table into {SEVERITY: count}.

    Mirrors ``mnik.tools.qa.parse_report`` so a manifest's QA counts match the
    homebase's fontspector.json exactly. Kept self-contained (no mnik import) so
    this file runs in CI on its own.
    """
    try:
        lines = md_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None
    header_idx, keys = None, []
    for i, line in enumerate(lines):
        if "|" not in line:
            continue
        up = line.upper()
        if "PASS" in up and "FAIL" in up and "WARN" in up:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            mapped = [next((s for s in SEVERITIES if s in c.upper()), None) for c in cells]
            if any(mapped):
                header_idx, keys = i, mapped
                break
    if header_idx is None:
        return None
    for line in lines[header_idx + 1:]:
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue
        nums = [int(c.replace(",", "")) if c.replace(",", "").isdigit() else None for c in cells]
        if any(n is not None for n in nums):
            summary: dict[str, int] = {}
            for key, n in zip(keys, nums):
                if key and n is not None:
                    summary[key] = summary.get(key, 0) + n
            return summary or None
    return None


def _qa_status(repo: Path, profile: str = "googlefonts") -> dict:
    """Read the fontspector report under out/ and reduce it to a verdict."""
    hits = sorted((repo / "out").rglob("fontspector-report.md")) if (repo / "out").is_dir() else []
    if not hits:
        return {"available": False}
    counts = _parse_fontspector_md(hits[0])
    if not counts:
        return {"available": False}
    total = sum(counts.get(s, 0) for s in SEVERITIES)
    checked = total - counts.get("SKIP", 0) - counts.get("DEBUG", 0)
    fail = counts.get("ERROR", 0) + counts.get("FAIL", 0)
    warn = counts.get("WARN", 0)
    verdict = "fail" if fail else ("warn" if warn else "pass")
    return {
        "available": True,
        "profile": profile,
        "counts": {s: counts[s] for s in SEVERITIES if s in counts},
        "total_checks": total,
        "pass_rate": round(100 * counts.get("PASS", 0) / checked) if checked else None,
        "verdict": verdict,
    }


# ── Fonts: hash every built binary and read its facts from the font itself ──
def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _font_facts(path: Path) -> dict:
    """Family/style/version/axes read from the font binary (best-effort)."""
    facts: dict = {}
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return facts
    try:
        font = TTFont(str(path), fontNumber=0, lazy=True)
    except Exception:
        return facts
    try:
        name = font["name"] if "name" in font else None
        if name is not None:
            fam = name.getDebugName(16) or name.getDebugName(1)
            sub = name.getDebugName(17) or name.getDebugName(2)
            if fam:
                facts["family"] = fam
            if sub:
                facts["style"] = sub
        if "head" in font:
            facts["version"] = f"{font['head'].fontRevision:.3f}"
        elif name is not None and name.getDebugName(5):
            facts["version"] = name.getDebugName(5)
        if "fvar" in font:
            facts["kind"] = "variable"
            facts["axes"] = [
                {"tag": a.axisTag, "min": a.minValue, "def": a.defaultValue, "max": a.maxValue}
                for a in font["fvar"].axes
            ]
        else:
            facts["kind"] = "static"
    except Exception:
        pass
    finally:
        font.close()
    return facts


def _fmt(path: Path) -> str:
    ext = path.suffix.lower().lstrip(".")
    return ext or "unknown"


def collect_files(repo: Path) -> list[dict]:
    fonts_root = repo / "fonts"
    if not fonts_root.is_dir():
        return []
    out: list[dict] = []
    for path in sorted(fonts_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in FONT_EXTS:
            continue
        rec = {
            "path": path.relative_to(repo).as_posix(),
            "format": _fmt(path),
            "bytes": path.stat().st_size,
            "sha256": _sha256(path),
        }
        rec.update(_font_facts(path))
        out.append(rec)
    return out


# ── Build context: channel + commit + run metadata from the CI environment ──
def _derive_channel(env: dict, override: str | None) -> str:
    if override:
        return override
    if env.get("MNIK_CHANNEL"):
        return env["MNIK_CHANNEL"]
    if env.get("GITHUB_REF_TYPE") == "tag":
        return "release"
    if env.get("GITHUB_EVENT_NAME") == "schedule":
        return "nightly"
    ref_name = env.get("GITHUB_REF_NAME") or ""
    if ref_name in ("dev",):
        return "dev"
    if ref_name in ("main", "master"):
        return "main"
    return ref_name or "local"


def build_context(env: dict, channel_override: str | None) -> dict:
    sha = env.get("GITHUB_SHA") or ""
    repo_slug = env.get("GITHUB_REPOSITORY") or ""
    run_id = env.get("GITHUB_RUN_ID") or ""
    server = env.get("GITHUB_SERVER_URL") or "https://github.com"
    on_ci = bool(env.get("GITHUB_ACTIONS"))
    ctx = {
        "channel": _derive_channel(env, channel_override),
        "ref": env.get("GITHUB_REF") or None,
        "ref_name": env.get("GITHUB_REF_NAME") or None,
        "ref_type": env.get("GITHUB_REF_TYPE") or None,
        "event": env.get("GITHUB_EVENT_NAME") or None,
        "commit": sha or None,
        "commit_short": sha[:7] if sha else None,
        "repository": repo_slug or None,
        "run_id": run_id or None,
        "run_number": env.get("GITHUB_RUN_NUMBER") or None,
        "run_url": f"{server}/{repo_slug}/actions/runs/{run_id}" if (repo_slug and run_id) else None,
        "actor": env.get("GITHUB_ACTOR") or None,
        "source": "github-actions" if on_ci else "local",
    }
    return ctx


def _modal_version(files: list[dict]) -> str | None:
    versions = [f["version"] for f in files if f.get("version")]
    if not versions:
        return None
    return max(set(versions), key=versions.count)


def build_manifest(repo: Path, channel_override: str | None = None,
                   env: dict | None = None) -> dict:
    env = env if env is not None else dict(os.environ)
    repo = repo.resolve()
    fp = repo / "fontpackage.json"
    font_id = None
    if fp.is_file():
        try:
            font_id = json.loads(fp.read_text(encoding="utf-8")).get("id")
        except (json.JSONDecodeError, OSError):
            font_id = None
    if not font_id:
        # Fall back to the directory slug, dropping a trailing -font.
        font_id = repo.name[:-5] if repo.name.endswith("-font") else repo.name

    files = collect_files(repo)
    return {
        "schema": SCHEMA,
        "id": font_id,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "build": build_context(env, channel_override),
        "version": _modal_version(files),
        "files": files,
        "qa": _qa_status(repo),
        "coverage": {},  # Phase 4 populates this via lanka-glyphsets; empty for now.
    }


def emit(repo: Path, out_path: Path | None = None, channel_override: str | None = None,
         env: dict | None = None) -> tuple[dict, Path]:
    """Build the manifest and write it to disk; return (manifest, path)."""
    manifest = build_manifest(repo, channel_override=channel_override, env=env)
    out_path = out_path or (repo / "out" / "fontstatus.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest, out_path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Emit fontstatus.json for a font repo.")
    ap.add_argument("--repo", default=".", help="repo root (default: current directory)")
    ap.add_argument("--out", default=None, help="output path (default: <repo>/out/fontstatus.json)")
    ap.add_argument("--channel", default=None, help="override the derived channel")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    out_path = Path(args.out) if args.out else None
    manifest, written = emit(repo, out_path=out_path, channel_override=args.channel)
    b = manifest["build"]
    qa = manifest["qa"]
    print(f"{manifest['id']}: {len(manifest['files'])} file(s), "
          f"channel={b['channel']}, version={manifest['version']}, "
          f"qa={qa.get('verdict', 'n/a')} -> {written}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
