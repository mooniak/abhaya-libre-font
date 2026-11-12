
අභය ලිබ්රේ අකුරු මුහුණත / Abhaya Libre Font
==============

[![Build][badge-build]][link-build]
[![Fontspector QA][badge-qa]][link-qa]
[![Release][badge-release]][link-release]
[![License: OFL 1.1][badge-license]][link-license]

[badge-build]: https://github.com/mooniak/abhaya-libre-font/actions/workflows/build.yaml/badge.svg?branch=dev
[badge-qa]: https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsrc.mooniak.com%2Fabhaya-libre-font%2Fbuild.json&query=%24.qa.pass_rate&suffix=%25&label=fontspector%20QA%20(dev%20build)&color=informational
[badge-release]: https://img.shields.io/github/v/release/mooniak/abhaya-libre-font?label=release
[badge-license]: https://img.shields.io/badge/license-OFL--1.1-green
[link-build]: https://github.com/mooniak/abhaya-libre-font/actions/workflows/build.yaml
[link-qa]: https://src.mooniak.com/abhaya-libre-font/reports/fontspector/fontspector-report.html
[link-release]: https://github.com/mooniak/abhaya-libre-font/releases
[link-license]: OFL.txt

Abhaya Libre is a text typeface designed for communications in Sinhala, Tamil and Latin scripts. The Abhaya Libre project aims to produce the most advanced and complete Sinhala font, with coverage for complex representations in Sinhala, Pali and Sanskrit texts.

In the true spirit of the Libre Fonts movement, the Abhaya Libre project brought together existing projects and a group of designers to develop a coherent typeface. The project started off with the aim of liberating (open sourcing) FM Abhaya, the most popular Sinhala legacy-format text font, by Pushpananda Ekanayake. The Tamil glyph set is based on typefaces by Modular Infotech, and the Latin was designed to match the Sinhala glyph set by Sol Matas.

The drawings for the original FM Abhaya were based on the common text typeface used by the Department of Government Printing in the 1970s—1990s. The roots of this style relate to the modulation structure and aesthetics introduced to the Sinhala script by N J Cooray of the Cooray Type Foundry in the late 1800s. FM Abhaya, which had a limited glyph set in ASCII encoding, was redrawn and expanded into a family with five weights and more glyphs. Driven by rigorous research and community contributions, Abhaya Libre includes an extensive set of ligatures, alternates, stylistic alternates, historical ligatures and OpenType features to support proper representation of text in Sinhala, Pali and Sanskrit.

The Latin characters match the aesthetics of ‘Abhaya Libre Sinhala’, which was inspired by the style of the original Sinhala, with an eminent contrast between distinctive strokes that go from thick to thin, and were further modified to co-exist with the visual logic of Latin typefaces. The ductus references the lines of a Didone typeface and adds a touch of Sinhala form to certain terminations. Large counters have been added along with small ascenders and descenders for optimized screen viewing.

The name ‘Abhaya’ comes from King Abhaya (474 BCE to 454 BCE), who reigned in Sri Lanka from the ancient kingdom of Upatissa Nuwara.

The initial development was funded by Google Fonts. The project is led by Mooniak, a collaborative collective of designers based in Colombo, Sri Lanka, with the cooperation of Pushpananda Ekanayake, the designer of the FM Abhaya font, and Sol Matas as the Latin designer.

See the discussions on the [Google Fonts mailing list](https://groups.google.com/d/topic/googlefonts-discuss/ET5kBjYxDiY/discussion).

See the [recorded discussions](https://www.youtube.com/playlist?list=PLpw12zH02-An-6i79877NUi_ld3U_4tmv).

***

## Get the font

- **On the web:** use it from [Google Fonts](https://fonts.google.com/specimen/Abhaya+Libre).
- **Download:** the [Releases](https://github.com/mooniak/abhaya-libre-font/releases) page has tagged, stable releases. A pre-release named `canary` is also published there; it is a rolling build of the latest development work and may be broken, so don't use it in production.
- **Build it yourself:** see [Building the fonts from source](#building-the-fonts-from-source).

## Font data

| | |
|---|---|
| **Version** | 2.000 |
| **Scripts** | Sinhala, Tamil, Latin |
| **Format** | Variable TrueType (`AbhayaLibre[wght].ttf`) and WOFF2 for the web (`AbhayaLibre[wght].woff2`) |
| **Axis** | `wght` 400–800, from two masters (Regular and ExtraBold) |
| **Named instances** | Regular 400, Medium 500, SemiBold 600, Bold 700, ExtraBold 800 |
| **Glyphs** | 1,204 (501 mapped to Unicode code points; the rest are alternates, ligatures and other forms used by OpenType features) |
| **Units per em** | 1000 |
| **Key heights** | Cap height 700, x-height 500, ascender 746, descender −254 (Regular master) |
| **Vertical metrics** | ascent 860, descent −348, line gap 0 (`hhea` and typo metrics) |
| **File size** | about 500 KB (TTF), about 115 KB (WOFF2) |
| **Source format** | [Glyphs](https://glyphsapp.com/) 3 package (`sources/AbhayaLibre.glyphspackage`) |
| **License** | [SIL Open Font License 1.1](OFL.txt) |

### Character coverage

| Range | Encoded |
|---|---|
| Basic Latin (U+0020–007E) | 95 of 95 |
| Latin-1 Supplement | 96 of 96 |
| Latin Extended-A | 85 of 128 |
| Latin Extended-B | 5 of 208 |
| Sinhala (U+0D80–0DFF) | 88 of 91 |
| Tamil (U+0B80–0BFF) | 72 of 72 |
| Devanagari | danda and double danda (U+0964, U+0965), for Pali and Sanskrit text |
| General Punctuation | 19, including curly quotes, dashes, bullet, ellipsis, ZWNJ and ZWJ |
| Currency | € ₹ ₺ ₽ |

Not yet encoded: the Sinhala vowel signs U+0DDF, U+0DF2 and U+0DF3, and the Sinhala Archaic Numbers block (U+111E0–111FF).

Checked against the [Google Fonts language data](https://github.com/googlefonts/lang), the font covers the base exemplar characters of 268 languages: Sinhala, Tamil and 266 Latin-script languages.

### OpenType features

| Layout table | Features |
|---|---|
| `GSUB` | `aalt` `abvs` `akhn` `blws` `dlig` `frac` `liga` `numr` `ordn` `pnum` `pstf` `psts` `rlig` `rphf` `sups` `tnum` `vatu` `ss01` `ss02` `ss03` `ss07` `ss08` `ss09` |
| `GPOS` | `abvm` `dist` `kern` `mark` |

Script tags in the font: `DFLT`, `sinh`, `taml` and `tml2`; `GPOS` also has `latn`.

## Repository structure

| Path | What it is |
|---|---|
| `sources/AbhayaLibre.glyphspackage` | The font sources: glyphs, masters, kerning and OpenType feature code, as a Glyphs 3 package |
| `sources/config.yaml` | Build configuration read by [gftools](https://github.com/googlefonts/gftools) |
| `Makefile` | Build, test and proof targets (see below) |
| `requirements.in`, `requirements.txt` | Python dependencies: the top-level list, and the pinned set used for builds |
| `fonts/` | Build output (created by `make build`; not committed) |
| `out/` | QA and proof reports (created by `make test` and `make proof`; not committed) |
| `documentation/` | Specimen scripts, project history (`development/`, `sources-v1.060/`) and the font description |
| `scripts/` | Helper scripts used by the Makefile and CI |
| `FONTLOG.txt`, `OFL.txt`, `AUTHORS.txt`, `CONTRIBUTORS.md` | Changelog, license, and credits |
| `BREIF.md` | The original project brief, as posted to the Google Fonts discussion list |

## Building the fonts from source

Building needs only free, open-source tools. You do **not** need Glyphs to build, only to edit the sources.

### Requirements

- **macOS or Linux** (on Windows, use [WSL](https://learn.microsoft.com/windows/wsl/)).
- **Python 3.12** with `venv` and `pip`. This is the version the project's CI uses; the dependencies in `requirements.txt` are pinned, and other Python versions may fail to install them.
- **Make** and **git**.
- Network access for the first build, to download the Python dependencies.

On Debian or Ubuntu, if `pip` fails to compile a dependency, install the system packages used by the project's CI first:

```sh
sudo apt-get install ttfautohint libcairo2-dev python3-cairo-dev pkg-config python3-dev
```

### Build

```sh
git clone https://github.com/mooniak/abhaya-libre-font.git
cd abhaya-libre-font

# Use Python 3.12 explicitly, then let make install the pinned dependencies into it
python3.12 -m venv venv
make build
```

`make build` installs the pinned dependencies from `requirements.txt` into `venv/` (first run only), then builds the fonts from `sources/AbhayaLibre.glyphspackage` using the settings in `sources/config.yaml`. Under the hood this runs [`gftools builder`](https://github.com/googlefonts/gftools), which:

1. compiles the variable font with [fontmake](https://github.com/googlefonts/fontmake) (glyphsLib → ufo2ft → fontTools),
2. post-processes it with `gftools-fix-font` and adds the `STAT` table with `gftools-gen-stat`,
3. compresses it to WOFF2.

The results are written to `fonts/`:

```
fonts/variable/AbhayaLibre[wght].ttf
fonts/webfonts/AbhayaLibre[wght].woff2
```

> Each rebuild deletes and recreates `fonts/`, so don't keep your own files there.

By default only the variable font and its WOFF2 are built. For static fonts, set `buildStatic: true` in `sources/config.yaml` and rebuild; you then also get a TTF, OTF and WOFF2 for each of the five weights in `fonts/ttf/`, `fonts/otf/` and `fonts/webfonts/`.

### After editing the sources

`make` decides whether to rebuild by comparing timestamps against the `.glyphspackage` folder itself, and editing a file *inside* the package doesn't update the folder's timestamp. So after you change the sources, `make build` may say `Nothing to be done`. Force a rebuild by removing the stamp file:

```sh
rm build.stamp
make build
```

### Quality checks and proofs

These are optional and need two extra tools, installed with [`cargo binstall`](https://github.com/cargo-bins/cargo-binstall):

```sh
cargo binstall fontspector     # for `make test`
cargo binstall diffenator3     # for `make proof`
```

| Command | What it does |
|---|---|
| `make test` | Runs [Fontspector](https://github.com/fonttools/fontspector) with the Google Fonts profile and writes HTML and Markdown reports to `out/fontspector/`. It prints a summary and does not stop the build on failures; read the report to see them. |
| `make proof` | Runs [diffenator3](https://github.com/googlefonts/diffenator3)'s `diff3proof` and writes an HTML proof to `out/proof/`. |
| `make images` | Renders the PNG specimen images from the DrawBot scripts in `documentation/`. Needs to run inside a git clone that has a commit and an `origin` remote. |
| `make clean` | Deletes the `venv/` folder. |

### Build badges

The badges at the top of this page come from the automated build, which runs on every push to `dev`:

- **Build** is the status of the latest [GitHub Actions run](https://github.com/mooniak/abhaya-libre-font/actions/workflows/build.yaml) (build, QA and proofs).
- **Fontspector QA** is the pass rate of the Google Fonts profile checks on that same build, read from the build manifest published with the [proof site](https://src.mooniak.com/abhaya-libre-font/). It tracks the latest development build, not the tagged release, and the [full report](https://src.mooniak.com/abhaya-libre-font/reports/fontspector/fontspector-report.html) lists every check.

You get the same data locally: `make test` also writes one small badge file per check category (Fontspector QA, OpenType specification, Universal profile, and others) to `out/badges/`, in the [shields.io endpoint format](https://shields.io/badges/endpoint-badge).

### Troubleshooting

- **`pip install` fails with a build error:** check you're on Python 3.12 (`venv/bin/python --version`). If `venv/` was created with another version, delete it and recreate it with `python3.12 -m venv venv`.
- **`fontspector not found` or `diff3proof not found`:** install them with `cargo binstall` as above and make sure `~/.cargo/bin` is on your `PATH`.
- **Your edits don't show up in the font:** see [After editing the sources](#after-editing-the-sources).

## Contributing

Bug reports, design feedback and pull requests are welcome in the [issue tracker](https://github.com/mooniak/abhaya-libre-font/issues). Before opening a pull request:

1. Open pull requests against the `dev` branch; `main` is only updated when a release is made.
2. Make your changes in `sources/AbhayaLibre.glyphspackage` (this needs [Glyphs 3](https://glyphsapp.com/)).
3. Rebuild (`rm build.stamp && make build`) and run `make test`.
4. Add your name and a short description of your contribution to [CONTRIBUTORS.md](CONTRIBUTORS.md), and add a change entry to [FONTLOG.txt](FONTLOG.txt).

## Credits

Abhaya Libre is the work of many people. Roles below come from [CONTRIBUTORS.md](CONTRIBUTORS.md), [AUTHORS.txt](AUTHORS.txt) and the project's git history and pull requests; see [CONTRIBUTORS.md](CONTRIBUTORS.md) for the contribution-by-contribution record.

### Design, development and research

| Name | Contribution |
|---|---|
| [Pushpananda Ekanayake](http://isiwara.lk) | Designer of the original FM Abhaya and of the basic Sinhala set |
| [Sol Matas](https://github.com/solmatas) | Designer of the Latin (Adobe Latin 3 character set) |
| [Pathum Egodawatta](https://github.com/pathumego) ([Mooniak](https://mooniak.com)) | OpenType layout, project coordination and design |
| [Ayantha Randika](https://github.com/paarandika) ([Mooniak](https://mooniak.com)) | OpenType layout and build |
| [Kosala Senevirathne](https://github.com/kosalaya) ([Mooniak](https://mooniak.com)) | Designer of the Sinhala numerals; Tamil updates and test documents |
| [Pria Ravichandran](https://foundryfivetype.com/) | Design consultation on Tamil |
| Janaka Attanayake | Research and development on Pali and Sanskrit support |
| Bertram G. Liyanage | Research and development on Pali and Sanskrit support |

### Engineering and project support

| Name | Contribution |
|---|---|
| [Liang Hai](https://github.com/lianghai) | Set up the original build (`build.py`, feature files and FDK compile) in 2015; consultancy and support |
| [Dave Crossland](https://github.com/davelab6) | Consultancy and support; the OFL license file |
| Sumanthri Samarawickrama | Consultancy and support |
| [Yanone](https://github.com/yanone) | Preparing the update for Google Fonts: vertical metrics, anchors, glyph fixes, copyright string and description |
| [Simon Cozens](https://github.com/simoncozens) | Fontspector fixes: interpolation contour order and start points, and name table cleanup |
| [DEVRAJ-20](https://github.com/DEVRAJ-20) | Path direction corrections and Tamil fixes |

### Organizations

- [Google Fonts](https://fonts.google.com/) funded the initial development.
- [Mooniak](https://mooniak.com/) leads the project.
- Modular Infotech designed the Tamil typefaces that the Tamil glyph set is based on.

And thanks to everyone who has reported issues and helped spot errors and bugs, including all the tweeps who did so.

## License

Abhaya Libre is released under the [SIL Open Font License, Version 1.1](OFL.txt). The license is also available with a FAQ at <https://openfontlicense.org>.

For information on what you're allowed to change or modify, consult [OFL.txt](OFL.txt) and the [OFL FAQ](https://openfontlicense.org/ofl-faq/). The FAQ also gives a very general rationale and various recommendations regarding why you would want to contribute to the project or make your own version of the font.
