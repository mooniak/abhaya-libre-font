#
# builder.sh
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

#!/bin/bash

cd ../sources/sfd

python ../../scripts/unlink.py AbhayaLibre-sinhala-0.sfd AbhayaLibre-sinhala-0-temp.sfd
python ../../scripts/unlink.py AbhayaLibre-sinhala-1.sfd AbhayaLibre-sinhala-1-temp.sfd

python ../../scripts/fontconvert AbhayaLibre-sinhala-0-temp.sfd ../../sources --ufo
python ../../scripts/fontconvert AbhayaLibre-sinhala-1-temp.sfd ../../sources --ufo

cd ../../scripts
rm -R -f ../ttf-build
rm -R -f ../masters/*.ufo
python merger.py ../masters/AbhayaLibre-Regular.ufo ../sources/AbhayaLibre-sinhala-0-temp.ufo ../sources/AbhayaLibre-latin-0.ufo
python merger.py ../masters/AbhayaLibre-ExtraBold.ufo ../sources/AbhayaLibre-sinhala-1-temp.ufo ../sources/AbhayaLibre-latin-1.ufo
cd ../
python gfbuild-s.py

cd sources/sfd
rm -R -f ../AbhayaLibre-sinhala-0-temp.ufo ../AbhayaLibre-sinhala-1-temp.ufo
rm -R -f AbhayaLibre-sinhala-0-temp.sfd AbhayaLibre-sinhala-1-temp.sfd
