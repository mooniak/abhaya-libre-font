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

python ../../scripts/fontconvert AbhayaLibre-sinhala-0.sfd ../../sources --ufo
python ../../scripts/fontconvert AbhayaLibre-sinhala-1.sfd ../../sources --ufo
python ../../scripts/fontconvert AbhayaLibre-tamil-0.sfd ../../sources --ufo
python ../../scripts/fontconvert AbhayaLibre-tamil-1.sfd ../../sources --ufo

cd ../../scripts
python merger.py ../masters/AbhayaLibre-Regular.ufo ../sources/AbhayaLibre-sinhala-0.ufo ../sources/AbhayaLibre-latin-0.ufo ../sources/AbhayaLibre-tamil-0.ufo
python merger.py ../masters/AbhayaLibre-ExtraBold.ufo ../sources/AbhayaLibre-sinhala-1.ufo ../sources/AbhayaLibre-latin-1.ufo ../sources/AbhayaLibre-tamil-1.ufo

cd ../
python build.py

echo "Update the gh-pages branch? [y/n]"
res="n"
read -t 120 res

if [ "$res" = "y" ];
  then
  echo "Please do not chage the files while the process ends"
  cp -a build ~
  git checkout gh-pages
  if [ $? -eq 0 ];
    then
    rm fonts/*
    mv ~/build/* fonts
    rm -r ~/build
    git add fonts/*
    git commit -m "Updated fonts"
    git push
    git checkout master
    echo "Done :)"
  else
    echo "Update gh-pages failed :("
  fi
fi
echo "Build Finished!"
