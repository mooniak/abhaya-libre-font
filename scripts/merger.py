#
# merger.py
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

from robofab.world import NewFont, OpenFont
from robofab import plistlib
import sys, os
def ufoGlyphOrderSetter(existingOrder, newOrder):
    outOrder=[]
    for glyphName in newOrder:
        if glyphName not in existingOrder:
            outOrder.append(glyphName)
    return outOrder

arguments=sys.argv
fontList=arguments[2:]

print "Merging fonts..."
print os.getcwd()
NewUFO = NewFont()
font_source = OpenFont(fontList[0])
for glyphName in ufoGlyphOrderSetter([], font_source.keys()):
    glyph = font_source[glyphName]
    NewUFO.insertGlyph(glyph)
    print glyphName,
    NewUFO[glyphName].unicode = font_source[glyphName].unicode
NewUFO.lib=font_source.lib
NewUFO.info=font_source.info

for font in fontList[1:]:
    source= OpenFont(font)
    for glyph_name in ufoGlyphOrderSetter(NewUFO.keys(), source.keys()):
        glyph = source[glyph_name]
        print glyph_name,
        NewUFO.insertGlyph(glyph)
        NewUFO[glyphName].unicode = font_source[glyphName].unicode
    # newLib=[i for i in source.lib['public.glyphOrder'] if i not in NewUFO.lib['public.glyphOrder']]+NewUFO.lib['public.glyphOrder']
    # NewUFO.lib['public.glyphOrder']=newLib

NewUFO.save(arguments[1])
print "\nMerge complete!"
