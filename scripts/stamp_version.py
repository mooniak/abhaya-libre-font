#!/usr/bin/env python3
"""stamp_version.py — write the OpenFV name ID 5 into built fonts, per channel.

Phase 3 of the tooling roadmap. Run in CI **after `make build`, before test/manifest**,
so QA and the emitted ``fontstatus.json`` see the stamped, channel-correct version.
Makes ``openfv.status``/``source`` real (the Phase 2 emitter only *reads* name ID 5).

Standalone by design (fontTools + stdlib only, no mnik import), and reuses the channel
derivation + OpenFV helpers from the sibling ``build_manifest.py``:

  canary  -> ``Version X.YYY; [<sha7>]-dev``   base = the source version already in the font
  dev     -> ``Version X.YYY; DEV``            base = the ``vX.YYY-dev.N`` tag
  release -> ``Version X.YYY``  (bare)         base = the ``vX.YYY`` tag
  local   -> no-op (nothing published locally)

Usage (in a repo root, after the build):  python3 scripts/stamp_version.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_manifest as bm  # noqa: E402  (channel derivation + OpenFV regexes)


def _base_from_tag(env: dict) -> str | None:
    """`vX.YYY` / `vX.YYY-dev.N` tag -> `X.YYY` (the OpenFV number)."""
    m = bm._OPENFV_VER.search((env.get("GITHUB_REF_NAME") or "").lstrip("v"))
    return m.group(0) if m else None


def _base_from_font(font) -> str | None:
    """The source-declared version already in the font -> `X.YYY`."""
    if "head" not in font:
        return None
    rev = font["head"].fontRevision
    major = int(rev)
    return f"{major}.{round((rev - major) * 1000):03d}"


def _name5(channel: str, base: str, sha: str) -> str:
    if channel == "canary":
        return f"Version {base}; [{sha[:7]}]-dev" if sha else f"Version {base}; DEV"
    if channel == "dev":
        return f"Version {base}; DEV"
    return f"Version {base}"  # release: bare (absence of a status word means release)


def stamp_font(path: Path, channel: str, tag_base: str | None, sha: str) -> str | None:
    from fontTools.ttLib import TTFont
    font = TTFont(str(path))
    try:
        base = tag_base or _base_from_font(font)
        if not base:
            return None
        value = _name5(channel, base, sha)
        # name ID 5 on the Windows (3,1,0x409) and Mac (1,0,0) records.
        font["name"].setName(value, 5, 3, 1, 0x409)
        font["name"].setName(value, 5, 1, 0, 0)
        major, minor = base.split(".")
        font["head"].fontRevision = int(major) + int(minor) / 1000
        font.save(str(path))
        return value
    finally:
        font.close()


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    env = dict(os.environ)
    channel = bm._derive_channel(env, env.get("MNIK_CHANNEL") or None)
    if channel == "local":
        print("stamp: local build — nothing to stamp")
        return 0
    sha = env.get("GITHUB_SHA") or ""
    tag_base = _base_from_tag(env) if channel in ("dev", "release") else None
    repo = Path(argv[0]) if argv else Path(".")
    fonts_root = repo / "fonts"
    fonts = ([p for p in sorted(fonts_root.rglob("*"))
              if p.is_file() and p.suffix.lower() in bm.FONT_EXTS]
             if fonts_root.is_dir() else [])
    n = 0
    for p in fonts:
        try:
            value = stamp_font(p, channel, tag_base, sha)
            if value:
                n += 1
                print(f"  {p.relative_to(repo)} -> {value}")
        except Exception as e:  # never fail the build on a single font
            print(f"  {p}: SKIP ({e})")
    print(f"stamp: channel={channel}, stamped {n} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
