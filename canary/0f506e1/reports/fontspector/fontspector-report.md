## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[1] fonts/variable</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** fonts/variable/AbhayaLibreCANARY[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: coptic, syriac, tai-le, tifinagh, todhri, math, old-permic, malayalam, duployan, hebrew, canadian-aboriginal
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+03C0 GREEK SMALL LETTER PI: try adding one of: math, greek, yi
* U+2010 HYPHEN: try adding one of: syloti-nagri, armenian, sora-sompeng, hebrew, kaithi, lisu, kayah-li, arabic, coptic, cham, kharoshthi, yi, sundanese
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2126 OHM SIGN: try adding math
* U+212E ESTIMATED SYMBOL: try adding math
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+2219 BULLET OPERATOR: try adding one of: math, symbols, tai-tham, yi
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+222B INTEGRAL: try adding math
* U+2248 ALMOST EQUAL TO: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CA LOZENGE: try adding one of: symbols, math

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin, sinhala, tamil [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[18] fonts/variable/AbhayaLibreCANARY[wght].ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts vertical metric schema (googlefonts/vertical_metrics)</summary>
    <div>








- 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1180 when it should be at least 1200 [code: bad-hhea-range]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check that OS/2 fsSelection WWS bit is set correctly. (opentype/fsselection_wws)</summary>
    <div>








- ⚠️ **WARN** OS/2 fsSelection WWS bit is not set, and the font does not have name IDs 21/22 (WWS Family/Subfamily). If the font's naming is WWS-conformant, the WWS bit should be set. [code: no-wws-without-wws-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. (opentype/GDEF_mark_chars)</summary>
    <div>








- ⚠️ **WARN** The following mark characters should be in the GDEF mark glyph class:

* U+0D81 (candrabindusinh) [code: mark-chars]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni0D9F (U+0D9F): found 2, expected one of: [1, 3, 5]
* uni0DA1 (U+0DA1): found 1, expected one of: [3, 4, 5]
* uni0DB7 (U+0DB7): found 2, expected one of: [1, 3, 4]
* uni0DC5 (U+0DC5): found 1, expected one of: [2, 3, 4]
* uni0B92 (U+0B92): found 4, expected one of: [2, 3]
* uni0B93 (U+0B93): found 5, expected one of: [2, 3]
* uni0B94 (U+0B94): found 7, expected one of: [4, 5]
* uni0B95 (U+0B95): found 1, expected one of: [2, 3, 4]
* uni0B99 (U+0B99): found 3, expected one of: [1, 4, 5]
* uni0B9A (U+0B9A): found 1, expected one of: [2, 3, 4]
* uni0B9E (U+0B9E): found 3, expected one of: [2, 5]
* uni0BA3 (U+0BA3): found 2, expected one of: [3, 4, 5]
* uni0BA8 (U+0BA8): found 2, expected one of: [1, 4, 5]
* uni0BA9 (U+0BA9): found 2, expected one of: [3, 4]
* uni0BB0 (U+0BB0): found 2, expected one of: [1, 3]
* uni0BB6 (U+0BB6): found 1, expected one of: [2, 3]
* uni0BB7 (U+0BB7): found 2, expected one of: [3, 4]
* uni0BB8 (U+0BB8): found 3, expected one of: [1, 2]
* uni0BF1 (U+0BF1): found 2, expected one of: [1, 3, 4]
* uni0BEB (U+0BEB): found 2, expected one of: [1, 3, 4]
* uni0BEE (U+0BEE): found 1, expected one of: [2, 3, 4]
* uni0BEF (U+0BEF): found 1, expected one of: [2, 4]
* uni0BF5 (U+0BF5): found 3, expected one of: [2, 6]
* uni0BF6 (U+0BF6): found 1, expected one of: [2, 4]
* uni0BF8 (U+0BF8): found 2, expected one of: [4, 5, 6]
* uni0BC2 (U+0BC2): found 3, expected one of: [2]
* Idotaccent (U+0130): found 4, expected one of: [2, 3, 6]
* Imacron (U+012A): found 4, expected one of: [2, 3, 6]
* U (U+0055): found 3, expected one of: [1, 2, 5]
* Uacute (U+00DA): found 4, expected one of: [2, 3, 6]
* Ugrave (U+00D9): found 4, expected one of: [2, 3, 6]
* Uhungarumlaut (U+0170): found 5, expected one of: [3, 4, 7]
* Umacron (U+016A): found 4, expected one of: [2, 3, 6]
* V (U+0056): found 3, expected one of: [1, 2, 5]
* z (U+007A): found 4, expected one of: [1, 2, 3]
* two (U+0032): found 3, expected one of: [1, 2, 5]
* three (U+0033): found 4, expected one of: [1, 2, 5]
* five (U+0035): found 3, expected one of: [1, 2, 5]
* seven (U+0037): found 3, expected one of: [1, 2, 5]
* two.osf (unencoded): found 3, expected one of: [1, 2]
* three.osf (unencoded): found 4, expected one of: [1, 3]
* four.osf (unencoded): found 4, expected one of: [1, 2]
* seven.osf (unencoded): found 3, expected one of: [1]
* three.numr (unencoded): found 4, expected one of: [1, 2, 3]
* four.numr (unencoded): found 4, expected one of: [1, 2, 3]
* seven.numr (unencoded): found 3, expected one of: [1, 2]
* uni00B2 (U+00B2): found 3, expected one of: [1, 2]
* uni00B3 (U+00B3): found 4, expected one of: [1, 2]
* divide (U+00F7): found 1, expected one of: [3, 7]
* summation (U+2211): found 5, expected one of: [1, 2] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. (mandatory_avar_table)</summary>
    <div>








- ⚠️ **WARN** The font does not include an avar table.  If the progression rates of axes is linear and no user-mapping is expected, this is fine, and this check can be ignored or excluded. [code: missing-avar]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>








- ⚠️ **WARN** The most common width is 469 among a set of 13  math glyphs.
The following math glyphs have a different width, though:
width=492: logicalnot
width=462: greater, less
width=400: multiply
width=495: approxequal [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>








- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* vocalicllsignsinh
* vocalicrrsignsinh
* gDhUsinh
* cCUsinh
* gDhUusinh
* ndRasinh
* nDRIsinh
* nDRIisinh
* yasign_viramasinh
* daa_virama._csinh
* ndaa_virama._csinh
* jnyaa_virama._csinh
* nyaa_virama._csinh
* nDaa_virama._csinh
* isign.alt3taml
* isign.alt4taml
* isign.alt5taml
* isign.alt6taml
* isign.alt7taml
* iisign.alt1taml
* mooniak
* vertical_stem_upper [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts have relatively consistent sidebearings. (suspicious_sidebearings)</summary>
    <div>








- ⚠️ **WARN** Glyph "isign.alt4taml" has suspiciously high variation (z-score 15.51) in right sidebearings at locations:
    wght=500.00
    wght=600.00
    wght=700.00
    wght=800.00 [code: large-rsb-variation]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure font has overlaps bit set correctly. (overlaps_bit)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlaps but the overlaps bit is not set:
* ghRIisinh
* tRasinh
* egrave (U+00E8)
* tta_rephasinh
* ycircumflex (U+0177)
* archaictwentysinh
* nyIsinh
* dDhUsinh
* section (U+00A7)
* bhRIsinh
* fRIisinh.hist
* wacute (U+1E83)
* llItaml
* jnyUsinh
* ndIisinh
* pUsinh
* shRasinh
* cItaml
* rAesinh
* uni0122 (U+0122)
* tthIisinh
* uni0BB3 (U+0BB3)
* ndRasinh
* nyaa_virama._csinh
* fsinh.hist
* gDhsinh
* ttUtaml
* uni2126 (U+2126)
* Wdieresis (U+1E84)
* Thorn (U+00DE)
* cRasinh
* E (U+0045)
* nnUutaml
* Hbar (U+0126)
* sRsinh
* Iacute (U+00CD)
* ngsinh
* archaicthirtysinh
* Scaron (U+0160)
* ngIitaml
* da_yansa_oosignsinh
* mIsinh
* ba_rephasinh
* threequarters (U+00BE)
* anusvarayaShUusinh
* dUsinh
* uni0DA3 (U+0DA3)
* eacute (U+00E9)
* uni0BC6 (U+0BC6)
* uni0B95 (U+0B95)
* uni00B2 (U+00B2)
* rrIitaml
* ttTthUsinh
* uni0BC0 (U+0BC0)
* seven.osf
* uni0DAB (U+0DAB)
* dVIisinh
* shIisinh
* ssRIisinh
* yIitaml
* yasign_iisignsinh
* dhRasinh
* hRIsinh
* jnyIisinh
* shIitaml
* khRIisinh
* x (U+0078)
* nyChUsinh
* khUusinh
* jUtaml
* greater (U+003E)
* at (U+0040)
* Ugrave (U+00D9)
* dRIsinh
* dRIisinh
* tRsinh
* bha_rephasinh
* nDhIisinh
* scaron (U+0161)
* nnIisinh
* ndUusinh
* jhRsinh
* Uring (U+016E)
* lItaml
* cRsinh
* kRIsinh
* fl (U+FB02)
* nyCsinh
* jnyRsinh
* florin (U+0192)
* dVsinh
* uni0DC3 (U+0DC3)
* ghIsinh
* hRasinh
* llUusinh
* four (U+0034)
* bhIisinh
* Edieresis (U+00CB)
* uni0D9A (U+0D9A)
* nyChIisinh
* kVasinh
* nDa_rephasinh
* nyjUusinh
* archaicsixtysinh
* cUsinh
* uni0DAC (U+0DAC)
* kRsinh
* pIisinh
* yasign_repha_uusignsinh
* Ccedilla (U+00C7)
* uni0BB8 (U+0BB8)
* bBIsinh
* shRsinh
* Aogonek (U+0104)
* sUtaml
* nUtaml
* aasign_viramasinh
* ttIsinh
* uni0BB7 (U+0BB7)
* tThsinh
* uni0B93 (U+0B93)
* kVIisinh
* z (U+007A)
* nyja_rephasinh
* nna2uutaml
* dRasinh
* uni0BC8 (U+0BC8)
* dda_rephasinh
* kIitaml
* uni0BA8 (U+0BA8)
* anusvarayaShUsinh
* rcaron (U+0159)
* ttRIsinh
* sinEight_Zerolith
* Egrave (U+00C8)
* nya_rephasinh
* Ydieresis (U+0178)
* wdieresis (U+1E85)
* gDhasinh
* lsinh
* zhUutaml
* tsinh
* daggerdbl (U+2021)
* infinity (U+221E)
* nna_rephasinh
* nnIsinh
* three (U+0033)
* fIsinh
* rrItaml
* uni0BF3 (U+0BF3)
* dhRIsinh
* uni0145 (U+0145)
* gRIisinh
* ndaae._csinh
* yUsinh
* Adieresis (U+00C4)
* ssUtaml
* Edotaccent (U+0116)
* sa_rephasinh
* ka_rephasinh
* h (U+0068)
* nine (U+0039)
* dUusinh
* cCUusinh
* fRasinh
* radical (U+221A)
* chUsinh
* mRsinh
* lla_rephasinh
* jItaml
* lUsinh
* ttRasinh
* uni0DA2 (U+0DA2)
* kSsataml
* sRIisinh
* pItaml
* ca_rephasinh
* Eth (U+00D0)
* dagger (U+2020)
* nnga_rephasinh
* cRIsinh
* nDae._csinh
* ampersand (U+0026)
* M (U+004D)
* nine.numr
* uni0DA4 (U+0DA4)
* jnyaa_virama._csinh
* llIsinh
* nVa_rephasinh
* archaiceightsinh
* shUusinh
* dollar (U+0024)
* la_rephasinh
* nyCUsinh
* uni0DB3 (U+0DB3)
* pi (U+03C0)
* archaicthreesinh
* nIitaml
* tVasinh
* hUsinh
* bhRIisinh
* six.numr
* Wcircumflex (U+0174)
* Ycircumflex (U+0176)
* jnysinh
* lIsinh
* uni0B90 (U+0B90)
* yIisinh
* uni20BA (U+20BA)
* ssRasinh
* dDhasinh
* fsinh
* nyUsinh
* uni0BE8 (U+0BE8)
* thUsinh
* uni0123 (U+0123)
* wgrave (U+1E81)
* jnyIsinh
* ttTthsinh
* sinFour_Zerolith
* five.osf
* chIsinh
* Scedilla (U+015E)
* csinh
* uni0DDD (U+0DDD)
* nUsinh
* ttTtha_rephasinh
* m (U+006D)
* nyIisinh
* nVUusinh
* uni0B8A (U+0B8A)
* hUtaml
* J (U+004A)
* jUutaml
* nnAataml
* uni0DC2 (U+0DC2)
* Agrave (U+00C0)
* mbUsinh
* uni0BB2 (U+0BB2)
* two (U+0032)
* uni0D95 (U+0D95)
* jhUusinh
* uni0BCB (U+0BCB)
* eogonek (U+0119)
* four.numr
* kVIsinh
* dcaron (U+010F)
* nnIitaml
* caron (U+02C7)
* mUsinh
* tVUusinh
* kUtaml
* nysinh
* bUusinh
* Wgrave (U+1E80)
* zdotaccent (U+017C)
* ngUutaml
* vIsinh
* lUusinh
* Ntilde (U+00D1)
* yIsinh
* Dcaron (U+010E)
* uni0302 (U+0302)
* nDhUusinh
* nyjUsinh
* ngIisinh
* uni0DA6 (U+0DA6)
* kUutaml
* uni0BE9 (U+0BE9)
* nyUutaml
* uni0163 (U+0163)
* psinh
* bRasinh
* ttUutaml
* uni0BF9 (U+0BF9)
* Uacute (U+00DA)
* nyCIsinh
* asterisk (U+002A)
* ssItaml
* uni0B85 (U+0B85)
* sinThree_Zerolith
* uni0BCA (U+0BCA)
* na_rephasinh
* I (U+0049)
* bBa_rephasinh
* seven (U+0037)
* jhUsinh
* tVIsinh
* uni0BF7 (U+0BF7)
* uni0DEA (U+0DEA)
* v (U+0076)
* nThUsinh
* sUsinh
* gIsinh
* Y (U+0059)
* nTha_rephasinh
* ghsinh
* jnyRasinh
* kSssinh
* nyCa_rephasinh
* jnyaa._csinh
* nyChsinh
* uni0BF0 (U+0BF0)
* nUusinh
* tcaron (U+0165)
* uni0D86 (U+0D86)
* abreve (U+0103)
* vUutaml
* kUusinh
* aogonek (U+0105)
* tVsinh
* Acircumflex (U+00C2)
* kSsItaml
* ttsinh
* kIsinh
* tthUusinh
* f_f
* archaiconehundredsinh
* ttUsinh
* W (U+0057)
* nngUusinh
* rrUtaml
* Dcroat (U+0110)
* ddIsinh
* Icircumflex (U+00CE)
* uni0DEC (U+0DEC)
* six.osf
* uni0162 (U+0162)
* uni0DA0 (U+0DA0)
* jhIsinh
* ghRasinh
* hRIisinh
* ttIitaml
* dVIsinh
* cCsinh
* tThUsinh
* nyjRsinh
* kSsIsinh
* uni0BF5 (U+0BF5)
* zhIitaml
* bBasinh
* khUsinh
* zcaron (U+017E)
* cCIsinh
* uni0BF4 (U+0BF4)
* hUutaml
* uni0D8F (U+0D8F)
* Idotaccent (U+0130)
* anusvarayaShIsinh
* llUutaml
* dVa_rephasinh
* g (U+0067)
* jRIisinh
* ssIitaml
* tVa_rephasinh
* ysinh
* R (U+0052)
* phIisinh
* hIsinh
* ghIisinh
* nyChUusinh
* pRasinh
* uni0DE6 (U+0DE6)
* y (U+0079)
* uni0B8E (U+0B8E)
* nna2itaml
* tIisinh
* bIsinh
* gbreve (U+011F)
* five.numr
* rrUutaml
* Idieresis (U+00CF)
* mUusinh
* uni0156 (U+0156)
* germandbls (U+00DF)
* ksinh
* nDsinh
* nyChIsinh
* tUsinh
* cRIisinh
* uni0DC5 (U+0DC5)
* mba_rephasinh
* kRasinh
* T (U+0054)
* uni2113 (U+2113)
* oe (U+0153)
* dDhIsinh
* nDUusinh
* cUtaml
* lAitaml
* product (U+220F)
* ddhUsinh
* f_f_l
* khIsinh
* jRasinh
* llIitaml
* yasign_viramasinh
* Ncaron (U+0147)
* vUusinh
* amacron (U+0101)
* uni0DA1 (U+0DA1)
* fUusinh
* fRIsinh
* fa_rephasinh.hist
* Atilde (U+00C3)
* ygrave (U+1EF3)
* agrave (U+00E0)
* OE (U+0152)
* X (U+0058)
* yacute (U+00FD)
* uni0B94 (U+0B94)
* ddhIsinh
* nyChasinh
* nDhIsinh
* asciicircum (U+005E)
* Ocircumflex (U+00D4)
* Aring (U+00C5)
* nThasinh
* Rcaron (U+0158)
* e (U+0065)
* bBUusinh
* ddRIsinh
* uogonek (U+0173)
* onehalf (U+00BD)
* gDha_rephasinh
* lIitaml
* Lacute (U+0139)
* ttTthasinh
* nnddIisinh
* jIitaml
* nVIsinh
* hsinh
* nyCUusinh
* llsinh
* kVUsinh
* logicalnot (U+00AC)
* archaicseventysinh
* phsinh
* cCIisinh
* Zcaron (U+017D)
* ssUusinh
* paragraph (U+00B6)
* ghRsinh
* archaicninetysinh
* six (U+0036)
* uni0BA4 (U+0BA4)
* gdotaccent (U+0121)
* lslash (U+0142)
* uni0BEB (U+0BEB)
* fIsinh.hist
* nyRsinh
* pUusinh
* gDhIisinh
* khRIsinh
* uni0BC2 (U+0BC2)
* onequarter (U+00BC)
* Ccaron (U+010C)
* summation (U+2211)
* nVsinh
* nIsinh
* fIisinh.hist
* ndRaa._csinh
* uni0D85 (U+0D85)
* tItaml
* ddIisinh
* nna2utaml
* sIitaml
* edieresis (U+00EB)
* edotaccent (U+0117)
* uni1E9E (U+1E9E)
* pRIsinh
* ecircumflex (U+00EA)
* bhRsinh
* zhItaml
* jIisinh
* L (U+004C)
* nDRIisinh
* bhUsinh
* uni0BEA (U+0BEA)
* Uogonek (U+0172)
* yen (U+00A5)
* uni0157 (U+0157)
* nVUsinh
* notequal (U+2260)
* uni0136 (U+0136)
* uni0DB7 (U+0DB7)
* dhRIisinh
* msinh
* nyUusinh
* ssUsinh
* lIisinh
* Abreve (U+0102)
* ttTthUusinh
* Gbreve (U+011E)
* ccedilla (U+00E7)
* jsinh
* nThIsinh
* tRIisinh
* kha_rephasinh
* bRsinh
* kSsUutaml
* Lslash (U+0141)
* q (U+0071)
* d (U+0064)
* gDhUusinh
* uni00B5 (U+00B5)
* nda_rephasinh
* dDhUusinh
* A (U+0041)
* uni0BA9 (U+0BA9)
* dsinh
* nyRIsinh
* Amacron (U+0100)
* sIisinh
* cCa_rephasinh
* kVsinh
* Iogonek (U+012E)
* yasign_usignsinh
* nine.osf
* mIisinh
* gUsinh
* kSsUusinh
* dDhIisinh
* bRIisinh
* lessequal (U+2264)
* nnUusinh
* jIsinh
* uni0BD7 (U+0BD7)
* pIitaml
* cIitaml
* ngIsinh
* rUtaml
* nyjIisinh
* ma_rephasinh
* nnddIsinh
* mbIisinh
* uni021A (U+021A)
* Umacron (U+016A)
* cent (U+00A2)
* archaictensinh
* Eogonek (U+0118)
* nDhUsinh
* Nacute (U+0143)
* jhRIisinh
* ccaron (U+010D)
* bhUusinh
* khIisinh
* nyRasinh
* dvocalicrr._csinh
* kSsUtaml
* uni0BC7 (U+0BC7)
* ghRIsinh
* dDha_rephasinh
* jnyRIsinh
* uni0BF2 (U+0BF2)
* hIisinh
* dIisinh
* nnddUusinh
* ddUsinh
* dvocalicr._csinh
* uni0B87 (U+0B87)
* dyUu._csinh
* tVUsinh
* jUsinh
* cIsinh
* D (U+0044)
* ndaa_virama._csinh
* ddRsinh
* ja_rephasinh
* G (U+0047)
* sRIsinh
* Aacute (U+00C1)
* llUsinh
* nDRIsinh
* ssa_rephasinh
* zhUtaml
* nDaa_virama._csinh
* nIisinh
* uni013B (U+013B)
* nna2iitaml
* Gdotaccent (U+0120)
* thIsinh
* gDhIsinh
* f (U+0066)
* sinOne_Zerolith
* uni0D87 (U+0D87)
* fRasinh.hist
* nsinh
* shRIsinh
* sinTwo_Zerolith
* chIisinh
* uni0BB5 (U+0BB5)
* tVIisinh
* dVasinh
* three.osf
* vItaml
* uni0BAF (U+0BAF)
* kSsUsinh
* aisigntaml.alt
* gRsinh
* Igrave (U+00CC)
* rIisinh
* ra_rephasinh
* rsinh
* tIitaml
* archaiconesinh
* dhUsinh
* bhRasinh
* gsinh
* fUusinh.hist
* uni0BE7 (U+0BE7)
* nVasinh
* ddhIisinh
* sUusinh
* ucircumflex (U+00FB)
* uni0BEF (U+0BEF)
* shreetaml
* numbersign (U+0023)
* kItaml
* ntilde (U+00F1)
* nyae._csinh
* archaicfivesinh
* oslash (U+00F8)
* uni0D9D (U+0D9D)
* tThasinh
* gRasinh
* V (U+0056)
* vocalicllsignsinh
* vRasinh
* dIsinh
* ddRIisinh
* bBsinh
* rIsinh
* ddhUusinh
* dha_rephasinh
* pIsinh
* Ucircumflex (U+00DB)
* seven.numr
* jnyUusinh
* Yacute (U+00DD)
* thsinh
* K (U+004B)
* pRIisinh
* uni0BEC (U+0BEC)
* nyCIisinh
* U (U+0055)
* plusminus (U+00B1)
* eight.numr
* nyjIsinh
* uni0B9E (U+0B9E)
* four.osf
* llAitaml
* nnddsinh
* ndIsinh
* nna2aitaml
* uni0BF6 (U+0BF6)
* uni2206 (U+2206)
* nna2aataml
* sRasinh
* uni0BB0 (U+0BB0)
* tIsinh
* mRIisinh
* thUusinh
* uni0B86 (U+0B86)
* mUtaml
* shsinh
* ydieresis (U+00FF)
* Ecaron (U+011A)
* archaicsevensinh
* yasign_isignsinh
* F (U+0046)
* fUsinh.hist
* iogonek (U+012F)
* uni0B9C (U+0B9C)
* sinSix_Zerolith
* b (U+0062)
* uni0B89 (U+0B89)
* ssIsinh
* archaicfoursinh
* fIisinh
* pRsinh
* ndaa._csinh
* rIitaml
* Oslash (U+00D8)
* uni0137 (U+0137)
* two.osf
* uni0BCC (U+0BCC)
* Euro (U+20AC)
* tThUusinh
* llIisinh
* jnyaae._csinh
* nyaa._csinh
* H (U+0048)
* thIisinh
* r (U+0072)
* nyRIisinh
* iisign.alt1taml
* nThsinh
* ddha_rephasinh
* kSsIitaml
* ddUusinh
* ncaron (U+0148)
* jnyRIisinh
* fRsinh.hist
* uni00B3 (U+00B3)
* eth (U+00F0)
* rUsinh
* phUusinh
* nyaae._csinh
* n (U+006E)
* lUutaml
* eight.osf
* uni0BB6 (U+0BB6)
* uni0D92 (U+0D92)
* icircumflex (U+00EE)
* Imacron (U+012A)
* sinSeven_Zerolith
* nyIitaml
* dVUsinh
* yItaml
* mbUusinh
* vUsinh
* uni0D90 (U+0D90)
* nVIisinh
* sItaml
* vIisinh
* w (U+0077)
* uni0B92 (U+0B92)
* lUtaml
* nThIisinh
* mbIsinh
* nDhasinh
* ddsinh
* dyaa._csinh
* nyUtaml
* hbar (U+0127)
* vRsinh
* kVUusinh
* iisign.alttaml
* dVUusinh
* kRIisinh
* uni0D91 (U+0D91)
* uni0BF8 (U+0BF8)
* a (U+0061)
* uni0D88 (U+0D88)
* phUsinh
* adieresis (U+00E4)
* uni0BB4 (U+0BB4)
* nThUusinh
* AE (U+00C6)
* ocircumflex (U+00F4)
* dhRsinh
* eight (U+0038)
* ttUusinh
* yasign_repha_usignsinh
* t (U+0074)
* gRIsinh
* yUusinh
* f_f_i
* nDIisinh
* Emacron (U+0112)
* uni20BD (U+20BD)
* gUusinh
* nyjRasinh
* anusvarayaShasinh
* hUusinh
* nngUsinh
* ordfeminine (U+00AA)
* dya._csinh
* phIsinh
* khsinh
* nDasinh
* ttRIisinh
* gDhUsinh
* uni0146 (U+0146)
* bhIsinh
* rAaesinh
* shIsinh
* nDRasinh
* kSsIisinh
* ghUsinh
* ttRsinh
* archaiconethousandsinh
* uni0B9A (U+0B9A)
* uni0DE9 (U+0DE9)
* hItaml
* ssinh
* plus (U+002B)
* jhRIsinh
* ssUutaml
* ttItaml
* Lcaron (U+013D)
* nnItaml
* uni0D93 (U+0D93)
* Tcaron (U+0164)
* ddRasinh
* ttIisinh
* uni0BA3 (U+0BA3)
* trademark (U+2122)
* va_rephasinh
* ndae._csinh
* jnya_rephasinh
* ttha_rephasinh
* ssRIsinh
* ddhsinh
* nDaae._csinh
* ndUsinh
* dyU._csinh
* uni0BEE (U+0BEE)
* jRIsinh
* anusvarayaShsinh
* two.numr
* rUutaml
* nyjsinh
* nndda_rephasinh
* kSsasinh
* khRsinh
* dcroat (U+0111)
* fRIsinh.hist
* kSsa_rephasinh
* dDhsinh
* Udieresis (U+00DC)
* nUutaml
* uni0DA5 (U+0DA5)
* uni0BAE (U+0BAE)
* ae (U+00E6)
* chUusinh
* Racute (U+0154)
* fi (U+FB01)
* tUutaml
* mItaml
* dRsinh
* yasign_uusignsinh
* nngIisinh
* tthUsinh
* ssRsinh
* cha_rephasinh
* uni0B99 (U+0B99)
* llUtaml
* nnUsinh
* circumflex (U+02C6)
* vIitaml
* nngIsinh
* jhRasinh
* mRIsinh
* pUutaml
* cCUsinh
* tThIsinh
* fRIisinh
* nyCha_rephasinh
* vRIisinh
* archaicsixsinh
* B (U+0042)
* k (U+006B)
* uni021B (U+021B)
* nnAitaml
* zacute (U+017A)
* daa_virama._csinh
* archaiceightysinh
* nyItaml
* Wacute (U+1E82)
* N (U+004E)
* uni0BF1 (U+0BF1)
* Ecircumflex (U+00CA)
* ghUusinh
* currency (U+00A4)
* tthsinh
* fUsinh
* bRIsinh
* uni0BD0 (U+0BD0)
* kIisinh
* nDhsinh
* uni0B8F (U+0B8F)
* bBUsinh
* racute (U+0155)
* mUutaml
* nnddUsinh
* dhUusinh
* sssinh
* sIsinh
* hRsinh
* ttTthIsinh
* mRasinh
* sterling (U+00A3)
* shItaml
* jnyae._csinh
* acircumflex (U+00E2)
* Eacute (U+00C9)
* cIisinh
* partialdiff (U+2202)
* three.numr
* nDaa._csinh
* uni030C (U+030C)
* bUsinh
* tUusinh
* jhIisinh
* greaterequal (U+2265)
* uni0DE8 (U+0DE8)
* nacute (U+0144)
* uni0D9F (U+0D9F)
* rItaml
* Ygrave (U+1EF2)
* Uhungarumlaut (U+0170)
* fRsinh
* kVa_rephasinh
* dRaa._csinh
* jha_rephasinh
* five (U+0035)
* jUusinh
* anusvarayaShIisinh
* cUutaml
* wcircumflex (U+0175)
* uni0BED (U+0BED)
* archaicfiftysinh
* mIitaml
* bBIisinh
* sinFive_Zerolith
* chsinh
* tthIsinh
* hIitaml
* multiply (U+00D7)
* tTha_rephasinh
* fasinh.hist
* khRasinh
* P (U+0050)
* Q (U+0051)
* jRsinh
* nDha_rephasinh
* shRIisinh
* rrAataml
* aring (U+00E5)
* tRIsinh
* archaicfortysinh
* kUsinh
* uni0BB1 (U+0BB1)
* gha_rephasinh
* tUtaml
* shUsinh
* nga_rephasinh
* nnUtaml
* bIisinh
* ndsinh
* ssIisinh
* nDUsinh
* cUusinh
* tThIisinh
* nngsinh
* nnsinh
* yUutaml
* less (U+003C)
* jhsinh
* aacute (U+00E1)
* ttTthIisinh
* sinNine_Zerolith
* ngItaml
* emacron (U+0113)
* bhsinh
* nyCasinh
* atilde (U+00E3)
* nDIsinh
* rUusinh
* vRIsinh
* nItaml
* ecaron (U+011B)
* uni0BB9 (U+0BB9)
* uni0DEF (U+0DEF) [code: no-overlaps-bit]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * cs_Latn (Czech)            |
|   The following auxiliary characters are missing from the font: Ĕ | * cy_Latn (Welsh)            |
|   The following auxiliary characters are missing from the font: Ĭ | * es_Latn (Spanish)          |
|   The following auxiliary characters are missing from the font: Ŏ | * hu_Latn (Hungarian)        |
|   The following auxiliary characters are missing from the font: Ŭ | * pt_Latn (Portuguese)       |
|   The following auxiliary characters are missing from the font: ĕ | * sk_Latn (Slovak)           |
|   The following auxiliary characters are missing from the font: ĭ | * tr_Latn (Turkish)          |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŀ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŀ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŝ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŝ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ĩ |                              |
|   The following auxiliary characters are missing from the font: Ũ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ĩ |                              |
|   The following auxiliary characters are missing from the font: ũ |                              |
|   Shaper didn't attach tildecomb to M when shaping the text 'M̃'   |                              |
|   Shaper didn't attach tildecomb to l when shaping the text 'l̃'   |                              |
|   Shaper didn't attach tildecomb to m when shaping the text 'm̃'   |                              |
| Auxiliary orthography codepoints:                                 | * nl_Latn (Dutch)            |
|   The following auxiliary characters are missing from the font: Ĳ |                              |
|   The following auxiliary characters are missing from the font: ĳ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** Missing separator glyph U+2028 [code: missing-separator-glyphs]
  
  


- ⚠️ **WARN** Missing separator glyph U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings:

* į̄
* į́
* į̌
* į̃
* į̂
* į̀The dot of soft dotted characters _should_ disappear in other cases, for example:

* į̆
* į̊
* į̋
* į̇
* į̈ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph (outline_direction)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have a counter-clockwise outer contour:

* .notdef has a counter-clockwise outer contour
* uni0D85 (U+0D85) has a counter-clockwise outer contour
* uni0D85 (U+0D85) has a counter-clockwise outer contour
* uni0D85 (U+0D85) has a counter-clockwise outer contour
* uni0D86 (U+0D86) has a counter-clockwise outer contour
* uni0D86 (U+0D86) has a counter-clockwise outer contour
* uni0D86 (U+0D86) has a counter-clockwise outer contour
* uni0D86 (U+0D86) has a counter-clockwise outer contour
* uni0D87 (U+0D87) has a counter-clockwise outer contour
* uni0D87 (U+0D87) has a counter-clockwise outer contour
* uni0D87 (U+0D87) has a counter-clockwise outer contour
* uni0D87 (U+0D87) has a counter-clockwise outer contour
* uni0D88 (U+0D88) has a counter-clockwise outer contour
* uni0D88 (U+0D88) has a counter-clockwise outer contour
* uni0D88 (U+0D88) has a counter-clockwise outer contour
* uni0D88 (U+0D88) has a counter-clockwise outer contour
* uni0D89 (U+0D89) has a counter-clockwise outer contour
* uni0D8A (U+0D8A) has a counter-clockwise outer contour
* uni0D8A (U+0D8A) has a counter-clockwise outer contour
* uni0D8B (U+0D8B) has a counter-clockwise outer contour
* uni0D8C (U+0D8C) has a counter-clockwise outer contour
* uni0D8C (U+0D8C) has a counter-clockwise outer contour
* uni0D8D (U+0D8D) has a counter-clockwise outer contour
* uni0D8D (U+0D8D) has a counter-clockwise outer contour
* uni0D8E (U+0D8E) has a counter-clockwise outer contour
* uni0D8E (U+0D8E) has a counter-clockwise outer contour
* uni0D8E (U+0D8E) has a counter-clockwise outer contour
* uni0D8F (U+0D8F) has a counter-clockwise outer contour
* uni0D8F (U+0D8F) has a counter-clockwise outer contour
* uni0D8F (U+0D8F) has a counter-clockwise outer contour
* uni0D90 (U+0D90) has a counter-clockwise outer contour
* uni0D90 (U+0D90) has a counter-clockwise outer contour
* uni0D90 (U+0D90) has a counter-clockwise outer contour
* uni0D90 (U+0D90) has a counter-clockwise outer contour
* uni0D91 (U+0D91) has a counter-clockwise outer contour
* uni0D91 (U+0D91) has a counter-clockwise outer contour
* uni0D92 (U+0D92) has a counter-clockwise outer contour
* uni0D92 (U+0D92) has a counter-clockwise outer contour
* uni0D92 (U+0D92) has a counter-clockwise outer contour
* uni0D93 (U+0D93) has a counter-clockwise outer contour
* uni0D93 (U+0D93) has a counter-clockwise outer contour
* uni0D93 (U+0D93) has a counter-clockwise outer contour
* uni0D94 (U+0D94) has a counter-clockwise outer contour
* uni0D95 (U+0D95) has a counter-clockwise outer contour
* uni0D95 (U+0D95) has a counter-clockwise outer contour
* uni0D96 (U+0D96) has a counter-clockwise outer contour
* uni0D96 (U+0D96) has a counter-clockwise outer contour
* uni0D9A (U+0D9A) has a counter-clockwise outer contour
* uni0D9B (U+0D9B) has a counter-clockwise outer contour
* uni0D9C (U+0D9C) has a counter-clockwise outer contour
* uni0D9D (U+0D9D) has a counter-clockwise outer contour
* uni0D9D (U+0D9D) has a counter-clockwise outer contour
* uni0D9E (U+0D9E) has a counter-clockwise outer contour
* uni0D9F (U+0D9F) has a counter-clockwise outer contour
* uni0D9F (U+0D9F) has a counter-clockwise outer contour
* uni0DA0 (U+0DA0) has a counter-clockwise outer contour
* uni0DA0 (U+0DA0) has a counter-clockwise outer contour
* uni0DA1 (U+0DA1) has a counter-clockwise outer contour
* uni0DA2 (U+0DA2) has a counter-clockwise outer contour
* uni0DA3 (U+0DA3) has a counter-clockwise outer contour
* uni0DA3 (U+0DA3) has a counter-clockwise outer contour
* uni0DA4 (U+0DA4) has a counter-clockwise outer contour
* uni0DA4 (U+0DA4) has a counter-clockwise outer contour
* uni0DA4 (U+0DA4) has a counter-clockwise outer contour
* uni0DA5 (U+0DA5) has a counter-clockwise outer contour
* uni0DA5 (U+0DA5) has a counter-clockwise outer contour
* uni0DA5 (U+0DA5) has a counter-clockwise outer contour
* uni0DA6 (U+0DA6) has a counter-clockwise outer contour
* uni0DA6 (U+0DA6) has a counter-clockwise outer contour
* uni0DA7 (U+0DA7) has a counter-clockwise outer contour
* uni0DA8 (U+0DA8) has a counter-clockwise outer contour
* uni0DA9 (U+0DA9) has a counter-clockwise outer contour
* uni0DAA (U+0DAA) has a counter-clockwise outer contour
* uni0DAB (U+0DAB) has a counter-clockwise outer contour
* uni0DAB (U+0DAB) has a counter-clockwise outer contour
* uni0DAC (U+0DAC) has a counter-clockwise outer contour
* uni0DAC (U+0DAC) has a counter-clockwise outer contour
* uni0DAD (U+0DAD) has a counter-clockwise outer contour
* uni0DAE (U+0DAE) has a counter-clockwise outer contour
* uni0DAF (U+0DAF) has a counter-clockwise outer contour
* uni0DB0 (U+0DB0) has a counter-clockwise outer contour
* uni0DB1 (U+0DB1) has a counter-clockwise outer contour
* uni0DB3 (U+0DB3) has a counter-clockwise outer contour
* uni0DB3 (U+0DB3) has a counter-clockwise outer contour
* uni0DB4 (U+0DB4) has a counter-clockwise outer contour
* uni0DB5 (U+0DB5) has a counter-clockwise outer contour
* uni0DB6 (U+0DB6) has a counter-clockwise outer contour
* uni0DB7 (U+0DB7) has a counter-clockwise outer contour
* uni0DB7 (U+0DB7) has a counter-clockwise outer contour
* uni0DB8 (U+0DB8) has a counter-clockwise outer contour
* uni0DB9 (U+0DB9) has a counter-clockwise outer contour
* uni0DBA (U+0DBA) has a counter-clockwise outer contour
* uni0DBB (U+0DBB) has a counter-clockwise outer contour
* uni0DBD (U+0DBD) has a counter-clockwise outer contour
* uni0DC0 (U+0DC0) has a counter-clockwise outer contour
* uni0DC1 (U+0DC1) has a counter-clockwise outer contour
* uni0DC2 (U+0DC2) has a counter-clockwise outer contour
* uni0DC3 (U+0DC3) has a counter-clockwise outer contour
* uni0DC3 (U+0DC3) has a counter-clockwise outer contour
* uni0DC4 (U+0DC4) has a counter-clockwise outer contour
* uni0DC5 (U+0DC5) has a counter-clockwise outer contour
* uni0DC6 (U+0DC6) has a counter-clockwise outer contour
* kSsasinh has a counter-clockwise outer contour
* kSsasinh has a counter-clockwise outer contour
* kVasinh has a counter-clockwise outer contour
* kVasinh has a counter-clockwise outer contour
* tVasinh has a counter-clockwise outer contour
* tVasinh has a counter-clockwise outer contour
* tThasinh has a counter-clockwise outer contour
* tThasinh has a counter-clockwise outer contour
* nDasinh has a counter-clockwise outer contour
* nDasinh has a counter-clockwise outer contour
* nDhasinh has a counter-clockwise outer contour
* nDhasinh has a counter-clockwise outer contour
* nVasinh has a counter-clockwise outer contour
* nVasinh has a counter-clockwise outer contour
* nThasinh has a counter-clockwise outer contour
* nThasinh has a counter-clockwise outer contour
* gDhasinh has a counter-clockwise outer contour
* gDhasinh has a counter-clockwise outer contour
* dVasinh has a counter-clockwise outer contour
* dVasinh has a counter-clockwise outer contour
* dDhasinh has a counter-clockwise outer contour
* dDhasinh has a counter-clockwise outer contour
* ttTthasinh has a counter-clockwise outer contour
* ttTthasinh has a counter-clockwise outer contour
* nyCasinh has a counter-clockwise outer contour
* nyCasinh has a counter-clockwise outer contour
* nyCasinh has a counter-clockwise outer contour
* nyChasinh has a counter-clockwise outer contour
* nyChasinh has a counter-clockwise outer contour
* cCasinh has a counter-clockwise outer contour
* bBasinh has a counter-clockwise outer contour
* uni0DD1 (U+0DD1) has a counter-clockwise outer contour
* uni0DD0 (U+0DD0) has a counter-clockwise outer contour
* uni0DDB (U+0DDB) has a counter-clockwise outer contour
* uni0DDB (U+0DDB) has a counter-clockwise outer contour
* uni0DDE (U+0DDE) has a counter-clockwise outer contour
* uni0DDE (U+0DDE) has a counter-clockwise outer contour
* uni0DD9 (U+0DD9) has a counter-clockwise outer contour
* uni0DDA (U+0DDA) has a counter-clockwise outer contour
* uni0DDA (U+0DDA) has a counter-clockwise outer contour
* uni0DD2 (U+0DD2) has a counter-clockwise outer contour
* uni0DD3 (U+0DD3) has a counter-clockwise outer contour
* vocaliclsignsinh has a counter-clockwise outer contour
* uni0DDC (U+0DDC) has a counter-clockwise outer contour
* uni0DDC (U+0DDC) has a counter-clockwise outer contour
* uni0DDD (U+0DDD) has a counter-clockwise outer contour
* uni0DDD (U+0DDD) has a counter-clockwise outer contour
* uni0DDD (U+0DDD) has a counter-clockwise outer contour
* uni0DD8 (U+0DD8) has a counter-clockwise outer contour
* vocalicrrsignsinh has a counter-clockwise outer contour
* vocalicrrsignsinh has a counter-clockwise outer contour
* uni0DD4 (U+0DD4) has a counter-clockwise outer contour
* uni0DD6 (U+0DD6) has a counter-clockwise outer contour
* usign.rasignsinh has a counter-clockwise outer contour
* uusign.rasignsinh has a counter-clockwise outer contour
* uni0DCA (U+0DCA) has a counter-clockwise outer contour
* rasignsinh has a counter-clockwise outer contour
* rephasinh has a counter-clockwise outer contour
* uni0D82 (U+0D82) has a counter-clockwise outer contour
* candrabindusinh (U+0D81) has a counter-clockwise outer contour
* uni0D83 (U+0D83) has a counter-clockwise outer contour
* uni0D83 (U+0D83) has a counter-clockwise outer contour
* uni0DCF (U+0DCF) has a counter-clockwise outer contour
* aasign_viramasinh has a counter-clockwise outer contour
* aasign_viramasinh has a counter-clockwise outer contour
* ksinh has a counter-clockwise outer contour
* ksinh has a counter-clockwise outer contour
* khsinh has a counter-clockwise outer contour
* khsinh has a counter-clockwise outer contour
* gsinh has a counter-clockwise outer contour
* gsinh has a counter-clockwise outer contour
* ghsinh has a counter-clockwise outer contour
* ghsinh has a counter-clockwise outer contour
* ghsinh has a counter-clockwise outer contour
* ngsinh has a counter-clockwise outer contour
* ngsinh has a counter-clockwise outer contour
* nngsinh has a counter-clockwise outer contour
* nngsinh has a counter-clockwise outer contour
* nngsinh has a counter-clockwise outer contour
* csinh has a counter-clockwise outer contour
* csinh has a counter-clockwise outer contour
* csinh has a counter-clockwise outer contour
* chsinh has a counter-clockwise outer contour
* chsinh has a counter-clockwise outer contour
* jsinh has a counter-clockwise outer contour
* jsinh has a counter-clockwise outer contour
* jhsinh has a counter-clockwise outer contour
* jhsinh has a counter-clockwise outer contour
* nysinh has a counter-clockwise outer contour
* nysinh has a counter-clockwise outer contour
* nysinh has a counter-clockwise outer contour
* nysinh has a counter-clockwise outer contour
* jnysinh has a counter-clockwise outer contour
* jnysinh has a counter-clockwise outer contour
* jnysinh has a counter-clockwise outer contour
* jnysinh has a counter-clockwise outer contour
* nyjsinh has a counter-clockwise outer contour
* nyjsinh has a counter-clockwise outer contour
* nyjsinh has a counter-clockwise outer contour
* ttsinh has a counter-clockwise outer contour
* ttsinh has a counter-clockwise outer contour
* tthsinh has a counter-clockwise outer contour
* tthsinh has a counter-clockwise outer contour
* ddsinh has a counter-clockwise outer contour
* ddsinh has a counter-clockwise outer contour
* ddhsinh has a counter-clockwise outer contour
* ddhsinh has a counter-clockwise outer contour
* nnsinh has a counter-clockwise outer contour
* nnsinh has a counter-clockwise outer contour
* nnsinh has a counter-clockwise outer contour
* nnddsinh has a counter-clockwise outer contour
* nnddsinh has a counter-clockwise outer contour
* nnddsinh has a counter-clockwise outer contour
* tsinh has a counter-clockwise outer contour
* tsinh has a counter-clockwise outer contour
* thsinh has a counter-clockwise outer contour
* thsinh has a counter-clockwise outer contour
* dsinh has a counter-clockwise outer contour
* dsinh has a counter-clockwise outer contour
* dhsinh has a counter-clockwise outer contour
* nsinh has a counter-clockwise outer contour
* nsinh has a counter-clockwise outer contour
* ndsinh has a counter-clockwise outer contour
* ndsinh has a counter-clockwise outer contour
* ndsinh has a counter-clockwise outer contour
* psinh has a counter-clockwise outer contour
* psinh has a counter-clockwise outer contour
* phsinh has a counter-clockwise outer contour
* phsinh has a counter-clockwise outer contour
* bsinh has a counter-clockwise outer contour
* bhsinh has a counter-clockwise outer contour
* bhsinh has a counter-clockwise outer contour
* bhsinh has a counter-clockwise outer contour
* msinh has a counter-clockwise outer contour
* msinh has a counter-clockwise outer contour
* mbsinh has a counter-clockwise outer contour
* ysinh has a counter-clockwise outer contour
* ysinh has a counter-clockwise outer contour
* rsinh has a counter-clockwise outer contour
* rsinh has a counter-clockwise outer contour
* lsinh has a counter-clockwise outer contour
* lsinh has a counter-clockwise outer contour
* vsinh has a counter-clockwise outer contour
* shsinh has a counter-clockwise outer contour
* shsinh has a counter-clockwise outer contour
* sssinh has a counter-clockwise outer contour
* sssinh has a counter-clockwise outer contour
* ssinh has a counter-clockwise outer contour
* ssinh has a counter-clockwise outer contour
* ssinh has a counter-clockwise outer contour
* hsinh has a counter-clockwise outer contour
* hsinh has a counter-clockwise outer contour
* llsinh has a counter-clockwise outer contour
* llsinh has a counter-clockwise outer contour
* fsinh has a counter-clockwise outer contour
* fsinh has a counter-clockwise outer contour
* kSssinh has a counter-clockwise outer contour
* kSssinh has a counter-clockwise outer contour
* kSssinh has a counter-clockwise outer contour
* kVsinh has a counter-clockwise outer contour
* kVsinh has a counter-clockwise outer contour
* tVsinh has a counter-clockwise outer contour
* tVsinh has a counter-clockwise outer contour
* tThsinh has a counter-clockwise outer contour
* tThsinh has a counter-clockwise outer contour
* tThsinh has a counter-clockwise outer contour
* nDsinh has a counter-clockwise outer contour
* nDsinh has a counter-clockwise outer contour
* nDsinh has a counter-clockwise outer contour
* nDhsinh has a counter-clockwise outer contour
* nDhsinh has a counter-clockwise outer contour
* nVsinh has a counter-clockwise outer contour
* nVsinh has a counter-clockwise outer contour
* nThsinh has a counter-clockwise outer contour
* nThsinh has a counter-clockwise outer contour
* nThsinh has a counter-clockwise outer contour
* gDhsinh has a counter-clockwise outer contour
* gDhsinh has a counter-clockwise outer contour
* dVsinh has a counter-clockwise outer contour
* dVsinh has a counter-clockwise outer contour
* dDhsinh has a counter-clockwise outer contour
* dDhsinh has a counter-clockwise outer contour
* ttTthsinh has a counter-clockwise outer contour
* ttTthsinh has a counter-clockwise outer contour
* ttTthsinh has a counter-clockwise outer contour
* nyCsinh has a counter-clockwise outer contour
* nyCsinh has a counter-clockwise outer contour
* nyCsinh has a counter-clockwise outer contour
* nyCsinh has a counter-clockwise outer contour
* nyChsinh has a counter-clockwise outer contour
* nyChsinh has a counter-clockwise outer contour
* nyChsinh has a counter-clockwise outer contour
* cCsinh has a counter-clockwise outer contour
* cCsinh has a counter-clockwise outer contour
* bBsinh has a counter-clockwise outer contour
* kIsinh has a counter-clockwise outer contour
* kIsinh has a counter-clockwise outer contour
* khIsinh has a counter-clockwise outer contour
* khIsinh has a counter-clockwise outer contour
* gIsinh has a counter-clockwise outer contour
* gIsinh has a counter-clockwise outer contour
* ghIsinh has a counter-clockwise outer contour
* ghIsinh has a counter-clockwise outer contour
* ghIsinh has a counter-clockwise outer contour
* ngIsinh has a counter-clockwise outer contour
* ngIsinh has a counter-clockwise outer contour
* nngIsinh has a counter-clockwise outer contour
* nngIsinh has a counter-clockwise outer contour
* nngIsinh has a counter-clockwise outer contour
* cIsinh has a counter-clockwise outer contour
* cIsinh has a counter-clockwise outer contour
* cIsinh has a counter-clockwise outer contour
* chIsinh has a counter-clockwise outer contour
* chIsinh has a counter-clockwise outer contour
* jIsinh has a counter-clockwise outer contour
* jIsinh has a counter-clockwise outer contour
* jhIsinh has a counter-clockwise outer contour
* jhIsinh has a counter-clockwise outer contour
* nyIsinh has a counter-clockwise outer contour
* nyIsinh has a counter-clockwise outer contour
* nyIsinh has a counter-clockwise outer contour
* nyIsinh has a counter-clockwise outer contour
* jnyIsinh has a counter-clockwise outer contour
* jnyIsinh has a counter-clockwise outer contour
* jnyIsinh has a counter-clockwise outer contour
* jnyIsinh has a counter-clockwise outer contour
* nyjIsinh has a counter-clockwise outer contour
* nyjIsinh has a counter-clockwise outer contour
* nyjIsinh has a counter-clockwise outer contour
* ttIsinh has a counter-clockwise outer contour
* ttIsinh has a counter-clockwise outer contour
* tthIsinh has a counter-clockwise outer contour
* tthIsinh has a counter-clockwise outer contour
* ddIsinh has a counter-clockwise outer contour
* ddIsinh has a counter-clockwise outer contour
* ddhIsinh has a counter-clockwise outer contour
* ddhIsinh has a counter-clockwise outer contour
* nnIsinh has a counter-clockwise outer contour
* nnIsinh has a counter-clockwise outer contour
* nnIsinh has a counter-clockwise outer contour
* nnddIsinh has a counter-clockwise outer contour
* nnddIsinh has a counter-clockwise outer contour
* nnddIsinh has a counter-clockwise outer contour
* tIsinh has a counter-clockwise outer contour
* tIsinh has a counter-clockwise outer contour
* thIsinh has a counter-clockwise outer contour
* thIsinh has a counter-clockwise outer contour
* dIsinh has a counter-clockwise outer contour
* dIsinh has a counter-clockwise outer contour
* dhIsinh has a counter-clockwise outer contour
* nIsinh has a counter-clockwise outer contour
* nIsinh has a counter-clockwise outer contour
* ndIsinh has a counter-clockwise outer contour
* ndIsinh has a counter-clockwise outer contour
* ndIsinh has a counter-clockwise outer contour
* pIsinh has a counter-clockwise outer contour
* pIsinh has a counter-clockwise outer contour
* phIsinh has a counter-clockwise outer contour
* phIsinh has a counter-clockwise outer contour
* bIsinh has a counter-clockwise outer contour
* bIsinh has a counter-clockwise outer contour
* bhIsinh has a counter-clockwise outer contour
* bhIsinh has a counter-clockwise outer contour
* bhIsinh has a counter-clockwise outer contour
* mIsinh has a counter-clockwise outer contour
* mIsinh has a counter-clockwise outer contour
* mbIsinh has a counter-clockwise outer contour
* mbIsinh has a counter-clockwise outer contour
* yIsinh has a counter-clockwise outer contour
* yIsinh has a counter-clockwise outer contour
* rIsinh has a counter-clockwise outer contour
* rIsinh has a counter-clockwise outer contour
* lIsinh has a counter-clockwise outer contour
* lIsinh has a counter-clockwise outer contour
* vIsinh has a counter-clockwise outer contour
* vIsinh has a counter-clockwise outer contour
* shIsinh has a counter-clockwise outer contour
* shIsinh has a counter-clockwise outer contour
* ssIsinh has a counter-clockwise outer contour
* ssIsinh has a counter-clockwise outer contour
* sIsinh has a counter-clockwise outer contour
* sIsinh has a counter-clockwise outer contour
* sIsinh has a counter-clockwise outer contour
* hIsinh has a counter-clockwise outer contour
* hIsinh has a counter-clockwise outer contour
* llIsinh has a counter-clockwise outer contour
* llIsinh has a counter-clockwise outer contour
* fIsinh has a counter-clockwise outer contour
* fIsinh has a counter-clockwise outer contour
* kSsIsinh has a counter-clockwise outer contour
* kSsIsinh has a counter-clockwise outer contour
* kSsIsinh has a counter-clockwise outer contour
* kVIsinh has a counter-clockwise outer contour
* kVIsinh has a counter-clockwise outer contour
* kVIsinh has a counter-clockwise outer contour
* tVIsinh has a counter-clockwise outer contour
* tVIsinh has a counter-clockwise outer contour
* tVIsinh has a counter-clockwise outer contour
* tThIsinh has a counter-clockwise outer contour
* tThIsinh has a counter-clockwise outer contour
* tThIsinh has a counter-clockwise outer contour
* nDIsinh has a counter-clockwise outer contour
* nDIsinh has a counter-clockwise outer contour
* nDIsinh has a counter-clockwise outer contour
* nDhIsinh has a counter-clockwise outer contour
* nDhIsinh has a counter-clockwise outer contour
* nVIsinh has a counter-clockwise outer contour
* nVIsinh has a counter-clockwise outer contour
* nVIsinh has a counter-clockwise outer contour
* nThIsinh has a counter-clockwise outer contour
* nThIsinh has a counter-clockwise outer contour
* nThIsinh has a counter-clockwise outer contour
* gDhIsinh has a counter-clockwise outer contour
* gDhIsinh has a counter-clockwise outer contour
* dVIsinh has a counter-clockwise outer contour
* dVIsinh has a counter-clockwise outer contour
* dVIsinh has a counter-clockwise outer contour
* dDhIsinh has a counter-clockwise outer contour
* dDhIsinh has a counter-clockwise outer contour
* ttTthIsinh has a counter-clockwise outer contour
* ttTthIsinh has a counter-clockwise outer contour
* ttTthIsinh has a counter-clockwise outer contour
* nyCIsinh has a counter-clockwise outer contour
* nyCIsinh has a counter-clockwise outer contour
* nyCIsinh has a counter-clockwise outer contour
* nyCIsinh has a counter-clockwise outer contour
* nyChIsinh has a counter-clockwise outer contour
* nyChIsinh has a counter-clockwise outer contour
* nyChIsinh has a counter-clockwise outer contour
* cCIsinh has a counter-clockwise outer contour
* cCIsinh has a counter-clockwise outer contour
* bBIsinh has a counter-clockwise outer contour
* kIisinh has a counter-clockwise outer contour
* kIisinh has a counter-clockwise outer contour
* khIisinh has a counter-clockwise outer contour
* khIisinh has a counter-clockwise outer contour
* gIisinh has a counter-clockwise outer contour
* ghIisinh has a counter-clockwise outer contour
* ghIisinh has a counter-clockwise outer contour
* ghIisinh has a counter-clockwise outer contour
* ngIisinh has a counter-clockwise outer contour
* ngIisinh has a counter-clockwise outer contour
* nngIisinh has a counter-clockwise outer contour
* nngIisinh has a counter-clockwise outer contour
* nngIisinh has a counter-clockwise outer contour
* cIisinh has a counter-clockwise outer contour
* cIisinh has a counter-clockwise outer contour
* cIisinh has a counter-clockwise outer contour
* chIisinh has a counter-clockwise outer contour
* chIisinh has a counter-clockwise outer contour
* jIisinh has a counter-clockwise outer contour
* jIisinh has a counter-clockwise outer contour
* jhIisinh has a counter-clockwise outer contour
* jhIisinh has a counter-clockwise outer contour
* nyIisinh has a counter-clockwise outer contour
* nyIisinh has a counter-clockwise outer contour
* nyIisinh has a counter-clockwise outer contour
* nyIisinh has a counter-clockwise outer contour
* jnyIisinh has a counter-clockwise outer contour
* jnyIisinh has a counter-clockwise outer contour
* jnyIisinh has a counter-clockwise outer contour
* jnyIisinh has a counter-clockwise outer contour
* nyjIisinh has a counter-clockwise outer contour
* nyjIisinh has a counter-clockwise outer contour
* nyjIisinh has a counter-clockwise outer contour
* ttIisinh has a counter-clockwise outer contour
* ttIisinh has a counter-clockwise outer contour
* tthIisinh has a counter-clockwise outer contour
* tthIisinh has a counter-clockwise outer contour
* ddIisinh has a counter-clockwise outer contour
* ddIisinh has a counter-clockwise outer contour
* ddhIisinh has a counter-clockwise outer contour
* ddhIisinh has a counter-clockwise outer contour
* nnIisinh has a counter-clockwise outer contour
* nnIisinh has a counter-clockwise outer contour
* nnIisinh has a counter-clockwise outer contour
* nnddIisinh has a counter-clockwise outer contour
* nnddIisinh has a counter-clockwise outer contour
* nnddIisinh has a counter-clockwise outer contour
* tIisinh has a counter-clockwise outer contour
* tIisinh has a counter-clockwise outer contour
* thIisinh has a counter-clockwise outer contour
* thIisinh has a counter-clockwise outer contour
* dIisinh has a counter-clockwise outer contour
* dIisinh has a counter-clockwise outer contour
* dhIisinh has a counter-clockwise outer contour
* nIisinh has a counter-clockwise outer contour
* nIisinh has a counter-clockwise outer contour
* ndIisinh has a counter-clockwise outer contour
* ndIisinh has a counter-clockwise outer contour
* ndIisinh has a counter-clockwise outer contour
* pIisinh has a counter-clockwise outer contour
* pIisinh has a counter-clockwise outer contour
* phIisinh has a counter-clockwise outer contour
* phIisinh has a counter-clockwise outer contour
* bIisinh has a counter-clockwise outer contour
* bIisinh has a counter-clockwise outer contour
* bhIisinh has a counter-clockwise outer contour
* bhIisinh has a counter-clockwise outer contour
* bhIisinh has a counter-clockwise outer contour
* mIisinh has a counter-clockwise outer contour
* mIisinh has a counter-clockwise outer contour
* mbIisinh has a counter-clockwise outer contour
* mbIisinh has a counter-clockwise outer contour
* yIisinh has a counter-clockwise outer contour
* yIisinh has a counter-clockwise outer contour
* rIisinh has a counter-clockwise outer contour
* rIisinh has a counter-clockwise outer contour
* lIisinh has a counter-clockwise outer contour
* lIisinh has a counter-clockwise outer contour
* vIisinh has a counter-clockwise outer contour
* vIisinh has a counter-clockwise outer contour
* shIisinh has a counter-clockwise outer contour
* shIisinh has a counter-clockwise outer contour
* ssIisinh has a counter-clockwise outer contour
* ssIisinh has a counter-clockwise outer contour
* sIisinh has a counter-clockwise outer contour
* sIisinh has a counter-clockwise outer contour
* sIisinh has a counter-clockwise outer contour
* hIisinh has a counter-clockwise outer contour
* hIisinh has a counter-clockwise outer contour
* llIisinh has a counter-clockwise outer contour
* llIisinh has a counter-clockwise outer contour
* fIisinh has a counter-clockwise outer contour
* fIisinh has a counter-clockwise outer contour
* kSsIisinh has a counter-clockwise outer contour
* kSsIisinh has a counter-clockwise outer contour
* kSsIisinh has a counter-clockwise outer contour
* kVIisinh has a counter-clockwise outer contour
* kVIisinh has a counter-clockwise outer contour
* kVIisinh has a counter-clockwise outer contour
* tVIisinh has a counter-clockwise outer contour
* tVIisinh has a counter-clockwise outer contour
* tVIisinh has a counter-clockwise outer contour
* tThIisinh has a counter-clockwise outer contour
* tThIisinh has a counter-clockwise outer contour
* tThIisinh has a counter-clockwise outer contour
* nDIisinh has a counter-clockwise outer contour
* nDIisinh has a counter-clockwise outer contour
* nDIisinh has a counter-clockwise outer contour
* nDhIisinh has a counter-clockwise outer contour
* nDhIisinh has a counter-clockwise outer contour
* nVIisinh has a counter-clockwise outer contour
* nVIisinh has a counter-clockwise outer contour
* nVIisinh has a counter-clockwise outer contour
* nThIisinh has a counter-clockwise outer contour
* nThIisinh has a counter-clockwise outer contour
* nThIisinh has a counter-clockwise outer contour
* gDhIisinh has a counter-clockwise outer contour
* gDhIisinh has a counter-clockwise outer contour
* dVIisinh has a counter-clockwise outer contour
* dVIisinh has a counter-clockwise outer contour
* dVIisinh has a counter-clockwise outer contour
* dDhIisinh has a counter-clockwise outer contour
* dDhIisinh has a counter-clockwise outer contour
* ttTthIisinh has a counter-clockwise outer contour
* ttTthIisinh has a counter-clockwise outer contour
* ttTthIisinh has a counter-clockwise outer contour
* nyCIisinh has a counter-clockwise outer contour
* nyCIisinh has a counter-clockwise outer contour
* nyCIisinh has a counter-clockwise outer contour
* nyCIisinh has a counter-clockwise outer contour
* nyChIisinh has a counter-clockwise outer contour
* nyChIisinh has a counter-clockwise outer contour
* nyChIisinh has a counter-clockwise outer contour
* cCIisinh has a counter-clockwise outer contour
* cCIisinh has a counter-clockwise outer contour
* bBIisinh has a counter-clockwise outer contour
* kUsinh has a counter-clockwise outer contour
* kUsinh has a counter-clockwise outer contour
* khUsinh has a counter-clockwise outer contour
* khUsinh has a counter-clockwise outer contour
* gUsinh has a counter-clockwise outer contour
* gUsinh has a counter-clockwise outer contour
* ghUsinh has a counter-clockwise outer contour
* ghUsinh has a counter-clockwise outer contour
* ghUsinh has a counter-clockwise outer contour
* nngUsinh has a counter-clockwise outer contour
* nngUsinh has a counter-clockwise outer contour
* nngUsinh has a counter-clockwise outer contour
* cUsinh has a counter-clockwise outer contour
* cUsinh has a counter-clockwise outer contour
* cUsinh has a counter-clockwise outer contour
* chUsinh has a counter-clockwise outer contour
* chUsinh has a counter-clockwise outer contour
* jUsinh has a counter-clockwise outer contour
* jUsinh has a counter-clockwise outer contour
* jhUsinh has a counter-clockwise outer contour
* jhUsinh has a counter-clockwise outer contour
* jhUsinh has a counter-clockwise outer contour
* nyUsinh has a counter-clockwise outer contour
* nyUsinh has a counter-clockwise outer contour
* nyUsinh has a counter-clockwise outer contour
* nyUsinh has a counter-clockwise outer contour
* jnyUsinh has a counter-clockwise outer contour
* jnyUsinh has a counter-clockwise outer contour
* jnyUsinh has a counter-clockwise outer contour
* jnyUsinh has a counter-clockwise outer contour
* nyjUsinh has a counter-clockwise outer contour
* nyjUsinh has a counter-clockwise outer contour
* nyjUsinh has a counter-clockwise outer contour
* ttUsinh has a counter-clockwise outer contour
* ttUsinh has a counter-clockwise outer contour
* tthUsinh has a counter-clockwise outer contour
* tthUsinh has a counter-clockwise outer contour
* ddUsinh has a counter-clockwise outer contour
* ddUsinh has a counter-clockwise outer contour
* ddhUsinh has a counter-clockwise outer contour
* ddhUsinh has a counter-clockwise outer contour
* nnUsinh has a counter-clockwise outer contour
* nnUsinh has a counter-clockwise outer contour
* nnUsinh has a counter-clockwise outer contour
* nnddUsinh has a counter-clockwise outer contour
* nnddUsinh has a counter-clockwise outer contour
* nnddUsinh has a counter-clockwise outer contour
* tUsinh has a counter-clockwise outer contour
* tUsinh has a counter-clockwise outer contour
* thUsinh has a counter-clockwise outer contour
* thUsinh has a counter-clockwise outer contour
* dUsinh has a counter-clockwise outer contour
* dUsinh has a counter-clockwise outer contour
* dhUsinh has a counter-clockwise outer contour
* dhUsinh has a counter-clockwise outer contour
* nUsinh has a counter-clockwise outer contour
* nUsinh has a counter-clockwise outer contour
* ndUsinh has a counter-clockwise outer contour
* ndUsinh has a counter-clockwise outer contour
* ndUsinh has a counter-clockwise outer contour
* pUsinh has a counter-clockwise outer contour
* pUsinh has a counter-clockwise outer contour
* phUsinh has a counter-clockwise outer contour
* phUsinh has a counter-clockwise outer contour
* bUsinh has a counter-clockwise outer contour
* bUsinh has a counter-clockwise outer contour
* bhUsinh has a counter-clockwise outer contour
* bhUsinh has a counter-clockwise outer contour
* bhUsinh has a counter-clockwise outer contour
* mUsinh has a counter-clockwise outer contour
* mUsinh has a counter-clockwise outer contour
* mbUsinh has a counter-clockwise outer contour
* mbUsinh has a counter-clockwise outer contour
* yUsinh has a counter-clockwise outer contour
* yUsinh has a counter-clockwise outer contour
* rUsinh has a counter-clockwise outer contour
* rUsinh has a counter-clockwise outer contour
* lUsinh has a counter-clockwise outer contour
* lUsinh has a counter-clockwise outer contour
* vUsinh has a counter-clockwise outer contour
* vUsinh has a counter-clockwise outer contour
* shUsinh has a counter-clockwise outer contour
* shUsinh has a counter-clockwise outer contour
* ssUsinh has a counter-clockwise outer contour
* ssUsinh has a counter-clockwise outer contour
* sUsinh has a counter-clockwise outer contour
* sUsinh has a counter-clockwise outer contour
* sUsinh has a counter-clockwise outer contour
* hUsinh has a counter-clockwise outer contour
* hUsinh has a counter-clockwise outer contour
* llUsinh has a counter-clockwise outer contour
* llUsinh has a counter-clockwise outer contour
* fUsinh has a counter-clockwise outer contour
* fUsinh has a counter-clockwise outer contour
* kSsUsinh has a counter-clockwise outer contour
* kSsUsinh has a counter-clockwise outer contour
* kSsUsinh has a counter-clockwise outer contour
* kVUsinh has a counter-clockwise outer contour
* kVUsinh has a counter-clockwise outer contour
* kVUsinh has a counter-clockwise outer contour
* tVUsinh has a counter-clockwise outer contour
* tVUsinh has a counter-clockwise outer contour
* tVUsinh has a counter-clockwise outer contour
* tThUsinh has a counter-clockwise outer contour
* tThUsinh has a counter-clockwise outer contour
* tThUsinh has a counter-clockwise outer contour
* nDUsinh has a counter-clockwise outer contour
* nDUsinh has a counter-clockwise outer contour
* nDUsinh has a counter-clockwise outer contour
* nDhUsinh has a counter-clockwise outer contour
* nDhUsinh has a counter-clockwise outer contour
* nDhUsinh has a counter-clockwise outer contour
* nVUsinh has a counter-clockwise outer contour
* nVUsinh has a counter-clockwise outer contour
* nVUsinh has a counter-clockwise outer contour
* nThUsinh has a counter-clockwise outer contour
* nThUsinh has a counter-clockwise outer contour
* nThUsinh has a counter-clockwise outer contour
* gDhUsinh has a counter-clockwise outer contour
* gDhUsinh has a counter-clockwise outer contour
* gDhUsinh has a counter-clockwise outer contour
* dVUsinh has a counter-clockwise outer contour
* dVUsinh has a counter-clockwise outer contour
* dVUsinh has a counter-clockwise outer contour
* dDhUsinh has a counter-clockwise outer contour
* dDhUsinh has a counter-clockwise outer contour
* dDhUsinh has a counter-clockwise outer contour
* ttTthUsinh has a counter-clockwise outer contour
* ttTthUsinh has a counter-clockwise outer contour
* ttTthUsinh has a counter-clockwise outer contour
* nyCUsinh has a counter-clockwise outer contour
* nyCUsinh has a counter-clockwise outer contour
* nyCUsinh has a counter-clockwise outer contour
* nyCUsinh has a counter-clockwise outer contour
* nyChUsinh has a counter-clockwise outer contour
* nyChUsinh has a counter-clockwise outer contour
* nyChUsinh has a counter-clockwise outer contour
* cCUsinh has a counter-clockwise outer contour
* cCUsinh has a counter-clockwise outer contour
* bBUsinh has a counter-clockwise outer contour
* bBUsinh has a counter-clockwise outer contour
* kUusinh has a counter-clockwise outer contour
* kUusinh has a counter-clockwise outer contour
* khUusinh has a counter-clockwise outer contour
* khUusinh has a counter-clockwise outer contour
* gUusinh has a counter-clockwise outer contour
* gUusinh has a counter-clockwise outer contour
* ghUusinh has a counter-clockwise outer contour
* ghUusinh has a counter-clockwise outer contour
* ghUusinh has a counter-clockwise outer contour
* nngUusinh has a counter-clockwise outer contour
* nngUusinh has a counter-clockwise outer contour
* nngUusinh has a counter-clockwise outer contour
* cUusinh has a counter-clockwise outer contour
* cUusinh has a counter-clockwise outer contour
* cUusinh has a counter-clockwise outer contour
* chUusinh has a counter-clockwise outer contour
* chUusinh has a counter-clockwise outer contour
* jUusinh has a counter-clockwise outer contour
* jUusinh has a counter-clockwise outer contour
* jhUusinh has a counter-clockwise outer contour
* jhUusinh has a counter-clockwise outer contour
* jhUusinh has a counter-clockwise outer contour
* nyUusinh has a counter-clockwise outer contour
* nyUusinh has a counter-clockwise outer contour
* nyUusinh has a counter-clockwise outer contour
* nyUusinh has a counter-clockwise outer contour
* jnyUusinh has a counter-clockwise outer contour
* jnyUusinh has a counter-clockwise outer contour
* jnyUusinh has a counter-clockwise outer contour
* jnyUusinh has a counter-clockwise outer contour
* nyjUusinh has a counter-clockwise outer contour
* nyjUusinh has a counter-clockwise outer contour
* nyjUusinh has a counter-clockwise outer contour
* ttUusinh has a counter-clockwise outer contour
* ttUusinh has a counter-clockwise outer contour
* tthUusinh has a counter-clockwise outer contour
* tthUusinh has a counter-clockwise outer contour
* ddUusinh has a counter-clockwise outer contour
* ddUusinh has a counter-clockwise outer contour
* ddhUusinh has a counter-clockwise outer contour
* ddhUusinh has a counter-clockwise outer contour
* nnUusinh has a counter-clockwise outer contour
* nnUusinh has a counter-clockwise outer contour
* nnUusinh has a counter-clockwise outer contour
* nnddUusinh has a counter-clockwise outer contour
* nnddUusinh has a counter-clockwise outer contour
* nnddUusinh has a counter-clockwise outer contour
* tUusinh has a counter-clockwise outer contour
* tUusinh has a counter-clockwise outer contour
* thUusinh has a counter-clockwise outer contour
* thUusinh has a counter-clockwise outer contour
* dUusinh has a counter-clockwise outer contour
* dUusinh has a counter-clockwise outer contour
* dhUusinh has a counter-clockwise outer contour
* dhUusinh has a counter-clockwise outer contour
* nUusinh has a counter-clockwise outer contour
* nUusinh has a counter-clockwise outer contour
* ndUusinh has a counter-clockwise outer contour
* ndUusinh has a counter-clockwise outer contour
* ndUusinh has a counter-clockwise outer contour
* pUusinh has a counter-clockwise outer contour
* pUusinh has a counter-clockwise outer contour
* phUusinh has a counter-clockwise outer contour
* phUusinh has a counter-clockwise outer contour
* bUusinh has a counter-clockwise outer contour
* bUusinh has a counter-clockwise outer contour
* bhUusinh has a counter-clockwise outer contour
* bhUusinh has a counter-clockwise outer contour
* bhUusinh has a counter-clockwise outer contour
* mUusinh has a counter-clockwise outer contour
* mUusinh has a counter-clockwise outer contour
* mbUusinh has a counter-clockwise outer contour
* mbUusinh has a counter-clockwise outer contour
* yUusinh has a counter-clockwise outer contour
* yUusinh has a counter-clockwise outer contour
* rUusinh has a counter-clockwise outer contour
* rUusinh has a counter-clockwise outer contour
* lUusinh has a counter-clockwise outer contour
* lUusinh has a counter-clockwise outer contour
* vUusinh has a counter-clockwise outer contour
* vUusinh has a counter-clockwise outer contour
* shUusinh has a counter-clockwise outer contour
* shUusinh has a counter-clockwise outer contour
* ssUusinh has a counter-clockwise outer contour
* ssUusinh has a counter-clockwise outer contour
* sUusinh has a counter-clockwise outer contour
* sUusinh has a counter-clockwise outer contour
* sUusinh has a counter-clockwise outer contour
* hUusinh has a counter-clockwise outer contour
* hUusinh has a counter-clockwise outer contour
* llUusinh has a counter-clockwise outer contour
* llUusinh has a counter-clockwise outer contour
* llUusinh has a counter-clockwise outer contour
* fUusinh has a counter-clockwise outer contour
* fUusinh has a counter-clockwise outer contour
* kSsUusinh has a counter-clockwise outer contour
* kSsUusinh has a counter-clockwise outer contour
* kSsUusinh has a counter-clockwise outer contour
* kVUusinh has a counter-clockwise outer contour
* kVUusinh has a counter-clockwise outer contour
* kVUusinh has a counter-clockwise outer contour
* tVUusinh has a counter-clockwise outer contour
* tVUusinh has a counter-clockwise outer contour
* tVUusinh has a counter-clockwise outer contour
* tThUusinh has a counter-clockwise outer contour
* tThUusinh has a counter-clockwise outer contour
* tThUusinh has a counter-clockwise outer contour
* nDUusinh has a counter-clockwise outer contour
* nDUusinh has a counter-clockwise outer contour
* nDUusinh has a counter-clockwise outer contour
* nDhUusinh has a counter-clockwise outer contour
* nDhUusinh has a counter-clockwise outer contour
* nDhUusinh has a counter-clockwise outer contour
* nVUusinh has a counter-clockwise outer contour
* nVUusinh has a counter-clockwise outer contour
* nVUusinh has a counter-clockwise outer contour
* nThUusinh has a counter-clockwise outer contour
* nThUusinh has a counter-clockwise outer contour
* nThUusinh has a counter-clockwise outer contour
* gDhUusinh has a counter-clockwise outer contour
* gDhUusinh has a counter-clockwise outer contour
* gDhUusinh has a counter-clockwise outer contour
* dVUusinh has a counter-clockwise outer contour
* dVUusinh has a counter-clockwise outer contour
* dVUusinh has a counter-clockwise outer contour
* dDhUusinh has a counter-clockwise outer contour
* dDhUusinh has a counter-clockwise outer contour
* dDhUusinh has a counter-clockwise outer contour
* ttTthUusinh has a counter-clockwise outer contour
* ttTthUusinh has a counter-clockwise outer contour
* ttTthUusinh has a counter-clockwise outer contour
* nyCUusinh has a counter-clockwise outer contour
* nyCUusinh has a counter-clockwise outer contour
* nyCUusinh has a counter-clockwise outer contour
* nyCUusinh has a counter-clockwise outer contour
* nyChUusinh has a counter-clockwise outer contour
* nyChUusinh has a counter-clockwise outer contour
* nyChUusinh has a counter-clockwise outer contour
* cCUusinh has a counter-clockwise outer contour
* cCUusinh has a counter-clockwise outer contour
* bBUusinh has a counter-clockwise outer contour
* bBUusinh has a counter-clockwise outer contour
* rAesinh has a counter-clockwise outer contour
* rAesinh has a counter-clockwise outer contour
* rAaesinh has a counter-clockwise outer contour
* rAaesinh has a counter-clockwise outer contour
* kRasinh has a counter-clockwise outer contour
* kRasinh has a counter-clockwise outer contour
* khRasinh has a counter-clockwise outer contour
* khRasinh has a counter-clockwise outer contour
* gRasinh has a counter-clockwise outer contour
* gRasinh has a counter-clockwise outer contour
* ghRasinh has a counter-clockwise outer contour
* ghRasinh has a counter-clockwise outer contour
* ghRasinh has a counter-clockwise outer contour
* cRasinh has a counter-clockwise outer contour
* cRasinh has a counter-clockwise outer contour
* cRasinh has a counter-clockwise outer contour
* jRasinh has a counter-clockwise outer contour
* jRasinh has a counter-clockwise outer contour
* jhRasinh has a counter-clockwise outer contour
* jhRasinh has a counter-clockwise outer contour
* jhRasinh has a counter-clockwise outer contour
* nyRasinh has a counter-clockwise outer contour
* nyRasinh has a counter-clockwise outer contour
* nyRasinh has a counter-clockwise outer contour
* nyRasinh has a counter-clockwise outer contour
* jnyRasinh has a counter-clockwise outer contour
* jnyRasinh has a counter-clockwise outer contour
* jnyRasinh has a counter-clockwise outer contour
* jnyRasinh has a counter-clockwise outer contour
* nyjRasinh has a counter-clockwise outer contour
* nyjRasinh has a counter-clockwise outer contour
* nyjRasinh has a counter-clockwise outer contour
* ttRasinh has a counter-clockwise outer contour
* ttRasinh has a counter-clockwise outer contour
* ddRasinh has a counter-clockwise outer contour
* ddRasinh has a counter-clockwise outer contour
* tRasinh has a counter-clockwise outer contour
* tRasinh has a counter-clockwise outer contour
* dRasinh has a counter-clockwise outer contour
* dRasinh has a counter-clockwise outer contour
* dhRasinh has a counter-clockwise outer contour
* dhRasinh has a counter-clockwise outer contour
* ndRasinh has a counter-clockwise outer contour
* ndRasinh has a counter-clockwise outer contour
* ndRasinh has a counter-clockwise outer contour
* pRasinh has a counter-clockwise outer contour
* pRasinh has a counter-clockwise outer contour
* bRasinh has a counter-clockwise outer contour
* bRasinh has a counter-clockwise outer contour
* bhRasinh has a counter-clockwise outer contour
* bhRasinh has a counter-clockwise outer contour
* bhRasinh has a counter-clockwise outer contour
* mRasinh has a counter-clockwise outer contour
* mRasinh has a counter-clockwise outer contour
* vRasinh has a counter-clockwise outer contour
* vRasinh has a counter-clockwise outer contour
* shRasinh has a counter-clockwise outer contour
* shRasinh has a counter-clockwise outer contour
* ssRasinh has a counter-clockwise outer contour
* ssRasinh has a counter-clockwise outer contour
* sRasinh has a counter-clockwise outer contour
* sRasinh has a counter-clockwise outer contour
* sRasinh has a counter-clockwise outer contour
* hRasinh has a counter-clockwise outer contour
* hRasinh has a counter-clockwise outer contour
* fRasinh has a counter-clockwise outer contour
* fRasinh has a counter-clockwise outer contour
* nDRasinh has a counter-clockwise outer contour
* nDRasinh has a counter-clockwise outer contour
* nDRasinh has a counter-clockwise outer contour
* kRsinh has a counter-clockwise outer contour
* kRsinh has a counter-clockwise outer contour
* kRsinh has a counter-clockwise outer contour
* khRsinh has a counter-clockwise outer contour
* khRsinh has a counter-clockwise outer contour
* khRsinh has a counter-clockwise outer contour
* gRsinh has a counter-clockwise outer contour
* gRsinh has a counter-clockwise outer contour
* gRsinh has a counter-clockwise outer contour
* ghRsinh has a counter-clockwise outer contour
* ghRsinh has a counter-clockwise outer contour
* ghRsinh has a counter-clockwise outer contour
* ghRsinh has a counter-clockwise outer contour
* cRsinh has a counter-clockwise outer contour
* cRsinh has a counter-clockwise outer contour
* cRsinh has a counter-clockwise outer contour
* cRsinh has a counter-clockwise outer contour
* jRsinh has a counter-clockwise outer contour
* jRsinh has a counter-clockwise outer contour
* jRsinh has a counter-clockwise outer contour
* jhRsinh has a counter-clockwise outer contour
* jhRsinh has a counter-clockwise outer contour
* jhRsinh has a counter-clockwise outer contour
* nyRsinh has a counter-clockwise outer contour
* nyRsinh has a counter-clockwise outer contour
* nyRsinh has a counter-clockwise outer contour
* nyRsinh has a counter-clockwise outer contour
* nyRsinh has a counter-clockwise outer contour
* jnyRsinh has a counter-clockwise outer contour
* jnyRsinh has a counter-clockwise outer contour
* jnyRsinh has a counter-clockwise outer contour
* jnyRsinh has a counter-clockwise outer contour
* jnyRsinh has a counter-clockwise outer contour
* nyjRsinh has a counter-clockwise outer contour
* nyjRsinh has a counter-clockwise outer contour
* nyjRsinh has a counter-clockwise outer contour
* nyjRsinh has a counter-clockwise outer contour
* ttRsinh has a counter-clockwise outer contour
* ttRsinh has a counter-clockwise outer contour
* ttRsinh has a counter-clockwise outer contour
* ddRsinh has a counter-clockwise outer contour
* ddRsinh has a counter-clockwise outer contour
* ddRsinh has a counter-clockwise outer contour
* tRsinh has a counter-clockwise outer contour
* tRsinh has a counter-clockwise outer contour
* tRsinh has a counter-clockwise outer contour
* dRsinh has a counter-clockwise outer contour
* dRsinh has a counter-clockwise outer contour
* dRsinh has a counter-clockwise outer contour
* dhRsinh has a counter-clockwise outer contour
* dhRsinh has a counter-clockwise outer contour
* pRsinh has a counter-clockwise outer contour
* pRsinh has a counter-clockwise outer contour
* pRsinh has a counter-clockwise outer contour
* bRsinh has a counter-clockwise outer contour
* bRsinh has a counter-clockwise outer contour
* bhRsinh has a counter-clockwise outer contour
* bhRsinh has a counter-clockwise outer contour
* bhRsinh has a counter-clockwise outer contour
* bhRsinh has a counter-clockwise outer contour
* mRsinh has a counter-clockwise outer contour
* mRsinh has a counter-clockwise outer contour
* mRsinh has a counter-clockwise outer contour
* vRsinh has a counter-clockwise outer contour
* vRsinh has a counter-clockwise outer contour
* shRsinh has a counter-clockwise outer contour
* shRsinh has a counter-clockwise outer contour
* shRsinh has a counter-clockwise outer contour
* ssRsinh has a counter-clockwise outer contour
* ssRsinh has a counter-clockwise outer contour
* ssRsinh has a counter-clockwise outer contour
* sRsinh has a counter-clockwise outer contour
* sRsinh has a counter-clockwise outer contour
* sRsinh has a counter-clockwise outer contour
* sRsinh has a counter-clockwise outer contour
* hRsinh has a counter-clockwise outer contour
* hRsinh has a counter-clockwise outer contour
* hRsinh has a counter-clockwise outer contour
* fRsinh has a counter-clockwise outer contour
* fRsinh has a counter-clockwise outer contour
* fRsinh has a counter-clockwise outer contour
* kRIsinh has a counter-clockwise outer contour
* kRIsinh has a counter-clockwise outer contour
* kRIsinh has a counter-clockwise outer contour
* khRIsinh has a counter-clockwise outer contour
* khRIsinh has a counter-clockwise outer contour
* khRIsinh has a counter-clockwise outer contour
* gRIsinh has a counter-clockwise outer contour
* gRIsinh has a counter-clockwise outer contour
* gRIsinh has a counter-clockwise outer contour
* ghRIsinh has a counter-clockwise outer contour
* ghRIsinh has a counter-clockwise outer contour
* ghRIsinh has a counter-clockwise outer contour
* ghRIsinh has a counter-clockwise outer contour
* cRIsinh has a counter-clockwise outer contour
* cRIsinh has a counter-clockwise outer contour
* cRIsinh has a counter-clockwise outer contour
* cRIsinh has a counter-clockwise outer contour
* jRIsinh has a counter-clockwise outer contour
* jRIsinh has a counter-clockwise outer contour
* jRIsinh has a counter-clockwise outer contour
* jhRIsinh has a counter-clockwise outer contour
* jhRIsinh has a counter-clockwise outer contour
* jhRIsinh has a counter-clockwise outer contour
* nyRIsinh has a counter-clockwise outer contour
* nyRIsinh has a counter-clockwise outer contour
* nyRIsinh has a counter-clockwise outer contour
* nyRIsinh has a counter-clockwise outer contour
* nyRIsinh has a counter-clockwise outer contour
* jnyRIsinh has a counter-clockwise outer contour
* jnyRIsinh has a counter-clockwise outer contour
* jnyRIsinh has a counter-clockwise outer contour
* jnyRIsinh has a counter-clockwise outer contour
* jnyRIsinh has a counter-clockwise outer contour
* ttRIsinh has a counter-clockwise outer contour
* ttRIsinh has a counter-clockwise outer contour
* ttRIsinh has a counter-clockwise outer contour
* ddRIsinh has a counter-clockwise outer contour
* ddRIsinh has a counter-clockwise outer contour
* ddRIsinh has a counter-clockwise outer contour
* tRIsinh has a counter-clockwise outer contour
* tRIsinh has a counter-clockwise outer contour
* tRIsinh has a counter-clockwise outer contour
* dRIsinh has a counter-clockwise outer contour
* dRIsinh has a counter-clockwise outer contour
* dRIsinh has a counter-clockwise outer contour
* dhRIsinh has a counter-clockwise outer contour
* dhRIsinh has a counter-clockwise outer contour
* pRIsinh has a counter-clockwise outer contour
* pRIsinh has a counter-clockwise outer contour
* pRIsinh has a counter-clockwise outer contour
* bRIsinh has a counter-clockwise outer contour
* bRIsinh has a counter-clockwise outer contour
* bRIsinh has a counter-clockwise outer contour
* bhRIsinh has a counter-clockwise outer contour
* bhRIsinh has a counter-clockwise outer contour
* bhRIsinh has a counter-clockwise outer contour
* bhRIsinh has a counter-clockwise outer contour
* mRIsinh has a counter-clockwise outer contour
* mRIsinh has a counter-clockwise outer contour
* mRIsinh has a counter-clockwise outer contour
* vRIsinh has a counter-clockwise outer contour
* vRIsinh has a counter-clockwise outer contour
* vRIsinh has a counter-clockwise outer contour
* shRIsinh has a counter-clockwise outer contour
* shRIsinh has a counter-clockwise outer contour
* shRIsinh has a counter-clockwise outer contour
* ssRIsinh has a counter-clockwise outer contour
* ssRIsinh has a counter-clockwise outer contour
* ssRIsinh has a counter-clockwise outer contour
* sRIsinh has a counter-clockwise outer contour
* sRIsinh has a counter-clockwise outer contour
* sRIsinh has a counter-clockwise outer contour
* sRIsinh has a counter-clockwise outer contour
* hRIsinh has a counter-clockwise outer contour
* hRIsinh has a counter-clockwise outer contour
* hRIsinh has a counter-clockwise outer contour
* fRIsinh has a counter-clockwise outer contour
* fRIsinh has a counter-clockwise outer contour
* fRIsinh has a counter-clockwise outer contour
* nDRIsinh has a counter-clockwise outer contour
* nDRIsinh has a counter-clockwise outer contour
* nDRIsinh has a counter-clockwise outer contour
* nDRIsinh has a counter-clockwise outer contour
* kRIisinh has a counter-clockwise outer contour
* kRIisinh has a counter-clockwise outer contour
* kRIisinh has a counter-clockwise outer contour
* khRIisinh has a counter-clockwise outer contour
* khRIisinh has a counter-clockwise outer contour
* khRIisinh has a counter-clockwise outer contour
* gRIisinh has a counter-clockwise outer contour
* gRIisinh has a counter-clockwise outer contour
* ghRIisinh has a counter-clockwise outer contour
* ghRIisinh has a counter-clockwise outer contour
* ghRIisinh has a counter-clockwise outer contour
* ghRIisinh has a counter-clockwise outer contour
* cRIisinh has a counter-clockwise outer contour
* cRIisinh has a counter-clockwise outer contour
* cRIisinh has a counter-clockwise outer contour
* cRIisinh has a counter-clockwise outer contour
* jRIisinh has a counter-clockwise outer contour
* jRIisinh has a counter-clockwise outer contour
* jRIisinh has a counter-clockwise outer contour
* jhRIisinh has a counter-clockwise outer contour
* jhRIisinh has a counter-clockwise outer contour
* jhRIisinh has a counter-clockwise outer contour
* nyRIisinh has a counter-clockwise outer contour
* nyRIisinh has a counter-clockwise outer contour
* nyRIisinh has a counter-clockwise outer contour
* nyRIisinh has a counter-clockwise outer contour
* nyRIisinh has a counter-clockwise outer contour
* jnyRIisinh has a counter-clockwise outer contour
* jnyRIisinh has a counter-clockwise outer contour
* jnyRIisinh has a counter-clockwise outer contour
* jnyRIisinh has a counter-clockwise outer contour
* jnyRIisinh has a counter-clockwise outer contour
* ttRIisinh has a counter-clockwise outer contour
* ttRIisinh has a counter-clockwise outer contour
* ttRIisinh has a counter-clockwise outer contour
* ddRIisinh has a counter-clockwise outer contour
* ddRIisinh has a counter-clockwise outer contour
* ddRIisinh has a counter-clockwise outer contour
* tRIisinh has a counter-clockwise outer contour
* tRIisinh has a counter-clockwise outer contour
* tRIisinh has a counter-clockwise outer contour
* dRIisinh has a counter-clockwise outer contour
* dRIisinh has a counter-clockwise outer contour
* dRIisinh has a counter-clockwise outer contour
* dhRIisinh has a counter-clockwise outer contour
* dhRIisinh has a counter-clockwise outer contour
* pRIisinh has a counter-clockwise outer contour
* pRIisinh has a counter-clockwise outer contour
* pRIisinh has a counter-clockwise outer contour
* bRIisinh has a counter-clockwise outer contour
* bRIisinh has a counter-clockwise outer contour
* bRIisinh has a counter-clockwise outer contour
* bhRIisinh has a counter-clockwise outer contour
* bhRIisinh has a counter-clockwise outer contour
* bhRIisinh has a counter-clockwise outer contour
* bhRIisinh has a counter-clockwise outer contour
* mRIisinh has a counter-clockwise outer contour
* mRIisinh has a counter-clockwise outer contour
* mRIisinh has a counter-clockwise outer contour
* vRIisinh has a counter-clockwise outer contour
* vRIisinh has a counter-clockwise outer contour
* vRIisinh has a counter-clockwise outer contour
* shRIisinh has a counter-clockwise outer contour
* shRIisinh has a counter-clockwise outer contour
* shRIisinh has a counter-clockwise outer contour
* ssRIisinh has a counter-clockwise outer contour
* ssRIisinh has a counter-clockwise outer contour
* ssRIisinh has a counter-clockwise outer contour
* sRIisinh has a counter-clockwise outer contour
* sRIisinh has a counter-clockwise outer contour
* sRIisinh has a counter-clockwise outer contour
* sRIisinh has a counter-clockwise outer contour
* hRIisinh has a counter-clockwise outer contour
* hRIisinh has a counter-clockwise outer contour
* hRIisinh has a counter-clockwise outer contour
* fRIisinh has a counter-clockwise outer contour
* fRIisinh has a counter-clockwise outer contour
* fRIisinh has a counter-clockwise outer contour
* nDRIisinh has a counter-clockwise outer contour
* nDRIisinh has a counter-clockwise outer contour
* nDRIisinh has a counter-clockwise outer contour
* nDRIisinh has a counter-clockwise outer contour
* ka_rephasinh has a counter-clockwise outer contour
* ka_rephasinh has a counter-clockwise outer contour
* kha_rephasinh has a counter-clockwise outer contour
* kha_rephasinh has a counter-clockwise outer contour
* ga_rephasinh has a counter-clockwise outer contour
* ga_rephasinh has a counter-clockwise outer contour
* gha_rephasinh has a counter-clockwise outer contour
* gha_rephasinh has a counter-clockwise outer contour
* gha_rephasinh has a counter-clockwise outer contour
* nga_rephasinh has a counter-clockwise outer contour
* nga_rephasinh has a counter-clockwise outer contour
* nnga_rephasinh has a counter-clockwise outer contour
* nnga_rephasinh has a counter-clockwise outer contour
* nnga_rephasinh has a counter-clockwise outer contour
* ca_rephasinh has a counter-clockwise outer contour
* ca_rephasinh has a counter-clockwise outer contour
* ca_rephasinh has a counter-clockwise outer contour
* cha_rephasinh has a counter-clockwise outer contour
* cha_rephasinh has a counter-clockwise outer contour
* ja_rephasinh has a counter-clockwise outer contour
* jha_rephasinh has a counter-clockwise outer contour
* jha_rephasinh has a counter-clockwise outer contour
* jha_rephasinh has a counter-clockwise outer contour
* nya_rephasinh has a counter-clockwise outer contour
* nya_rephasinh has a counter-clockwise outer contour
* nya_rephasinh has a counter-clockwise outer contour
* nya_rephasinh has a counter-clockwise outer contour
* jnya_rephasinh has a counter-clockwise outer contour
* jnya_rephasinh has a counter-clockwise outer contour
* jnya_rephasinh has a counter-clockwise outer contour
* jnya_rephasinh has a counter-clockwise outer contour
* nyja_rephasinh has a counter-clockwise outer contour
* nyja_rephasinh has a counter-clockwise outer contour
* tta_rephasinh has a counter-clockwise outer contour
* tta_rephasinh has a counter-clockwise outer contour
* ttha_rephasinh has a counter-clockwise outer contour
* ttha_rephasinh has a counter-clockwise outer contour
* dda_rephasinh has a counter-clockwise outer contour
* dda_rephasinh has a counter-clockwise outer contour
* ddha_rephasinh has a counter-clockwise outer contour
* ddha_rephasinh has a counter-clockwise outer contour
* nna_rephasinh has a counter-clockwise outer contour
* nna_rephasinh has a counter-clockwise outer contour
* nna_rephasinh has a counter-clockwise outer contour
* nndda_rephasinh has a counter-clockwise outer contour
* nndda_rephasinh has a counter-clockwise outer contour
* nndda_rephasinh has a counter-clockwise outer contour
* ta_rephasinh has a counter-clockwise outer contour
* ta_rephasinh has a counter-clockwise outer contour
* tha_rephasinh has a counter-clockwise outer contour
* tha_rephasinh has a counter-clockwise outer contour
* da_rephasinh has a counter-clockwise outer contour
* da_rephasinh has a counter-clockwise outer contour
* dha_rephasinh has a counter-clockwise outer contour
* dha_rephasinh has a counter-clockwise outer contour
* na_rephasinh has a counter-clockwise outer contour
* na_rephasinh has a counter-clockwise outer contour
* nda_rephasinh has a counter-clockwise outer contour
* nda_rephasinh has a counter-clockwise outer contour
* nda_rephasinh has a counter-clockwise outer contour
* pa_rephasinh has a counter-clockwise outer contour
* pa_rephasinh has a counter-clockwise outer contour
* pha_rephasinh has a counter-clockwise outer contour
* pha_rephasinh has a counter-clockwise outer contour
* ba_rephasinh has a counter-clockwise outer contour
* ba_rephasinh has a counter-clockwise outer contour
* bha_rephasinh has a counter-clockwise outer contour
* bha_rephasinh has a counter-clockwise outer contour
* bha_rephasinh has a counter-clockwise outer contour
* ma_rephasinh has a counter-clockwise outer contour
* ma_rephasinh has a counter-clockwise outer contour
* mba_rephasinh has a counter-clockwise outer contour
* mba_rephasinh has a counter-clockwise outer contour
* ya_rephasinh has a counter-clockwise outer contour
* ya_rephasinh has a counter-clockwise outer contour
* ra_rephasinh has a counter-clockwise outer contour
* ra_rephasinh has a counter-clockwise outer contour
* la_rephasinh has a counter-clockwise outer contour
* la_rephasinh has a counter-clockwise outer contour
* va_rephasinh has a counter-clockwise outer contour
* va_rephasinh has a counter-clockwise outer contour
* sha_rephasinh has a counter-clockwise outer contour
* sha_rephasinh has a counter-clockwise outer contour
* ssa_rephasinh has a counter-clockwise outer contour
* ssa_rephasinh has a counter-clockwise outer contour
* sa_rephasinh has a counter-clockwise outer contour
* sa_rephasinh has a counter-clockwise outer contour
* sa_rephasinh has a counter-clockwise outer contour
* ha_rephasinh has a counter-clockwise outer contour
* ha_rephasinh has a counter-clockwise outer contour
* lla_rephasinh has a counter-clockwise outer contour
* lla_rephasinh has a counter-clockwise outer contour
* fa_rephasinh has a counter-clockwise outer contour
* fa_rephasinh has a counter-clockwise outer contour
* kSsa_rephasinh has a counter-clockwise outer contour
* kSsa_rephasinh has a counter-clockwise outer contour
* kSsa_rephasinh has a counter-clockwise outer contour
* kVa_rephasinh has a counter-clockwise outer contour
* kVa_rephasinh has a counter-clockwise outer contour
* kVa_rephasinh has a counter-clockwise outer contour
* tVa_rephasinh has a counter-clockwise outer contour
* tVa_rephasinh has a counter-clockwise outer contour
* tVa_rephasinh has a counter-clockwise outer contour
* tTha_rephasinh has a counter-clockwise outer contour
* tTha_rephasinh has a counter-clockwise outer contour
* tTha_rephasinh has a counter-clockwise outer contour
* nDa_rephasinh has a counter-clockwise outer contour
* nDa_rephasinh has a counter-clockwise outer contour
* nDa_rephasinh has a counter-clockwise outer contour
* nDha_rephasinh has a counter-clockwise outer contour
* nDha_rephasinh has a counter-clockwise outer contour
* nDha_rephasinh has a counter-clockwise outer contour
* nVa_rephasinh has a counter-clockwise outer contour
* nVa_rephasinh has a counter-clockwise outer contour
* nVa_rephasinh has a counter-clockwise outer contour
* nTha_rephasinh has a counter-clockwise outer contour
* nTha_rephasinh has a counter-clockwise outer contour
* nTha_rephasinh has a counter-clockwise outer contour
* gDha_rephasinh has a counter-clockwise outer contour
* gDha_rephasinh has a counter-clockwise outer contour
* gDha_rephasinh has a counter-clockwise outer contour
* dVa_rephasinh has a counter-clockwise outer contour
* dVa_rephasinh has a counter-clockwise outer contour
* dVa_rephasinh has a counter-clockwise outer contour
* dDha_rephasinh has a counter-clockwise outer contour
* dDha_rephasinh has a counter-clockwise outer contour
* dDha_rephasinh has a counter-clockwise outer contour
* ttTtha_rephasinh has a counter-clockwise outer contour
* ttTtha_rephasinh has a counter-clockwise outer contour
* ttTtha_rephasinh has a counter-clockwise outer contour
* nyCa_rephasinh has a counter-clockwise outer contour
* nyCa_rephasinh has a counter-clockwise outer contour
* nyCa_rephasinh has a counter-clockwise outer contour
* nyCa_rephasinh has a counter-clockwise outer contour
* nyCha_rephasinh has a counter-clockwise outer contour
* nyCha_rephasinh has a counter-clockwise outer contour
* cCa_rephasinh has a counter-clockwise outer contour
* cCa_rephasinh has a counter-clockwise outer contour
* bBa_rephasinh has a counter-clockwise outer contour
* bBa_rephasinh has a counter-clockwise outer contour
* yasign_isignsinh has a counter-clockwise outer contour
* yasign_isignsinh has a counter-clockwise outer contour
* yasign_iisignsinh has a counter-clockwise outer contour
* yasign_iisignsinh has a counter-clockwise outer contour
* yasign_rephasinh has a counter-clockwise outer contour
* yasign_rephasinh has a counter-clockwise outer contour
* yasignsinh has a counter-clockwise outer contour
* yasign_repha_aasignsinh has a counter-clockwise outer contour
* yasign_repha_aasignsinh has a counter-clockwise outer contour
* yasign_repha_aasignsinh has a counter-clockwise outer contour
* yasign_uusignsinh has a counter-clockwise outer contour
* yasign_uusignsinh has a counter-clockwise outer contour
* yasign_usignsinh has a counter-clockwise outer contour
* yasign_usignsinh has a counter-clockwise outer contour
* yasign_repha_usignsinh has a counter-clockwise outer contour
* yasign_repha_usignsinh has a counter-clockwise outer contour
* yasign_repha_usignsinh has a counter-clockwise outer contour
* yasign_repha_uusignsinh has a counter-clockwise outer contour
* yasign_repha_uusignsinh has a counter-clockwise outer contour
* yasign_repha_uusignsinh has a counter-clockwise outer contour
* yasign_viramasinh has a counter-clockwise outer contour
* yasign_viramasinh has a counter-clockwise outer contour
* dae._csinh has a counter-clockwise outer contour
* daae._csinh has a counter-clockwise outer contour
* daa._csinh has a counter-clockwise outer contour
* dvocalicr._csinh has a counter-clockwise outer contour
* dvocalicr._csinh has a counter-clockwise outer contour
* dvocalicrr._csinh has a counter-clockwise outer contour
* dvocalicrr._csinh has a counter-clockwise outer contour
* dvocalicrr._csinh has a counter-clockwise outer contour
* dya._csinh has a counter-clockwise outer contour
* dya._csinh has a counter-clockwise outer contour
* dyaa._csinh has a counter-clockwise outer contour
* dyaa._csinh has a counter-clockwise outer contour
* dyU._csinh has a counter-clockwise outer contour
* dyU._csinh has a counter-clockwise outer contour
* dyU._csinh has a counter-clockwise outer contour
* da_yansa_oosignsinh has a counter-clockwise outer contour
* da_yansa_oosignsinh has a counter-clockwise outer contour
* da_yansa_oosignsinh has a counter-clockwise outer contour
* da_yansa_oosignsinh has a counter-clockwise outer contour
* dyUu._csinh has a counter-clockwise outer contour
* dyUu._csinh has a counter-clockwise outer contour
* dyUu._csinh has a counter-clockwise outer contour
* ndae._csinh has a counter-clockwise outer contour
* ndae._csinh has a counter-clockwise outer contour
* ndaae._csinh has a counter-clockwise outer contour
* ndaae._csinh has a counter-clockwise outer contour
* jnyae._csinh has a counter-clockwise outer contour
* jnyae._csinh has a counter-clockwise outer contour
* jnyae._csinh has a counter-clockwise outer contour
* jnyaae._csinh has a counter-clockwise outer contour
* jnyaae._csinh has a counter-clockwise outer contour
* jnyaae._csinh has a counter-clockwise outer contour
* jnyaa._csinh has a counter-clockwise outer contour
* jnyaa._csinh has a counter-clockwise outer contour
* jnyaa._csinh has a counter-clockwise outer contour
* nyae._csinh has a counter-clockwise outer contour
* nyae._csinh has a counter-clockwise outer contour
* nyae._csinh has a counter-clockwise outer contour
* nyaae._csinh has a counter-clockwise outer contour
* nyaae._csinh has a counter-clockwise outer contour
* nyaae._csinh has a counter-clockwise outer contour
* nyaa._csinh has a counter-clockwise outer contour
* nyaa._csinh has a counter-clockwise outer contour
* nyaa._csinh has a counter-clockwise outer contour
* nDaa._csinh has a counter-clockwise outer contour
* nDaa._csinh has a counter-clockwise outer contour
* nDaae._csinh has a counter-clockwise outer contour
* nDaae._csinh has a counter-clockwise outer contour
* nDae._csinh has a counter-clockwise outer contour
* nDae._csinh has a counter-clockwise outer contour
* daa_virama._csinh has a counter-clockwise outer contour
* daa_virama._csinh has a counter-clockwise outer contour
* ndaa_virama._csinh has a counter-clockwise outer contour
* ndaa_virama._csinh has a counter-clockwise outer contour
* ndaa_virama._csinh has a counter-clockwise outer contour
* jnyaa_virama._csinh has a counter-clockwise outer contour
* jnyaa_virama._csinh has a counter-clockwise outer contour
* jnyaa_virama._csinh has a counter-clockwise outer contour
* jnyaa_virama._csinh has a counter-clockwise outer contour
* nyaa_virama._csinh has a counter-clockwise outer contour
* nyaa_virama._csinh has a counter-clockwise outer contour
* nyaa_virama._csinh has a counter-clockwise outer contour
* nyaa_virama._csinh has a counter-clockwise outer contour
* nDaa_virama._csinh has a counter-clockwise outer contour
* nDaa_virama._csinh has a counter-clockwise outer contour
* nDaa_virama._csinh has a counter-clockwise outer contour
* dRaa._csinh has a counter-clockwise outer contour
* dRaa._csinh has a counter-clockwise outer contour
* dRaa._csinh has a counter-clockwise outer contour
* ndRaa._csinh has a counter-clockwise outer contour
* ndRaa._csinh has a counter-clockwise outer contour
* ndRaa._csinh has a counter-clockwise outer contour
* ndRaa._csinh has a counter-clockwise outer contour
* anusvarayaShasinh has a counter-clockwise outer contour
* anusvarayaShasinh has a counter-clockwise outer contour
* anusvarayaShIsinh has a counter-clockwise outer contour
* anusvarayaShIsinh has a counter-clockwise outer contour
* anusvarayaShIsinh has a counter-clockwise outer contour
* anusvarayaShsinh has a counter-clockwise outer contour
* anusvarayaShsinh has a counter-clockwise outer contour
* anusvarayaShsinh has a counter-clockwise outer contour
* anusvarayaShIisinh has a counter-clockwise outer contour
* anusvarayaShIisinh has a counter-clockwise outer contour
* anusvarayaShIisinh has a counter-clockwise outer contour
* anusvarayaShUsinh has a counter-clockwise outer contour
* anusvarayaShUsinh has a counter-clockwise outer contour
* anusvarayaShUsinh has a counter-clockwise outer contour
* anusvarayaShUusinh has a counter-clockwise outer contour
* anusvarayaShUusinh has a counter-clockwise outer contour
* anusvarayaShUusinh has a counter-clockwise outer contour
* archaiconesinh has a counter-clockwise outer contour
* archaiconesinh has a counter-clockwise outer contour
* archaictwosinh has a counter-clockwise outer contour
* archaicthreesinh has a counter-clockwise outer contour
* archaicthreesinh has a counter-clockwise outer contour
* archaicfoursinh has a counter-clockwise outer contour
* archaicfivesinh has a counter-clockwise outer contour
* archaicfivesinh has a counter-clockwise outer contour
* archaicfivesinh has a counter-clockwise outer contour
* archaicsixsinh has a counter-clockwise outer contour
* archaicsixsinh has a counter-clockwise outer contour
* archaicsevensinh has a counter-clockwise outer contour
* archaiceightsinh has a counter-clockwise outer contour
* archaicninesinh has a counter-clockwise outer contour
* archaictensinh has a counter-clockwise outer contour
* archaictensinh has a counter-clockwise outer contour
* archaictwentysinh has a counter-clockwise outer contour
* archaictwentysinh has a counter-clockwise outer contour
* archaictwentysinh has a counter-clockwise outer contour
* archaicthirtysinh has a counter-clockwise outer contour
* archaicthirtysinh has a counter-clockwise outer contour
* archaicfortysinh has a counter-clockwise outer contour
* archaicfortysinh has a counter-clockwise outer contour
* archaicfiftysinh has a counter-clockwise outer contour
* archaicfiftysinh has a counter-clockwise outer contour
* archaicfiftysinh has a counter-clockwise outer contour
* archaicseventysinh has a counter-clockwise outer contour
* archaicseventysinh has a counter-clockwise outer contour
* archaicseventysinh has a counter-clockwise outer contour
* archaiceightysinh has a counter-clockwise outer contour
* archaiceightysinh has a counter-clockwise outer contour
* archaicninetysinh has a counter-clockwise outer contour
* archaicninetysinh has a counter-clockwise outer contour
* archaicninetysinh has a counter-clockwise outer contour
* archaiconehundredsinh has a counter-clockwise outer contour
* archaiconehundredsinh has a counter-clockwise outer contour
* archaiconethousandsinh has a counter-clockwise outer contour
* archaiconethousandsinh has a counter-clockwise outer contour
* archaiconethousandsinh has a counter-clockwise outer contour
* candrabindusinh.001 has a counter-clockwise outer contour
* rephasinh.001 has a counter-clockwise outer contour
* rephasinh.002 has a counter-clockwise outer contour
* rephasinh.003 has a counter-clockwise outer contour
* rephasinh.004 has a counter-clockwise outer contour
* rephasinh.005 has a counter-clockwise outer contour
* rephasinh.006 has a counter-clockwise outer contour
* rephasinh.007 has a counter-clockwise outer contour
* rephasinh.008 has a counter-clockwise outer contour
* rephasinh.009 has a counter-clockwise outer contour
* rephasinh.010 has a counter-clockwise outer contour
* fsinh.hist has a counter-clockwise outer contour
* fsinh.hist has a counter-clockwise outer contour
* fsinh.hist has a counter-clockwise outer contour
* fsinh.hist has a counter-clockwise outer contour
* fIsinh.hist has a counter-clockwise outer contour
* fIsinh.hist has a counter-clockwise outer contour
* fIsinh.hist has a counter-clockwise outer contour
* fIsinh.hist has a counter-clockwise outer contour
* fIisinh.hist has a counter-clockwise outer contour
* fIisinh.hist has a counter-clockwise outer contour
* fIisinh.hist has a counter-clockwise outer contour
* fIisinh.hist has a counter-clockwise outer contour
* fRsinh.hist has a counter-clockwise outer contour
* fRsinh.hist has a counter-clockwise outer contour
* fRsinh.hist has a counter-clockwise outer contour
* fRsinh.hist has a counter-clockwise outer contour
* fRsinh.hist has a counter-clockwise outer contour
* fRIsinh.hist has a counter-clockwise outer contour
* fRIsinh.hist has a counter-clockwise outer contour
* fRIsinh.hist has a counter-clockwise outer contour
* fRIsinh.hist has a counter-clockwise outer contour
* fRIsinh.hist has a counter-clockwise outer contour
* fRIisinh.hist has a counter-clockwise outer contour
* fRIisinh.hist has a counter-clockwise outer contour
* fRIisinh.hist has a counter-clockwise outer contour
* fRIisinh.hist has a counter-clockwise outer contour
* fRIisinh.hist has a counter-clockwise outer contour
* fRasinh.hist has a counter-clockwise outer contour
* fRasinh.hist has a counter-clockwise outer contour
* fRasinh.hist has a counter-clockwise outer contour
* fRasinh.hist has a counter-clockwise outer contour
* fa_rephasinh.hist has a counter-clockwise outer contour
* fa_rephasinh.hist has a counter-clockwise outer contour
* fa_rephasinh.hist has a counter-clockwise outer contour
* fa_rephasinh.hist has a counter-clockwise outer contour
* fasinh.hist has a counter-clockwise outer contour
* fasinh.hist has a counter-clockwise outer contour
* fasinh.hist has a counter-clockwise outer contour
* fUsinh.hist has a counter-clockwise outer contour
* fUsinh.hist has a counter-clockwise outer contour
* fUsinh.hist has a counter-clockwise outer contour
* fUsinh.hist has a counter-clockwise outer contour
* fUusinh.hist has a counter-clockwise outer contour
* fUusinh.hist has a counter-clockwise outer contour
* fUusinh.hist has a counter-clockwise outer contour
* fUusinh.hist has a counter-clockwise outer contour
* uni0BFA (U+0BFA) has a counter-clockwise outer contour
* ttUtaml has a counter-clockwise outer contour
* ttUutaml has a counter-clockwise outer contour
* zhUtaml has a counter-clockwise outer contour
* zhUutaml has a counter-clockwise outer contour
* isign.alt3taml has a counter-clockwise outer contour
* isign.alt4taml has a counter-clockwise outer contour
* isign.alt5taml has a counter-clockwise outer contour
* isign.alt6taml has a counter-clockwise outer contour
* isign.alt7taml has a counter-clockwise outer contour
* Abreve (U+0102) has a counter-clockwise outer contour
* Atilde (U+00C3) has a counter-clockwise outer contour
* Gbreve (U+011E) has a counter-clockwise outer contour
* Ntilde (U+00D1) has a counter-clockwise outer contour
* Otilde (U+00D5) has a counter-clockwise outer contour
* U (U+0055) has a counter-clockwise outer contour
* U (U+0055) has a counter-clockwise outer contour
* U (U+0055) has a counter-clockwise outer contour
* Uacute (U+00DA) has a counter-clockwise outer contour
* Uacute (U+00DA) has a counter-clockwise outer contour
* Uacute (U+00DA) has a counter-clockwise outer contour
* Ucircumflex (U+00DB) has a counter-clockwise outer contour
* Ucircumflex (U+00DB) has a counter-clockwise outer contour
* Ucircumflex (U+00DB) has a counter-clockwise outer contour
* Udieresis (U+00DC) has a counter-clockwise outer contour
* Udieresis (U+00DC) has a counter-clockwise outer contour
* Udieresis (U+00DC) has a counter-clockwise outer contour
* Ugrave (U+00D9) has a counter-clockwise outer contour
* Ugrave (U+00D9) has a counter-clockwise outer contour
* Ugrave (U+00D9) has a counter-clockwise outer contour
* Uhungarumlaut (U+0170) has a counter-clockwise outer contour
* Uhungarumlaut (U+0170) has a counter-clockwise outer contour
* Uhungarumlaut (U+0170) has a counter-clockwise outer contour
* Umacron (U+016A) has a counter-clockwise outer contour
* Umacron (U+016A) has a counter-clockwise outer contour
* Umacron (U+016A) has a counter-clockwise outer contour
* Uogonek (U+0172) has a counter-clockwise outer contour
* Uogonek (U+0172) has a counter-clockwise outer contour
* Uogonek (U+0172) has a counter-clockwise outer contour
* Uring (U+016E) has a counter-clockwise outer contour
* Uring (U+016E) has a counter-clockwise outer contour
* Uring (U+016E) has a counter-clockwise outer contour
* abreve (U+0103) has a counter-clockwise outer contour
* atilde (U+00E3) has a counter-clockwise outer contour
* gbreve (U+011F) has a counter-clockwise outer contour
* ntilde (U+00F1) has a counter-clockwise outer contour
* otilde (U+00F5) has a counter-clockwise outer contour
* s (U+0073) has a counter-clockwise outer contour
* sacute (U+015B) has a counter-clockwise outer contour
* scaron (U+0161) has a counter-clockwise outer contour
* uni015F (U+015F) has a counter-clockwise outer contour
* uni0219 (U+0219) has a counter-clockwise outer contour
* sinEight_Zerolith has a counter-clockwise outer contour
* sinEight_Zerolith has a counter-clockwise outer contour
* sinEight_Zerolith has a counter-clockwise outer contour
* sinFive_Zerolith has a counter-clockwise outer contour
* sinFive_Zerolith has a counter-clockwise outer contour
* sinFive_Zerolith has a counter-clockwise outer contour
* sinFour_Zerolith has a counter-clockwise outer contour
* sinFour_Zerolith has a counter-clockwise outer contour
* sinFour_Zerolith has a counter-clockwise outer contour
* sinNine_Zerolith has a counter-clockwise outer contour
* sinNine_Zerolith has a counter-clockwise outer contour
* sinNine_Zerolith has a counter-clockwise outer contour
* sinNine_Zerolith has a counter-clockwise outer contour
* sinNine_Zerolith has a counter-clockwise outer contour
* sinOne_Zerolith has a counter-clockwise outer contour
* sinOne_Zerolith has a counter-clockwise outer contour
* sinOne_Zerolith has a counter-clockwise outer contour
* sinSeven_Zerolith has a counter-clockwise outer contour
* sinSeven_Zerolith has a counter-clockwise outer contour
* sinSeven_Zerolith has a counter-clockwise outer contour
* sinSix_Zerolith has a counter-clockwise outer contour
* sinSix_Zerolith has a counter-clockwise outer contour
* sinSix_Zerolith has a counter-clockwise outer contour
* sinThree_Zerolith has a counter-clockwise outer contour
* sinThree_Zerolith has a counter-clockwise outer contour
* sinThree_Zerolith has a counter-clockwise outer contour
* sinThree_Zerolith has a counter-clockwise outer contour
* sinThree_Zerolith has a counter-clockwise outer contour
* sinTwo_Zerolith has a counter-clockwise outer contour
* sinTwo_Zerolith has a counter-clockwise outer contour
* sinTwo_Zerolith has a counter-clockwise outer contour
* sinTwo_Zerolith has a counter-clockwise outer contour
* uni0DE6 (U+0DE6) has a counter-clockwise outer contour
* uni0DE6 (U+0DE6) has a counter-clockwise outer contour
* uni0DE7 (U+0DE7) has a counter-clockwise outer contour
* uni0DE8 (U+0DE8) has a counter-clockwise outer contour
* uni0DE8 (U+0DE8) has a counter-clockwise outer contour
* uni0DE9 (U+0DE9) has a counter-clockwise outer contour
* uni0DE9 (U+0DE9) has a counter-clockwise outer contour
* uni0DE9 (U+0DE9) has a counter-clockwise outer contour
* uni0DEA (U+0DEA) has a counter-clockwise outer contour
* uni0DEB (U+0DEB) has a counter-clockwise outer contour
* uni0DEC (U+0DEC) has a counter-clockwise outer contour
* uni0DED (U+0DED) has a counter-clockwise outer contour
* uni0DEE (U+0DEE) has a counter-clockwise outer contour
* uni0DEF (U+0DEF) has a counter-clockwise outer contour
* uni0DEF (U+0DEF) has a counter-clockwise outer contour
* uni0DEF (U+0DEF) has a counter-clockwise outer contour
* eight (U+0038) has a counter-clockwise outer contour
* eight.osf has a counter-clockwise outer contour
* eight.numr has a counter-clockwise outer contour
* uni200C (U+200C) has a counter-clockwise outer contour
* uni200D (U+200D) has a counter-clockwise outer contour
* uni0964 (U+0964) has a counter-clockwise outer contour
* uni0965 (U+0965) has a counter-clockwise outer contour
* uni0965 (U+0965) has a counter-clockwise outer contour
* uni0DF4 (U+0DF4) has a counter-clockwise outer contour
* uni2010 (U+2010) has a counter-clockwise outer contour
* braceleft (U+007B) has a counter-clockwise outer contour
* braceright (U+007D) has a counter-clockwise outer contour
* bracketleft (U+005B) has a counter-clockwise outer contour
* bracketright (U+005D) has a counter-clockwise outer contour
* bar (U+007C) has a counter-clockwise outer contour
* uni20B9 (U+20B9) has a counter-clockwise outer contour
* approxequal (U+2248) has a counter-clockwise outer contour
* approxequal (U+2248) has a counter-clockwise outer contour
* asciitilde (U+007E) has a counter-clockwise outer contour
* breve (U+02D8) has a counter-clockwise outer contour
* tilde (U+02DC) has a counter-clockwise outer contour
* tildecomb (U+0303) has a counter-clockwise outer contour
* uni0306 (U+0306) has a counter-clockwise outer contour
* mooniak has a counter-clockwise outer contour
* mooniak has a counter-clockwise outer contour [code: ccw-outer-contour]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlapping path segments:

* archaiconehundredsinh: Line(Line { p0: (383.0, 0.0), p1: (383.0, -26.0) }) has the same coordinates as a previous segment.
* sItaml: Line(Line { p0: (856.0, 411.0), p1: (876.0, 435.0) }) has the same coordinates as a previous segment.
* f (U+0066): Line(Line { p0: (181.0, 431.0), p1: (106.0, 441.0) }) has the same coordinates as a previous segment.
* z (U+007A): Line(Line { p0: (22.0, 22.0), p1: (115.0, 26.0) }) has the same coordinates as a previous segment.
* zacute (U+017A): Line(Line { p0: (22.0, 22.0), p1: (115.0, 26.0) }) has the same coordinates as a previous segment.
* zcaron (U+017E): Line(Line { p0: (22.0, 22.0), p1: (115.0, 26.0) }) has the same coordinates as a previous segment.
* zdotaccent (U+017C): Line(Line { p0: (22.0, 22.0), p1: (115.0, 26.0) }) has the same coordinates as a previous segment.
* f_f: Line(Line { p0: (107.0, 441.0), p1: (182.0, 431.0) }) has the same coordinates as a previous segment.
* f_f: Line(Line { p0: (383.0, 441.0), p1: (458.0, 431.0) }) has the same coordinates as a previous segment.
* f_f_i: Line(Line { p0: (107.0, 441.0), p1: (182.0, 431.0) }) has the same coordinates as a previous segment.
* f_f_i: Line(Line { p0: (383.0, 441.0), p1: (458.0, 431.0) }) has the same coordinates as a previous segment.
* f_f_l: Line(Line { p0: (107.0, 441.0), p1: (182.0, 431.0) }) has the same coordinates as a previous segment.
* f_f_l: Line(Line { p0: (458.0, 431.0), p1: (383.0, 441.0) }) has the same coordinates as a previous segment.
* fi (U+FB01): Line(Line { p0: (182.0, 431.0), p1: (107.0, 441.0) }) has the same coordinates as a previous segment.
* fl (U+FB02): Line(Line { p0: (182.0, 431.0), p1: (107.0, 441.0) }) has the same coordinates as a previous segment.
* two (U+0032): Line(Line { p0: (35.0, 20.0), p1: (89.0, 68.0) }) has the same coordinates as a previous segment.
* three (U+0033): Line(Line { p0: (171.0, 303.0), p1: (149.0, 321.0) }) has the same coordinates as a previous segment.
* three (U+0033): Line(Line { p0: (427.0, 580.0), p1: (330.0, 530.0) }) has the same coordinates as a previous segment.
* two.osf: Line(Line { p0: (30.0, 20.0), p1: (80.0, 70.0) }) has the same coordinates as a previous segment.
* three.osf: Line(Line { p0: (171.0, 233.0), p1: (149.0, 251.0) }) has the same coordinates as a previous segment.
* three.osf: Line(Line { p0: (427.0, 510.0), p1: (330.0, 460.0) }) has the same coordinates as a previous segment.
* two.numr: Line(Line { p0: (16.0, 13.0), p1: (61.0, 56.0) }) has the same coordinates as a previous segment.
* three.numr: Line(Line { p0: (110.0, 142.0), p1: (96.0, 154.0) }) has the same coordinates as a previous segment.
* three.numr: Line(Line { p0: (272.0, 307.0), p1: (205.0, 265.0) }) has the same coordinates as a previous segment.
* onehalf (U+00BD): Line(Line { p0: (431.0, 13.0), p1: (476.0, 56.0) }) has the same coordinates as a previous segment.
* threequarters (U+00BE): Line(Line { p0: (130.0, 431.0), p1: (116.0, 443.0) }) has the same coordinates as a previous segment.
* threequarters (U+00BE): Line(Line { p0: (292.0, 596.0), p1: (225.0, 554.0) }) has the same coordinates as a previous segment.
* uni00B2 (U+00B2): Line(Line { p0: (31.0, 342.0), p1: (76.0, 385.0) }) has the same coordinates as a previous segment.
* uni00B3 (U+00B3): Line(Line { p0: (130.0, 471.0), p1: (116.0, 483.0) }) has the same coordinates as a previous segment.
* uni00B3 (U+00B3): Line(Line { p0: (292.0, 636.0), p1: (225.0, 594.0) }) has the same coordinates as a previous segment.
* yen (U+00A5): Line(Line { p0: (251.0, 299.0), p1: (336.0, 309.0) }) has the same coordinates as a previous segment.
* uni2206 (U+2206): Line(Line { p0: (244.0, 600.0), p1: (281.0, 600.0) }) has the same coordinates as a previous segment. [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Description strings in the name table must not exceed 200 characters. (googlefonts/name/description_max_length)</summary>
    <div>








- ⚠️ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'MNIK' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 1 | 19 | 20 | 119 | 62 | 
| 0% | 9% | 9% | 54% | 28% | 



