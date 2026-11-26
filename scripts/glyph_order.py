#!/usr/bin/env python3
"""Sort a font's glyphs into the Mooniak glyph order: the order of Abhaya Libre.

Every Mooniak font keeps its glyphs in the order of Abhaya Libre's source
(abhaya-libre-font, sources/AbhayaLibre.glyphspackage/order.plist), so the Glyphs
font view, the built font's glyph IDs and every proof list the same glyphs in the
same place in every font. The order ships as ``glyph-order.txt`` next to this file.

How a font's order is worked out:

  * a glyph Abhaya Libre has goes where it is in Abhaya Libre;
  * a glyph Abhaya Libre doesn't have (a font-specific alternate, an extra symbol)
    goes after its base glyph (``ka-sinh.ss01`` after ``ka-sinh``) when the base is
    in Abhaya Libre, else after the Abhaya Libre glyph it follows now; several such
    glyphs keep their current order among themselves.

What gets written (glyphs are only moved; nothing else changes):

  * .glyphspackage: ``order.plist``;
  * .glyphs: the order of the ``glyphs`` list;
  * either, if it has one: the font's ``glyphOrder`` custom parameter (which
    overrides the file order on export), set to the same order;
  * UFO (also the UFOs a .designspace lists): ``public.glyphOrder`` in lib.plist.

Usage, from a font repo (the sources in sources/config*.yaml):

    python3 scripts/glyph_order.py            # check; exit 1 if a source is out of order
    python3 scripts/glyph_order.py --write    # sort the sources
    python3 scripts/glyph_order.py sources/Foo.glyphspackage ...

Close the font in Glyphs.app first: Glyphs saves its own order over the file.

This file and glyph-order.txt are byte-identical copies of
mooniak-font-tools/mnik/tools/glyphorder/ (where ``mnik glyph-order`` runs it over
every font repo); edit them there and sync the template.
"""
from __future__ import annotations

import argparse
import plistlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFERENCE = HERE / "glyph-order.txt"

_BARE = re.compile(r"[A-Za-z_.][A-Za-z0-9_.]*")


# ── the reference order ────────────────────────────────────────────────────────

def load_reference(path: Path | None = None) -> list[str]:
    """The Abhaya Libre glyph order: one name per line, '#' lines are comments."""
    text = Path(path or REFERENCE).read_text(encoding="utf-8")
    return [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]


def merged_order(current: list[str], reference: list[str]) -> list[str]:
    """``current`` re-sorted by ``reference`` (see the module docstring)."""
    ref = {n: i for i, n in enumerate(reference)}
    keys = {}
    anchor = -1
    for seq, name in enumerate(current):
        if name in ref:
            anchor = ref[name]
            keys[name] = (ref[name], 0, 0)
            continue
        base = name.split(".", 1)[0]
        keys[name] = (ref.get(base, anchor), 1, seq)
    seen = set()
    unique = [n for n in current if not (n in seen or seen.add(n))]
    return sorted(unique, key=keys.__getitem__)


# ── the sources a repo builds ──────────────────────────────────────────────────

def _config_sources(config: Path) -> list[str]:
    """The ``sources:`` list of a gftools builder config (no YAML library needed)."""
    out, inside = [], False
    for line in config.read_text(encoding="utf-8").splitlines():
        if re.match(r"^sources\s*:", line):
            inside = True
            inline = line.split(":", 1)[1].strip()
            if inline.startswith("["):
                return [s.strip(" '\"") for s in inline.strip("[]").split(",") if s.strip()]
            continue
        if inside:
            m = re.match(r"^\s+-\s*(.+?)\s*$", line)
            if m:
                out.append(m.group(1).strip("'\""))
            elif line.strip() and not line.startswith((" ", "\t", "#")):
                break
    return out


def _designspace_ufos(ds: Path) -> list[Path]:
    root = ET.parse(ds).getroot()
    return [(ds.parent / s.get("filename")).resolve()
            for s in root.iter("source") if s.get("filename")]


def font_sources(repo: Path) -> list[Path]:
    """The Glyphs/UFO sources a repo builds (sources/config*.yaml), designspaces
    resolved to their UFOs. When the config names none that exist (or only the
    template's MyFont placeholder), every Glyphs source in sources/ instead."""
    src = repo / "sources"
    names = []
    for cfg in sorted(src.glob("config*.yaml")):
        names += _config_sources(cfg)
    names = [n for n in names if (src / n).exists() and not n.startswith("MyFont")]
    if not names:
        names = sorted(p.name for p in src.glob("*") if p.suffix in (".glyphs", ".glyphspackage")
                       and "(Autosaved)" not in p.name)
    out: list[Path] = []
    for n in names:
        p = (src / n).resolve()
        for q in (_designspace_ufos(p) if p.suffix == ".designspace" and p.is_file() else [p]):
            if q.exists() and q not in out:
                out.append(q)
    return out


# ── Glyphs files ───────────────────────────────────────────────────────────────

def _openstep():
    import openstep_plist  # ships with glyphsLib (gftools)
    return openstep_plist


def _token(name: str) -> str:
    """How a glyph name is written in a Glyphs plist (quoted unless plain)."""
    if _BARE.fullmatch(name):
        return name
    return '"' + name.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _untoken(tok: str) -> str:
    tok = tok.strip()
    if tok.startswith('"') and tok.endswith('"'):
        return _openstep().loads(tok)
    return tok


def _match_brace(text: str, i: int) -> int:
    """Index just past the '}' closing the '{' at ``i`` (quoted strings skipped)."""
    depth, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == '"':
            i += 1
            while text[i] != '"':
                i += 2 if text[i] == "\\" else 1
        elif c in "{(":
            depth += 1
        elif c in "})":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced braces")


def _split_glyphs(text: str) -> tuple[int, int, list[str]]:
    """(start, end, chunks) of the top-level ``glyphs = (...)`` list of a .glyphs file."""
    m = re.search(r"^glyphs = \(\n", text, re.M)
    if not m:
        raise ValueError("no glyphs list")
    i, chunks = m.end(), []
    while True:
        while text[i] in " \t\r\n":
            i += 1
        if text[i] == ")":
            break
        if text[i] != "{":
            raise ValueError(f"unexpected {text[i]!r} in the glyphs list")
        j = _match_brace(text, i)
        chunks.append(text[i:j])
        i = j
        if text[i] == ",":
            i += 1
    start = m.end()
    if text[start:i] != ",\n".join(chunks) + "\n":
        raise ValueError("glyphs list isn't in the one-glyph-per-block layout Glyphs writes")
    return start, i, chunks


_PARAM = re.compile(r"(name = glyphOrder;\nvalue = \()(.*?)(\);)", re.S)


def _param_names(head: str) -> list[str] | None:
    """The font's glyphOrder custom parameter (first one in ``head``), or None."""
    m = _PARAM.search(head)
    if not m:
        return None
    return [_untoken(t) for t in m.group(2).split(",\n") if t.strip()]


def _set_param(head: str, tokens: list[str]) -> str:
    return _PARAM.sub(lambda m: m.group(1) + "\n" + ",\n".join(tokens) + "\n" + m.group(3),
                      head, count=1)


def _effective(file_order: list[str], param: list[str] | None) -> list[str]:
    """What export uses: the glyphOrder parameter if there is one (glyphs it leaves
    out follow, in file order), else the file order."""
    if param is None:
        return list(file_order)
    have = set(file_order)
    listed = [n for n in param if n in have]
    seen = set(listed)
    return listed + [n for n in file_order if n not in seen]


class GlyphsPackage:
    def __init__(self, path: Path):
        self.path = path
        self.order_file = path / "order.plist"
        self.info_file = path / "fontinfo.plist"
        text = self.order_file.read_text(encoding="utf-8")
        body = text.strip()
        if not (body.startswith("(") and body.endswith(")")):
            raise ValueError("order.plist isn't a list")
        toks = [t.strip() for t in body[1:-1].split(",\n") if t.strip()]
        self.tokens = {_untoken(t): t for t in toks}
        self.file_order = list(self.tokens)
        # glyph files order.plist doesn't list (Glyphs appends them)
        for g in sorted((path / "glyphs").glob("*.glyph")):
            name = re.search(r"^glyphname = (.+);$", g.read_text(encoding="utf-8"), re.M)
            if name:
                n = _untoken(name.group(1))
                if n not in self.tokens:
                    self.tokens[n] = name.group(1)
                    self.file_order.append(n)
        self.info = self.info_file.read_text(encoding="utf-8")
        self.param = _param_names(self.info)

    def order(self) -> list[str]:
        return _effective(self.file_order, self.param)

    def in_order(self, wanted: list[str]) -> bool:
        return self.file_order == wanted and self.param in (None, wanted)

    def write(self, wanted: list[str]) -> None:
        toks = [self.tokens[n] for n in wanted]
        self.order_file.write_text("(\n" + ",\n".join(toks) + "\n)", encoding="utf-8")
        if self.param is not None:
            self.info_file.write_text(_set_param(self.info, toks), encoding="utf-8")
        _verify_glyphs_package(self.path, wanted, self.param is not None)


def _verify_glyphs_package(path: Path, wanted: list[str], param: bool) -> None:
    op = _openstep()
    got = list(op.loads((path / "order.plist").read_text(encoding="utf-8")))
    assert got == wanted, f"{path.name}: order.plist didn't come out as planned"
    if param:
        info = op.loads((path / "fontinfo.plist").read_text(encoding="utf-8"))
        vals = [p["value"] for p in info.get("customParameters", []) if p.get("name") == "glyphOrder"]
        assert list(vals[0]) == wanted, f"{path.name}: glyphOrder parameter didn't come out as planned"


class GlyphsFile:
    def __init__(self, path: Path):
        self.path = path
        self.text = path.read_text(encoding="utf-8")
        self.start, self.end, self.chunks = _split_glyphs(self.text)
        names = []
        self.tokens = {}
        for c in self.chunks:
            m = re.search(r"^glyphname = (.+);$", c, re.M)
            if not m:
                raise ValueError("a glyph without a glyphname")
            n = _untoken(m.group(1))
            names.append(n)
            self.tokens[n] = m.group(1)
        self.file_order = names
        self.by_name = dict(zip(names, self.chunks))
        self.param = _param_names(self.text[:self.start])

    def order(self) -> list[str]:
        return _effective(self.file_order, self.param)

    def in_order(self, wanted: list[str]) -> bool:
        return self.file_order == wanted and self.param in (None, wanted)

    def write(self, wanted: list[str]) -> None:
        if len(set(self.file_order)) != len(self.file_order):
            raise ValueError("duplicate glyph names: fix those first")
        head = self.text[:self.start]
        if self.param is not None:
            head = _set_param(head, [self.tokens[n] for n in wanted])
        body = ",\n".join(self.by_name[n] for n in wanted) + "\n"
        new = head + body + self.text[self.end:]
        # check before writing: same font, only the glyph order differs
        op = _openstep()
        before, after = op.loads(self.text), op.loads(new)
        assert [g["glyphname"] for g in after["glyphs"]] == wanted
        key = lambda g: g["glyphname"]  # noqa: E731
        assert sorted(before["glyphs"], key=key) == sorted(after["glyphs"], key=key)
        for d in (before, after):
            d.pop("glyphs")
            for p in d.get("customParameters", []):
                if p.get("name") == "glyphOrder":
                    p["value"] = None
        assert before == after, "something other than the glyph order would change"
        self.path.write_text(new, encoding="utf-8")


class UFO:
    def __init__(self, path: Path):
        self.path = path
        self.lib_file = path / "lib.plist"
        self.lib = plistlib.loads(self.lib_file.read_bytes()) if self.lib_file.exists() else {}
        glyphs = plistlib.loads((path / "glyphs" / "contents.plist").read_bytes())
        listed = [n for n in self.lib.get("public.glyphOrder", []) if n in glyphs]
        seen = set(listed)
        # ufo2ft puts glyphs public.glyphOrder leaves out at the end, sorted
        self.file_order = listed + sorted(n for n in glyphs if n not in seen)
        self.raw = self.lib.get("public.glyphOrder")

    def order(self) -> list[str]:
        return self.file_order

    def in_order(self, wanted: list[str]) -> bool:
        return self.raw == wanted

    def write(self, wanted: list[str]) -> None:
        self.lib["public.glyphOrder"] = wanted
        try:  # the plist writer ufoLib uses, so lib.plist keeps its layout
            from fontTools.misc import plistlib as ft_plistlib
            data = ft_plistlib.dumps(self.lib)
        except ImportError:
            data = plistlib.dumps(self.lib)
        self.lib_file.write_bytes(data)


def open_source(path: Path):
    if path.suffix == ".glyphspackage":
        return GlyphsPackage(path)
    if path.suffix == ".glyphs":
        return GlyphsFile(path)
    if path.suffix == ".ufo":
        return UFO(path)
    raise ValueError(f"not a Glyphs or UFO source: {path.name}")


# ── check / sort ───────────────────────────────────────────────────────────────

def plan(path: Path, reference: list[str]) -> dict:
    """What sorting one source would do (no writes)."""
    src = open_source(path)
    current = src.order()
    wanted = merged_order(current, reference)
    ref = set(reference)
    moved = sum(1 for a, b in zip(current, wanted) if a != b)
    return {
        "path": path, "source": src, "wanted": wanted, "ok": src.in_order(wanted),
        "glyphs": len(wanted), "moved": moved,
        "extra": [n for n in wanted if n not in ref],
        "param": getattr(src, "param", None) is not None,
    }


def describe(p: dict) -> str:
    what = "in Abhaya Libre order" if p["ok"] else (
        f"{p['moved']} of {p['glyphs']} glyphs out of place" if p["moved"]
        else "glyphOrder parameter differs from the file order")
    extra = f"; {len(p['extra'])} not in Abhaya Libre" if p["extra"] else ""
    return f"{p['path'].name}: {what}{extra}"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("sources", nargs="*", type=Path,
                    help="Glyphs/UFO/designspace sources (default: sources/config*.yaml)")
    ap.add_argument("--write", action="store_true", help="sort the sources (default: check only)")
    ap.add_argument("--reference", type=Path, default=REFERENCE, help="glyph order file")
    args = ap.parse_args(argv)
    reference = load_reference(args.reference)
    paths: list[Path] = []
    for s in args.sources or font_sources(Path.cwd()):
        s = Path(s).resolve()
        paths += _designspace_ufos(s) if s.suffix == ".designspace" else [s]
    if not paths:
        print("no sources found (sources/config*.yaml)")
        return 2
    bad = 0
    for path in paths:
        p = plan(path, reference)
        print(("✓ " if p["ok"] else "✗ ") + describe(p))
        if p["ok"]:
            continue
        if args.write:
            p["source"].write(p["wanted"])
            print(f"  sorted {path.name}")
        else:
            bad += 1
    if bad:
        print("sort with --write (make glyph-order WRITE=1); close the font in Glyphs.app first")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
