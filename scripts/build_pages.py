#!/usr/bin/env python3
"""build_pages.py — assemble the per-font GitHub Pages site from a finished build.

Standalone (stdlib + the vendored proof core), like ``build_manifest.py``: it runs in
each font repo's CI from ``scripts/``. Layout of what it writes to ``--out``:

    index.html          landing page: build details, stage gate, QA, live tester (+ downloads, dev/release only)
    build.json          machine-readable build details (what the canary index is built from)
    fonts/              the fonts the proof pages and tester load. Canary builds: woff2 only, never
                        linked. dev/release builds: every ttf / otf / woff2, listed for download.
    proof/              stage-gated proof pages (one per font file; variable font preferred over statics)
    reports/            fontspector + diffenator reports, if the build produced them

Canary builds are test documents, not releases, so they offer **no font downloads**: no links, no
"Fonts" nav entry, and no desktop-installable files (ttf/otf) anywhere in the site. The pages still
have to load a font to draw proofs, so a woff2 is served for that -- a browser cannot render a font
it was not sent -- but nothing points at it, and ``assert_no_installable_fonts`` fails the build if
a ttf/otf/ttc/eot slips through (a report that bundles its own, say).

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


def _core():
    """The proof engine, imported on demand: --canary-index runs under the CI runner's bare
    system python3 (no PyYAML / fontTools), so it must not pull the engine in at import time."""
    try:  # homebase
        from mnik.tools.proofpdf import core
    except ImportError:  # vendored: scripts/proof_core.py
        import proof_core as core
    return core

FONT_SUFFIXES = (".ttf", ".otf", ".woff2")
# Files a user can install on a desktop (or that make the site a font mirror). Canary builds ship none.
INSTALLABLE_SUFFIXES = (".ttf", ".otf", ".ttc", ".otc", ".woff", ".eot")
# Only these channels list fonts for download. Anything else -- canary, or a channel we do not
# recognise -- is a test build: fail closed.
DOWNLOAD_CHANNELS = ("dev", "release")
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


def offers_downloads(channel: str | None) -> bool:
    return channel in DOWNLOAD_CHANNELS


def copy_fonts(repo: Path, out: Path) -> list[Path]:
    """Every font of the build -> out/fonts/ (dev/release: these are the downloads)."""
    dest = out / "fonts"
    dest.mkdir(parents=True, exist_ok=True)
    got = []
    for p in sorted((repo / "fonts").rglob("*")):
        if p.is_file() and p.suffix.lower() in FONT_SUFFIXES:
            shutil.copy2(p, dest / p.name)
            got.append(dest / p.name)
    return got


def to_woff2(src: Path, dest_dir: Path) -> Path:
    """``src`` as <stem>.woff2 in ``dest_dir`` (needs fontTools + brotli; both are in the font stack)."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{src.stem}.woff2"
    if src.suffix.lower() == ".woff2":
        if src.resolve() != dest.resolve():
            shutil.copy2(src, dest)
        return dest
    from fontTools.ttLib import TTFont
    tt = TTFont(str(src))
    tt.flavor = "woff2"
    tt.save(str(dest))
    tt.close()
    return dest


def web_fonts(sources: list[Path], dest_dir: Path) -> list[Path]:
    """Canary: only the fonts the proofs/tester need, as woff2. No ttf/otf, no extras."""
    return [to_woff2(s, dest_dir) for s in sources]


def _woff2_in_place(root: Path) -> None:
    """Replace every ttf/otf under ``root`` with a woff2 and re-point the HTML that loads it.
    (diff3proof's report drops old-*.ttf / new-*.ttf beside its page and loads them by name.)"""
    renamed: dict[str, str] = {}
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in (".ttf", ".otf", ".woff"):
            renamed[p.name] = to_woff2(p, p.parent).name
            p.unlink()
    if not renamed:
        return
    for page in root.rglob("*.htm*"):
        text = page.read_text(encoding="utf-8", errors="surrogateescape")
        new = text
        for old, nw in renamed.items():
            new = new.replace(old, nw).replace(quote(old), quote(nw))
        if new != text:
            page.write_text(new, encoding="utf-8", errors="surrogateescape")


def assert_no_installable_fonts(out: Path) -> None:
    """Canary guard: the finished site must hold no desktop-installable font file. Fails the build."""
    bad = sorted(str(p.relative_to(out)) for p in out.rglob("*")
                 if p.is_file() and p.suffix.lower() in INSTALLABLE_SUFFIXES)
    if bad:
        raise SystemExit("build_pages: refusing to publish a canary site that carries installable fonts: "
                         + ", ".join(bad))


def copy_assets(out: Path) -> None:
    """Site assets (the Mooniak logo) -> out/assets/. Lives beside this script, in homebase and vendored."""
    src = Path(__file__).resolve().parent / "assets"
    if src.is_dir():
        shutil.copytree(src, out / "assets", dirs_exist_ok=True)


def copy_reports(repo: Path, out: Path, web_only: bool = False) -> dict[str, str]:
    """``web_only``: any ttf/otf a report bundles (the diffenator report carries old/new fonts)
    is converted to woff2 so the site never serves an installable font."""
    links = {}
    for src, name, entry in (("out/fontspector", "fontspector", "fontspector-report.html"),
                             ("out/proof", "diffenator", "diffenator2-report.html")):
        d = repo / src
        if d.is_dir():
            shutil.copytree(d, out / "reports" / name, dirs_exist_ok=True)
            if web_only:
                _woff2_in_place(out / "reports" / name)
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


# ── site furniture: header + nav, the standing warning, about text, footer ───────────────
WARNING = ("<b>Test documents &mdash; work in progress.</b> These are automatically generated test pages "
           "for open-source fonts that are still being developed. They are <b>not releases</b>, can be wrong "
           "or broken, and change with every commit. <b>Please do not file issues in the GitHub trackers based "
           "on these pages</b> unless you know what you are doing and are part of the "
           "<b>Mooniak Circle</b> programme.")

ABOUT = ("<p><a href=\"https://mooniak.com/\">Mooniak</a> designs and develops typefaces for Sinhala, Tamil and Latin "
         "scripts, many of them open source. Each font lives in its own repository; every time its "
         "<code>dev</code> branch changes, the font is rebuilt and tested automatically, and the result is published "
         "here so designers and testers can see where it stands.</p>"
         "<p>Each build is checked for quality (fontspector) and measured against a "
         "<b>design-stage model</b>: stage 0&ndash;10, from the first drawn letters to the full conjunct and "
         "long-tail character set. The proof pages only show the text a font has <i>earned</i> by its stage, so an "
         "early font is not judged on glyphs it does not have yet.</p>")

_CHIP_CSS = """
.chip { display:inline-block; padding:1px 9px; border-radius:99px; font-size:.75rem; font-weight:600;
  text-transform:uppercase; letter-spacing:.04em; background:#eee; vertical-align:middle }
.c-canary { background:#fff3c4 } .c-dev { background:#d6e8ff } .c-release { background:#d3f3dc }
"""

_CHROME_CSS = """
.site-head { display:flex; align-items:center; gap:1.2rem; flex-wrap:wrap; padding:.9rem 1.2rem;
  border-bottom:1px solid #e3e3e3; background:#fff; font:14px system-ui,sans-serif }
.site-head .logo img { height:52px; width:auto; display:block }
.site-head .where { color:#666; font-size:.8rem; line-height:1.3 } .site-head .where b { color:#111; font-size:.95rem; display:block }
.site-nav { margin-left:auto; display:flex; gap:.2rem; flex-wrap:wrap }
.site-nav a { color:#222; text-decoration:none; padding:.35rem .7rem; border-radius:6px }
.site-nav a:hover { background:#f0f0f0 } .site-nav a.on { background:#111; color:#fff }
.test-warning { margin:0; padding:.7rem 1.2rem; background:#fff3cd; border-bottom:2px solid #e0a800; color:#4d3b00;
  font:13.5px/1.5 system-ui,sans-serif }
.test-warning::before { content:"\\26A0\\FE0F\\00a0" }
.site-foot { max-width:60rem; margin:3rem auto 2rem; padding:1rem 1.2rem 0; border-top:1px solid #e3e3e3;
  color:#666; font:12.5px/1.6 system-ui,sans-serif }
@media print { .site-head, .site-foot { display:none } .test-warning { border:1px solid #e0a800 } }
"""


def _site_base(repository: str | None) -> str | None:
    """Absolute path prefix of this repo's Pages site: /<repo-name>/ (org Pages, CNAME src.mooniak.com)."""
    return f"/{repository.split('/')[-1]}/" if repository else None


def chrome(info: dict, root: str, active: str = "") -> str:
    """Header + nav + warning for a page. ``root`` = relative path from the page to *this build's*
    root ('' for index.html, '../' for proof/). 'Latest' and 'Canary builds' use the absolute
    /<repo>/ path so they work from canary/<sha7>/ copies too; with no repository known (a local
    preview) they fall back to relative links."""
    repo = info.get("repository")
    base = _site_base(repo)
    latest = base or (root or "./")
    canary = (base + "canary/") if base else (root + "canary/")
    items = [("home", "Overview", (root or "./")),
             ("proofs", "Proofs", f"{root}index.html#proofs"),
             ("reports", "Reports", f"{root}index.html#reports")]
    if offers_downloads(info.get("channel")):          # canary pages never link to font files
        items.append(("fonts", "Fonts", f"{root}index.html#fonts"))
    items += [("latest", "Latest build", latest),
              ("canary", "Canary builds", canary)]
    if repo:
        items.append(("src", "Source", f"https://github.com/{repo}"))
    items.append(("mooniak", "mooniak.com", "https://mooniak.com/"))
    nav = "".join(f'<a href="{_h(h)}"{" class=on" if k == active else ""}>{_h(t)}</a>' for k, t, h in items)
    return (f'<header class="site-head"><a class="logo" href="https://mooniak.com/">'
            f'<img src="{_h(root)}assets/mooniak-logo.svg" alt="Mooniak"></a>'
            f'<div class="where"><b>{_h(info.get("family") or "")}</b>font test pages &middot; '
            f'<span class="chip c-{_h(info.get("channel") or "canary")}">{_h(info.get("channel") or "canary")}</span></div>'
            f'<nav class="site-nav">{nav}</nav></header>'
            f'<p class="test-warning">{WARNING}</p>')


def footer() -> str:
    return ('<footer class="site-foot">Generated by Mooniak\'s font tooling from the font\'s source repository. '
            'Fonts are licensed as stated in each repository. Everything here is for testing: do not use these '
            'builds in production, and do not treat the results as a statement about the finished font.</footer>')


def _counts(st: dict) -> str:
    if st.get("cumulative") in (None, "?") or st.get("total") in (None, "?"):
        return ""
    return f'<span class="mute">({_h(st["cumulative"])}/{_h(st["total"])} glyph forms)</span>'


def render_index(info: dict, fonts: list[Path], proofs: list[tuple[str, str]], reports: dict[str, str],
                 tester_fonts: list[Path] | None = None) -> str:
    """``fonts`` = everything in out/fonts/ (listed for download only on dev/release);
    ``tester_fonts`` = the proof fonts the live tester draws from (default: ``fonts``)."""
    downloads = offers_downloads(info.get("channel"))
    sample = next((SAMPLE[s] for s in info["scripts"] if s in SAMPLE), LATIN)
    pool = fonts if tester_fonts is None else tester_fonts
    # a roman, not an italic, and a web-ready file when there is a choice
    tester = next(iter(sorted(pool, key=lambda f: ("italic" in f.name.lower(), f.suffix != ".woff2"))), None)
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
    fonts_section = (f'<h2 id="fonts">Fonts</h2><table><tr><th>File</th><th>Size</th></tr>{ftab}</table>'
                     if downloads else "")
    plinks = [(f'proof/{quote(Path(p).name)}', f"Type proof — {n}") for n, p in proofs]
    rlinks = [(href, label) for label, href in (("Fontspector QA report", reports.get("fontspector")),
                                                 ("Diffenator report", reports.get("diffenator"))) if href]
    if repo:
        rlinks.append((f"https://github.com/{repo}", "Source repository"))
        if downloads:       # /releases lists the rolling canary pre-release and its font zips
            rlinks.append((f"https://github.com/{repo}/releases", "Releases"))
    ptxt = "".join(f'<li><a href="{_h(h)}">{_h(t)}</a></li>' for h, t in plinks) or '<li class="mute">none</li>'
    rtxt = "".join(f'<li><a href="{_h(h)}">{_h(t)}</a></li>' for h, t in rlinks)
    note = ('<p class="warn"><b>Canary build &mdash; may be broken.</b> The latest build of the <code>dev</code> '
            'branch, cut automatically. It is not a release, and its font files are not offered for download.</p>'
            if not downloads else "")
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_h(info["family"])} — {_h(info["channel"])} build</title><style>{face}{_CSS}{_CHROME_CSS}</style></head><body>
{chrome(info, "", "home")}<main>
<h1>{_h(info["family"])}</h1>{note}
<h2>About these pages</h2>{ABOUT}
<h2>Build</h2><dl>{dl}</dl>
<h2>Try it</h2><textarea spellcheck="false">{_h(sample)}</textarea>
<h2 id="proofs">Proofs</h2><ul>{ptxt}</ul>
<h2 id="reports">Reports &amp; links</h2><ul>{rtxt}</ul>
{fonts_section}</main>{footer()}</body></html>"""


def build(repo: Path, out: Path, channel: str | None, pdf_dir: Path | None = None) -> dict:
    info = gather(repo, channel)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    core = _core()
    downloads = offers_downloads(info["channel"])
    # Proofs use the variable font when the build has one, else the statics.
    sources = core.font_files(repo, prefer_variable=True)
    if downloads:       # dev / release: every font of the build, listed for download
        fonts = copy_fonts(repo, out)
        served = [out / "fonts" / s.name for s in sources]
        proof_inputs = sources
    else:               # canary: just the proof fonts, as unlinked woff2 -- nothing to download
        fonts = served = proof_inputs = web_fonts(sources, out / "fonts")
    copy_assets(out)
    reports = copy_reports(repo, out, web_only=not downloads)
    proofs: list[tuple[str, str]] = []
    if proof_inputs:
        pages = core.build_proof_pages(proof_inputs, out / "proof", out / "fonts",
                                       family=info["family"], channel=info["channel"], build=info,
                                       chrome=chrome(info, "../", "proofs") + f'<p class="mute" style="padding:0 1.2rem">'
                                              f'<a href="../index.html#proofs">&larr; all proofs</a></p>',
                                       extra_css=_CHROME_CSS + _CHIP_CSS)
        proofs = [(pg.stem, str(pg.html_path)) for pg in pages]
        g = pages[0].gate
        if pdf_dir is not None and g.pdf:
            # development stage dev/release -> also a printable book per font
            for pg in pages:
                core.render_pdf(pg.html_path, pdf_dir / f"{pg.stem}-proof.pdf")
        info["proof_gate"] = {"stage": g.stage, "gated": g.gated, "shown": g.shown,
                              "withheld": [list(w) for w in g.withheld], "missing_for_next": g.next_gaps,
                              "scripts": g.scripts}
        if info["stage"] is None and g.stage is not None:
            info["stage"] = {"n": g.stage, "name": g.stage_name, "cumulative": "?", "total": "?"}
    (out / "build.json").write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "index.html").write_text(render_index(info, fonts, proofs, reports, tester_fonts=served), encoding="utf-8")
    if not downloads:
        assert_no_installable_fonts(out)
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
    repository = (builds[0].get("repository") if builds else None) or os.environ.get("GITHUB_REPOSITORY")
    info = {"family": builds[0].get("family") if builds else "", "channel": "canary", "repository": repository}
    # canary/ sits one level under the site root: its own "root" for assets is ../ ; the
    # Pages publisher copies assets/ to the site root, so ../assets/ resolves.
    head = chrome(info, "../", "canary")
    (canary_dir / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{fam} — canary builds</title><style>{_CSS}{_CHROME_CSS}</style></head><body>
{head}<main>
<h1>{fam} — canary builds</h1>
<p class="warn"><b>May be broken.</b> One entry per push to <code>dev</code>. Only the most recent builds keep their files.</p>
<table><tr><th>Commit</th><th>Version</th><th>Built</th><th>Design stage</th><th>QA</th><th>CI</th></tr>{"".join(rows)}</table>
</main>{footer()}</body></html>""", encoding="utf-8")


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
          f"(stage {g.get('stage')}, {len(g.get('shown', []))} section(s) shown, {len(g.get('withheld', []))} withheld"
          + (f", + {', '.join(g['scripts'])}" if g.get("scripts") else "") + ")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
