import os, shutil, subprocess
from subprocess import check_output
from config import *

import robofab.world

def get_font(directory, suffix = ''):

    font_file_name = ''

    for file_name in os.listdir(directory):
        if file_name.endswith(suffix + ".ufo"):
            font_file_name = file_name
            break
    if font_file_name:
        print font_file_name
        font = robofab.world.OpenFont(directory + '/' + font_file_name)
        return font
    else:
        print "#ITF: Can't find the font file with suffix `%s`." % suffix
        return None

def fix_Glyphs_UFO_masters(masters):

    for font in masters:

        if not font.info.postscriptFamilyBlues:
            font.info.postscriptFamilyBlues = []
        if not font.info.postscriptFamilyOtherBlues:
            font.info.postscriptFamilyOtherBlues = []
        if not font.info.postscriptStemSnapH:
            font.info.postscriptStemSnapH = []
        if not font.info.postscriptStemSnapV:
            font.info.postscriptStemSnapV = []
        if not font.info.postscriptBlueValues:
            font.info.postscriptBlueValues=[]
        if not font.info.postscriptOtherBlues:
            font.info.postscriptOtherBlues=[]

        font.save()

masters = [
        i for i in [
            get_font('masters', suffix) for suffix in ['_0', '_1']
        ] if i
    ]

fix_Glyphs_UFO_masters(masters)

style_path=("style")
if os.path.isdir(style_path):
    shutil.rmtree(style_path)
os.makedirs("style")
subprocess.call(['python', 'UFOInstanceGenerator.py', 'masters', '-o', 'style']+UFOIG_ARGS)
build_path=("build")
if not os.path.isdir(build_path):
    os.makedirs('build')
else:
    fileList = os.listdir(build_path)
    for file in fileList:
        os.unlink(build_path+"/"+file)

STYLE_NAMES = ['ExtraBold','Regular','Medium','SemiBold','Bold']
TEMPLATE_FEATURES = '''\
#!opentype
include (../../family.fea);
'''
makeotf_args=""
for arg in MAKEOTF_ARGS:
    makeotf_args+=" "+arg

for font in STYLE_NAMES:
    style_dir="style/"+font
    f=open(style_dir+'/features', 'w')
    f.write(TEMPLATE_FEATURES)
    f.close()
    otf_path=build_path+"/"+FAMILY_NAME+"-"+font+".otf"
    print check_output("makeotf -f "+style_dir+"/font.ufo -o "+otf_path+" -mf FontMenuNameDB -gf GlyphOrderAndAliasDB"+makeotf_args, shell=True)
