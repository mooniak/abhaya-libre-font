#!/usr/bin/env bash
# publish_channel.sh <canary|dev|release> — publish built fonts + the build manifest
# to a GitHub Release, per the Mooniak channel model (docs/channels-and-versioning.md).
#
#   canary   rolling pre-release tagged `canary` (tag moved to this commit, assets clobbered)
#   dev      pre-release at the `vX.YYY-dev.N` tag
#   release  Release at the `vX.YYY` tag
#
# Assets: <slug>-<channel>-fonts.zip + individual .ttf/.otf/.woff2 + fontstatus.json
# (+ OFL.txt / ARTICLE if present). Runs in CI (needs GH_TOKEN + the GITHUB_* env);
# standalone (gh + zip only). See docs/fontpipe-migration-brief.md §3.
set -euo pipefail

CHANNEL="${1:?usage: publish_channel.sh <canary|dev|release>}"
SLUG="${GITHUB_REPOSITORY##*/}"
OUT=publish

# Nothing to publish if the build produced no fonts.
if [ -z "$(find fonts -type f \( -name '*.ttf' -o -name '*.otf' -o -name '*.woff2' \) 2>/dev/null)" ]; then
  echo "publish_channel: no built fonts — skipping"; exit 0
fi

rm -rf "$OUT" && mkdir -p "$OUT"
( cd fonts && zip -qr "../$OUT/${SLUG}-${CHANNEL}-fonts.zip" . )
find fonts -type f \( -name '*.ttf' -o -name '*.otf' -o -name '*.woff2' \) -exec cp {} "$OUT/" \;
[ -f out/fontstatus.json ] && cp out/fontstatus.json "$OUT/"          # decision 1: manifest as an asset
[ -f OFL.txt ] && cp OFL.txt "$OUT/" || true
[ -f documentation/ARTICLE.en_us.html ] && cp documentation/ARTICLE.en_us.html "$OUT/" || true

echo "publish_channel: $CHANNEL — assets:"; ls -1 "$OUT"

# `gh release` glob-expands each asset argument itself, so glob metacharacters in
# the filenames must be escaped. Google Fonts variable fonts follow the axis-tuple
# naming standard `Family[wght].ttf`; left unescaped, gh reads `[wght]` as a glob
# character class, matches nothing, and aborts with "no matches found". Escape
# [ ] * ? so gh takes each name literally. Assets are always passed as "${ASSETS[@]}".
ASSETS=()
for f in "$OUT"/*; do
  esc=$f
  esc=${esc//\[/\\[}
  esc=${esc//\]/\\]}
  esc=${esc//\*/\\*}
  esc=${esc//\?/\\?}
  ASSETS+=("$esc")
done

case "$CHANNEL" in
  canary)
    # Rolling: retarget the `canary` tag to this commit, replace all assets.
    gh release delete canary --cleanup-tag --yes 2>/dev/null || true
    gh release create canary --prerelease --target "$GITHUB_SHA" \
      --title "canary — rolling dev build" \
      --notes "Bleeding-edge build of \`dev\`. **May be broken.** Exact commit, version and QA are in \`fontstatus.json\`." \
      "${ASSETS[@]}"
    ;;
  dev)
    if gh release view "$GITHUB_REF_NAME" >/dev/null 2>&1; then
      gh release upload "$GITHUB_REF_NAME" "${ASSETS[@]}" --clobber
    else
      gh release create "$GITHUB_REF_NAME" --prerelease --title "$GITHUB_REF_NAME" \
        --notes "Development pre-release \`$GITHUB_REF_NAME\`." "${ASSETS[@]}"
    fi
    ;;
  release)
    if gh release view "$GITHUB_REF_NAME" >/dev/null 2>&1; then
      gh release upload "$GITHUB_REF_NAME" "${ASSETS[@]}" --clobber
    else
      NOTES="$(git tag -l --format='%(contents:body)' "$GITHUB_REF_NAME" 2>/dev/null || true)"
      gh release create "$GITHUB_REF_NAME" --title "$GITHUB_REF_NAME" \
        --notes "${NOTES:-Release $GITHUB_REF_NAME}" "${ASSETS[@]}"
    fi
    ;;
  *) echo "publish_channel: unknown channel '$CHANNEL'" >&2; exit 1 ;;
esac
echo "publish_channel: done ($CHANNEL)"
