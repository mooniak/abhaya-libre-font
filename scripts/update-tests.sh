#!/bin/bash
#Run this for automation: fswatch -0 sources/ | xargs -0 -n1 -I{} sh scripts/update-tests.sh
cd ../sources/

fontforge ../scripts/fontconvert AbhayaLibre-Regular.sfd --otf
fontforge ../scripts/fontconvert AbhayaLibre-ExtraBold.sfd --otf

mv *otf ../tests/fonts
cd ../tests/
git add .
git commit -m 'Updating Tests Doc'
