#!/usr/bin/env python3
"""sinhala_coverage.py — compute Sinhala design-stage coverage for a built font.

Called by the sibling ``build_manifest.py`` (Phase 4 of the tooling roadmap,
``docs/tooling-roadmap.md`` §4) to populate ``coverage.sinhala_design_stage`` in
``fontstatus.json``. Standalone by design, same contract as ``build_manifest.py``:
stdlib only, no network, no ``mnik`` import — reads its sibling ``stages.json`` off
disk. That file is a copy of the generated design-stage model authored in
``tools/sinhala-design-stages/`` (migrated from lanka-glyphsets 2026-07-18 — see
that directory's README for the model itself and how to regenerate it).

``stages.json`` has 110 glyph entries of three kinds, each needing a different check:

  - 80 entries carry a ``codepoint`` (types base/mark/vowel/sign/composite) — checked
    directly against the font's cmap. No glyph-naming convention involved, so this
    half is immune to naming-convention drift.
  - 21 ``form-family`` entries are composed base+mark ligatures (e.g. ටි/ඩි) — checked
    via a composed glyph name, built from a small **static, ported** consonant-short-
    name table (lanka-glyphsets' glyphsets/sinhala-0-kernel.yaml "Orthographical
    conjuncts" naming rule: drop the base's trailing "a", append a mark-suffix) and
    probed against the font's glyph order under several candidate spellings. The
    documented convention is a hyphenated ``{short}-sinh``; every real shipped font
    checked when this was written (aggnni, mandakini, gagan, singithi, sarani,
    dedigama — 2026-07-18) actually uses the bare ``{short}sinh`` form instead, so
    both (and two more fallbacks) are checked defensively.
  - 6 ``conjunct-system`` entries (the true ZWJ conjuncts: rakaransaya, yansaya,
    repaya, ksha, classic-conjuncts) + 1 no-host ``form-family`` (conjunct-i-forms) +
    3 ``process`` entries (completion-sweep, hal-sweep, kerning-pass) have **no
    structural data to check at all** — their real applicability lives in shaping
    exception-list *logic* (lanka-glyphsets' sinhala-glyph-chart tool), not inert
    data reachable from stages.json. These are always unverifiable (``None``), and
    since 6 of them are tagged kernel-level, ``kernel_complete`` can never honestly
    become ``true`` from this heuristic alone — see ``_classify`` below.
"""
from __future__ import annotations

import json
from pathlib import Path

_STAGES_PATH = Path(__file__).resolve().parent / "stages.json"
_NAMESPACE = "sinh"

# codepoint (upper-hex, e.g. "0DA7") -> lanka-glyphsets base glyph name (from
# glyphsets/sinhala-0-kernel.yaml's "Letters" category). Static, ported table —
# stable, documented spec; not fetched. Consonants only (vowels are never a
# form-family host in the current model).
_CONSONANT_NAME = {
    "0D9A": "ka", "0D9B": "kha", "0D9C": "ga", "0D9D": "gha", "0D9E": "nga", "0D9F": "nnga",
    "0DA0": "ca", "0DA1": "cha", "0DA2": "ja", "0DA3": "jha", "0DA4": "nya",
    "0DA5": "jnya", "0DA6": "nyja",  # core-level letters, but hosts of kernel-level families
    "0DA7": "tta", "0DA8": "ttha", "0DA9": "dda", "0DAA": "ddha", "0DAB": "nna", "0DAC": "nndda",
    "0DAD": "ta", "0DAE": "tha", "0DAF": "da", "0DB0": "dha", "0DB1": "na", "0DB3": "nda",
    "0DB4": "pa", "0DB5": "pha", "0DB6": "ba", "0DB7": "bha", "0DB8": "ma", "0DB9": "mba",
    "0DBA": "ya", "0DBB": "ra", "0DBD": "la", "0DC0": "va", "0DC1": "sha", "0DC2": "ssa",
    "0DC3": "sa", "0DC4": "ha", "0DC5": "lla", "0DC6": "fa",
}

# stages.json form-family "mark" -> composed-name suffix, per lanka-glyphsets'
# "drop trailing a, add sign abbreviation" rule. Only these 3 marks are ever used
# by a form-family in the current model (verified against stages.json directly).
_MARK_SUFFIX = {"ි": "I", "ු": "U", "්": ""}


def _short_name(codepoint_hex: str | None) -> str | None:
    if not codepoint_hex:
        return None
    name = _CONSONANT_NAME.get(codepoint_hex.upper())
    if name is None:
        return None
    return name[:-1] if name.endswith("a") else name


def _candidates(short: str) -> list[str]:
    return [f"{short}{_NAMESPACE}", f"{short}-{_NAMESPACE}", f"{_NAMESPACE}.{short}", short]


def load_stage_model(path: Path | None = None) -> dict | None:
    """Load stages.json (best-effort; None on any failure)."""
    p = path or _STAGES_PATH
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _check_codepoint_entry(entry: dict, cmap: set[int]) -> bool | None:
    cp = entry.get("codepoint")
    if not cp:
        return None
    try:
        return int(cp, 16) in cmap
    except ValueError:
        return None


def _composite_satisfied(key: str, entries: dict, cmap: set[int], memo: dict[str, bool | None]) -> bool | None:
    """A composite (e.g. ේ = ෙ + ්) is satisfied if the font maps the precomposed
    codepoint directly, OR can build it by decomposition -- Sinhala shaping engines
    normally decompose these and never need a direct cmap entry, so checking the
    precomposed codepoint alone under-reports on essentially every real font.
    """
    if key in memo:
        return memo[key]
    entry = entries[key]
    cp = entry.get("codepoint")
    if cp and int(cp, 16) in cmap:
        memo[key] = True
        return True
    parents = entry.get("parents") or []
    if not parents:
        memo[key] = False
        return False
    result: bool | None = True
    for p in parents:
        pe = entries.get(p)
        if pe is None:
            result = None
            continue
        if pe.get("type") == "composite":
            r = _composite_satisfied(p, entries, cmap, memo)
        else:
            r = _check_codepoint_entry(pe, cmap)
        if r is False:
            result = False
            break
        if r is None and result is not False:
            result = None
    memo[key] = result
    return result


def _check_form_family(entry: dict, glyphs_index: dict, glyph_order_lower: set[str]) -> bool | None:
    hosts = entry.get("hosts") or []
    mark = entry.get("mark")
    if not hosts or mark not in _MARK_SUFFIX:
        return None  # no structural data: conjunct-system, or a no-host form-family
    suffix = _MARK_SUFFIX[mark]
    for host_char in hosts:
        host = glyphs_index.get(host_char) or {}
        short = _short_name(host.get("codepoint"))
        if short is None:
            return None  # host isn't a resolvable consonant -- can't judge
        if not any(name.lower() in glyph_order_lower for name in _candidates(short + suffix)):
            return False
    return True


def _host_glyph_present(host_char: str, suffix: str, glyphs_index: dict, glyph_order_lower: set[str]) -> bool | None:
    host = glyphs_index.get(host_char) or {}
    short = _short_name(host.get("codepoint"))
    if short is None:
        return None
    return any(name.lower() in glyph_order_lower for name in _candidates(short + suffix))


def _form_family_satisfied_by(entry: dict, n: int, glyphs_index: dict, glyph_order_lower: set[str]) -> bool | None:
    """Whether a form-family's hosts *introduced by stage n* are all present.

    A form-family's `hosts` list accumulates across stages (e.g. fam-i-tthi is
    declared at stage 1 via its first host ඪ, but ඨ/ථ/ඵ only join in stages 5-6 --
    see stages.json's own `ai.construction` prose). So the cumulative stage-boundary
    check must only require hosts whose *own* `stage` is already <= n, not the
    family's full (eventual) host list -- that full-list check is what
    `_check_form_family` (unbounded by n) is for, used separately for
    `kernel_checkable_complete`.
    """
    hosts = entry.get("hosts") or []
    mark = entry.get("mark")
    if not hosts or mark not in _MARK_SUFFIX:
        return None
    suffix = _MARK_SUFFIX[mark]
    due_hosts = [h for h in hosts if (glyphs_index.get(h) or {}).get("stage", 0) <= n]
    if not due_hosts:
        return None  # nothing to check yet at this stage
    results = [_host_glyph_present(h, suffix, glyphs_index, glyph_order_lower) for h in due_hosts]
    if any(r is False for r in results):
        return False
    if all(r is None for r in results):
        return None
    return True


def _evaluate(stage_model: dict, cmap: set[int], glyph_order_lower: set[str]) -> dict[str, bool | None]:
    entries = stage_model["glyphs"]
    result: dict[str, bool | None] = {}
    composite_memo: dict[str, bool | None] = {}
    for key, entry in entries.items():
        etype = entry.get("type")
        if etype == "composite":
            result[key] = _composite_satisfied(key, entries, cmap, composite_memo)
        elif etype in ("base", "mark", "vowel", "sign"):
            result[key] = _check_codepoint_entry(entry, cmap)
        elif etype == "form-family":
            result[key] = _check_form_family(entry, entries, glyph_order_lower)
        else:  # conjunct-system, process -- always unverifiable from static data
            result[key] = None
    return result


def _classify(glyphs_have: dict[str, bool | None], stage_model: dict,
              glyphs_index: dict, glyph_order_lower: set[str]) -> dict:
    """Highest cumulative stage satisfied, plus honest kernel-completeness fields.

    Cumulative semantics: gate on each entry's own `stage` number (which already
    encodes design-dependency order), not a `parents`-transitive-closure walk --
    equivalent, and much simpler. Unverifiable (None) entries don't block the
    cumulative stage number (an optimistic read -- that boundary only needs to
    separate `sketch` from not-sketch, see docs/tooling-roadmap.md §4); the 6
    kernel-level entries that are always unverifiable are surfaced separately so
    `kernel_complete` never silently overclaims.

    Form-family entries are re-checked stage-by-stage via
    `_form_family_satisfied_by` (only hosts *due* by that stage), instead of
    reusing the strict, full-host-list `glyphs_have` result computed by
    `_evaluate` -- that strict result is still used below for
    `kernel_checkable_complete`, which intentionally does want the full list.
    """
    entries = stage_model["glyphs"]
    stages = stage_model["stages"]
    satisfied = stages[0]
    for stage in stages:
        n = stage["n"]
        in_scope = [k for k, v in entries.items() if v.get("stage", 0) <= n]
        ok = True
        for k in in_scope:
            if entries[k].get("type") == "form-family":
                v = _form_family_satisfied_by(entries[k], n, glyphs_index, glyph_order_lower)
            else:
                v = glyphs_have.get(k)
            if v is False:
                ok = False
                break
        if ok:
            satisfied = stage
        else:
            break

    kernel_keys = [k for k, v in entries.items() if v.get("level") == "sinhala-0-kernel"]
    checkable = [k for k in kernel_keys if glyphs_have.get(k) is not None]
    unverified = sorted(k for k in kernel_keys if glyphs_have.get(k) is None)
    kernel_checkable_complete = bool(checkable) and all(glyphs_have.get(k) for k in checkable)

    return {
        "n": satisfied["n"],
        "name": satisfied["name"],
        "cumulative": satisfied["cumulative_count"],
        "total": satisfied["total"],
        "gate_met": True,  # true by construction -- `satisfied` only advances when it holds
        "kernel_checkable_complete": kernel_checkable_complete,
        "kernel_complete": None,  # stays null until real shaping-based verification exists
        "unverified_kernel_entries": unverified,
    }


def compute(font_paths: list[Path], cmap_fn, glyph_order_fn,
            stage_model: dict | None = None) -> dict | None:
    """Compute sinhala_design_stage coverage from a set of built font binaries.

    cmap_fn/glyph_order_fn are injected (build_manifest.py's `_font_cmap`/
    `_font_glyph_order`) so this module reuses their best-effort font-opening
    logic rather than duplicating it. Coverage is the UNION of cmap/glyph-order
    across every file passed in -- a variable font's single file already carries
    everything; for statics this is the most defensible "does this family
    support X" reading absent any existing precedent either way.
    """
    model = stage_model if stage_model is not None else load_stage_model()
    if model is None or not font_paths:
        return None
    cmap: set[int] = set()
    glyph_order: set[str] = set()
    for p in font_paths:
        cmap |= cmap_fn(p)
        glyph_order |= glyph_order_fn(p)
    if not cmap and not glyph_order:
        return None
    # Case-insensitive: real fonts diverge from the documented naming convention
    # (e.g. aggnni-font uses "dDhIsinh", not the yaml's literal "ddhIsinh") --
    # this is one of several surveyed Sinhala naming conventions across the fleet.
    glyph_order_lower = {g.lower() for g in glyph_order}
    have = _evaluate(model, cmap, glyph_order_lower)
    return _classify(have, model, model["glyphs"], glyph_order_lower)
