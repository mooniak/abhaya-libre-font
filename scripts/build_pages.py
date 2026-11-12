#!/usr/bin/env python3
"""build_pages.py — assemble the per-font GitHub Pages site from a finished build.

Standalone (stdlib + the vendored proof core), like ``build_manifest.py``: it runs in
each font repo's CI from ``scripts/``. Layout of what it writes to ``--out``:

    index.html          landing page: build details, stage gate, QA, live tester, downloads
    build.json          machine-readable build details (what the canary index is built from)
    fonts/              ttf / otf / woff2 of this build
    proof/              stage-gated proof pages (one per font file)
    reports/            fontspector + diffenator reports, if the build produced them

``scripts/publish_pages.sh`` puts that tree at the Pages root (latest ``dev`` build) and
at ``canary/<sha7>/``, then calls ``--canary-index`` here to regenerate ``canary/index.html``
from ``canary/builds.json`` (the per-commit build log).

    build_pages.py --out _site [--channel canary|dev|release] [--repo .] [--pdf out/proofs-pdf]
    build_pages.py --canary-index <pages-checkout>/canary
"""
from __future__ import annotations

import argparse
import html
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:  # homebase
    from mnik.tools.proofpdf import core
except ImportError:  # vendored: scripts/proof_core.py
    import proof_core as core

FONT_SUFFIXES = (".ttf", ".otf", ".woff2")
SAMPLE = {"Sinh": "බක්මහා ආරේන්දුවක් සුළං දැවැන්තය", "Taml": "தமிழ் எழுத்துருக்கள்"}
LATIN = "The quick brown fox jumps over the lazy dog 0123456789"

_CSS = """
:root { --ink:#111; --mute:#666; --line:#e3e3e3; --bg:#fafafa; }
* { box-sizing:border-box } body { font:15px/1.55 system-ui,sans-serif; color:var(--ink); margin:0; background:#fff }
main { max-width:60rem; margin:0 auto; padding:2.2rem 1.2rem 4rem }
h1 { font-size:2rem; margin:.2rem 0 .3rem } h2 { font-size:1rem; text-transform:uppercase; letter-spacing:.05em;
  color:var(--mute); border-bottom:1px solid var(--line); padding-bottom:.35rem; margin:2.2rem 0 .8rem }
a { color:#0b57d0 } .mute { color:var(--mute) } code, .mono { font-family:Menlo,Consolas,monospace; font-size:.85em }
.chip { display:inline-block; padding:1px 9px; border-radius:99px; font-size:.75rem; font-weight:600;
  text-transform:uppercase; letter-spacing:.04em; background:#eee; vertical-align:middle }
.c-canary { background:#fff3c4 } .c-dev { background:#d6e8ff } .c-release { background:#d3f3dc }
.q-pass { background:#d3f3dc } .q-warn { background:#fff3c4 } .q-fail { background:#fbd5d5 }
dl { display:grid; grid-template-columns:9rem 1fr; gap:.3rem 1rem; margin:0 } dt { color:var(--mute) } dd { margin:0 }
table { border-collapse:collapse; width:100% } th,td { text-align:left; padding:.4rem .6rem; border-bottom:1px solid var(--line) }
th { color:var(--mute); font-weight:500; font-size:.85rem }
textarea { width:100%; min-height:5.5rem; font-size:2.2rem; line-height:1.5; border:1px solid var(--line);
  border-radius:6px; padding:.6rem .8rem; font-family:"Tester",sans-serif }
.warn { background:#fff8e1; border:1px solid #f0d98a; border-radius:6px; padding:.6rem .9rem; font-size:.9rem }
"""


def _h(x) -> str:
    return html.escape("" if x is None else str(x))


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def gather(repo: Path, channel: str | None) -> dict:
    """Build details from the manifest fontstatus.json, falling back to the CI env."""
    st = _read_json(repo / "out" / "fontstatus.json")
    pkg = _read_json(repo / "fontpackage.json")
    b = st.get("build") or {}
    env = os.environ
    sha = b.get("commit") or env.get("GITHUB_SHA") or ""
    ch = channel or b.get("channel") or env.get("MNIK_CHANNEL") or "canary"
    qa = st.get("qa") or {}
    stage = ((st.get("coverage") or {}).get("sinhala_design_stage")) or None
    repository = b.get("repository") or env.get("GITHUB_REPOSITORY") or ""
    return {
        "id": st.get("id") or pkg.get("id") or repo.resolve().name,
        "family": pkg.get("name") or st.get("id") or repo.resolve().name,
        "scripts": pkg.get("scripts") or [],
        "version": st.get("version"),
        "channel": ch,
        "commit": sha or None,
        "commit_short": (b.get("commit_short") or sha[:7]) or None,
        "ref_name": b.get("ref_name") or env.get("GITHUB_REF_NAME"),
        "repository": repository or None,
        "run_url": b.get("run_url") or (f"{env.get('GITHUB_SERVER_URL', 'https://github.com')}/{repository}/actions/runs/{env.get('GITHUB_RUN_ID')}"
                                        if repository and env.get("GITHUB_RUN_ID") else None),
        "actor": b.get("actor") or env.get("GITHUB_ACTOR"),
        "generated_at": st.get("generated_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "qa": {k: qa.get(k) for k in ("profile", "verdict", "pass_rate", "counts", "total_checks")} if qa else None,
        "stage": stage,
        "files": [{k: f.get(k) for k in ("path", "format", "bytes", "sha256", "style", "kind")}
                  for f in (st.get("files") or [])],
    }


def copy_fonts(repo: Path, out: Path) -> list[Path]:
    dest = out / "fonts"
    dest.mkdir(parents=True, exist_ok=True)
    got = []
    for p in sorted((repo / "fonts").rglob("*")):
        if p.is_file() and p.suffix.lower() in FONT_SUFFIXES:
            shutil.copy2(p, dest / p.name)
            got.append(dest / p.name)
    return got


def copy_reports(repo: Path, out: Path) -> dict[str, str]:
    links = {}
    for src, name, entry in (("out/fontspector", "fontspector", "fontspector-report.html"),
                             ("out/proof", "diffenator", "diffenator2-report.html")):
        d = repo / src
        if d.is_dir():
            shutil.copytree(d, out / "reports" / name, dirs_exist_ok=True)
            idx = out / "reports" / name / entry
            if not idx.exists():
                htmls = sorted((out / "reports" / name).glob("*.html"))
                idx = htmls[0] if htmls else None
            if idx:
                links[name] = f"reports/{name}/{quote(idx.name)}"
    return links


def _qa_chip(qa: dict | None) -> str:
    if not qa:
        return '<span class="mute">no QA report</span>'
    v = (qa.get("verdict") or "").lower()
    cls = {"pass": "q-pass", "warn": "q-warn"}.get(v, "q-fail" if v else "")
    c = qa.get("counts") or {}
    detail = ", ".join(f"{c[k]} {k}" for k in ("FAIL", "WARN", "PASS") if k in c)
    rate = f" · {qa['pass_rate']}% pass" if qa.get("pass_rate") is not None else ""
    return f'<span class="chip {cls}">{_h(v or "n/a")}</span> <span class="mute">{_h(detail)}{rate} · profile {_h(qa.get("profile"))}</span>'


def _counts(st: dict) -> str:
    if st.get("cumulative") in (None, "?") or st.get("total") in (None, "?"):
        return ""
    return f'<span class="mute">({_h(st["cumulative"])}/{_h(st["total"])} glyph forms)</span>'


def render_index(info: dict, fonts: list[Path], proofs: list[tuple[str, str]], reports: dict[str, str]) -> str:
    sample = next((SAMPLE[s] for s in info["scripts"] if s in SAMPLE), LATIN)
    tester = next((f for f in fonts if f.suffix == ".woff2"), fonts[0] if fonts else None)
    face = ""
    if tester:
        fmt = "woff2" if tester.suffix == ".woff2" else "opentype" if tester.suffix == ".otf" else "truetype"
        face = f'@font-face{{font-family:"Tester";src:url("fonts/{quote(tester.name)}") format("{fmt}")}}'
    repo = info.get("repository")
    sha = info.get("commit_short")
    commit = (f'<a href="https://github.com/{_h(repo)}/commit/{_h(info["commit"])}"><code>{_h(sha)}</code></a>'
              if repo and info.get("commit") else (f"<code>{_h(sha)}</code>" if sha else "—"))
    st = info.get("stage")
    stage = (f'<b>{_h(st["n"])}</b> — {_h(st["name"])} {_counts(st)}'
             if st else '<span class="mute">n/a</span>')
    rows = [("Channel", f'<span class="chip c-{_h(info["channel"])}">{_h(info["channel"])}</span>'),
            ("Version", f'<code>{_h(info.get("version") or "—")}</code>'),
            ("Commit", f'{commit} on <code>{_h(info.get("ref_name") or "—")}</code>'),
            ("Built", f'{_h(info["generated_at"])}' + (f' by {_h(info["actor"])}' if info.get("actor") else "")),
            ("Design stage", stage),
            ("QA", _qa_chip(info.get("qa")))]
    if info.get("run_url"):
        rows.append(("CI run", f'<a href="{_h(info["run_url"])}">{_h(info["run_url"].rsplit("/", 1)[-1])}</a>'))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    ftab = "".join(f'<tr><td><a href="fonts/{quote(f.name)}">{_h(f.name)}</a></td><td>{f.stat().st_size / 1024:.0f} KB</td></tr>'
                   for f in fonts)
    links = [(f'proof/{quote(Path(p).name)}', f"Type proof — {n}") for n, p in proofs]
    links += [(href, label) for label, href in (("Fontspector QA report", reports.get("fontspector")),
                                                 ("Diffenator report", reports.get("diffenator"))) if href]
    if repo:
        links += [(f"https://github.com/{repo}", "Source repository"),
                  (f"https://github.com/{repo}/releases", "Releases")]
    ltxt = "".join(f'<li><a href="{_h(h)}">{_h(t)}</a></li>' for h, t in links)
    warn = ('<p class="warn"><b>Canary build — may be broken.</b> This is the latest build of the <code>dev</code> branch, '
            'cut automatically. It is not a release.</p>' if info["channel"] == "canary" else "")
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_h(info["family"])} — {_h(info["channel"])} build</title><style>{face}{_CSS}</style></head><body><main>
<p class="mute" style="margin:0"><a href="https://src.mooniak.com/">src.mooniak.com</a> · <a href="canary/">canary build log</a></p>
<h1>{_h(info["family"])}</h1>{warn}
<h2>Build</h2><dl>{dl}</dl>
<h2>Try it</h2><textarea spellcheck="false">{_h(sample)}</textarea>
<h2>Proofs &amp; reports</h2><ul>{ltxt}</ul>
<h2>Fonts</h2><table><tr><th>File</th><th>Size</th></tr>{ftab}</table>
</main></body></html>"""


def build(repo: Path, out: Path, channel: str | None, pdf_dir: Path | None = None) -> dict:
    info = gather(repo, channel)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    fonts = copy_fonts(repo, out)
    reports = copy_reports(repo, out)
    proofs: list[tuple[str, str]] = []
    statics = core.font_files(repo)
    if statics:
        pages = core.build_proof_pages(statics, out / "proof", out / "fonts",
                                       family=info["family"], channel=info["channel"], build=info)
        proofs = [(pg.stem, str(pg.html_path)) for pg in pages]
        g = pages[0].gate
        if pdf_dir is not None and g.pdf:
            # development stage dev/release -> also a printable book per font
            for pg in pages:
                core.render_pdf(pg.html_path, pdf_dir / f"{pg.stem}-proof.pdf")
        info["proof_gate"] = {"stage": g.stage, "gated": g.gated, "shown": g.shown,
                              "withheld": [list(w) for w in g.withheld], "missing_for_next": g.next_gaps}
        if info["stage"] is None and g.stage is not None:
            info["stage"] = {"n": g.stage, "name": g.stage_name, "cumulative": "?", "total": "?"}
    (out / "build.json").write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "index.html").write_text(render_index(info, fonts, proofs, reports), encoding="utf-8")
    return info


def canary_index(canary_dir: Path) -> None:
    """(Re)write canary/index.html from canary/builds.json, newest first."""
    builds = json.loads((canary_dir / "builds.json").read_text(encoding="utf-8"))
    builds.sort(key=lambda b: b.get("generated_at") or "", reverse=True)
    rows = []
    for i, b in enumerate(builds):
        short = b.get("commit_short") or "?"
        present = (canary_dir / short).is_dir()
        link = f'<a href="{_h(short)}/">{_h(short)}</a>' if present else f"{_h(short)} <span class='mute'>(pruned)</span>"
        st = b.get("stage")
        q = b.get("qa") or {}
        v = (q.get("verdict") or "").lower()
        qcls = {"pass": "q-pass", "warn": "q-warn"}.get(v, "q-fail" if v else "")
        run = f'<a href="{_h(b["run_url"])}">run</a>' if b.get("run_url") else ""
        rows.append(f'<tr><td>{link}{" <span class=chip>latest</span>" if i == 0 else ""}</td>'
                    f'<td><code>{_h(b.get("version") or "—")}</code></td>'
                    f'<td>{_h(b.get("generated_at") or "")}</td>'
                    f'<td>{_h(st["n"]) if st else "—"}</td>'
                    f'<td><span class="chip {qcls}">{_h(v or "n/a")}</span></td><td>{run}</td></tr>')
    fam = _h(builds[0].get("family")) if builds else ""
    (canary_dir / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{fam} — canary builds</title><style>{_CSS}</style></head><body><main>
<p class="mute" style="margin:0"><a href="../">← {fam} (latest)</a></p>
<h1>{fam} — canary builds</h1>
<p class="warn"><b>May be broken.</b> One entry per push to <code>dev</code>. Only the most recent builds keep their files.</p>
<table><tr><th>Commit</th><th>Version</th><th>Built</th><th>Design stage</th><th>QA</th><th>CI</th></tr>{"".join(rows)}</table>
</main></body></html>""", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path)
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--channel", choices=["canary", "dev", "release"])
    ap.add_argument("--pdf", type=Path, metavar="DIR",
                    help="also render PDF proof books here, if the channel's depth calls for them (dev/release; needs Playwright)")
    ap.add_argument("--canary-index", type=Path, metavar="DIR")
    a = ap.parse_args()
    if a.canary_index:
        canary_index(a.canary_index)
        return 0
    if not a.out:
        ap.error("--out is required")
    info = build(a.repo, a.out, a.channel, a.pdf)
    g = info.get("proof_gate") or {}
    print(f"build_pages: {info['family']} {info.get('version')} [{info['channel']}] -> {a.out} "
          f"(stage {g.get('stage')}, {len(g.get('shown', []))} section(s) shown, {len(g.get('withheld', []))} withheld)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
