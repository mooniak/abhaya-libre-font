#
# merger.py
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

from defcon import Font
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
new_ufo = Font()
new_ufo = Font(fontList[0])
new_ufo._get_lib()
new_ufo._lib["public.glyphOrder"]=[]

for font in fontList[1:]:
    source= Font(font)
    if source.kerning._dataOnDisk is not None:
        pair_list=source.kerning.keys()
        for pair in pair_list:
            new_ufo.kerning[pair]=source.kerning[pair]
    glyph_name_list=ufoGlyphOrderSetter(new_ufo.keys(), source.keys())
    for glyph_name in glyph_name_list:
        new_ufo._lib["public.glyphOrder"].append(glyph_name)
        glyph = source[glyph_name]
        print glyph_name,
        new_ufo._glyphSet._insertGlyph(glyph)

new_ufo.save(arguments[1])
print "\nMerge complete!"
