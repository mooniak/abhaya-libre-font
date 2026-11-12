"""proofpdf.core — stage-gated type proofs, standalone (no ``mnik`` import).

Same contract as ``manifest/build_manifest.py``: stdlib + fontTools + PyYAML only, so
this file travels to the project template's ``scripts/`` and runs in CI, where the
homebase does not exist. The ``mnik proof-pdf`` CLI (``__init__.py``) is a thin
workspace wrapper around it.

Two independent axes decide what a proof contains (see ``gates.json``):

* **Design stage** (0-10) -- computed from the built font by ``sinhala_coverage``
  against ``stages.json``. Decides WHICH sections appear: a section shows once the
  font has reached its ``min_stage``.
* **Development stage** (the build channel: canary / dev / release). Decides HOW
  DEEP the proof goes: canary = HTML only, dev = HTML + PDF, release = ungated.

Output is HTML first. Each proof page references its font by a *relative* URL, so the
same file works as a page on the published site and (loaded from disk) as the source
for the PDF render.
"""
from __future__ import annotations

import html as _html
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import yaml

try:  # homebase
    from mnik.mdrender import md_to_html
except ImportError:  # vendored into a font repo's scripts/ next to mdrender.py
    from mdrender import md_to_html

HERE = Path(__file__).resolve().parent
SECTIONS_DIR = HERE / "sections"
GATES_PATH = HERE / "gates.json"

FONT_EXTS = (".ttf", ".otf")
GLYPHSET_SLUG = "glyphset-coverage"
GLYPHSET_TITLE = "Glyph Coverage"

_FRONTMATTER = re.compile(r"\A---\n(.*?\n)---\n?(.*)\Z", re.DOTALL)
_STAGE_HEADING = re.compile(r"^##\s+Stage\s+(\d+)\b.*$", re.MULTILINE)

# Text for fonts with no Sinhala corpus to draw on (Latin/Tamil/symbol fonts).
_FALLBACK_TEXT = (
    "<p>ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789</p>"
    "<p>The quick brown fox jumps over the lazy dog.</p>"
    "<p>Sphinx of black quartz, judge my vow.</p>"
    "<p>!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[\\]^_`{|}~</p>"
)


# ── data ────────────────────────────────────────────────────────────────────
@dataclass
class Section:
    slug: str
    title: str
    html: str
    meta: dict = field(default_factory=dict)
    min_stage: int = 0
    lang: str = "si"


@dataclass
class Gate:
    """What was decided for one font, and why. Rendered onto the proof's cover."""
    stage: int | None            # None = undetectable / not a Sinhala font
    stage_name: str | None
    channel: str                 # canary | dev | release
    gated: bool
    pdf: bool
    shown: list[str] = field(default_factory=list)
    withheld: list[tuple[str, int]] = field(default_factory=list)   # (slug, min_stage)
    next_gaps: list[str] = field(default_factory=list)              # missing for stage+1


def load_gates(path: Path | None = None) -> dict:
    return json.loads((path or GATES_PATH).read_text(encoding="utf-8"))


# ── sections ────────────────────────────────────────────────────────────────
def _parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FRONTMATTER.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, m.group(2)


def filter_stage_blocks(body: str, stage: int | None) -> str:
    """Keep a '## Stage N' block only if N <= stage. Text before the first Stage
    heading is always kept. ``stage=None`` (ungated) keeps everything."""
    if stage is None:
        return body
    marks = list(_STAGE_HEADING.finditer(body))
    if not marks:
        return body
    out = [body[:marks[0].start()]]
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        if int(re.search(r"\d+", m.group(0)).group(0)) <= stage:
            out.append(body[m.start():end])
    return "".join(out)


def discover_sections(sections_dir: Path | None = None, gates: dict | None = None,
                      stage: int | None = None) -> list[Section]:
    """Every ``*.md`` in sections/, in filename order, tagged with its min_stage.

    ``stage`` only affects stage-blocked sections (see gates.json ``stage_blocks``): their
    body is cut to the blocks the font has reached. Dropping a new .md file in is still
    enough to add a section; it lands at ``default_min_stage`` until gates.json says otherwise.
    """
    d = sections_dir or SECTIONS_DIR
    g = gates or load_gates()
    mins = g["sections"]
    default_min = g.get("default_min_stage", 9)
    blocked = set(g.get("stage_blocks", {}).get("slugs", []))
    out: list[Section] = []
    if not d.is_dir():
        return out
    for f in sorted(d.glob("*.md")):
        meta, body = _parse_frontmatter(f.read_text(encoding="utf-8"))
        if f.stem in blocked:
            body = filter_stage_blocks(body, stage)
        title = meta.get("title") or f.stem.replace("-", " ").replace("_", " ").title()
        out.append(Section(slug=f.stem, title=title, meta=meta,
                           html=md_to_html(body.strip()),
                           min_stage=int(mins.get(f.stem, default_min))))
    return out


def fallback_section() -> Section:
    return Section(slug="specimen", title="Specimen", html=_FALLBACK_TEXT,
                   min_stage=0, lang="en")


# ── font files ──────────────────────────────────────────────────────────────
def font_files(repo_path: Path) -> list[Path]:
    """Binaries to proof for one repo: ttf preferred, else otf, else variable.
    (A variable font's default instance makes a poor proof target, so statics win.)"""
    root = repo_path / "fonts"
    for sub in ("ttf", "otf", "variable"):
        d = root / sub
        if d.is_dir():
            files = sorted(p for p in d.rglob("*")
                           if p.is_file() and p.suffix.lower() in FONT_EXTS)
            if files:
                return files
    return []


# ── stage detection ─────────────────────────────────────────────────────────
def _import_coverage():
    try:  # homebase
        from mnik.tools.manifest import sinhala_coverage
    except ImportError:  # vendored: scripts/sinhala_coverage.py beside this file
        import sinhala_coverage
    return sinhala_coverage


def _cmap_and_order(paths: list[Path]) -> tuple[set[int], set[str]]:
    from fontTools.ttLib import TTFont
    cmap: set[int] = set()
    order: set[str] = set()
    for p in paths:
        try:
            tt = TTFont(str(p), lazy=True)
            cmap |= set((tt.getBestCmap() or {}).keys())
            order |= set(tt.getGlyphOrder())
            tt.close()
        except Exception:
            continue
    return cmap, order


def detect_stage(paths: list[Path]) -> dict | None:
    """The font's Sinhala design stage, plus what stops it reaching the next one.

    Returns ``{"n", "name", "next_gaps": [...]}`` or None when the stage model is
    unavailable or the font has no usable cmap. The union of all given binaries is
    used, matching ``coverage.sinhala_design_stage`` in fontstatus.json.
    """
    try:
        sc = _import_coverage()
        model = sc.load_stage_model()
        if model is None or not paths:
            return None
        cmap, order = _cmap_and_order(paths)
        if not cmap and not order:
            return None
        res = sc.compute(paths, lambda p: _cmap_and_order([p])[0],
                         lambda p: _cmap_and_order([p])[1], stage_model=model)
        if res is None:
            return None
        lower = {g.lower() for g in order}
        have = sc._evaluate(model, cmap, lower)
        gaps = sorted(k for k, v in model["glyphs"].items()
                      if v.get("stage", 0) == res["n"] + 1 and have.get(k) is False)
        return {"n": res["n"], "name": res["name"], "next_gaps": gaps}
    except Exception:
        return None


# ── gating ──────────────────────────────────────────────────────────────────
def plan(channel: str, gates: dict | None = None) -> dict:
    """Development stage -> proof depth ({'gated', 'pdf'}). Unknown channel = canary."""
    g = (gates or load_gates())["channels"]
    return g.get(channel) or g["canary"]


def apply_gates(sections: list[Section], stage: dict | None, channel: str,
                gates: dict | None = None, ungated: bool = False) -> tuple[list[Section], Gate]:
    """Pick the sections this font has earned. Fonts whose stage can't be determined
    (non-Sinhala, or no model) get the generic specimen instead of the Sinhala corpus."""
    p = plan(channel, gates)
    gated = p["gated"] and not ungated
    gate = Gate(stage=stage["n"] if stage else None,
                stage_name=stage["name"] if stage else None,
                channel=channel, gated=gated, pdf=p["pdf"],
                next_gaps=(stage or {}).get("next_gaps", []))
    if stage is None:
        gate.gated = False
        gate.shown = ["specimen"]
        return [fallback_section()], gate
    keep: list[Section] = []
    for s in sections:
        if not gated or s.min_stage <= stage["n"]:
            keep.append(s)
            gate.shown.append(s.slug)
        else:
            gate.withheld.append((s.slug, s.min_stage))
    return keep, gate


# ── glyph coverage grid ─────────────────────────────────────────────────────
# Private-use area (BMP) used to make GSUB-only glyphs (ligatures, conjuncts,
# composites -- most of a Sinhala font's glyph set) addressable by one codepoint, so
# the coverage grid can show literally every glyph, not just natively-mapped ones.
_PUA_START, _PUA_END = 0xE000, 0xF8FF


def _assign_pua(used: set[int], names: list[str]) -> dict[int, str]:
    out: dict[int, str] = {}
    cp = _PUA_START
    for n in names:
        while cp in used and cp <= _PUA_END:
            cp += 1
        if cp > _PUA_END:
            break
        out[cp] = n
        used.add(cp)
        cp += 1
    return out


def build_glyphset_section(font_path: Path, patched_out: Path) -> tuple[Section, Path | None]:
    """Every glyph in the font as a grid. A working copy with synthetic PUA cmap
    entries (written to ``patched_out``) lets unreachable glyphs be shown by name; the
    original font is never modified."""
    from fontTools.ttLib import TTFont

    tt = TTFont(str(font_path))
    order = tt.getGlyphOrder()
    best = tt.getBestCmap() or {}
    mapped = set(best.values())
    cp_by_name = {g: cp for cp, g in best.items()}
    unmapped = [g for g in order if g != ".notdef" and g not in mapped]
    pua = _assign_pua(set(best.keys()), unmapped)
    patched = None
    if pua:
        for st in tt["cmap"].tables:
            if hasattr(st, "cmap"):
                st.cmap.update(pua)
        patched_out.parent.mkdir(parents=True, exist_ok=True)
        tt.save(str(patched_out))
        patched = patched_out
    tt.close()
    cp_by_name.update({g: cp for cp, g in pua.items()})
    dropped = len(unmapped) - len(pua)

    cells = []
    for g in order:
        if g == ".notdef":
            continue
        cp = cp_by_name.get(g)
        if cp is None:
            continue
        label = f"U+{cp:04X}" if g in mapped else _html.escape(g)
        cells.append(f'<div class="glyph-cell"><div class="glyph-glyph">{_html.escape(chr(cp))}</div>'
                     f'<div class="glyph-label">{label}</div></div>')
    note = (f'<p class="glyphset-note">{len(order) - 1} glyph(s) in the font (excluding .notdef). '
            f'{len(mapped)} have a native Unicode codepoint (labelled U+XXXX); the other '
            f'{len(unmapped)} are reachable only via OpenType substitution (ligatures, conjuncts, '
            f'composites) and are shown through a synthetic private-use mapping, labelled by glyph name.</p>')
    if dropped > 0:
        note += f'<p class="glyphset-note">{dropped} glyph(s) not shown: private-use range exhausted.</p>'
    sec = Section(slug=GLYPHSET_SLUG, title=GLYPHSET_TITLE, min_stage=0,
                  html=note + '<div class="glyph-grid">' + "".join(cells) + "</div>")
    sec.meta["glyphset"] = True
    return sec, patched


# ── HTML ────────────────────────────────────────────────────────────────────
_CSS = """
@page { size: A4; margin: 22mm 16mm 18mm 16mm; }
* { box-sizing: border-box; }
body { font-family: system-ui, sans-serif; margin: 0; color: #111; }
.cover { min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 0 1.2rem; }
.cover h1 { font-size: 2rem; margin: 0 0 0.5rem; }
.cover .meta { color: #555; font-size: 0.95rem; line-height: 1.6; }
.gate { margin-top: 1.4rem; padding: 0.9rem 1rem; border: 1px solid #ddd; border-radius: 6px;
        font-size: 0.85rem; line-height: 1.55; color: #333; max-width: 46rem; }
.gate b { color: #000; }
.gate .chan { display: inline-block; padding: 1px 8px; border-radius: 99px; font-size: 0.75rem;
              font-weight: 600; letter-spacing: .04em; text-transform: uppercase; background: #eee; }
.chan-canary { background: #fff3c4 !important; } .chan-dev { background: #d6e8ff !important; }
.chan-release { background: #d3f3dc !important; }
.gate ul { margin: .3rem 0 0 1.1rem; padding: 0; }
.section { page-break-before: always; padding: 0 1.2rem; }
.section h2 { font-size: 1.1rem; color: #555; text-transform: uppercase; letter-spacing: 0.04em;
              border-bottom: 1px solid #ddd; padding-bottom: 0.4rem; }
.section h2 small { font-weight: 400; text-transform: none; letter-spacing: 0; color: #999; }
.proof-text { font-family: "ProofFont", sans-serif; font-size: 15pt; line-height: 1.9; margin-top: 1.2rem; }
.proof-text p { margin: 0 0 1.1em; }
.proof-text h1, .proof-text h2, .proof-text h3 { font-weight: 600; margin: 1em 0 0.4em; }
.proof-text table { border-collapse: collapse; } .proof-text td, .proof-text th { padding: 2px 8px; vertical-align: top; }
.proof-text .glyphset-note, .glyphset-note { font-family: system-ui, sans-serif; font-size: 9pt; color: #555; margin-top: 0.8rem; line-height: 1.5; }
.glyph-grid { display: flex; flex-wrap: wrap; margin-top: 1rem; }
.glyph-cell { width: 11%; text-align: center; padding: 3mm 0; break-inside: avoid; }
.glyph-glyph { font-family: "ProofGlyphset", sans-serif; font-size: 18pt; line-height: 1.2; }
.glyph-label { font-family: Menlo, Consolas, monospace; font-size: 5.5pt; color: #888; margin-top: 2px;
               line-height: 1.15; word-break: break-all; padding: 0 2px; }
@media screen { .section { page-break-before: auto; margin-top: 3rem; } .cover { min-height: 60vh; } }
"""


def _fmt(href: str) -> str:
    h = href.lower()
    return "woff2" if h.endswith(".woff2") else "opentype" if h.endswith(".otf") else "truetype"


def font_face(href: str, family: str = "ProofFont") -> str:
    return f'@font-face {{ font-family: "{family}"; src: url("{href}") format("{_fmt(href)}"); }}'


def rel_href(from_dir: Path, target: Path) -> str:
    """URL-quoted relative path from a directory to a file (font names contain [ ])."""
    import os
    return quote(os.path.relpath(target, from_dir).replace(os.sep, "/"), safe="/")


def _gate_html(g: Gate) -> str:
    rows = [f'<span class="chan chan-{g.channel}">{_html.escape(g.channel)}</span>']
    if g.stage is not None:
        rows.append(f'Design stage <b>{g.stage}</b> &mdash; {_html.escape(g.stage_name or "")}')
    else:
        rows.append("Design stage not determined (no Sinhala stage model for this font) &mdash; generic specimen")
    mode = ("gated by design stage" if g.gated else
            "ungated &mdash; every section shown" + (" (release)" if g.channel == "release" else ""))
    rows.append(f"Proof depth: {mode}")
    out = "<br>".join(rows)
    if g.withheld:
        late = ", ".join(f"{_html.escape(s)} (stage {n})" for s, n in g.withheld)
        out += f"<br>Withheld until the font reaches the stage: {late}"
    if g.next_gaps:
        shown = ", ".join(_html.escape(x) for x in g.next_gaps[:24])
        more = f" +{len(g.next_gaps) - 24} more" if len(g.next_gaps) > 24 else ""
        out += f"<br>Missing for stage {(g.stage or 0) + 1}: {shown}{more}"
    return f'<div class="gate">{out}</div>'


def build_html(family: str, style: str, font_href: str, sections: list[Section], gate: Gate,
               build: dict | None = None, glyphset_href: str | None = None) -> str:
    b = build or {}
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    meta_bits = [style]
    if b.get("version"):
        meta_bits.append(f"Version {_html.escape(str(b['version']))}")
    if b.get("commit_short"):
        meta_bits.append(f"commit {_html.escape(b['commit_short'])}")
    meta_bits.append(f"Type proof &mdash; generated {generated}")
    faces = font_face(font_href)
    if glyphset_href:
        faces += "\n" + font_face(glyphset_href, "ProofGlyphset")
    body = "\n".join(
        f'<div class="section"><h2>{_html.escape(s.title)}'
        + (f' <small>stage {s.min_stage}+</small>' if gate.gated and s.min_stage else "")
        + f'</h2><div class="proof-text" lang="{s.lang}">{s.html}</div></div>'
        for s in sections)
    return (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{_html.escape(family)} &mdash; proof</title>'
            f'<style>{faces}\n{_CSS}</style></head><body>\n'
            f'<div class="cover"><h1>{_html.escape(family)}</h1>'
            f'<div class="meta">{"<br>".join(meta_bits)}</div>{_gate_html(gate)}</div>\n'
            f'{body}\n</body></html>')


# ── orchestration ───────────────────────────────────────────────────────────
@dataclass
class ProofPage:
    stem: str
    html_path: Path
    gate: Gate


def build_proof_pages(font_paths: list[Path], proof_dir: Path, fonts_dir: Path, *, family: str,
                      channel: str, build: dict | None = None, stage_override: int | None = None,
                      ungated: bool = False, only: set[str] | None = None,
                      gates: dict | None = None) -> list[ProofPage]:
    """Write one proof HTML per font into ``proof_dir``.

    Fonts are referenced by relative URL from ``fonts_dir`` (the caller copies them
    there), so pages are portable. The stage is detected once from the union of all
    binaries -- a family has one stage -- and applied to every page.
    """
    g = gates or load_gates()
    stage = detect_stage(font_paths)
    if stage_override is not None:
        stage = {"n": stage_override, "name": (stage or {}).get("name") or f"stage {stage_override}",
                 "next_gaps": []}
    pages: list[ProofPage] = []
    proof_dir.mkdir(parents=True, exist_ok=True)
    corpus = discover_sections(gates=g, stage=None if (ungated or not plan(channel, g)["gated"])
                               else (stage["n"] if stage else None))
    sections, gate = apply_gates(corpus, stage, channel, g, ungated=ungated)
    if only:
        unknown = only - {s.slug for s in corpus} - {GLYPHSET_SLUG}
        if unknown:
            raise SystemExit(f"Unknown section(s): {', '.join(sorted(unknown))}")
        sections = [s for s in sections if s.slug in only]
    want_glyphset = (not only) or GLYPHSET_SLUG in only
    for fp in font_paths:
        page_sections = list(sections)
        patched_href = None
        if want_glyphset:
            patched_path = proof_dir / f"{fp.stem}.glyphset{fp.suffix}"
            sec, patched = build_glyphset_section(fp, patched_path)
            page_sections.insert(0, sec)
            patched_href = rel_href(proof_dir, patched or fp)
        html = build_html(family, fp.stem, rel_href(proof_dir, fonts_dir / fp.name), page_sections,
                          gate, build, patched_href)
        out = proof_dir / f"{fp.stem}.html"
        out.write_text(html, encoding="utf-8")
        pages.append(ProofPage(fp.stem, out, gate))
    return pages


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    """Print a proof page to PDF with headless Chromium, so complex-script shaping
    (conjuncts, rakaransaya, vowel-sign reordering) comes out right."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise SystemExit("playwright is not installed. `pip install playwright && playwright install chromium`.")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri())
        page.evaluate("document.fonts.ready")
        page.pdf(path=str(pdf_path), print_background=True, display_header_footer=True,
                 header_template="<span></span>",
                 footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#888;">'
                                 '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')
        browser.close()
