#!/bin/bash

cd ../sources/

fontforge ../scripts/fontconvert AbhayaLibre-Regular.sfd --ufo
fontforge ../scripts/fontconvert AbhayaLibre-ExtraBold.sfd --ufo

mv AbhayaLibre-Regular.ufo ../build/masters/AbhayaLibre_0.ufo
mv AbhayaLibre-ExtraBold.ufo ../build/masters/AbhayaLibre_1.ufo