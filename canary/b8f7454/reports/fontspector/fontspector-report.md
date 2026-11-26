## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[15] fonts/variable/AbhayaLibreCANARY[wght].ttf</summary>
<div>


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
    <summary>⚠️ <b>WARN</b> Check that format 12 cmap subtables are correctly constituted. (cmap/format_12)</summary>
    <div>








- ⚠️ **WARN** The format 12 subtable did not contain all codepoints from the format 4 subtable:

* U+FFFF [code: missing-format-4]
  
  


- ⚠️ **WARN** The format 12 subtable did not contain all codepoints from the format 4 subtable:

* U+FFFF [code: missing-format-4]
  
  

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
width=495: approxequal
width=400: multiply
width=462: less, greater
width=492: logicalnot [code: width-outliers]
  
  

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

* yasign_repha_aasignsinh
* yasign_repha_usignsinh
* yasign_repha_uusignsinh
* isigntaml.alt3
* isigntaml.alt4
* isigntaml.alt5
* isigntaml.alt6
* isigntaml.alt7
* iisigntaml.alt1
* mooniak
* vertical_stem_upper [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts have relatively consistent sidebearings. (suspicious_sidebearings)</summary>
    <div>








- ⚠️ **WARN** Glyph "isigntaml.alt4" has suspiciously high variation (z-score 15.51) in right sidebearings at locations:
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
* uni0D8F (U+0D8F)
* jhRIsinh
* dhUusinh
* jRIsinh
* dvocalicr._csinh
* nIisinh
* egrave (U+00E8)
* hUutaml
* zcaron (U+017E)
* threequarters (U+00BE)
* ttRsinh
* gUsinh
* jnyRIsinh
* trademark (U+2122)
* anusvarayaShUsinh
* ampersand (U+0026)
* kha_rephasinh
* jnyRIisinh
* Abreve (U+0102)
* Wacute (U+1E82)
* uni0D87 (U+0D87)
* dhRsinh
* nThUusinh
* ae (U+00E6)
* X (U+0058)
* cIsinh
* mbIsinh
* phsinh
* uni0BB6 (U+0BB6)
* B (U+0042)
* fRIisinh
* lUtaml
* Thorn (U+00DE)
* Wgrave (U+1E80)
* edieresis (U+00EB)
* uni2113 (U+2113)
* nIsinh
* onequarter (U+00BC)
* caron (U+02C7)
* llUusinh
* shRsinh
* bhUsinh
* shIsinh
* iogonek (U+012F)
* kUtaml
* thIisinh
* phIisinh
* six.osf
* lessequal (U+2264)
* dRasinh
* hRIsinh
* nyjUusinh
* dDha_rephasinh
* nda_rephasinh
* Y (U+0059)
* kSsIitaml
* ddRIsinh
* dvocalicrr._csinh
* shIitaml
* Euro (U+20AC)
* bBUsinh
* u111E1 (U+111E1)
* bhIsinh
* llUsinh
* dVIsinh
* ka_rephasinh
* dVUusinh
* sssinh
* jhRasinh
* nyCasinh
* dDhsinh
* ddIisinh
* uni0BB4 (U+0BB4)
* two.numr
* ddRIisinh
* jRIisinh
* ddUsinh
* tsinh
* uni0137 (U+0137)
* lithfive_lithzerosinh
* uni0D9F (U+0D9F)
* uni0DC5 (U+0DC5)
* rUusinh
* ttIisinh
* aring (U+00E5)
* ghIisinh
* ccaron (U+010D)
* uni0B8A (U+0B8A)
* zhUutaml
* ttTthIisinh
* dRIisinh
* dUsinh
* jnysinh
* gDhUusinh
* gbreve (U+011F)
* nDasinh
* section (U+00A7)
* nyjUsinh
* dhRIisinh
* ghUsinh
* kItaml
* Eacute (U+00C9)
* Scedilla (U+015E)
* edotaccent (U+0117)
* fpasinh
* ngIitaml
* lithseven_lithzerosinh
* yasign_viramasinh
* ccedilla (U+00E7)
* seven.osf
* mba_rephasinh
* eogonek (U+0119)
* bBIsinh
* wdieresis (U+1E85)
* tthIsinh
* lAitaml
* uni0B9C (U+0B9C)
* ssIitaml
* uni0162 (U+0162)
* uni013B (U+013B)
* ndaa._csinh
* uni0BB5 (U+0BB5)
* five.osf
* nnddIsinh
* gUusinh
* vUusinh
* kSsUtaml
* u111EB (U+111EB)
* germandbls (U+00DF)
* f_f_i
* infinity (U+221E)
* uni0D86 (U+0D86)
* ttTthUsinh
* m (U+006D)
* ttRIisinh
* uni0BD0 (U+0BD0)
* nItaml
* plus (U+002B)
* vRIisinh
* nngUsinh
* shIisinh
* kVasinh
* cRIisinh
* kRIsinh
* fpa_rephasinh
* zhItaml
* eth (U+00F0)
* a (U+0061)
* Egrave (U+00C8)
* uni0BA9 (U+0BA9)
* nnddsinh
* gdotaccent (U+0121)
* ngItaml
* nyItaml
* w (U+0077)
* bBIisinh
* anusvarayaShIsinh
* khRasinh
* wgrave (U+1E81)
* ttUusinh
* Ygrave (U+1EF2)
* F (U+0046)
* nyChsinh
* nnsinh
* dUusinh
* ssIisinh
* llIisinh
* lithfour_lithzerosinh
* Igrave (U+00CC)
* nnUutaml
* ucircumflex (U+00FB)
* uni0DA4 (U+0DA4)
* dRsinh
* nnIsinh
* dyU._csinh
* ttUsinh
* nnUtaml
* bBa_rephasinh
* ghRasinh
* mIitaml
* Ccaron (U+010C)
* chIisinh
* product (U+220F)
* nVIsinh
* nDaa_virama._csinh
* jhIisinh
* rUutaml
* J (U+004A)
* gRsinh
* Aring (U+00C5)
* mRasinh
* kSsasinh
* kVUsinh
* uni0BF4 (U+0BF4)
* u111E4 (U+111E4)
* Iacute (U+00CD)
* dVsinh
* g (U+0067)
* nnddIisinh
* rAaesinh
* hRIisinh
* va_rephasinh
* nyja_rephasinh
* uni0BF0 (U+0BF0)
* yIitaml
* uni0DEA (U+0DEA)
* T (U+0054)
* aasign_viramasinh
* vRsinh
* hRasinh
* phUusinh
* dhUsinh
* tRIisinh
* hsinh
* ba_rephasinh
* kVIsinh
* daa_virama._csinh
* ttTthsinh
* anusvarayaShsinh
* AE (U+00C6)
* z (U+007A)
* nysinh
* Uacute (U+00DA)
* kUsinh
* tThsinh
* nUsinh
* vIisinh
* jRasinh
* rIitaml
* tthUsinh
* ssinh
* nnnUtaml
* eight.osf
* N (U+004E)
* kRasinh
* mUtaml
* bhRasinh
* la_rephasinh
* Atilde (U+00C3)
* Lcaron (U+013D)
* dyaa._csinh
* wcircumflex (U+0175)
* llUtaml
* tcaron (U+0165)
* zacute (U+017A)
* nyIisinh
* ndUusinh
* jRsinh
* cRsinh
* scaron (U+0161)
* bBUusinh
* uni0BF2 (U+0BF2)
* rItaml
* q (U+0071)
* D (U+0044)
* tthIisinh
* cUutaml
* cCsinh
* nyCIsinh
* P (U+0050)
* hItaml
* sItaml
* cRIsinh
* uni0BCA (U+0BCA)
* fpRIisinh
* dcaron (U+010F)
* kVUusinh
* racute (U+0155)
* ca_rephasinh
* nUtaml
* five (U+0035)
* cRasinh
* Lslash (U+0141)
* llItaml
* nIitaml
* pItaml
* ma_rephasinh
* cItaml
* tUsinh
* dRIsinh
* cIitaml
* fpsinh
* rIsinh
* aacute (U+00E1)
* greaterequal (U+2265)
* V (U+0056)
* iisigntaml.alt1
* icircumflex (U+00EE)
* Gbreve (U+011E)
* uni0D92 (U+0D92)
* fpIisinh
* jhRIisinh
* nyjIisinh
* phIsinh
* lItaml
* ttsinh
* pRIisinh
* khRIsinh
* nyaae._csinh
* nnddUusinh
* Aogonek (U+0104)
* bhIisinh
* nThasinh
* two.osf
* u111EC (U+111EC)
* nyaa_virama._csinh
* tThIsinh
* nyCsinh
* uni0BB8 (U+0BB8)
* uni0DC2 (U+0DC2)
* ddRasinh
* pUsinh
* M (U+004D)
* uni0BA4 (U+0BA4)
* ttIitaml
* nDaae._csinh
* ddhUusinh
* dDhUusinh
* dIsinh
* ssUsinh
* nyChUusinh
* Eogonek (U+0118)
* seven.numr
* nyCUsinh
* kSsUsinh
* hRsinh
* wacute (U+1E83)
* bBsinh
* uni0BEB (U+0BEB)
* zdotaccent (U+017C)
* jnyIisinh
* nnAataml
* lslash (U+0142)
* uni0BB7 (U+0BB7)
* emacron (U+0113)
* tVIsinh
* sRIsinh
* tThUsinh
* uni0BE9 (U+0BE9)
* cCUusinh
* ja_rephasinh
* uni0BB3 (U+0BB3)
* cent (U+00A2)
* nnnItaml
* nyjIsinh
* two (U+0032)
* nnIisinh
* bhRIisinh
* uni0B85 (U+0B85)
* uni0B90 (U+0B90)
* nnItaml
* nyCa_rephasinh
* h (U+0068)
* fIsinh
* Lacute (U+0139)
* tta_rephasinh
* nndda_rephasinh
* asciicircum (U+005E)
* E (U+0045)
* bhsinh
* gRIsinh
* yasign_repha_uusignsinh
* uni0DEC (U+0DEC)
* ddhUsinh
* dDhasinh
* t (U+0074)
* nDhIisinh
* nyChIisinh
* nUusinh
* tRsinh
* uni0BC6 (U+0BC6)
* tTha_rephasinh
* hIisinh
* uni0BB2 (U+0BB2)
* f_f_l
* ndUsinh
* nDaa._csinh
* dIisinh
* shRIisinh
* Adieresis (U+00C4)
* nyRIsinh
* uni0BB9 (U+0BB9)
* Edieresis (U+00CB)
* u111EF (U+111EF)
* ydieresis (U+00FF)
* mUutaml
* ddhIsinh
* jnyaae._csinh
* nDUusinh
* ssUutaml
* uni0D9D (U+0D9D)
* dVIisinh
* fpUusinh
* pUusinh
* tVUsinh
* uni0BF1 (U+0BF1)
* nnnIitaml
* Edotaccent (U+0116)
* Ycircumflex (U+0176)
* ttha_rephasinh
* b (U+0062)
* rsinh
* u111E8 (U+111E8)
* onehalf (U+00BD)
* H (U+0048)
* asterisk (U+002A)
* nna_rephasinh
* tRIsinh
* sRIisinh
* cCIsinh
* fsinh
* nyUusinh
* fpRasinh
* dRaa._csinh
* lithtwo_lithzerosinh
* mIisinh
* uni0BCB (U+0BCB)
* uni030C (U+030C)
* uni0302 (U+0302)
* agrave (U+00E0)
* kSsIsinh
* dyaa_virama._csinh
* uni0BEE (U+0BEE)
* fIisinh
* nyjRasinh
* thIsinh
* Iogonek (U+012E)
* ddhIisinh
* Wcircumflex (U+0174)
* nDsinh
* rrUutaml
* k (U+006B)
* Uogonek (U+0172)
* uni0BCC (U+0BCC)
* ndsinh
* yIsinh
* nyIitaml
* nsinh
* nnnUutaml
* three.numr
* mRIisinh
* sIisinh
* nngUusinh
* r (U+0072)
* lIsinh
* v (U+0076)
* uni0D88 (U+0D88)
* dDhIsinh
* bRsinh
* uni0136 (U+0136)
* khRsinh
* kSsa_rephasinh
* ttItaml
* uni0123 (U+0123)
* na_rephasinh
* tUusinh
* uni0B93 (U+0B93)
* cha_rephasinh
* G (U+0047)
* ghUusinh
* tThUusinh
* nine.numr
* logicalnot (U+00AC)
* uni2126 (U+2126)
* lithsix_lithzerosinh
* uni0DEF (U+0DEF)
* yUutaml
* ttTtha_rephasinh
* uni0DA6 (U+0DA6)
* dda_rephasinh
* uni1E9E (U+1E9E)
* ndRaa._csinh
* Imacron (U+012A)
* oe (U+0153)
* Rcaron (U+0158)
* yacute (U+00FD)
* uni0B8F (U+0B8F)
* nyRIisinh
* cCa_rephasinh
* Uhungarumlaut (U+0170)
* uni00B2 (U+00B2)
* sUusinh
* Eth (U+00D0)
* rrItaml
* ttIsinh
* uni0B87 (U+0B87)
* gDhUsinh
* hIitaml
* yasign_isignsinh
* lsinh
* lUsinh
* pRIsinh
* ssRsinh
* lUutaml
* fpRsinh
* ngIisinh
* tVsinh
* kSsataml
* nVUusinh
* pIsinh
* tThIisinh
* uni0156 (U+0156)
* u111E3 (U+111E3)
* shsinh
* jhsinh
* dVasinh
* eacute (U+00E9)
* nacute (U+0144)
* summation (U+2211)
* uni0D93 (U+0D93)
* aisigntaml.la
* fi (U+FB01)
* bRasinh
* gDha_rephasinh
* khIisinh
* ghRsinh
* uni0145 (U+0145)
* four.osf
* kIisinh
* bhRsinh
* gIsinh
* ghIsinh
* uni021B (U+021B)
* bhUusinh
* nngIsinh
* anusvarayaShIisinh
* nyUtaml
* paragraph (U+00B6)
* llsinh
* pUutaml
* zhUtaml
* jhRsinh
* gRIisinh
* thUsinh
* three (U+0033)
* jIsinh
* fUusinh
* vIsinh
* tVa_rephasinh
* uni0BAE (U+0BAE)
* u111ED (U+111ED)
* uni0DE6 (U+0DE6)
* amacron (U+0101)
* cIisinh
* lla_rephasinh
* kIitaml
* Amacron (U+0100)
* Q (U+0051)
* nDha_rephasinh
* bhRIsinh
* uni0BA3 (U+0BA3)
* R (U+0052)
* uni20BD (U+20BD)
* ghRIsinh
* ndaa_virama._csinh
* Zcaron (U+017D)
* dollar (U+0024)
* msinh
* ssRasinh
* uogonek (U+0173)
* tVUusinh
* abreve (U+0103)
* chsinh
* tIitaml
* dha_rephasinh
* tthsinh
* hUsinh
* anusvarayaShUusinh
* gDhasinh
* uni0DA2 (U+0DA2)
* kUusinh
* Ecaron (U+011A)
* gDhsinh
* mRIsinh
* ndae._csinh
* ncaron (U+0148)
* jUsinh
* ttUtaml
* f (U+0066)
* ssa_rephasinh
* rrUtaml
* nga_rephasinh
* Ccedilla (U+00C7)
* nThIsinh
* cUtaml
* nngsinh
* n (U+006E)
* uni0B89 (U+0B89)
* uni0B8E (U+0B8E)
* jhIsinh
* dVUsinh
* bRIsinh
* nVa_rephasinh
* llUutaml
* I (U+0049)
* fRasinh
* khsinh
* four (U+0034)
* florin (U+0192)
* dDhIisinh
* sIitaml
* nUutaml
* currency (U+00A4)
* ssIsinh
* rrAataml
* yen (U+00A5)
* uni0BF6 (U+0BF6)
* shUsinh
* dhRIsinh
* gRasinh
* W (U+0057)
* khIsinh
* fpIsinh
* uni0D91 (U+0D91)
* vUsinh
* dagger (U+2020)
* four.numr
* uni0B9E (U+0B9E)
* uni0DB3 (U+0DB3)
* tIsinh
* nDIisinh
* nyCIisinh
* nnIitaml
* uni0BA8 (U+0BA8)
* ssItaml
* Nacute (U+0143)
* psinh
* uni20BA (U+20BA)
* jnyae._csinh
* x (U+0078)
* kIsinh
* Udieresis (U+00DC)
* vRasinh
* lIisinh
* uni0BF7 (U+0BF7)
* uni0D9A (U+0D9A)
* uni0BE7 (U+0BE7)
* gDhIsinh
* rAesinh
* nnnAataml
* dVa_rephasinh
* nyjsinh
* uni0B92 (U+0B92)
* three.osf
* nyjRsinh
* d (U+0064)
* jnyIsinh
* nnga_rephasinh
* ddsinh
* kVa_rephasinh
* kVIisinh
* Gdotaccent (U+0120)
* Acircumflex (U+00C2)
* rcaron (U+0159)
* u111E7 (U+111E7)
* Ydieresis (U+0178)
* jhUsinh
* yasign_uusignsinh
* eight.numr
* Yacute (U+00DD)
* bIisinh
* nine.osf
* ssRIisinh
* Agrave (U+00C0)
* ssUtaml
* ngUutaml
* iisigntaml.alt
* nyRsinh
* uni0BAF (U+0BAF)
* uni0BF9 (U+0BF9)
* ndaae._csinh
* ygrave (U+1EF3)
* uni2206 (U+2206)
* six (U+0036)
* bUusinh
* daggerdbl (U+2021)
* nThIisinh
* mUusinh
* nyCha_rephasinh
* mbUusinh
* nnUusinh
* jnyUusinh
* kSsUusinh
* ttRasinh
* ttTthIsinh
* yasign_usignsinh
* uni0BC0 (U+0BC0)
* Racute (U+0154)
* Hbar (U+0126)
* Icircumflex (U+00CE)
* uni0BEA (U+0BEA)
* nDhsinh
* hUusinh
* rUtaml
* dDhUsinh
* hbar (U+0127)
* nTha_rephasinh
* tUtaml
* yUusinh
* nyUutaml
* rIisinh
* tVIisinh
* nDUsinh
* pRsinh
* vRIsinh
* phUsinh
* khRIisinh
* mRsinh
* sa_rephasinh
* uni0122 (U+0122)
* five.numr
* ecaron (U+011B)
* ddUusinh
* ksinh
* tVasinh
* bBasinh
* nDae._csinh
* mItaml
* yasign_iisignsinh
* sUtaml
* greater (U+003E)
* lIitaml
* Ntilde (U+00D1)
* mIsinh
* nThsinh
* uni0BEC (U+0BEC)
* nyCUusinh
* jIisinh
* nngIisinh
* mUsinh
* uni0BC2 (U+0BC2)
* thUusinh
* Idieresis (U+00CF)
* jnyaa_virama._csinh
* llIitaml
* fpRIsinh
* Uring (U+016E)
* ordfeminine (U+00AA)
* nVIisinh
* jhUusinh
* dya._csinh
* ndIsinh
* uni0D95 (U+0D95)
* rrIitaml
* seven (U+0037)
* uni0DA0 (U+0DA0)
* ysinh
* fpUsinh
* kUutaml
* Dcroat (U+0110)
* vIitaml
* yItaml
* ndIisinh
* Ugrave (U+00D9)
* ddRsinh
* nDhasinh
* litheight_lithzerosinh
* ttRIsinh
* less (U+003C)
* nnUsinh
* nDhIsinh
* jItaml
* nya_rephasinh
* u111E5 (U+111E5)
* ngsinh
* nnddUsinh
* hIsinh
* gDhIisinh
* chUsinh
* nyRasinh
* kSssinh
* circumflex (U+02C6)
* kSsUutaml
* uni0DDD (U+0DDD)
* dsinh
* jsinh
* shRIsinh
* tItaml
* vUutaml
* Wdieresis (U+1E84)
* pi (U+03C0)
* pIitaml
* ttUutaml
* fRsinh
* u111E6 (U+111E6)
* ttTthUusinh
* Ecircumflex (U+00CA)
* uni0BB1 (U+0BB1)
* uni0B99 (U+0B99)
* uni0BC7 (U+0BC7)
* Ocircumflex (U+00D4)
* Dcaron (U+010E)
* gsinh
* tIisinh
* bUsinh
* nDhUusinh
* ra_rephasinh
* rUsinh
* yasign_repha_usignsinh
* mbUsinh
* uni0BD7 (U+0BD7)
* nDRasinh
* shreetaml
* dcroat (U+0111)
* jha_rephasinh
* notequal (U+2260)
* tthUusinh
* kSsIisinh
* fRIsinh
* jIitaml
* atilde (U+00E3)
* radical (U+221A)
* ghsinh
* uni0157 (U+0157)
* uni0DA1 (U+0DA1)
* ddhsinh
* nVasinh
* uni0B94 (U+0B94)
* uni0DAB (U+0DAB)
* thsinh
* uni0DF3 (U+0DF3)
* jUutaml
* U (U+0055)
* cCUsinh
* nyIsinh
* yUsinh
* oslash (U+00F8)
* chIsinh
* gha_rephasinh
* uni0BF3 (U+0BF3)
* uni0BB0 (U+0BB0)
* uni0DB7 (U+0DB7)
* csinh
* pIisinh
* y (U+0079)
* uni0DA5 (U+0DA5)
* ttTthasinh
* uni0146 (U+0146)
* dyUu._csinh
* nThUsinh
* Scaron (U+0160)
* nDIsinh
* Umacron (U+016A)
* fUsinh
* vItaml
* eight (U+0038)
* uni0BF5 (U+0BF5)
* nyae._csinh
* kRsinh
* ssRIsinh
* ddha_rephasinh
* kVsinh
* dhRasinh
* khUsinh
* llIsinh
* adieresis (U+00E4)
* uni0163 (U+0163)
* nyChasinh
* u111F2 (U+111F2)
* uni0D90 (U+0D90)
* six.numr
* llAitaml
* Ucircumflex (U+00DB)
* u111F1 (U+111F1)
* ddIsinh
* partialdiff (U+2202)
* nDhUsinh
* e (U+0065)
* sterling (U+00A3)
* OE (U+0152)
* uni0B95 (U+0B95)
* ocircumflex (U+00F4)
* uni0BEF (U+0BEF)
* jnya_rephasinh
* hUtaml
* bRIisinh
* jnyRasinh
* ngIsinh
* liththree_lithzerosinh
* sRasinh
* cUsinh
* uni0DE8 (U+0DE8)
* acircumflex (U+00E2)
* f_f
* nVsinh
* anusvarayaShasinh
* uni0BC8 (U+0BC8)
* cCIisinh
* uni0BF8 (U+0BF8)
* cUusinh
* Ncaron (U+0147)
* u111F4 (U+111F4)
* bha_rephasinh
* nDRIisinh
* khUusinh
* Oslash (U+00D8)
* uni0BED (U+0BED)
* sIsinh
* kSsItaml
* Emacron (U+0112)
* uni0DC3 (U+0DC3)
* uni0DA3 (U+0DA3)
* Tcaron (U+0164)
* ndRasinh
* at (U+0040)
* nnAitaml
* ghRIisinh
* nDa_rephasinh
* ntilde (U+00F1)
* tRasinh
* pRasinh
* chUusinh
* uni021A (U+021A)
* jUtaml
* aogonek (U+0105)
* ssUusinh
* L (U+004C)
* ecircumflex (U+00EA)
* jUusinh
* lithone_lithzerosinh
* multiply (U+00D7)
* nyChIsinh
* shItaml
* mbIisinh
* nyUsinh
* uni0B86 (U+0B86)
* uni0DE9 (U+0DE9)
* nine (U+0039)
* nyChUsinh
* numbersign (U+0023)
* uni00B3 (U+00B3)
* Aacute (U+00C1)
* K (U+004B)
* Idotaccent (U+0130)
* uni0B9A (U+0B9A)
* uni0DAC (U+0DAC)
* nDRIsinh
* ycircumflex (U+0177)
* nnnAitaml
* shUusinh
* jnyaa._csinh
* fl (U+FB02)
* kRIisinh
* u111F0 (U+111F0)
* tUutaml
* zhIitaml
* nVUsinh
* lUusinh
* bIsinh
* shRasinh
* plusminus (U+00B1)
* uni00B5 (U+00B5)
* sRsinh
* lithnine_lithzerosinh
* uni0D85 (U+0D85)
* yIisinh
* jnyRsinh
* jnyUsinh
* sUsinh
* tThasinh
* u111F3 (U+111F3)
* u111EA (U+111EA)
* uni0BE8 (U+0BE8)
* A (U+0041)
* nyaa._csinh
* u111EE (U+111EE) [code: no-overlaps-bit]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font follows the Google Fonts vertical metric schema (googlefonts/vertical_metrics)</summary>
    <div>








- ⚠️ **WARN** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1180 when it should be at least 1200 (Overriden: line height is a design choice for Mooniak display faces) [code: bad-hhea-range]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

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
* uni0DDF (U+0DDF) has a counter-clockwise outer contour
* uni0DDC (U+0DDC) has a counter-clockwise outer contour
* uni0DDC (U+0DDC) has a counter-clockwise outer contour
* uni0DDD (U+0DDD) has a counter-clockwise outer contour
* uni0DDD (U+0DDD) has a counter-clockwise outer contour
* uni0DDD (U+0DDD) has a counter-clockwise outer contour
* uni0DD8 (U+0DD8) has a counter-clockwise outer contour
* uni0DF2 (U+0DF2) has a counter-clockwise outer contour
* uni0DF2 (U+0DF2) has a counter-clockwise outer contour
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
* dyaa_virama._csinh has a counter-clockwise outer contour
* dyaa_virama._csinh has a counter-clockwise outer contour
* dyaa_virama._csinh has a counter-clockwise outer contour
* dyaa_virama._csinh has a counter-clockwise outer contour
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
* u111E1 (U+111E1) has a counter-clockwise outer contour
* u111E1 (U+111E1) has a counter-clockwise outer contour
* u111E2 (U+111E2) has a counter-clockwise outer contour
* u111E3 (U+111E3) has a counter-clockwise outer contour
* u111E3 (U+111E3) has a counter-clockwise outer contour
* u111E4 (U+111E4) has a counter-clockwise outer contour
* u111E5 (U+111E5) has a counter-clockwise outer contour
* u111E5 (U+111E5) has a counter-clockwise outer contour
* u111E5 (U+111E5) has a counter-clockwise outer contour
* u111E6 (U+111E6) has a counter-clockwise outer contour
* u111E6 (U+111E6) has a counter-clockwise outer contour
* u111E7 (U+111E7) has a counter-clockwise outer contour
* u111E8 (U+111E8) has a counter-clockwise outer contour
* u111E9 (U+111E9) has a counter-clockwise outer contour
* u111EA (U+111EA) has a counter-clockwise outer contour
* u111EA (U+111EA) has a counter-clockwise outer contour
* u111EB (U+111EB) has a counter-clockwise outer contour
* u111EB (U+111EB) has a counter-clockwise outer contour
* u111EB (U+111EB) has a counter-clockwise outer contour
* u111EC (U+111EC) has a counter-clockwise outer contour
* u111EC (U+111EC) has a counter-clockwise outer contour
* u111ED (U+111ED) has a counter-clockwise outer contour
* u111ED (U+111ED) has a counter-clockwise outer contour
* u111EE (U+111EE) has a counter-clockwise outer contour
* u111EE (U+111EE) has a counter-clockwise outer contour
* u111EE (U+111EE) has a counter-clockwise outer contour
* u111F0 (U+111F0) has a counter-clockwise outer contour
* u111F0 (U+111F0) has a counter-clockwise outer contour
* u111F0 (U+111F0) has a counter-clockwise outer contour
* u111F1 (U+111F1) has a counter-clockwise outer contour
* u111F1 (U+111F1) has a counter-clockwise outer contour
* u111F2 (U+111F2) has a counter-clockwise outer contour
* u111F2 (U+111F2) has a counter-clockwise outer contour
* u111F2 (U+111F2) has a counter-clockwise outer contour
* u111F3 (U+111F3) has a counter-clockwise outer contour
* u111F3 (U+111F3) has a counter-clockwise outer contour
* u111F4 (U+111F4) has a counter-clockwise outer contour
* u111F4 (U+111F4) has a counter-clockwise outer contour
* u111F4 (U+111F4) has a counter-clockwise outer contour
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
* fpsinh has a counter-clockwise outer contour
* fpsinh has a counter-clockwise outer contour
* fpsinh has a counter-clockwise outer contour
* fpsinh has a counter-clockwise outer contour
* fpIsinh has a counter-clockwise outer contour
* fpIsinh has a counter-clockwise outer contour
* fpIsinh has a counter-clockwise outer contour
* fpIsinh has a counter-clockwise outer contour
* fpIisinh has a counter-clockwise outer contour
* fpIisinh has a counter-clockwise outer contour
* fpIisinh has a counter-clockwise outer contour
* fpIisinh has a counter-clockwise outer contour
* fpRsinh has a counter-clockwise outer contour
* fpRsinh has a counter-clockwise outer contour
* fpRsinh has a counter-clockwise outer contour
* fpRsinh has a counter-clockwise outer contour
* fpRsinh has a counter-clockwise outer contour
* fpRIsinh has a counter-clockwise outer contour
* fpRIsinh has a counter-clockwise outer contour
* fpRIsinh has a counter-clockwise outer contour
* fpRIsinh has a counter-clockwise outer contour
* fpRIsinh has a counter-clockwise outer contour
* fpRIisinh has a counter-clockwise outer contour
* fpRIisinh has a counter-clockwise outer contour
* fpRIisinh has a counter-clockwise outer contour
* fpRIisinh has a counter-clockwise outer contour
* fpRIisinh has a counter-clockwise outer contour
* fpRasinh has a counter-clockwise outer contour
* fpRasinh has a counter-clockwise outer contour
* fpRasinh has a counter-clockwise outer contour
* fpRasinh has a counter-clockwise outer contour
* fpa_rephasinh has a counter-clockwise outer contour
* fpa_rephasinh has a counter-clockwise outer contour
* fpa_rephasinh has a counter-clockwise outer contour
* fpa_rephasinh has a counter-clockwise outer contour
* fpasinh has a counter-clockwise outer contour
* fpasinh has a counter-clockwise outer contour
* fpasinh has a counter-clockwise outer contour
* fpUsinh has a counter-clockwise outer contour
* fpUsinh has a counter-clockwise outer contour
* fpUsinh has a counter-clockwise outer contour
* fpUsinh has a counter-clockwise outer contour
* fpUusinh has a counter-clockwise outer contour
* fpUusinh has a counter-clockwise outer contour
* fpUusinh has a counter-clockwise outer contour
* fpUusinh has a counter-clockwise outer contour
* uni0BFA (U+0BFA) has a counter-clockwise outer contour
* ttUtaml has a counter-clockwise outer contour
* ttUutaml has a counter-clockwise outer contour
* zhUtaml has a counter-clockwise outer contour
* zhUutaml has a counter-clockwise outer contour
* isigntaml.alt3 has a counter-clockwise outer contour
* isigntaml.alt4 has a counter-clockwise outer contour
* isigntaml.alt5 has a counter-clockwise outer contour
* isigntaml.alt6 has a counter-clockwise outer contour
* isigntaml.alt7 has a counter-clockwise outer contour
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
* litheight_lithzerosinh has a counter-clockwise outer contour
* litheight_lithzerosinh has a counter-clockwise outer contour
* litheight_lithzerosinh has a counter-clockwise outer contour
* lithfive_lithzerosinh has a counter-clockwise outer contour
* lithfive_lithzerosinh has a counter-clockwise outer contour
* lithfive_lithzerosinh has a counter-clockwise outer contour
* lithfour_lithzerosinh has a counter-clockwise outer contour
* lithfour_lithzerosinh has a counter-clockwise outer contour
* lithfour_lithzerosinh has a counter-clockwise outer contour
* lithnine_lithzerosinh has a counter-clockwise outer contour
* lithnine_lithzerosinh has a counter-clockwise outer contour
* lithnine_lithzerosinh has a counter-clockwise outer contour
* lithnine_lithzerosinh has a counter-clockwise outer contour
* lithnine_lithzerosinh has a counter-clockwise outer contour
* lithone_lithzerosinh has a counter-clockwise outer contour
* lithone_lithzerosinh has a counter-clockwise outer contour
* lithone_lithzerosinh has a counter-clockwise outer contour
* lithseven_lithzerosinh has a counter-clockwise outer contour
* lithseven_lithzerosinh has a counter-clockwise outer contour
* lithseven_lithzerosinh has a counter-clockwise outer contour
* lithsix_lithzerosinh has a counter-clockwise outer contour
* lithsix_lithzerosinh has a counter-clockwise outer contour
* lithsix_lithzerosinh has a counter-clockwise outer contour
* liththree_lithzerosinh has a counter-clockwise outer contour
* liththree_lithzerosinh has a counter-clockwise outer contour
* liththree_lithzerosinh has a counter-clockwise outer contour
* liththree_lithzerosinh has a counter-clockwise outer contour
* liththree_lithzerosinh has a counter-clockwise outer contour
* lithtwo_lithzerosinh has a counter-clockwise outer contour
* lithtwo_lithzerosinh has a counter-clockwise outer contour
* lithtwo_lithzerosinh has a counter-clockwise outer contour
* lithtwo_lithzerosinh has a counter-clockwise outer contour
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

* u111F3 (U+111F3): Line(Line { p0: (383.0, 0.0), p1: (383.0, -26.0) }) has the same coordinates as a previous segment.
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
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings:

* į̌
* į́
* į̂
* į̃
* į̀
* į̄The dot of soft dotted characters _should_ disappear in other cases, for example:

* į̆
* į̋
* į̇
* į̊
* į̈ [code: soft-dotted]
  
  

</div>
</details>


</div>
</details>






### Summary

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 16 | 12 | 97 | 33 | 
| 10% | 8% | 61% | 21% | 



