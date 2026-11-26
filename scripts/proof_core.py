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

Other scripts (Tamil) have no design-stage model yet. A font whose cmap covers one gets
that script's sections *added*, ungated, whatever its Sinhala stage -- see
``detect_scripts`` and gates.json ``scripts``.

Output is HTML first. Each proof page references its font by a *relative* URL, so the
same file works as a page on the published site and (loaded from disk) as the source
for the PDF render.

On screen a page has a sticky toolbar (text size; the variable font's named instances and a
slider per axis, or a button per style of a static family), a large editable mixed-script
sample on top, and one tab per script (Sinhala, Tamil, Latin) plus the glyph set. Print shows
every tab in turn and hides the controls, so the PDF book is unchanged by them. A section may
turn OpenType features on with ``features:`` in its frontmatter (``features: ss09``).
"""
from __future__ import annotations

import html as _html
import json
import re
from dataclasses import dataclass, field, replace
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
LATIN_WATERFALL_SLUG = "latin-waterfall"
LATIN_WATERFALL_TITLE = "Latin Coverage"
LATIN_GLYPHSETS_PATH = HERE / "latin_glyphsets.json"
# The GF Latin tier ladder (gftools/glyphsets' GF_Latin_*.nam, vendored as
# latin_glyphsets.json): each tier is a strict superset of the previous one, so the
# highest fully-covered tier is the font's Latin coverage level. African/Vietnamese are
# separate add-on sets, not rungs of this ladder -- reported alongside it, not in it.
_LATIN_LADDER = ("Kernel", "Core", "Plus", "Beyond")
_LATIN_EXTRAS = ("African", "Vietnamese")

_FRONTMATTER = re.compile(r"\A---\n(.*?\n)---\n?(.*)\Z", re.DOTALL)
_STAGE_HEADING = re.compile(r"^##\s+Stage\s+(\d+)\b.*$", re.MULTILINE)

# Text for fonts with neither a Sinhala stage nor a covered script group to draw on
# (Latin/symbol fonts).
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
    script: str | None = None    # gates.json 'scripts' key this section belongs to, if any
    features: list[str] = field(default_factory=list)   # OpenType features the section turns on


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
    scripts: list[str] = field(default_factory=list)                # labels of non-Sinhala scripts proofed


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


def script_groups(gates: dict | None = None) -> dict[str, dict]:
    """gates.json 'scripts' without its '_doc' entries: {key: {label, lang, block, ...}}."""
    return {k: v for k, v in (gates or load_gates()).get("scripts", {}).items()
            if not k.startswith("_")}


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
    group = {slug: (key, sc) for key, sc in script_groups(g).items() for slug in sc["sections"]}
    out: list[Section] = []
    if not d.is_dir():
        return out
    for f in sorted(d.glob("*.md")):
        meta, body = _parse_frontmatter(f.read_text(encoding="utf-8"))
        if f.stem in blocked:
            body = filter_stage_blocks(body, stage)
        title = meta.get("title") or f.stem.replace("-", " ").replace("_", " ").title()
        key, sc = group.get(f.stem, (None, {}))
        # A section only a script group owns is not stage-gated (stage 0); one that is also in
        # 'sections' (tamil-pangram) keeps its Sinhala stage for Sinhala fonts.
        min_stage = int(mins[f.stem]) if f.stem in mins else (0 if key else default_min)
        out.append(Section(slug=f.stem, title=title, meta=meta,
                           html=md_to_html(body.strip()),
                           min_stage=min_stage, lang=sc.get("lang", "si"), script=key,
                           features=_feature_tags(meta.get("features"))))
    return out


_FEATURE_TAG = re.compile(r"^[A-Za-z0-9 ]{4}$")


def _feature_tags(value) -> list[str]:
    """Frontmatter ``features:`` (``ss09``, ``ss01 dlig`` or a list) -> valid 4-letter tags."""
    if not value:
        return []
    items = value.replace(",", " ").split() if isinstance(value, str) else [str(v) for v in value]
    return [t for t in items if _FEATURE_TAG.match(t)]


def fallback_section() -> Section:
    return Section(slug="specimen", title="Specimen", html=_FALLBACK_TEXT,
                   min_stage=0, lang="en")


# ── font files ──────────────────────────────────────────────────────────────
def font_files(repo_path: Path, prefer_variable: bool = False) -> list[Path]:
    """Binaries to proof for one repo.

    Default (local ``mnik proof-pdf``): ttf, else otf, else variable -- a variable font's
    default instance makes a poor print proof, so statics win. ``prefer_variable`` (the
    Pages site) flips that: variable, else ttf, else otf, so a build that ships both is
    proofed once from its variable font rather than once per static instance."""
    root = repo_path / "fonts"
    for sub in (("variable", "ttf", "otf") if prefer_variable else ("ttf", "otf", "variable")):
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


_SINHALA_BLOCK = (0x0D80, 0x0DFF)


def covers_sinhala(paths: list[Path]) -> bool:
    """Does any binary map a single Sinhala codepoint? (The stage model has a floor, stage 0,
    that a font with no Sinhala at all also lands on -- this tells the two apart.)"""
    cmap, _ = _cmap_and_order(paths)
    return any(_SINHALA_BLOCK[0] <= cp <= _SINHALA_BLOCK[1] for cp in cmap)


def detect_scripts(paths: list[Path], gates: dict | None = None) -> list[str]:
    """Keys of the non-Sinhala scripts (gates.json 'scripts') the font covers, by cmap.

    A script counts once ``min_codepoints`` of its Unicode block are mapped in the union
    of the given binaries, so a logo font with a stray letter or two does not. No stage
    model is involved: this only decides which script groups' sections are added."""
    groups = script_groups(gates)
    if not groups or not paths:
        return []
    cmap, _ = _cmap_and_order(paths)
    found = []
    for key, sc in groups.items():
        lo, hi = sc["block"]
        if sum(1 for cp in cmap if lo <= cp <= hi) >= sc.get("min_codepoints", 1):
            found.append(key)
    return found


# ── gating ──────────────────────────────────────────────────────────────────
def plan(channel: str, gates: dict | None = None) -> dict:
    """Development stage -> proof depth ({'gated', 'pdf'}). Unknown channel = canary."""
    g = (gates or load_gates())["channels"]
    return g.get(channel) or g["canary"]


def apply_gates(sections: list[Section], stage: dict | None, channel: str,
                gates: dict | None = None, ungated: bool = False,
                scripts: list[str] | None = None) -> tuple[list[Section], Gate]:
    """Pick the sections this font has earned.

    * Sinhala sections are gated by ``stage`` (a font with no stage gets none of them).
    * ``scripts`` (from ``detect_scripts``) ADD that script group's sections, ungated, in the
      order gates.json lists them. A section owned only by a script group never reaches a
      font that does not cover the script.
    * A font with neither a stage nor a covered script gets the generic specimen."""
    g = gates or load_gates()
    groups = script_groups(g)
    scripts = [k for k in (scripts or []) if k in groups]
    p = plan(channel, g)
    gated = p["gated"] and not ungated
    gate = Gate(stage=stage["n"] if stage else None,
                stage_name=stage["name"] if stage else None,
                channel=channel, gated=gated, pdf=p["pdf"],
                next_gaps=(stage or {}).get("next_gaps", []),
                scripts=[groups[k]["label"] for k in scripts])
    if stage is None and not scripts:
        gate.gated = False
        gate.shown = ["specimen"]
        return [fallback_section()], gate
    covered = {slug for k in scripts for slug in groups[k]["sections"]}      # added below
    owned = {slug for sc in groups.values() for slug in sc["sections"]}
    staged = set(g["sections"])
    keep: list[Section] = []
    if stage is None:
        gate.gated = False      # nothing to gate on: the script groups are ungated
    else:
        for s in sections:
            if s.slug in covered or (s.slug in owned and s.slug not in staged):
                continue        # a covered script's, shown below; or another script's, not for this font
            if not gated or s.min_stage <= stage["n"]:
                keep.append(s)
                gate.shown.append(s.slug)
            else:
                gate.withheld.append((s.slug, s.min_stage))
    by_slug = {s.slug: s for s in sections}
    for k in scripts:
        for slug in groups[k]["sections"]:
            if slug in by_slug and slug not in gate.shown:
                keep.append(replace(by_slug[slug], min_stage=0))   # ungated: no "stage N+" tag
                gate.shown.append(slug)
    return keep, gate


# ── Latin coverage waterfall ────────────────────────────────────────────────
def load_latin_glyphsets(path: Path | None = None) -> dict[str, list[int]]:
    try:
        return json.loads((path or LATIN_GLYPHSETS_PATH).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def compute_latin_tiers(cmap: set[int], glyphsets: dict[str, list[int]] | None = None) -> dict:
    """Coverage of the font's cmap against each GF Latin tier.

    Returns ``{"ladder": [{"tier", "have", "total", "pct", "complete"}, ...],
    "extras": [...], "level": <highest fully-covered ladder tier, or None>}``.
    """
    gs = glyphsets if glyphsets is not None else load_latin_glyphsets()
    ladder = []
    level = None
    for tier in _LATIN_LADDER:
        cps = gs.get(tier, [])
        have = sum(1 for cp in cps if cp in cmap)
        total = len(cps)
        complete = total > 0 and have == total
        if complete:
            level = tier
        ladder.append({"tier": tier, "have": have, "total": total,
                       "pct": round(100 * have / total, 1) if total else 0.0,
                       "complete": complete})
    extras = []
    for tier in _LATIN_EXTRAS:
        cps = gs.get(tier, [])
        have = sum(1 for cp in cps if cp in cmap)
        total = len(cps)
        extras.append({"tier": tier, "have": have, "total": total,
                       "pct": round(100 * have / total, 1) if total else 0.0,
                       "complete": total > 0 and have == total})
    return {"ladder": ladder, "extras": extras, "level": level}


def build_latin_waterfall_section(cmap: set[int], glyphsets: dict[str, list[int]] | None = None) -> Section:
    """A table of GF Latin tier coverage (Kernel..Beyond, plus African/Vietnamese)."""
    result = compute_latin_tiers(cmap, glyphsets)
    rows = []
    for row in result["ladder"] + result["extras"]:
        status = "complete" if row["complete"] else ("partial" if row["have"] else "none")
        rows.append(
            f'<tr class="latin-tier latin-tier-{status}"><td>{_html.escape(row["tier"])}</td>'
            f'<td>{row["have"]} / {row["total"]}</td><td>{row["pct"]}%</td>'
            f'<td>{"complete" if row["complete"] else ""}</td></tr>')
    level = result["level"] or "below Kernel"
    note = (f'<p class="glyphset-note">Highest fully-covered GF Latin tier: <b>{_html.escape(level)}</b>. '
            f'Kernel/Core/Plus/Beyond are cumulative (each a superset of the last); African and '
            f'Vietnamese are separate add-on sets, not rungs of that ladder.</p>')
    table = ('<table class="latin-waterfall"><thead><tr><th>Tier</th><th>Covered</th>'
             f'<th>%</th><th></th></tr></thead><tbody>{"".join(rows)}</tbody></table>')
    sec = Section(slug=LATIN_WATERFALL_SLUG, title=LATIN_WATERFALL_TITLE, min_stage=0,
                  html=note + table, lang="en")
    sec.meta["latin_waterfall"] = True
    return sec


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


# ── on-screen controls: styles, tabs, the mixed-script sample ───────────────
@dataclass
class Axis:
    tag: str
    name: str
    minimum: float
    default: float
    maximum: float


@dataclass
class Styles:
    """What the page's weight controls can switch between. A variable font has ``axes`` and
    named ``instances`` ({name: {tag: value}}); a static family has ``statics``, one
    (style name, font href) per file, the page's own font first in weight order."""
    axes: list[Axis] = field(default_factory=list)
    instances: list[tuple[str, dict[str, float]]] = field(default_factory=list)
    statics: list[tuple[str, str]] = field(default_factory=list)
    current: int = 0                 # index into statics of this page's own font


def _style_name(tt) -> str:
    name = tt["name"]
    return (name.getDebugName(17) or name.getDebugName(2) or "Regular").strip()


def style_info(font_path: Path, family_paths: list[Path] | None = None,
               href=lambda p: p.name) -> Styles:
    """Axes and named instances of a variable font; else the styles of its static family
    (``family_paths``), sorted roman before italic, then by weight class. ``href`` maps a
    font path to the URL the page loads it from."""
    from fontTools.ttLib import TTFont
    out = Styles()
    try:
        tt = TTFont(str(font_path), lazy=True)
    except Exception:
        return out
    try:
        if "fvar" in tt:
            fvar, name = tt["fvar"], tt["name"]
            for a in fvar.axes:
                if a.maxValue <= a.minValue:
                    continue            # a degenerate axis (Vineetha's wght is 400-400): nothing to slide
                out.axes.append(Axis(a.axisTag, (name.getDebugName(a.axisNameID) or a.axisTag).strip(),
                                     a.minValue, a.defaultValue, a.maxValue))
            for inst in fvar.instances:
                label = (name.getDebugName(inst.subfamilyNameID) or "").strip()
                if label:
                    out.instances.append((label, dict(inst.coordinates)))
            return out
    finally:
        tt.close()
    rows = []
    for p in family_paths or [font_path]:
        try:
            t = TTFont(str(p), lazy=True)
            if "fvar" in t:
                t.close()
                continue
            os2 = t["OS/2"] if "OS/2" in t else None
            weight = os2.usWeightClass if os2 else 400
            italic = bool(os2 and os2.fsSelection & 1) or "italic" in p.name.lower()
            rows.append((italic, weight, _style_name(t), p))
            t.close()
        except Exception:
            continue
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    if len(rows) > 1:
        out.statics = [(label, href(p)) for _, _, label, p in rows]
        out.current = next((i for i, r in enumerate(rows) if r[3] == font_path), 0)
    return out


# Tabs, in order. A section goes in its script's tab; Sinhala-staged sections (the
# multi-script probes included) go in the Sinhala one.
TAB_LABELS = {"sinhala": "Sinhala", "tamil": "Tamil", "latin": "Latin",
              "specimen": "Specimen", "glyphs": "Glyph set"}

# The large editable sample at the top of the page: a mixed line in every script the font
# covers, then one line per script.
HERO_MIX = {"sinhala": "ශ්‍රී ලංකා", "tamil": "இலங்கை", "latin": "Sri Lanka"}
HERO_LINES = {"sinhala": "බක්මහා ආරේන්දුවක් සුළං දැවැන්තය",
              "tamil": "ஒளிரும் தமிழ் மொழியின் சக்தி",
              "latin": "The quick brown fox jumps over the lazy dog"}
HERO_LANG = {"sinhala": "si", "tamil": "ta", "latin": "en"}


def tab_of(section: Section, scripts: list[str]) -> str:
    if section.meta.get("glyphset"):
        return "glyphs"
    if section.meta.get("latin_waterfall"):
        return "latin"
    if section.slug == "specimen":
        return "specimen"
    if section.script and section.script in scripts:
        return section.script
    return "sinhala"


def group_tabs(sections: list[Section], scripts: list[str]) -> list[tuple[str, list[Section]]]:
    """[(tab key, its sections)] in TAB_LABELS order, glyph set last; empty tabs dropped."""
    groups: dict[str, list[Section]] = {}
    for s in sections:
        groups.setdefault(tab_of(s, scripts), []).append(s)
    order = [k for k in TAB_LABELS if k != "glyphs"] + ["glyphs"]
    return [(k, groups[k]) for k in order if k in groups]


def _hero_html(hero_scripts: list[str]) -> str:
    keys = [k for k in ("sinhala", "tamil", "latin") if k in hero_scripts] or ["latin"]
    mix = " ".join(f'<span lang="{HERO_LANG[k]}">{_html.escape(HERO_MIX[k])}</span>' for k in keys)
    lines = [f'<div>{mix}</div>'] if len(keys) > 1 else []
    lines += [f'<div lang="{HERO_LANG[k]}">{_html.escape(HERO_LINES[k])}</div>' for k in keys]
    return ('<div class="proof-hero" contenteditable="true" spellcheck="false" '
            'title="Type here to try your own text">' + "".join(lines) + "</div>")


def _num(x: float) -> str:
    return f"{x:g}"


def _toolbar_html(styles: Styles) -> str:
    parts = ['<label class="pt-size">Size <input type="range" id="pt-size" min="8" max="96" step="1" value="15">'
             ' <output id="pt-size-out">15 pt</output></label>']
    if styles.axes:
        if styles.instances:
            btns = "".join(
                f'<button type="button" class="pt-inst" data-coords="{_html.escape(json.dumps(c))}">'
                f'{_html.escape(n)}</button>' for n, c in styles.instances)
            parts.append(f'<span class="pt-group" aria-label="Named instances">{btns}</span>')
        for a in styles.axes:
            step = 1 if a.maximum - a.minimum > 10 else 0.1
            parts.append(f'<label class="pt-axis">{_html.escape(a.name)} '
                         f'<input type="range" data-axis="{_html.escape(a.tag)}" min="{_num(a.minimum)}" '
                         f'max="{_num(a.maximum)}" step="{step}" value="{_num(a.default)}"> '
                         f'<output>{_num(a.default)}</output></label>')
    elif styles.statics:
        btns = "".join(
            f'<button type="button" class="pt-static{" on" if i == styles.current else ""}" '
            f'data-family="ProofStyle{i}">{_html.escape(n)}</button>' for i, (n, _) in enumerate(styles.statics))
        parts.append(f'<span class="pt-group" aria-label="Styles">{btns}</span>')
    return '<div class="proof-tools" role="toolbar">' + "".join(parts) + "</div>"


_JS = """
(function () {
  var root = document.documentElement;
  var size = document.getElementById('pt-size'), sizeOut = document.getElementById('pt-size-out');
  if (size) size.addEventListener('input', function () {
    root.style.setProperty('--proof-size', size.value + 'pt'); sizeOut.textContent = size.value + ' pt';
  });
  var axes = [].slice.call(document.querySelectorAll('.pt-axis input'));
  var insts = [].slice.call(document.querySelectorAll('.pt-inst'));
  function applyAxes() {
    var v = axes.map(function (i) { i.nextElementSibling.textContent = i.value; return '"' + i.dataset.axis + '" ' + i.value; });
    root.style.setProperty('--proof-variation', v.join(', ') || 'normal');
    insts.forEach(function (b) {
      var c = JSON.parse(b.dataset.coords);
      b.classList.toggle('on', axes.every(function (i) { return !(i.dataset.axis in c) || +i.value === c[i.dataset.axis]; }));
    });
  }
  axes.forEach(function (i) { i.addEventListener('input', applyAxes); });
  insts.forEach(function (b) { b.addEventListener('click', function () {
    var c = JSON.parse(b.dataset.coords);
    axes.forEach(function (i) { if (i.dataset.axis in c) i.value = c[i.dataset.axis]; });
    applyAxes();
  }); });
  if (axes.length) applyAxes();
  var statics = [].slice.call(document.querySelectorAll('.pt-static'));
  statics.forEach(function (b) { b.addEventListener('click', function () {
    root.style.setProperty('--proof-family', '"' + b.dataset.family + '"');
    statics.forEach(function (o) { o.classList.toggle('on', o === b); });
  }); });
  var tabs = [].slice.call(document.querySelectorAll('.proof-tabs button'));
  function show(key) {
    tabs.forEach(function (t) { t.classList.toggle('on', t.dataset.tab === key); t.setAttribute('aria-selected', t.dataset.tab === key); });
    [].forEach.call(document.querySelectorAll('.tab-panel'), function (p) { p.hidden = p.dataset.tab !== key; });
  }
  tabs.forEach(function (t) { t.addEventListener('click', function () {
    show(t.dataset.tab); history.replaceState(null, '', '#tab-' + t.dataset.tab);
  }); });
  if (tabs.length) {
    var want = (location.hash.match(/^#tab-(.+)$/) || [])[1];
    show(tabs.some(function (t) { return t.dataset.tab === want; }) ? want : tabs[0].dataset.tab);
  }
})();
"""


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
.proof-text { font-family: var(--proof-family, "ProofFont"), sans-serif; font-size: var(--proof-size, 15pt);
              font-variation-settings: var(--proof-variation, normal); line-height: 1.9; margin-top: 1.2rem; }
.proof-text p { margin: 0 0 1.1em; }
.proof-text h1, .proof-text h2, .proof-text h3 { font-weight: 600; margin: 1em 0 0.4em; }
.proof-text table { border-collapse: collapse; } .proof-text td, .proof-text th { padding: 2px 8px; vertical-align: top; }
.proof-text .glyphset-note, .glyphset-note { font-family: system-ui, sans-serif; font-size: 9pt; color: #555; margin-top: 0.8rem; line-height: 1.5; }
.glyph-grid { display: flex; flex-wrap: wrap; margin-top: 1rem; }
.glyph-cell { width: 11%; text-align: center; padding: 3mm 0; break-inside: avoid; }
.glyph-glyph { font-family: "ProofGlyphset", sans-serif; font-size: calc(var(--proof-size, 15pt) * 1.2);
               font-variation-settings: var(--proof-variation, normal); line-height: 1.2; }
.glyph-label { font-family: Menlo, Consolas, monospace; font-size: 5.5pt; color: #888; margin-top: 2px;
               line-height: 1.15; word-break: break-all; padding: 0 2px; }
.latin-waterfall { font-family: system-ui, sans-serif; font-size: 10pt; width: 100%; margin-top: 1rem; border-collapse: collapse; }
.latin-waterfall th, .latin-waterfall td { border-bottom: 1px solid #eee; padding: 4px 8px; text-align: left; }
.latin-tier-complete td { color: #1a7a33; } .latin-tier-partial td { color: #996a00; } .latin-tier-none td { color: #999; }
.section h2 .feat { font-family: Menlo, Consolas, monospace; font-size: .8em; color: #999; text-transform: none; }
.proof-hero { font-family: var(--proof-family, "ProofFont"), sans-serif; font-variation-settings: var(--proof-variation, normal);
              font-size: calc(var(--proof-size, 15pt) * 3.4); line-height: 1.35; margin: 1.4rem 0 .4rem; outline: none;
              overflow-wrap: anywhere; }
.proof-hero > div { margin: 0 0 .15em; }
.proof-tools { position: sticky; top: 0; z-index: 5; display: flex; flex-wrap: wrap; align-items: center; gap: .5rem 1.2rem;
               padding: .55rem 1.2rem; background: rgba(255,255,255,.96); border-bottom: 1px solid #e3e3e3;
               font: 13px system-ui, sans-serif; color: #333; }
.proof-tools label { display: inline-flex; align-items: center; gap: .4rem; white-space: nowrap; }
.proof-tools input[type=range] { width: 9rem; }
.proof-tools output { min-width: 3.2em; color: #666; font-variant-numeric: tabular-nums; }
.pt-group { display: inline-flex; flex-wrap: wrap; gap: .25rem; }
.pt-group button, .proof-tabs button { font: inherit; border: 1px solid #ccc; background: #fff; border-radius: 6px;
               padding: .2rem .6rem; cursor: pointer; color: #222; }
.pt-group button.on, .proof-tabs button.on { background: #111; border-color: #111; color: #fff; }
.proof-tabs { display: flex; flex-wrap: wrap; gap: .3rem; padding: 0 1.2rem; margin: 2rem 0 0;
              border-bottom: 1px solid #ddd; font: 14px system-ui, sans-serif; }
.proof-tabs button { border-radius: 6px 6px 0 0; border-bottom: none; padding: .4rem .9rem; }
@media screen { .section { page-break-before: auto; margin-top: 3rem; scroll-margin-top: 3.5rem; }
                .tab-panel > .section:first-child { margin-top: 1.5rem; }
                .cover { min-height: 0; padding-top: 1.5rem; } }
@media print { .proof-tools, .proof-tabs { display: none !important; } .tab-panel[hidden] { display: block !important; }
               .proof-hero { font-size: 40pt; } }
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
    scripts = ", ".join(_html.escape(x) for x in g.scripts)
    if g.stage is not None:
        rows.append(f'Design stage <b>{g.stage}</b> &mdash; {_html.escape(g.stage_name or "")}')
        if scripts:
            rows.append(f"Also proofed: {scripts} (no design-stage model yet &mdash; every {scripts} section shown)")
    elif scripts:
        rows.append(f"Design stage not determined (staging is Sinhala-only) &mdash; "
                    f"{scripts} proofed in full, not stage-gated")
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


def _section_html(s: Section, gate: Gate) -> str:
    feats = ""
    style = ""
    if s.features:
        feats = f' <span class="feat">{_html.escape(" ".join(s.features))}</span>'
        style = ' style="font-feature-settings: ' + ", ".join(f"&quot;{t}&quot; 1" for t in s.features) + '"'
    return (f'<div class="section"><h2>{_html.escape(s.title)}'
            + (f' <small>stage {s.min_stage}+</small>' if gate.gated and s.min_stage else "")
            + f'{feats}</h2><div class="proof-text" lang="{s.lang}"{style}>{s.html}</div></div>')


def build_html(family: str, style: str, font_href: str, sections: list[Section], gate: Gate,
               build: dict | None = None, glyphset_href: str | None = None,
               chrome: str = "", extra_css: str = "", scripts: list[str] | None = None,
               styles: Styles | None = None, hero_scripts: list[str] | None = None) -> str:
    """``chrome`` is site furniture (header/nav/warning) placed above the cover; ``extra_css``
    styles it. Both come from build_pages.py -- the engine itself knows nothing of the site.
    ``scripts`` (detected script keys) sorts sections into tabs; ``styles`` feeds the weight
    controls; ``hero_scripts`` picks the lines of the sample on top."""
    b = build or {}
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    meta_bits = [style]
    if b.get("version"):
        meta_bits.append(f"Version {_html.escape(str(b['version']))}")
    if b.get("commit_short"):
        meta_bits.append(f"commit {_html.escape(b['commit_short'])}")
    meta_bits.append(f"Type proof &mdash; generated {generated}")
    st = styles or Styles()
    faces = font_face(font_href)
    if glyphset_href:
        faces += "\n" + font_face(glyphset_href, "ProofGlyphset")
    for i, (_, href) in enumerate(st.statics):
        faces += "\n" + font_face(href, f"ProofStyle{i}")
    tabs = group_tabs(sections, scripts or [])
    tab_bar = ""
    if len(tabs) > 1:
        tab_bar = ('<div class="proof-tabs" role="tablist">' + "".join(
            f'<button type="button" role="tab" data-tab="{k}">{_html.escape(TAB_LABELS[k])}</button>'
            for k, _ in tabs) + "</div>")
    body = "\n".join(
        f'<div class="tab-panel" role="tabpanel" data-tab="{k}" id="tab-{k}">'
        + "\n".join(_section_html(s, gate) for s in secs) + "</div>"
        for k, secs in tabs)
    family_var = f':root {{ --proof-family: "ProofStyle{st.current}"; }}' if st.statics else ""
    return (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{_html.escape(family)} &mdash; proof</title>'
            f'<style>{faces}\n{family_var}\n{_CSS}\n{extra_css}</style></head><body>\n{chrome}\n'
            f'{_toolbar_html(st)}\n'
            f'<div class="cover"><h1>{_html.escape(family)}</h1>'
            f'<div class="meta">{"<br>".join(meta_bits)}</div>'
            f'{_hero_html(hero_scripts or [])}{_gate_html(gate)}</div>\n'
            f'{tab_bar}\n{body}\n<script>{_JS}</script>\n</body></html>')


# ── orchestration ───────────────────────────────────────────────────────────
@dataclass
class ProofPage:
    stem: str
    html_path: Path
    gate: Gate


def build_proof_pages(font_paths: list[Path], proof_dir: Path, fonts_dir: Path, *, family: str,
                      channel: str, build: dict | None = None, stage_override: int | None = None,
                      ungated: bool = False, only: set[str] | None = None,
                      gates: dict | None = None, chrome: str = "",
                      extra_css: str = "") -> list[ProofPage]:
    """Write one proof HTML per font into ``proof_dir``.

    Fonts are referenced by relative URL from ``fonts_dir`` (the caller copies them
    there), so pages are portable. The stage and the covered scripts are detected once from
    the union of all binaries -- a family has one of each -- and applied to every page.
    """
    g = gates or load_gates()
    stage = detect_stage(font_paths)
    scripts = detect_scripts(font_paths, g)
    if scripts and stage is not None and stage["n"] == 0 and not covers_sinhala(font_paths):
        stage = None    # a Tamil font with no Sinhala at all: the Sinhala model has nothing to say
    if stage_override is not None:
        stage = {"n": stage_override, "name": (stage or {}).get("name") or f"stage {stage_override}",
                 "next_gaps": []}
    pages: list[ProofPage] = []
    proof_dir.mkdir(parents=True, exist_ok=True)
    corpus = discover_sections(gates=g, stage=None if (ungated or not plan(channel, g)["gated"])
                               else (stage["n"] if stage else None))
    sections, gate = apply_gates(corpus, stage, channel, g, ungated=ungated, scripts=scripts)
    if only:
        unknown = only - {s.slug for s in corpus} - {GLYPHSET_SLUG, LATIN_WATERFALL_SLUG}
        if unknown:
            raise SystemExit(f"Unknown section(s): {', '.join(sorted(unknown))}")
        sections = [s for s in sections if s.slug in only]
    want_glyphset = (not only) or GLYPHSET_SLUG in only
    want_waterfall = "latin" in scripts and ((not only) or LATIN_WATERFALL_SLUG in only)
    if want_waterfall:
        gate.shown.append(LATIN_WATERFALL_SLUG)
    hero_scripts = (["sinhala"] if covers_sinhala(font_paths) else []) + scripts
    for fp in font_paths:
        page_sections = list(sections)
        patched_href = None
        if want_glyphset:
            patched_path = proof_dir / f"{fp.stem}.glyphset{fp.suffix}"
            sec, patched = build_glyphset_section(fp, patched_path)
            page_sections.insert(0, sec)
            patched_href = rel_href(proof_dir, patched or fp)
        if want_waterfall:
            cmap, _ = _cmap_and_order([fp])
            page_sections.insert(1 if want_glyphset else 0, build_latin_waterfall_section(cmap))
        styles = style_info(fp, font_paths, href=lambda p: rel_href(proof_dir, fonts_dir / p.name))
        html = build_html(family, fp.stem, rel_href(proof_dir, fonts_dir / fp.name), page_sections,
                          gate, build, patched_href, chrome, extra_css,
                          scripts=scripts, styles=styles, hero_scripts=hero_scripts)
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
