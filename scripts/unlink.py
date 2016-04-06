import os, sys
import fontforge

path=sys.argv[1]
path2=sys.argv[2]
font = fontforge.open(path)
font.selection.all()
font.unlinkReferences()
font.save(path2)
