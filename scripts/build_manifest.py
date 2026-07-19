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
``mooniak-font-tools/mnik/tools/manifest/build_manifest.py``; ``mnik manifest`` imports
and runs it for local/dev parity, and a copy is synced into each font repo's
``scripts/`` by the project template so CI can run it self-contained.

Reads (all relative to the repo root, the current directory by default):
  fontpackage.json                       -> id, scripts (Sinhala gate for coverage)
  fonts/{variable,ttf,otf,webfonts}/*    -> built binaries (hash, size, names, axes)
  out/fontspector/fontspector-report.md  -> QA verdict, if a report is present
  environment (GITHUB_*)                  -> channel, commit, ref, run metadata
  <own dir>/sinhala_coverage.py + stages.json -> Sinhala design-stage coverage, if present

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
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "mooniak-fontstatus/v1"
FONT_EXTS = (".ttf", ".otf", ".woff2", ".woff")
# fontspector report severities, worst-first (matches mnik.tools.qa.SEVERITIES).
SEVERITIES = ["ERROR", "FAIL", "WARN", "SKIP", "INFO", "PASS", "DEBUG"]

# OpenFV (https://github.com/openfv/openfv): name ID 5 is "<Version>; <Status/State>; ...".
# Version is MAJOR.MINOR with MINOR a 3-digit zero-padded number; MAJOR 0 == pre-production.
_OPENFV_VER = re.compile(r"(\d{1,3})\.(\d{3})")
# A `*-dev` / `*-dev.N` git tag is the `dev` (pre-release) channel; any other tag is `release`.
_DEV_TAG = re.compile(r"-dev(\.\d+)?$")


def _parse_openfv(name5: str | None) -> dict | None:
    """Parse an OpenFV name ID 5 string into its version + dev/release status.

    Understands the spec's forms: ``Version 1.001``, ``Version 1.001; DEV``,
    ``Version 1.001; [abcd123]-dev``, ``1.001; [abcd123]-dev; build metadata``.
    ``status``/``source`` stay None until CI stamps the name table (Phase 3).
    """
    if not name5:
        return None
    parts = [p.strip() for p in name5.split(";")]
    m = _OPENFV_VER.search(parts[0])
    if not m:
        return None
    major, minor = int(m.group(1)), m.group(2)
    status, source = None, None
    for seg in parts[1:]:
        low = seg.lower()
        if "release" in low:
            status = "release"
        elif "dev" in low:
            status = "dev"
        b = re.search(r"\[([^\]]+)\]", seg)
        if b:
            source = b.group(1)
    return {
        "version": f"{major}.{minor}",
        "major": major,
        "minor": minor,
        "status": status,           # dev | release | None (name table not yet stamped)
        "source": source,           # source-state label from [ … ], if any
        "prerelease": major == 0,   # OpenFV: MAJOR 0 == pre-production (cannot be a release)
    }


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
        if name is not None:
            ofv = _parse_openfv(name.getDebugName(5))
            if ofv:
                facts["openfv"] = ofv
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


def _font_cmap(path: Path) -> set[int]:
    """Codepoints the font's cmap resolves to a glyph (best-effort)."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return set()
    try:
        font = TTFont(str(path), fontNumber=0, lazy=True)
    except Exception:
        return set()
    try:
        return set(font.getBestCmap().keys())
    except Exception:
        return set()
    finally:
        font.close()


def _font_glyph_order(path: Path) -> set[str]:
    """The font's raw glyph-order names (best-effort)."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return set()
    try:
        font = TTFont(str(path), fontNumber=0, lazy=True)
    except Exception:
        return set()
    try:
        return set(font.getGlyphOrder())
    except Exception:
        return set()
    finally:
        font.close()


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
    """Map the CI trigger to an OpenFV-aligned channel: canary | dev | release.

    - a ``*-dev`` / ``*-dev.N`` tag  -> ``dev``     (a cut pre-release; ``Version X.YYY; DEV``)
    - any other tag                  -> ``release`` (curated, stable; bare ``Version X.YYY``)
    - any untagged CI build          -> ``canary``  (bleeding edge; ``X.YYY; [<sha>]-dev``)
    - no CI env (a local run)        -> ``local``   (not a published channel)

    (``nightly`` was retired: canary already serves the rolling bleeding edge.)
    """
    if override:
        return override
    if env.get("MNIK_CHANNEL"):
        return env["MNIK_CHANNEL"]
    if not env.get("GITHUB_ACTIONS"):
        return "local"
    if env.get("GITHUB_REF_TYPE") == "tag":
        return "dev" if _DEV_TAG.search(env.get("GITHUB_REF_NAME") or "") else "release"
    return "canary"


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


# ── Coverage: Sinhala design-stage progress (Phase 4), gated on fontpackage.json's `scripts` ──
def _sinhala_coverage(repo: Path, files: list[dict]) -> dict | None:
    """coverage.sinhala_design_stage for Sinhala fonts; None if not applicable/available.

    Delegates to the sibling ``sinhala_coverage`` module (also mnik-free, reads its own
    sibling ``stages.json`` off disk -- no network). See tools/sinhala-design-stages/ for
    the model's authoring source and docs/tooling-roadmap.md §4 for the design.
    """
    fp = repo / "fontpackage.json"
    scripts: list = []
    if fp.is_file():
        try:
            scripts = json.loads(fp.read_text(encoding="utf-8")).get("scripts") or []
        except (json.JSONDecodeError, OSError):
            scripts = []
    if "Sinh" not in scripts:
        return None
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import sinhala_coverage
    except ImportError:
        return None
    font_paths = [repo / f["path"] for f in files]
    try:
        return sinhala_coverage.compute(font_paths, _font_cmap, _font_glyph_order)
    except Exception:
        return None


def _modal_version(files: list[dict]) -> str | None:
    versions = [f["version"] for f in files if f.get("version")]
    if not versions:
        return None
    return max(set(versions), key=versions.count)


def _openfv(files: list[dict]) -> dict | None:
    """The families' OpenFV version/status (from the first file that carries one)."""
    for f in files:
        if f.get("openfv"):
            return f["openfv"]
    return None


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
    sd = _sinhala_coverage(repo, files)
    return {
        "schema": SCHEMA,
        "id": font_id,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "build": build_context(env, channel_override),
        "version": _modal_version(files),
        "openfv": _openfv(files),  # parsed OpenFV version/status; null until CI stamps name ID 5
        "files": files,
        "qa": _qa_status(repo),
        "coverage": {"sinhala_design_stage": sd} if sd else {},
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
