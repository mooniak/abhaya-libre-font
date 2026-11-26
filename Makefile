SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(shell ls documentation/*.py)
DRAWBOT_OUTPUT=$(shell ls documentation/*.py | sed 's/\.py/.png/g')
# QA profiles (mooniak-font-tools mnik/tiers.py qa_profiles). Every font runs the
# Mooniak profile (scripts/fontspector-mooniak.toml): the blocking report, in
# out/fontspector/ with the badges. Free fonts that declare "google_fonts": true in
# fontpackage.json also run the stock googlefonts profile, as a second report in
# out/fontspector-googlefonts/. Missing tier = premium = no googlefonts (fail closed).
QA_PROFILE=scripts/fontspector-mooniak.toml
GOOGLE_FONTS=$(shell python3 -c "import json;d=json.load(open('fontpackage.json'));print('yes' if d.get('tier')=='free' and d.get('google_fonts') is True else '')" 2>/dev/null)

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontspector"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make pages:  Builds the stage-gated proof site in _site/ (landing page, proofs, build details)"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo "  make features: Regenerates the lankafea OpenType features (fonts with sources/lankafea.yaml)"
	@echo

build: build.stamp

venv: venv/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv sources/config.yaml $(SOURCES)
	rm -rf fonts
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)  && touch build.stamp

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: build.stamp
	which fontspector || (echo "fontspector not found. Please install it with 'cargo binstall fontspector'." && exit 1)
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; \
	rm -rf out/fontspector out/fontspector-googlefonts out/badges; mkdir -p out/fontspector; \
	echo mooniak > out/fontspector/fontspector-profile.txt; \
	fontspector --profile $(QA_PROFILE) -l warn --full-lists --succinct --html out/fontspector/fontspector-report.html --ghmarkdown out/fontspector/fontspector-report.md --badges out/badges $$TOCHECK || echo '::warning file=sources/config.yaml,title=fontspector failures::The fontspector QA check (Mooniak profile) reported errors in your font. Please check the generated report.'; \
	if [ -n "$(GOOGLE_FONTS)" ]; then \
	  mkdir -p out/fontspector-googlefonts; echo googlefonts > out/fontspector-googlefonts/fontspector-profile.txt; \
	  fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector-googlefonts/fontspector-report.html --ghmarkdown out/fontspector-googlefonts/fontspector-report.md $$TOCHECK || echo '::warning file=sources/config.yaml,title=fontspector googlefonts failures::The googlefonts profile reported errors (this font is headed for Google Fonts). Please check the second report.'; \
	fi

proof: venv build.stamp
	which diff3proof || (echo "diff3proof not found. Please install it with 'cargo binstall diffenator3'." && exit 1)
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diff3proof $$TOCHECK --output out/proof

# Stage-gated proof site: landing page + build details + one proof page per font, written to
# _site/. The font's computed design stage picks which proof sections appear; the build channel
# picks the depth (canary = HTML, dev/release add PDF books). Run after `manifest` so the page
# carries the build's channel, version, commit and QA verdict. In CI, publish_pages.sh puts
# _site at the Pages root (latest dev build) and under canary/<sha>/.
# PDF=1 also renders PDF books into out/proofs-pdf/ (dev/release only; needs Playwright).
pages: build.stamp
	. venv/bin/activate; python3 scripts/build_pages.py --out _site $(if $(PDF),--pdf out/proofs-pdf,)

# Regenerate the OpenType features that lankafea generates from the LankaGlyphset standard,
# for fonts that keep their settings in sources/lankafea.yaml (one section per script:
# sinhala:, tamil:). Only the layout code in the source changes; hand-written features
# lankafea doesn't own (Latin, a script not yet generated) are kept. Commit the result:
# the build itself doesn't need lankafea. LANKAFEA defaults to the sinhala-font-tools
# checkout beside font-repos/.
LANKAFEA ?= ../../sinhala-font-tools/tools/feature-generator/.venv/bin/lankafea
features:
	@if [ ! -f sources/lankafea.yaml ]; then echo "No sources/lankafea.yaml: this font's features are hand-written."; exit 0; fi; \
	for script in $$(grep -E '^(sinhala|tamil):' sources/lankafea.yaml | tr -d ':'); do \
	  for source in $(SOURCES); do \
	    echo "lankafea: $$script features -> $$source"; \
	    $(LANKAFEA) generate --script $$script --font $$source --glyphs-out $$source --quiet -o /dev/null < /dev/null || exit 1; \
	  done; \
	done

# Stamp the OpenFV name ID 5 into built fonts per channel (canary/dev/release),
# derived from the CI environment; no-op locally. Run right after `build`, before
# `test`/`manifest` so they see the stamped version. See docs/channels-and-versioning.md.
stamp: build.stamp
	. venv/bin/activate; python3 scripts/stamp_version.py --rename-files

# Emit out/fontstatus.json — the per-build computed-fact manifest (files+hashes,
# version, channel, QA verdict). Run after `build` (needs fonts) and `test` (reads
# the fontspector report for the QA verdict). See mooniak docs/manifest-schema.md.
manifest: build.stamp
	mkdir -p out/; . venv/bin/activate; python3 scripts/build_manifest.py

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/mooniak/mooniak-font-project-template/

update: venv
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	git commit -m "Update requirements" requirements.txt
	git push
