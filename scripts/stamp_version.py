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

Also suffixes the channel onto the **menu-facing** names — family (ID 1/16), full name
(ID 4), PostScript name (ID 6/25), and any fvar named-instance PostScript names — so a
canary/dev build doesn't sit name-identical to a release build in the OS font menu. See
``docs/channels-and-versioning.md`` ("The channel also shows in the font menu"). Style/
subfamily (ID 2/17) is left untouched. release writes bare names (no suffix), matching
the same "absence means release" rule as name ID 5.

**License (every build).** If ``fontpackage.json`` declares
``"tier": "premium"``, name ID 13 is set to the Mooniak Fonts EULA notice and name ID 14
(license URL) is removed — whatever the source said. A premium binary must never carry an
OFL grant, so a failure here fails the step (unlike the version stamp, which never does).
Free fonts are left exactly as built.

Filenames: with ``--rename-files`` (what ``mnik build`` uses) the channel suffix is also put
into the built files' names — ``AbhayaLibre-Bold.ttf`` -> ``AbhayaLibreDEV-Bold.ttf``,
``AbhayaLibre[wght].ttf`` -> ``AbhayaLibreCANARY[wght].ttf`` — matching the PostScript name.
CI doesn't pass it (its asset names are unchanged).

There is no "local" channel: the channel is always one of canary | dev | release, from the CI
trigger or ``MNIK_CHANNEL`` (``mnik build`` asks you).

Usage (in a repo root, after the build):  python3 scripts/stamp_version.py [repo] [--rename-files]
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_manifest as bm  # noqa: E402  (channel derivation + OpenFV regexes)


# Keep in step with mooniak-font-tools/mnik/tiers.py (PREMIUM_LICENSE_DESCRIPTION).
PREMIUM_LICENSE_DESCRIPTION = (
    "This Font Software is licensed under the Mooniak Fonts EULA. "
    "It is not open source and is not licensed under the SIL Open Font License. "
    "For licensing, contact hello@mooniak.com."
)


def _tier(repo: Path) -> str | None:
    try:
        return json.loads((repo / "fontpackage.json").read_text(encoding="utf-8")).get("tier")
    except (OSError, json.JSONDecodeError):
        return None


def stamp_license(path: Path) -> None:
    """Premium: name ID 13 = the EULA notice on every platform; drop name ID 14."""
    from fontTools.ttLib import TTFont
    font = TTFont(str(path))
    try:
        name = font["name"]
        name.removeNames(nameID=13)
        name.removeNames(nameID=14)
        for pid, eid, lid in ((3, 1, 0x409), (1, 0, 0)):
            name.setName(PREMIUM_LICENSE_DESCRIPTION, 13, pid, eid, lid)
        font.save(str(path))
    finally:
        font.close()


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


# Menu-facing family suffix per channel — UPPERCASE, deliberately visible (not blended
# in with normal Title Case family names). release: "" (bare — absence means release).
CHANNEL_SUFFIX = {"canary": "CANARY", "dev": "DEV", "release": ""}

_NAME_PLATFORMS = ((3, 1, 0x409), (1, 0, 0))  # Windows, Mac


def _strip_suffix(value: str, suffix: str) -> str:
    """Undo a previous stamp of this exact suffix, so re-stamping is idempotent."""
    if suffix and value.endswith(f" {suffix}"):
        return value[: -(len(suffix) + 1)]
    return value


def _rebase(value: str | None, clean_prefix: str, new_prefix: str) -> str | None:
    """Swap a leading `clean_prefix` for `new_prefix`, first undoing a previous
    stamp if `value` already starts with `new_prefix` (idempotent re-stamping).
    Returns None if `value` doesn't start with either — caller leaves it alone.
    """
    if value is None:
        return None
    if value.startswith(new_prefix):
        value = clean_prefix + value[len(new_prefix):]
    if not value.startswith(clean_prefix):
        return None
    return new_prefix + value[len(clean_prefix):]


def _stamp_channel_names(font, channel: str) -> None:
    """Suffix family (ID 1/16), full name (ID 4), and PostScript name (ID 6/25 +
    fvar instance PS names) by channel, so canary/dev/release builds of the same
    font are distinguishable in the OS font menu instead of name-identical.
    Style/subfamily (ID 2/17) is left untouched, so weight/style linking still
    works within each channel's own family.
    """
    suffix = CHANNEL_SUFFIX.get(channel, "")
    if not suffix:
        return  # release: bare names, nothing to do
    name = font["name"]
    family = name.getDebugName(1)
    if family is None:
        return
    family = _strip_suffix(family, suffix)
    new_family = f"{family} {suffix}"

    typo_family = name.getDebugName(16)
    if typo_family is not None:
        typo_family = _strip_suffix(typo_family, suffix)
        new_typo_family = f"{typo_family} {suffix}"
    else:
        new_typo_family = None

    # PostScript-family names (ID 6/25 + fvar instances) are rooted in the
    # *typographic* family when one exists, not ID 1 — a VF whose default
    # instance isn't Regular bakes its style into ID 1 (e.g. "Gemunu Libre
    # Light Extra"), but ID 6/25 stay rooted in the clean typographic family
    # ("GemunuLibre"). Falls back to ID 1 for fonts with no ID 16 at all.
    ps_root = (typo_family or family).replace(" ", "")
    new_ps_root = (new_typo_family or new_family).replace(" ", "")

    full = _rebase(name.getDebugName(4), family, new_family)
    ps = _rebase(name.getDebugName(6), ps_root, new_ps_root)
    var_prefix = _rebase(name.getDebugName(25), ps_root, new_ps_root)

    for pid, eid, lid in _NAME_PLATFORMS:
        name.setName(new_family, 1, pid, eid, lid)
        if new_typo_family is not None:
            name.setName(new_typo_family, 16, pid, eid, lid)
        if full is not None:
            name.setName(full, 4, pid, eid, lid)
        if ps is not None:
            name.setName(ps, 6, pid, eid, lid)
        if var_prefix is not None:
            name.setName(var_prefix, 25, pid, eid, lid)

    # Named instances (variable fonts) often carry their own PostScript-name
    # record distinct from ID 6 — suffix those too, or non-default instances
    # would silently stay unstamped.
    if "fvar" in font:
        for inst in font["fvar"].instances:
            nid = inst.postscriptNameID
            if nid in (0xFFFF, None, 6):
                continue
            new = _rebase(name.getDebugName(nid), ps_root, new_ps_root)
            if new is None:
                continue
            for pid, eid, lid in _NAME_PLATFORMS:
                name.setName(new, nid, pid, eid, lid)


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
        _stamp_channel_names(font, channel)
        major, minor = base.split(".")
        font["head"].fontRevision = int(major) + int(minor) / 1000
        font.save(str(path))
        return value
    finally:
        font.close()


def channel_filename(name: str, channel: str) -> str:
    """`AbhayaLibre-Bold.ttf` -> `AbhayaLibreDEV-Bold.ttf` (suffix goes on the family
    root, before the first `-` or `[`). release / already-suffixed names are unchanged."""
    suffix = CHANNEL_SUFFIX.get(channel, "")
    if not suffix:
        return name
    m = re.match(r"^([^-\[.]+)(.*)$", name)
    if not m or m.group(1).endswith(suffix):
        return name
    return m.group(1) + suffix + m.group(2)


def rename_for_channel(path: Path, channel: str) -> Path:
    new = path.with_name(channel_filename(path.name, channel))
    if new != path:
        path.rename(new)
    return new


def list_fonts(repo: Path) -> list[Path]:
    root = repo / "fonts"
    return ([p for p in sorted(root.rglob("*"))
             if p.is_file() and p.suffix.lower() in bm.FONT_EXTS] if root.is_dir() else [])


def stamp_repo(repo: Path, channel: str, sha: str = "", tag_base: str | None = None,
               rename: bool = False, log=print) -> int:
    """Stamp every built font in ``repo/fonts``: premium license, then version + names
    (+ filenames if ``rename``) for ``channel``. Returns the number of fonts stamped.
    Raises ValueError for an unknown channel; a premium license failure raises RuntimeError.
    """
    if channel not in CHANNEL_SUFFIX:
        raise ValueError(f"unknown channel {channel!r} (use canary | dev | release)")
    fonts = list_fonts(repo)
    tier = _tier(repo)
    if tier == "premium":
        failed = []
        for p in fonts:
            try:
                stamp_license(p)
            except Exception as e:
                failed.append(f"{p.relative_to(repo)} ({e})")
        log(f"stamp: premium — Mooniak Fonts EULA license stamped into "
            f"{len(fonts) - len(failed)} file(s)")
        if failed:
            raise RuntimeError("could not stamp the EULA license into: " + ", ".join(failed))
    elif tier is None:
        log("stamp: WARNING — fontpackage.json declares no 'tier' (free|premium); "
            "license strings left as built")
    n = 0
    for p in fonts:
        try:
            value = stamp_font(p, channel, tag_base, sha)
            if value:
                n += 1
                q = rename_for_channel(p, channel) if rename else p
                log(f"  {q.relative_to(repo)} -> {value}")
        except Exception as e:  # never fail the build on a single font
            log(f"  {p}: SKIP ({e})")
    log(f"stamp: channel={channel}, stamped {n} file(s)")
    return n


def main(argv=None) -> int:
    argv = list(argv if argv is not None else sys.argv[1:])
    rename = "--rename-files" in argv
    argv = [a for a in argv if a != "--rename-files"]
    env = dict(os.environ)
    try:
        channel = bm._derive_channel(env, env.get("MNIK_CHANNEL") or None)
    except ValueError as e:
        print(f"stamp: ERROR — {e}")
        return 1
    repo = Path(argv[0]) if argv else Path(".")
    sha = env.get("GITHUB_SHA") or ""
    tag_base = _base_from_tag(env) if channel in ("dev", "release") else None
    try:
        stamp_repo(repo, channel, sha=sha, tag_base=tag_base, rename=rename)
    except (ValueError, RuntimeError) as e:
        print(f"stamp: ERROR — {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
