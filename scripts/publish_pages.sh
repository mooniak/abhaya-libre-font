#!/usr/bin/env bash
# publish_pages.sh <site_dir> — publish a built proof site to the repo's gh-pages branch.
#
#   /                  the latest build of the `dev` branch (replaced each push)
#   /canary/<sha7>/    that same build, kept per commit (newest $PAGES_KEEP_CANARY retained)
#   /canary/           index of every canary build: commit, version, time, design stage, QA, CI run
#
# Served at https://src.mooniak.com/<repo-name>/ (org Pages site, CNAME src.mooniak.com).
# <site_dir> comes from scripts/build_pages.py. Runs in CI (needs GH_TOKEN + GITHUB_* env,
# git, python3); standalone otherwise. Keeps no history: gh-pages is force-pushed as ONE
# commit each time, so font binaries never accumulate in the repo's history.
#
# First run over a gh-pages branch this tool did not create (no .mnik-pages marker — old
# fontbakery reports, Jekyll sites): the branch is archived to `gh-pages-legacy`, then replaced.
set -euo pipefail

SITE="${1:?usage: publish_pages.sh <site_dir>}"
REPO="${GITHUB_REPOSITORY:?GITHUB_REPOSITORY not set}"
SHA="${GITHUB_SHA:?GITHUB_SHA not set}"
SHORT="${SHA:0:7}"
KEEP="${PAGES_KEEP_CANARY:-5}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE="$(cd "$SITE" && pwd)"

[ -f "$SITE/index.html" ] || { echo "publish_pages: $SITE has no index.html — skipping"; exit 0; }

# PAGES_REMOTE overrides the push target (used by tests against a local bare repo).
REMOTE="${PAGES_REMOTE:-https://x-access-token:${GH_TOKEN:?GH_TOKEN not set}@github.com/${REPO}.git}"
WT="$(mktemp -d)"
trap 'rm -rf "$WT"' EXIT

if git ls-remote --exit-code --heads "$REMOTE" gh-pages >/dev/null 2>&1; then
  git clone --quiet --branch gh-pages "$REMOTE" "$WT"      # full clone: needed to archive old history
else
  git init --quiet "$WT"
fi
cd "$WT"
git config user.name  "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

# Archive a gh-pages we did not write, once, before replacing it.
if [ -n "$(git rev-parse --verify --quiet HEAD || true)" ] && [ ! -f .mnik-pages ]; then
  if ! git ls-remote --exit-code --heads "$REMOTE" gh-pages-legacy >/dev/null 2>&1; then
    echo "publish_pages: archiving pre-existing gh-pages -> gh-pages-legacy"
    git push --quiet "$REMOTE" HEAD:refs/heads/gh-pages-legacy
  fi
  # not ours: start clean, nothing of the old site is carried into canary/
  find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
fi

# Root = the latest build. canary/ is the one thing that survives the swap.
find . -mindepth 1 -maxdepth 1 ! -name .git ! -name canary -exec rm -rf {} +
cp -a "$SITE"/. .

# canary/<sha7>/ = this build, kept. Its "canary build log" link must climb out of the folder.
mkdir -p canary
rm -rf "canary/$SHORT"
mkdir "canary/$SHORT"
cp -a "$SITE"/. "canary/$SHORT/"
sed -i.bak 's#href="canary/"#href="../"#' "canary/$SHORT/index.html" && rm -f "canary/$SHORT/index.html.bak"

# Upsert this build into canary/builds.json, prune the oldest build folders, rewrite the index.
python3 - "$SITE/build.json" canary/builds.json "$KEEP" <<'PY'
import json, shutil, sys
from pathlib import Path
build, log, keep = Path(sys.argv[1]), Path(sys.argv[2]), int(sys.argv[3])
b = json.loads(build.read_text(encoding="utf-8"))
entry = {k: b.get(k) for k in ("family", "commit", "commit_short", "version", "generated_at",
                               "stage", "qa", "run_url", "ref_name", "channel", "repository")}
builds = json.loads(log.read_text(encoding="utf-8")) if log.exists() else []
builds = [x for x in builds if x.get("commit_short") != entry["commit_short"]] + [entry]
builds.sort(key=lambda x: x.get("generated_at") or "", reverse=True)
for old in builds[keep:]:
    shutil.rmtree(log.parent / (old.get("commit_short") or "_none_"), ignore_errors=True)
log.write_text(json.dumps(builds, indent=1, ensure_ascii=False), encoding="utf-8")
PY
# build_pages.py sits beside this script once vendored into a font repo's scripts/;
# in the homebase it lives in ../proofpdf/.
BP="$HERE/build_pages.py"; [ -f "$BP" ] || BP="$HERE/../proofpdf/build_pages.py"
python3 "$BP" --canary-index canary

touch .nojekyll
printf '{"tool":"mnik publish_pages","latest":"%s"}\n' "$SHORT" > .mnik-pages

# One commit, force-pushed: no font binaries pile up in history.
git checkout --quiet --orphan _publish
git add -A
git commit --quiet -m "Pages: ${REPO##*/} ${SHORT} (latest dev build)"
git push --quiet --force "$REMOTE" HEAD:refs/heads/gh-pages
echo "publish_pages: published ${REPO##*/} @ ${SHORT} -> https://src.mooniak.com/${REPO##*/}/  (+ /canary/${SHORT}/)"
