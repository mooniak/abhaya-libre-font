# All rights reserved 2014 - Path Nirvana
# www.facebook.com/path.nirvana
import sys
print "Fonts  opened: ", len(fl);
# select the fonts
for i in range(len(fl)):
	if fl[i].family_name == "FMAbhaya":
		fo = fl[i];
		foi = i;
	elif fl[i].family_name == "UN-Abhaya":
		fn = fl[i];
		fni = i;

print "old font: ", fo.family_name;
print "new font: ", fn.family_name;
bandiWidthReduction = 150;

# apply the mappings [old code, new name, new code]
# this copies the glyphs from the old font to the new font

map = [
#feature abvs
[0x002f, 'ra.ae'],
[0x003f, 'ra.aee'],
[0x005c, 'nda.aa'],
[0x00a2, 'nda.i'],
[0x00a3, 'nda.ii'],
[0x00a5, 'da.uu'],
[0x00a7, 'da.ii'],
[0x00a8, 'la.u'],
[0x00a9, 'reph.ya'],
[0x00aa, 'nda.uu'],
[0x00af, 'kdha.i'],
[0x00b0, 'kdha.ii'],
[0x00b1, 'da.ae'],
#[0x00b5, 'da.yansa'], #old abahaya version
[0x00be, 'ra.al'],
[0x00bf, 'La.u'], 
[0x00c0, 'Ta.i'],
[0x00c1, 'Ta.ii'],
[0x00c2, 'Ja.ii'],
[0x00c4, 'kha.al'],
[0x00c5, 'kha.i'],
[0x00c6, 'la.uu'],
[0x00c7, 'kha.ii'],
[0x00c8, 'da.i'],
[0x00c9, 'cha.al'],
[0x00ca, 'ja.al'],
[0x00cd, 'ra.ii'],
[0x00ce, 'Dha.i'],
#[0x00cf, 'da.yansa.aa'], #old abahaya version
[0x00d0, 'Dha.ii'],
[0x00d1, 'cha.i'],
[0x00d2, 'Tha.ii'],
[0x00d3, 'Tha.i'],
[0x00d4, 'ja.ii'],
[0x00d6, 'cha.ii'],
[0x00d7, 'gna.aa'],
[0x00d8, 'kna.aa'],
[0x00d9, 'knaasi.al'],
[0x00da, 'pha.ii'],
[0x00dc, 'ta.al'],
[0x00dd, 'pha.i'],
[0x00de, 'da.aa'],
[0x00df, 'ra.i'],
[0x00e0, 'ta.ii'],
[0x00e1, 'ta.i'],
[0x00e2, 'Da.al'],
[0x00e3, 'Da.ii'],
[0x00e4, 'Da.i'],
[0x00e5, 'nDa.al'],
[0x00e7, 'nDa.i'],
[0x00e8, 'dha.al'],
[0x00e9, 'nDa.ii'],
[0x00ea, 'dha.i'],
[0x00eb, 'dha.ii'],
[0x00ec, 'ba.i'],
[0x00ed, 'ba.al'],
[0x00ee, 'ba.ii'],
[0x00ef, 'ma.al'],
[0x00f0, 'ja.i'],
[0x00f1, 'ma.i'],
[0x00f2, 'mba.al'],
[0x00f3, 'ma.ii'],
[0x00f4, 'mba.i'],
[0x00f5, 'va.al'],
[0x00f6, 'mba.ii'],
[0x00f7, 'nda.u'],
[0x00f8, 'da.rakar'],
[0x00f9, 'va.ii'],
[0x00fa, 'va.i'],
[0x00fb, 'kna.u'],
[0x00fc, 'kna.uu'],
[0x00fd, 'Ja.i'],
[0x00fe, 'Ja.al'],
[0x00ff, 'da.u'],
[0x0152, 'Na.ii'],
[0x0153, 'reph.yansa'], #how will this interact with the rules below for reph and yansa
[0x0192, 'nda.ae'],
[0x201a, 'Na.i'],
[0x201c, 'reph.Na'],
[0x203a, 'sha.rakar.ii'], #shri

# feature [akhn]
#conjuncts
[0x00cb, 'ka.al.zwj.Sha'],
[0x2020, 'tha.al.zwj.Tha'],
[0x2021, 'na.al.zwj.da'],
[0x2026, 'tha.al.zwj.va'],
[0x02c6, 'na.al.zwj.da.aa'],
[0x0160, 'da.al.zwj.dha'], #as in buddha
[0x2039, 'da.al.zwj.dha.i'], #as in buddhi
[0x201e, 'da.al.zwj.va'], #as in dvandava
[0x2030, 'da.al.zwj.va.i'],
# k n and th - half conjuncts
[0x0043, 'ka.al.zwj'],
[0x0046, 'tha.al.zwj'],
[0x004a, 'na.al.zwj'],

# reph, yansa and rakar
[0x005f, 'reph'], [0x2013, 'reph2'],
[0x0048, 'yansa'],
[0x0025, 'rakar'],

#signs
[0x0078, 'anusa', 0x0d82],
[0x0023, 'visar', 0x0d83],
#vowels
[0x0077, 'v_a', 0x0d85],
[0x0077, 'v_aa', 0x0d86, 1],
[0x0077, 'v_ae', 0x0d87, 1],
[0x0077, 'v_aee', 0x0d88, 1],
[0x0062, 'v_i', 0x0d89],
[0x0042, 'v_ii', 0x0d8a],
[0x0057, 'v_u', 0x0d8b],
[0x0057, 'v_uu', 0x0d8c, 1],
[0x0052, 'v_iru', 0x0d8d],
[0x0052, 'v_iruu', 0x0d8e, 1],
[0x00cc, 'v_ilu', 0x0d8f],
[0x00cf, 'v_iluu', 0x0d90],
[0x0074, 'v_e', 0x0d91],
[0x0074, 'v_ee', 0x0d92, 1],
[0x0074, 'v_ei', 0x0d93, 1],
[0x0054, 'v_o', 0x0d94],
[0x00b4, 'v_oo', 0x0d95],
[0x0054, 'v_ou', 0x0d96, 1],
#consos
[0x006c, 'ka', 0x0d9a], [0x006c, 'ka_bandi'],
[0x004c, 'kha', 0x0d9b], [0x004c, 'kha_bandi'],
[0x002e, 'ga', 0x0d9c], [0x002e, 'ga_bandi'],
[0x003e, 'gha', 0x0d9d],
[0x0058, 'knaasi', 0x0d9e], [0x0058, 'knaasi_bandi'],
[0x00d5, 'nga', 0x0d9f],
[0x0070, 'cha', 0x0da0], [0x0070, 'cha_bandi'],
[0x0050, 'Ja', 0x0da1],
[0x0063, 'ja', 0x0da2], [0x0063, 'ja_bandi'],
[0x00ae, 'kdha', 0x0da3],
[0x005b, 'kna', 0x0da4], [0x005b, 'kna_bandi'],
[0x007b, 'gna', 0x0da5],
[0x0063, 'nja', 0x0da6, 1],
[0x0067, 'ta', 0x0da7], [0x0067, 'ta_bandi'],
[0x0047, 'Ta', 0x0da8],
[0x0076, 'Da', 0x0da9], [0x0076, 'Da_bandi'],
[0x0056, 'Dha', 0x0daa],
[0x004b, 'Na', 0x0dab], [0x004b, 'Na_bandi'],
[0x007e, 'nDa', 0x0dac],
[0x003b, 'tha', 0x0dad], [0x003b, 'tha_bandi'],
[0x003a, 'Tha', 0x0dae],
[0x006f, 'da', 0x0daf], [0x006f, 'da_bandi'],
[0x004f, 'dha', 0x0db0], [0x004f, 'dha_bandi'],
[0x006b, 'na', 0x0db1], [0x006b, 'na_bandi'],
[0x007c, 'nda', 0x0db3],
[0x006d, 'pa', 0x0db4], [0x006d, 'pa_bandi'],
[0x004d, 'pha', 0x0db5],
[0x006e, 'ba', 0x0db6], [0x006e, 'ba_bandi'],
[0x004e, 'bha', 0x0db7],
[0x0075, 'ma', 0x0db8], [0x0075, 'ma_bandi'],
[0x0055, 'mba', 0x0db9],
[0x0068, 'ya', 0x0dba], [0x0068, 'ya_bandi'],
[0x0072, 'ra', 0x0dbb],
[0x002c, 'la', 0x0dbd], [0x002c, 'la_bandi'],
[0x006a, 'va', 0x0dc0], [0x006a, 'va_bandi'],
[0x0059, 'sha', 0x0dc1],
[0x0049, 'Sha', 0x0dc2],
[0x0069, 'sa', 0x0dc3], [0x0069, 'sa_bandi'],
[0x0079, 'ha', 0x0dc4], [0x0079, 'ha_bandi'],
[0x003c, 'La', 0x0dc5], [0x003c, 'La_bandi'],
[0x002a, 'fa', 0x0dc6],
#dependent vowels
[0x0061, 'al', 0x0dca], [0x0041, 'al2', 0], #short one 0041
[0x0064, 'aa', 0x0dcf],
[0x0065, 'ae', 0x0dd0],
[0x0045, 'aee', 0x0dd1],
[0x0073, 'i', 0x0dd2], [0x2018, 'i2', 0], #2018
[0x0053, 'ii', 0x0dd3], [0x2019, 'ii2', 0], #2019
[0x0071, 'u', 0x0dd4], [0x003d, 'u2', 0], #003d for ka and tha
[0x0051, 'uu', 0x0dd6], [0x002b, 'uu2', 0], #002b
[0x0044, 'gp', 0x0dd8], #gata pilla
[0x0066, 'e', 0x0dd9],
[0, 'ei', 0x0dda],
[0x0066, 'ee', 0x0ddb, 1],
[0, 'o', 0x0ddc],
[0, 'oo', 0x0ddd], [0x0064, 'oo_sub', 0, 1], #split matra
[0, 'ou', 0x0dde], [0x0021, 'ou_sub', 0], #split matra
[0x0021, 'gk', 0x0ddf], #gayanu kitta
[0x0044, 'dgp', 0x0df2, 1],
[0x0021, 'dgk', 0x0df3, 1],
[0x0060, 'kna_unused', 0], #no use - but copyover for ref
# punctuation, zwj etc
# leave in the template
# ascii chars
[0x0020, 'space', 0x0020],
[0x0022, 'comma', 0x002c],
[0x0024, 'slash', 0x002f],
[0x0026, 'bracket1', 0x0029],
[0x0027, 'dot', 0x002E],
[0x0028, 'colon', 0x003A],
[0x0029, 'asterisk', 0x002A],
[0x002D, 'short_dash1', 0x002D], [0x002D, 'short_dash2', 0x2010],
[0x0030, '0', 0x0030],
[0x0031, '1', 0x0031],
[0x0032, '2', 0x0032],
[0x0033, '3', 0x0033],
[0x0034, '4', 0x0034],
[0x0035, '5', 0x0035],
[0x0036, '6', 0x0036],
[0x0037, '7', 0x0037],
[0x0038, '8', 0x0038],
[0x0039, '9', 0x0039],
[0x0040, 'question', 0x003F],
[0x005a, 'quoteright', 0x2019],
[0x005d, 'percentage', 0x0025],
[0x005e, 'bracket2', 0x0028],
[0x007a, 'quoteleft', 0x2018],
[0x007d, 'equals', 0x003d],
[0x0080, 'wide_space', 0], #80 mapped to space in FM conversion script. so not needed
[0x00a0, 'apostrophe', 0x0027],
[0x00a1, 'smalldot', 0], #not sure , but conv script substitute to dot
[0x00a4, 'finedash', 0x2013],
[0x00a6, 'semicolon', 0x003b],
[0x00ab, 'multiply', 0x00d7], 
[0x00ac, 'plus', 0x002b],
[0x00ad, 'divide', 0x00f7],
[0x00b2, 'black_circle', 0x25cf],
[0x00b3, 'black_star', 0x22c6],
[0x00b8, 'roman_i', 0x0069],
[0x00b9, 'roman_v', 0x0076],
[0x00ba, 'roman_x', 0x0078],
[0x00bb, 'roman_I', 0x0049],
[0x00bc, 'roman_V', 0x0056],
[0x00bd, 'roman_X', 0x0058],
[0x00b5, 'not_used_da_yansa', 0x00b5], #retain presentation
[0x00b6, 'unknown_al', 0x00b6], #retain presentation
[0x00b7, 'unknown_8', 0x00b7], #retain presentation
[0x00c3, 'black_triangle', 0x25b2],
[0x00e6, 'exclaim', 0x0021],
[0x0131, 'big_space', 0], #conv script maps this to a normal space
[0x0161, 'brace_close', 0x007d],
[0x0178, 'top_white_circle', 0x02da],
[0x02dc, 'dblquote_right', 0x201d],
[0x2014, 'dblquote_left', 0x201c],
[0x201d, 'white_square', 0x25a1],
[0x2022, 'black_square', 0x25a0],
[0x2122, 'brace_open', 0x007b]
];

doneCount = 0;
newCount = 0;
for m in map:
	markNew = 0;
	copyCode = m[0];
	if m[0] == 0: #no glyph to copy, so copy the space
		copyCode = 0x0020;
		markNew = 1;
	elif len(m) > 3 and m[3] > 0:
		markNew = 1;
		
	ogi = fo.FindGlyph(copyCode);
	if (ogi == -1):
		print "glyph with unicode value ", copyCode, " not found in ", fo.family_name;
	else:
		# find a conflit by unicode and name
		ngi = -1;
		if len(m) > 2 and m[2] > 0:
			ngi = fn.FindGlyph(m[2]);
		if ngi == -1:
			ngi = fn.FindGlyph(m[1]);
		if ngi != -1:
			print "Conflict: name ", m[1], "already in new font. Overwriting";
			fn.glyphs[ngi] = fo[ogi];
		else:
			# if no conflit add a new glyph
			fn.glyphs.append(fo[ogi]);
			fl.UpdateFont(fni);
			ngi = fn.FindGlyph(copyCode);
		
		# update new glyph info
		print copyCode, " ngi:", ngi;
		fn[ngi].name = m[1];
		fn[ngi].mark = 0; #in case ogi had a mark already
		if len(m) > 2 and m[2] > 0:
			fn[ngi].unicodes = [m[2]];
		else:
			fn[ngi].unicodes = [];
		
		# process bandi chars
		if "_bandi" in m[1]:
			fn[ngi].width -= bandiWidthReduction;
		
		# marking
		if markNew == 1:
			fn[ngi].mark = 1;
		else: #mark old as copied over
			fo[ogi].mark = 1;
			fl.UpdateFont(foi);
		
		fl.UpdateFont(fni);
		#counting
		newCount += markNew;
		doneCount += 1;
		
print "created ", newCount, " glyphs in ", fn.family_name;
print "copied ", doneCount - newCount, " glyphs from ", fo.family_name;