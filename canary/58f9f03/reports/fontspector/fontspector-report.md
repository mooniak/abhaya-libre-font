## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[21] fonts/variable/AbhayaLibre[wght].ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>








- 🔥 **FAIL** Lcaron uses component: caron [code: wrong-mark]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. (name/family_and_style_max_length)</summary>
    <div>








- 🔥 **FAIL** Variable font instance name 'Abhaya Libre DEV CANARY ExtraBold' formed by space-separated concatenation of font family name (nameID FAMILY_NAME) and instance subfamily nameID ExtraBold exceeds 32 characterss (1 characters too long).

This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11. [code: instance-too-long]
  
  


- 🔥 **FAIL** Variable font instance name 'Abhaya Libre DEV CANARY ExtraBold' formed by space-separated concatenation of font family name (nameID FAMILY_NAME) and instance subfamily nameID ExtraBold exceeds 32 characterss (1 characters too long).

This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11. [code: instance-too-long]
  
  


- ⚠️ **WARN** Name ID 6 'PostScript Name' exceeds 27 characters (1 characters too long). This has been found to cause problems with PostScript printers, especially on Mac platforms. [code: nameid6-too-long]
  
  


- ⚠️ **WARN** Name ID 6 'PostScript Name' exceeds 27 characters (1 characters too long). This has been found to cause problems with PostScript printers, especially on Mac platforms. [code: nameid6-too-long]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Name table records must not have trailing spaces. (name/trailing_spaces)</summary>
    <div>








- 🔥 **FAIL** Name table record 3/1/1033/NameId 266 has trailing spaces that must be removed:
`Name: ` [code: trailing-space]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- 🔥 **FAIL** Failed language shaping:

| Message                                                                                       | Languages                    |
|-----------------------------------------------------------------------------------------------|------------------------------|
| Mandatory orthography codepoints:                                                             | * de_Latn (German)           |
|   The following base characters are missing from the font: ẞ                                  |                              |
|   The following mark characters are missing from the font: ̈, ̀, ́                               |                              |
| Mandatory orthography codepoints:                                                             | * nl_Latn (Dutch)            |
|   The following base characters are missing from the font: ÍJ́, íj́                             |                              |
|   The following mark characters are missing from the font: ̈, ́, ̀, ̂                             |                              |
| Mandatory orthography codepoints:                                                             | * sv_Latn (Swedish)          |
|   The following mark characters are missing from the font: ́, ̈, ̀, ̊                             |                              |
| Mandatory orthography codepoints:                                                             | * lt_Latn (Lithuanian)       |
|   The following mark characters are missing from the font: ̄, ̇, ̌, ̨                             |                              |
| Mandatory orthography codepoints:                                                             | * cy_Latn (Welsh)            |
|   The following base characters are missing from the font: ŷ, ẁ, Ŵ, ẃ, Ẃ, Ỳ, ỳ, Ẅ, Ẁ, ẅ, ŵ, Ŷ |                              |
|   The following mark characters are missing from the font: ̀, ́, ̈, ̂                             |                              |
| Mandatory orthography codepoints:                                                             | * es_Latn (Spanish)          |
|   The following mark characters are missing from the font: ̃, ́, ̈                               |                              |
| Mandatory orthography codepoints:                                                             | * da_Latn (Danish)           |
|   The following mark characters are missing from the font: ̊, ́                                 |                              |
| Mandatory orthography codepoints:                                                             | * fi_Latn (Finnish)          |
|   The following mark characters are missing from the font: ̈, ̊, ̃, ̌                             |                              |
| Mandatory orthography codepoints:                                                             | * hr_Latn (Croatian)         |
|   The following mark characters are missing from the font: ́, ̌                                 |                              |
| Mandatory orthography codepoints:                                                             | * sk_Latn (Slovak)           |
|   The following mark characters are missing from the font: ̂, ̌, ́, ̈                             |                              |
| Mandatory orthography codepoints:                                                             | * sq_Latn (Albanian)         |
|   The following mark characters are missing from the font: ̧, ̈                                 |                              |
| Mandatory orthography codepoints:                                                             | * nb_Latn (Norwegian Bokmål) |
|   The following mark characters are missing from the font: ̊, ̂, ̈, ́, ̀                           |                              |
| Mandatory orthography codepoints:                                                             | * cs_Latn (Czech)            |
|   The following mark characters are missing from the font: ̊, ́, ̌                               |                              |
| Mandatory orthography codepoints:                                                             | * ca_Latn (Catalan)          |
|   The following mark characters are missing from the font: ̀, ́, ̈, ̧                             |                              |
| Mandatory orthography codepoints:                                                             | * pl_Latn (Polish)           |
|   The following mark characters are missing from the font: ́, ̇, ̨                               |                              |
| Mandatory orthography codepoints:                                                             | * en_Latn (English)          |
|   The following mark characters are missing from the font: ́, ̂, ̃, ̀, ̈, ̧                         |                              |
| Mandatory orthography codepoints:                                                             | * pt_Latn (Portuguese)       |
|   The following mark characters are missing from the font: ̈, ̧, ̃, ́, ̂, ̀                         |                              |
| Mandatory orthography codepoints:                                                             | * it_Latn (Italian)          |
|   The following mark characters are missing from the font: ̂, ̈, ́, ̀                             |                              |
| Mandatory orthography codepoints:                                                             | * tr_Latn (Turkish)          |
|   The following mark characters are missing from the font: ̆, ̇, ̦, ̧, ̈, ̂                         |                              |
| Mandatory orthography codepoints:                                                             | * ro_Latn (Romanian)         |
|   The following mark characters are missing from the font: ̦, ̆, ̧, ̂                             |                              |
| Mandatory orthography codepoints:                                                             | * is_Latn (Icelandic)        |
|   The following mark characters are missing from the font: ̈, ́, ̨                               |                              |
| Mandatory orthography codepoints:                                                             | * lv_Latn (Latvian)          |
|   The following mark characters are missing from the font: ̄, ̌, ̧                               |                              |
| Mandatory orthography codepoints:                                                             | * mt_Latn (Maltese)          |
|   The following base characters are missing from the font: ħ, ġ, Ċ, GĦ, Ħ, ċ, Ġ, għ           |                              |
|   The following mark characters are missing from the font: ̂, ̇, ̀                               |                              |
| Mandatory orthography codepoints:                                                             | * fr_Latn (French)           |
|   The following mark characters are missing from the font: ̧, ̈, ̀, ́, ̂                           |                              |
| Mandatory orthography codepoints:                                                             | * hu_Latn (Hungarian)        |
|   The following mark characters are missing from the font: ̈, ̋, ́                               |                              | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * it_Latn (Italian)          |
|   The following auxiliary characters are missing from the font: ẞ | * pl_Latn (Polish)           |
| Auxiliary orthography codepoints:                                 | * tr_Latn (Turkish)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * nl_Latn (Dutch)            |
|   The following auxiliary characters are missing from the font: Ĳ |                              |
|   The following auxiliary characters are missing from the font: ĳ |                              |
| Auxiliary orthography codepoints:                                 | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ċ |                              |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ħ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŝ |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ċ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ħ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŝ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
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
| Auxiliary orthography codepoints:                                 | * cs_Latn (Czech)            |
|   The following auxiliary characters are missing from the font: Ĕ | * cy_Latn (Welsh)            |
|   The following auxiliary characters are missing from the font: Ĭ | * es_Latn (Spanish)          |
|   The following auxiliary characters are missing from the font: Ŏ | * hu_Latn (Hungarian)        |
|   The following auxiliary characters are missing from the font: Ŭ | * pt_Latn (Portuguese)       |
|   The following auxiliary characters are missing from the font: ĕ | * sk_Latn (Slovak)           |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ą́ |                              |
|   The following auxiliary characters are missing from the font: Ą̃ |                              |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ę́ |                              |
|   The following auxiliary characters are missing from the font: Ę̃ |                              |
|   The following auxiliary characters are missing from the font: Ė́ |                              |
|   The following auxiliary characters are missing from the font: Ė̃ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: Ĩ |                              |
|   The following auxiliary characters are missing from the font: Į́ |                              |
|   The following auxiliary characters are missing from the font: Į̇́ |                              |
|   The following auxiliary characters are missing from the font: Į̃ |                              |
|   The following auxiliary characters are missing from the font: Į̇̃ |                              |
|   The following auxiliary characters are missing from the font: J̃ |                              |
|   The following auxiliary characters are missing from the font: J̇̃ |                              |
|   The following auxiliary characters are missing from the font: L̃ |                              |
|   The following auxiliary characters are missing from the font: M̃ |                              |
|   The following auxiliary characters are missing from the font: R̃ |                              |
|   The following auxiliary characters are missing from the font: Ũ |                              |
|   The following auxiliary characters are missing from the font: Ų́ |                              |
|   The following auxiliary characters are missing from the font: Ų̃ |                              |
|   The following auxiliary characters are missing from the font: Ū́ |                              |
|   The following auxiliary characters are missing from the font: Ū̃ |                              |
|   The following auxiliary characters are missing from the font: ą́ |                              |
|   The following auxiliary characters are missing from the font: ą̃ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ę́ |                              |
|   The following auxiliary characters are missing from the font: ę̃ |                              |
|   The following auxiliary characters are missing from the font: ė́ |                              |
|   The following auxiliary characters are missing from the font: ė̃ |                              |
|   The following auxiliary characters are missing from the font: i̇́ |                              |
|   The following auxiliary characters are missing from the font: i̇̀ |                              |
|   The following auxiliary characters are missing from the font: i̇̃ |                              |
|   The following auxiliary characters are missing from the font: ĩ |                              |
|   The following auxiliary characters are missing from the font: į́ |                              |
|   The following auxiliary characters are missing from the font: į̇́ |                              |
|   The following auxiliary characters are missing from the font: į̃ |                              |
|   The following auxiliary characters are missing from the font: į̇̃ |                              |
|   The following auxiliary characters are missing from the font: j̃ |                              |
|   The following auxiliary characters are missing from the font: j̇̃ |                              |
|   The following auxiliary characters are missing from the font: l̃ |                              |
|   The following auxiliary characters are missing from the font: m̃ |                              |
|   The following auxiliary characters are missing from the font: r̃ |                              |
|   The following auxiliary characters are missing from the font: ũ |                              |
|   The following auxiliary characters are missing from the font: ų́ |                              |
|   The following auxiliary characters are missing from the font: ų̃ |                              |
|   The following auxiliary characters are missing from the font: ū́ |                              |
|   The following auxiliary characters are missing from the font: ū̃ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: Ŭ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ŭ |                              |
|   The following auxiliary characters are missing from the font: ʻ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. (dotted_circle)</summary>
    <div>








- 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

* uni0BCD
* uni0B82
* uni0326 [code: unattached-dotted-circle-marks]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. (googlefonts/canonical_filename)</summary>
    <div>








- 🔥 **FAIL** Expected "AbhayaLibreDEVCANARY[wght].ttf". Got "AbhayaLibre[wght].ttf". [code: bad-filename]
  
  

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
    <summary>⚠️ <b>WARN</b> Check GDEF mark glyph class doesn't have characters that are not marks. (opentype/GDEF_non_mark_chars)</summary>
    <div>








- ⚠️ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:

* U+F6C3 (uni0326) [code: non-mark-chars]
  
  

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
width=492: logicalnot
width=462: less, greater
width=400: multiply [code: width-outliers]
  
  

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








- ⚠️ **WARN** Glyph "isign.alt4taml" has suspiciously high variation (z-score 15.41) in right sidebearings at locations:
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
* ttIsinh
* nyUtaml
* thUsinh
* pItaml
* uni0BE8 (U+0BE8)
* Imacron (U+012A)
* gDhasinh
* uni0DEC (U+0DEC)
* nThUusinh
* Tcaron (U+0164)
* lUusinh
* uni0B8E (U+0B8E)
* Q (U+0051)
* tThUsinh
* kIsinh
* nyjRasinh
* anusvarayaShIisinh
* jhRIisinh
* Ecaron (U+011A)
* kSsIsinh
* nnUtaml
* g (U+0067)
* six.tf
* ssIisinh
* uni0BAE (U+0BAE)
* kItaml
* zcaron (U+017E)
* jnyIisinh
* tIitaml
* ae (U+00E6)
* nyChsinh
* nTha_rephasinh
* jnysinh
* Abreve (U+0102)
* tIisinh
* nyCUsinh
* jnyae._csinh
* ddhUusinh
* nyae._csinh
* jhIisinh
* fRsinh.hist
* Amacron (U+0100)
* nine.tf
* ssUutaml
* kSssinh
* shRIsinh
* seven (U+0037)
* nyChUusinh
* jhUsinh
* nnddIisinh
* dvocalicr._csinh
* llAitaml
* Dcroat (U+0110)
* tVa_rephasinh
* nna_rephasinh
* jhRIsinh
* lUtaml
* nyChasinh
* Uacute (U+00DA)
* six (U+0036)
* asterisk (U+002A)
* aisigntaml.alt
* vUusinh
* Icircumflex (U+00CE)
* tVasinh
* lslash (U+0142)
* uni0157 (U+0157)
* anusvarayaShUusinh
* rUutaml
* nDha_rephasinh
* nVIsinh
* pIitaml
* jIsinh
* gDha_rephasinh
* yasign_uusignsinh
* uni0BC8 (U+0BC8)
* uni0123 (U+0123)
* nna2itaml
* ghUsinh
* nyja_rephasinh
* rrAataml
* oslash (U+00F8)
* dcroat (U+0111)
* nThIisinh
* fUusinh
* ddRIsinh
* ydieresis (U+00FF)
* Scaron (U+0160)
* nndda_rephasinh
* dhRIisinh
* sItaml
* jha_rephasinh
* cUtaml
* thsinh
* uni0BED (U+0BED)
* z (U+007A)
* fasinh.hist
* kSsItaml
* nDhUusinh
* uni0D90 (U+0D90)
* mItaml
* nDhUsinh
* threequarters (U+00BE)
* shItaml
* archaicthreesinh
* four.tf
* rAaesinh
* hRasinh
* ghUusinh
* tVUsinh
* cRIisinh
* kVsinh
* nda_rephasinh
* iisign.alttaml
* Ugrave (U+00D9)
* b (U+0062)
* e (U+0065)
* jRIsinh
* nItaml
* ssIsinh
* uni0BB0 (U+0BB0)
* ttUsinh
* sUtaml
* ocircumflex (U+00F4)
* tthIisinh
* ddUusinh
* aring (U+00E5)
* sRasinh
* caron (U+02C7)
* yasign_repha_uusignsinh
* partialdiff (U+2202)
* nUsinh
* jItaml
* nDasinh
* csinh
* gDhIsinh
* nIisinh
* Rcaron (U+0158)
* uni0BEE (U+0BEE)
* dyaa._csinh
* dRaa._csinh
* nnddsinh
* ndRasinh
* mRsinh
* ca_rephasinh
* uogonek (U+0173)
* emacron (U+0113)
* uni0DEA (U+0DEA)
* ra_rephasinh
* dyUu._csinh
* shsinh
* Acircumflex (U+00C2)
* uni2206 (U+2206)
* archaictensinh
* jhUusinh
* lItaml
* pUutaml
* jnyaae._csinh
* bUusinh
* hIsinh
* vItaml
* nyjRsinh
* vRsinh
* nUusinh
* tVUusinh
* nDae._csinh
* uni0156 (U+0156)
* daa_virama._csinh
* uni0163 (U+0163)
* uni0BEB (U+0BEB)
* Ccedilla (U+00C7)
* ttTthUusinh
* rUusinh
* nDUusinh
* T (U+0054)
* y (U+0079)
* uni0DAB (U+0DAB)
* uni0122 (U+0122)
* uni0BC2 (U+0BC2)
* nga_rephasinh
* vIisinh
* yUusinh
* eacute (U+00E9)
* ttRasinh
* Adieresis (U+00C4)
* plus (U+002B)
* iisign.alt1taml
* nyCa_rephasinh
* rUsinh
* dDhIisinh
* bRsinh
* Edieresis (U+00CB)
* uni0BD0 (U+0BD0)
* nnUutaml
* phIsinh
* uni0DA0 (U+0DA0)
* dhUsinh
* ddha_rephasinh
* uni0146 (U+0146)
* nDUsinh
* thIsinh
* yasign_viramasinh
* sinEight_Zerolith
* kVasinh
* llIisinh
* five.tf
* Edotaccent (U+0116)
* bRasinh
* ba_rephasinh
* anusvarayaShIsinh
* fi (U+FB01)
* khUsinh
* currency (U+00A4)
* uni0BB8 (U+0BB8)
* mRasinh
* nDhsinh
* gDhIisinh
* icircumflex (U+00EE)
* V (U+0056)
* nya_rephasinh
* shIsinh
* uni0DC3 (U+0DC3)
* nnddUsinh
* khRasinh
* uni0DA2 (U+0DA2)
* uni0BC6 (U+0BC6)
* eth (U+00F0)
* chIisinh
* oe (U+0153)
* thIisinh
* jnyUsinh
* ttRIisinh
* M (U+004D)
* nyaa_virama._csinh
* phUsinh
* ghRasinh
* uni0BB6 (U+0BB6)
* kUutaml
* f_f_l
* hUusinh
* uni0B86 (U+0B86)
* uni0BA8 (U+0BA8)
* fl (U+FB02)
* ssinh
* pRsinh
* khIisinh
* tRsinh
* uni0DA6 (U+0DA6)
* ghRsinh
* nDhasinh
* ssItaml
* dhRasinh
* bRIisinh
* Zcaron (U+017D)
* yasign_repha_usignsinh
* fRIisinh.hist
* ghIisinh
* dDhUsinh
* kVIsinh
* cIitaml
* nysinh
* Ydieresis (U+0178)
* bhsinh
* dyU._csinh
* zacute (U+017A)
* uni0B99 (U+0B99)
* dollar (U+0024)
* f_f
* amacron (U+0101)
* Uring (U+016E)
* kSsasinh
* nThasinh
* shRIisinh
* nyRsinh
* three.tf
* J (U+004A)
* hIitaml
* uni0BCA (U+0BCA)
* tUusinh
* Idieresis (U+00CF)
* germandbls (U+00DF)
* at (U+0040)
* uni0BA4 (U+0BA4)
* uni0BC0 (U+0BC0)
* nnsinh
* dVIsinh
* L (U+004C)
* Scedilla (U+015E)
* uni20BA (U+20BA)
* bBIsinh
* jRasinh
* nThIsinh
* ndsinh
* florin (U+0192)
* pi (U+03C0)
* bRIsinh
* khsinh
* cCa_rephasinh
* bha_rephasinh
* tsinh
* cRsinh
* yasign_iisignsinh
* tVIsinh
* uni0BAF (U+0BAF)
* ttha_rephasinh
* bhRsinh
* Igrave (U+00CC)
* abreve (U+0103)
* Euro (U+20AC)
* nnUusinh
* bIsinh
* ma_rephasinh
* uni0B8F (U+0B8F)
* infinity (U+221E)
* uni0DA3 (U+0DA3)
* dVsinh
* anusvarayaShsinh
* A (U+0041)
* F (U+0046)
* tVsinh
* bUsinh
* sinNine_Zerolith
* uni00B5 (U+00B5)
* nyIsinh
* fIisinh.hist
* kRasinh
* jUusinh
* uni0D9D (U+0D9D)
* acircumflex (U+00E2)
* yen (U+00A5)
* ttTthIisinh
* atilde (U+00E3)
* gUusinh
* uni0BE9 (U+0BE9)
* lIisinh
* tThsinh
* rIisinh
* nyCIisinh
* sUsinh
* na_rephasinh
* jnyRsinh
* la_rephasinh
* archaicfivesinh
* sRIisinh
* uni0BEC (U+0BEC)
* uni0BF6 (U+0BF6)
* ncaron (U+0148)
* Thorn (U+00DE)
* R (U+0052)
* q (U+0071)
* nThUsinh
* six.numr
* tTha_rephasinh
* uni0BF4 (U+0BF4)
* archaiconehundredsinh
* uni0DAC (U+0DAC)
* nDIsinh
* ssUsinh
* fUsinh
* uni0BB7 (U+0BB7)
* zdotaccent (U+017C)
* eight (U+0038)
* fa_rephasinh.hist
* jnyRasinh
* seven.numr
* nnAataml
* kSsa_rephasinh
* notequal (U+2260)
* archaicfiftysinh
* ccaron (U+010D)
* vIsinh
* jhRsinh
* hRIisinh
* vRasinh
* yUutaml
* da_yansa_oosignsinh
* mUsinh
* uni0DA4 (U+0DA4)
* sinThree_Zerolith
* egrave (U+00E8)
* fRsinh
* chIsinh
* chUusinh
* kha_rephasinh
* sRIsinh
* lUsinh
* cha_rephasinh
* nyCIsinh
* nVa_rephasinh
* nsinh
* nnIitaml
* ddhsinh
* uni0B8A (U+0B8A)
* uni2113 (U+2113)
* mIsinh
* jIitaml
* tThasinh
* pIsinh
* gRIisinh
* uni0145 (U+0145)
* jhsinh
* two.tf
* tcaron (U+0165)
* gha_rephasinh
* logicalnot (U+00AC)
* zhUutaml
* sinFour_Zerolith
* uni0D88 (U+0D88)
* ssRsinh
* gRasinh
* sIisinh
* rrUtaml
* ordfeminine (U+00AA)
* ddUsinh
* jnyaa._csinh
* dhRIsinh
* ka_rephasinh
* sa_rephasinh
* nna2uutaml
* archaiconethousandsinh
* pUusinh
* ampersand (U+0026)
* archaiceightsinh
* uni0B89 (U+0B89)
* nngUsinh
* uni0BF8 (U+0BF8)
* shRsinh
* nyIitaml
* tthsinh
* sinFive_Zerolith
* ttRsinh
* cRasinh
* Ocircumflex (U+00D4)
* W (U+0057)
* ddRIisinh
* ttUtaml
* uni0B9C (U+0B9C)
* khRIsinh
* a (U+0061)
* fRasinh
* ndaa._csinh
* t (U+0074)
* jUsinh
* bhRasinh
* ddIsinh
* uni0B93 (U+0B93)
* uni0BB2 (U+0BB2)
* I (U+0049)
* uni0DE9 (U+0DE9)
* jUtaml
* uni0B87 (U+0B87)
* n (U+006E)
* v (U+0076)
* nyCsinh
* nVsinh
* uni0BB1 (U+0BB1)
* uni2126 (U+2126)
* lIsinh
* kVUsinh
* tthIsinh
* bBasinh
* vUutaml
* jnyRIsinh
* uni0B85 (U+0B85)
* ndIsinh
* Eogonek (U+0118)
* nyRIsinh
* kSsUtaml
* kSsIitaml
* nngUusinh
* uni0BCB (U+0BCB)
* lAitaml
* uni0BA9 (U+0BA9)
* nnddUusinh
* gDhUusinh
* kUsinh
* mbUsinh
* rsinh
* ucircumflex (U+00FB)
* ttTthUsinh
* nDaa._csinh
* nUutaml
* nngIisinh
* nnItaml
* r (U+0072)
* ssUtaml
* cRIsinh
* uni00B3 (U+00B3)
* cCIisinh
* tItaml
* nine (U+0039)
* uni0D86 (U+0D86)
* kSsUutaml
* llsinh
* dUsinh
* fsinh
* nDIisinh
* phIisinh
* section (U+00A7)
* Dcaron (U+010E)
* B (U+0042)
* sIsinh
* bhUsinh
* rIitaml
* chsinh
* nIsinh
* nyCUusinh
* four.numr
* gDhUsinh
* cIsinh
* asciicircum (U+005E)
* nThsinh
* kRIisinh
* nnAitaml
* vUsinh
* ttTthsinh
* k (U+006B)
* sterling (U+00A3)
* jnyRIisinh
* vocalicllsignsinh
* uni021B (U+021B)
* kIitaml
* sinOne_Zerolith
* uni0BB4 (U+0BB4)
* shUusinh
* ksinh
* cCUusinh
* llIsinh
* Idotaccent (U+0130)
* ttTtha_rephasinh
* ddhIsinh
* va_rephasinh
* llUusinh
* archaicseventysinh
* nDRIsinh
* nDhIisinh
* dVa_rephasinh
* dagger (U+2020)
* kVIisinh
* uni0B94 (U+0B94)
* mIisinh
* archaicninetysinh
* Udieresis (U+00DC)
* Lacute (U+0139)
* tRasinh
* tta_rephasinh
* E (U+0045)
* three.numr
* nngIsinh
* nyRasinh
* uni0BA3 (U+0BA3)
* dvocalicrr._csinh
* ndaa_virama._csinh
* ddsinh
* dDha_rephasinh
* ghRIsinh
* archaiceightysinh
* ngItaml
* rrItaml
* shRasinh
* uni0BF9 (U+0BF9)
* ngUutaml
* numbersign (U+0023)
* nyaa._csinh
* nyjUsinh
* tIsinh
* dha_rephasinh
* nyUsinh
* kVa_rephasinh
* summation (U+2211)
* ssRIsinh
* ttTthIsinh
* ssUusinh
* hRsinh
* llIitaml
* vIitaml
* fUsinh.hist
* yIitaml
* ecaron (U+011B)
* hIisinh
* kSsUusinh
* ndUusinh
* nDRasinh
* mbIisinh
* uni0BF1 (U+0BF1)
* archaicsixtysinh
* Ucircumflex (U+00DB)
* edieresis (U+00EB)
* uni0BD7 (U+0BD7)
* circumflex (U+02C6)
* Lslash (U+0141)
* tthUusinh
* nyCasinh
* jUutaml
* nyjsinh
* rrIitaml
* two (U+0032)
* radical (U+221A)
* four (U+0034)
* OE (U+0152)
* dVasinh
* khRsinh
* mRIisinh
* fRIsinh
* nyjIsinh
* tVIisinh
* sIitaml
* fIsinh.hist
* ttIisinh
* jnyIsinh
* ddhIisinh
* Agrave (U+00C0)
* uni0D93 (U+0D93)
* fIsinh
* nyChIsinh
* Uhungarumlaut (U+0170)
* cCsinh
* nyUusinh
* yacute (U+00FD)
* nna2aataml
* Aogonek (U+0104)
* P (U+0050)
* tthUsinh
* seven.tf
* nna2aitaml
* ntilde (U+00F1)
* kIisinh
* nyItaml
* ssIitaml
* aacute (U+00E1)
* uni00B2 (U+00B2)
* nyChUsinh
* plusminus (U+00B1)
* uni0137 (U+0137)
* rItaml
* uni0DB7 (U+0DB7)
* Umacron (U+016A)
* sinTwo_Zerolith
* khUusinh
* ngIitaml
* sinSix_Zerolith
* nDRIisinh
* shIitaml
* nIitaml
* Ncaron (U+0147)
* nVasinh
* dVIisinh
* D (U+0044)
* uni0D8F (U+0D8F)
* greater (U+003E)
* jRIisinh
* mRIsinh
* tRIisinh
* ddRsinh
* ndae._csinh
* yItaml
* Iogonek (U+012E)
* ttIitaml
* agrave (U+00E0)
* Y (U+0059)
* uni0DE6 (U+0DE6)
* five.numr
* dda_rephasinh
* eight.tf
* archaictwentysinh
* uni0D9F (U+0D9F)
* five (U+0035)
* nyIisinh
* nine.numr
* nngsinh
* AE (U+00C6)
* ddIisinh
* iogonek (U+012F)
* rcaron (U+0159)
* eight.numr
* tRIsinh
* sinSeven_Zerolith
* uni0DB3 (U+0DB3)
* lsinh
* tUutaml
* fIisinh
* rAesinh
* ssa_rephasinh
* llItaml
* kVUusinh
* mbIsinh
* bBa_rephasinh
* lla_rephasinh
* archaicfortysinh
* phsinh
* fRasinh.hist
* uni0BF5 (U+0BF5)
* uni013B (U+013B)
* ndIisinh
* d (U+0064)
* gRsinh
* uni0DA5 (U+0DA5)
* cCIsinh
* ghIsinh
* dhUusinh
* dVUusinh
* bhIisinh
* tThUusinh
* dIsinh
* uni0BCC (U+0BCC)
* uni0B90 (U+0B90)
* racute (U+0155)
* gbreve (U+011F)
* ndRaa._csinh
* tUsinh
* nUtaml
* gDhsinh
* uni0D87 (U+0D87)
* X (U+0058)
* cUusinh
* U (U+0055)
* Egrave (U+00C8)
* jIisinh
* h (U+0068)
* Aring (U+00C5)
* sssinh
* nDhIsinh
* uni0BE7 (U+0BE7)
* archaicthirtysinh
* eogonek (U+0119)
* nVIisinh
* bhRIsinh
* onehalf (U+00BD)
* mUutaml
* bIisinh
* sUusinh
* jhIsinh
* uni0BB5 (U+0BB5)
* dRsinh
* archaicsevensinh
* rUtaml
* ttsinh
* uni0B95 (U+0B95)
* jnya_rephasinh
* uni0BB3 (U+0BB3)
* uni0BEF (U+0BEF)
* yasign_isignsinh
* uni0BC7 (U+0BC7)
* zhItaml
* Ccaron (U+010C)
* uni0D95 (U+0D95)
* two.numr
* bhUusinh
* shreetaml
* llUsinh
* nDsinh
* uni0BB9 (U+0BB9)
* archaicsixsinh
* ndUsinh
* archaicfoursinh
* nnga_rephasinh
* fRIsinh.hist
* msinh
* rIsinh
* kSsataml
* khRIisinh
* cIisinh
* khIsinh
* shUsinh
* vRIisinh
* uni0DEF (U+0DEF)
* onequarter (U+00BC)
* pIisinh
* nyUutaml
* Emacron (U+0112)
* x (U+0078)
* edotaccent (U+0117)
* jhRasinh
* Gbreve (U+011E)
* gRIsinh
* uni0DC5 (U+0DC5)
* jnyaa_virama._csinh
* zhIitaml
* pUsinh
* Ecircumflex (U+00CA)
* hUsinh
* uni0BF0 (U+0BF0)
* cUutaml
* dRIisinh
* Eacute (U+00C9)
* G (U+0047)
* uni0D85 (U+0D85)
* dRasinh
* fRIisinh
* thUusinh
* greaterequal (U+2265)
* kSsUsinh
* dDhsinh
* ysinh
* jnyUusinh
* ja_rephasinh
* mba_rephasinh
* ndaae._csinh
* tThIsinh
* hUutaml
* lUutaml
* aogonek (U+0105)
* ttRIsinh
* dDhUusinh
* dsinh
* dDhasinh
* dya._csinh
* Aacute (U+00C1)
* N (U+004E)
* archaiconesinh
* bhIsinh
* tUtaml
* dUusinh
* uni0DDD (U+0DDD)
* scaron (U+0161)
* ssRasinh
* nyjUusinh
* ddhUsinh
* nVUsinh
* fUusinh.hist
* lessequal (U+2264)
* nyjIisinh
* pRIisinh
* daggerdbl (U+2021)
* uni0162 (U+0162)
* gIsinh
* ghsinh
* cent (U+00A2)
* cUsinh
* cCUsinh
* Lcaron (U+013D)
* dVUsinh
* three (U+0033)
* aasign_viramasinh
* shIisinh
* yIsinh
* dDhIsinh
* yUsinh
* ccedilla (U+00E7)
* nnddIsinh
* nyCha_rephasinh
* mUusinh
* zhUtaml
* uni0DE8 (U+0DE8)
* nyaae._csinh
* nDa_rephasinh
* m (U+006D)
* uni0B9A (U+0B9A)
* nyChIisinh
* uni0D92 (U+0D92)
* uni0B9E (U+0B9E)
* uni0D91 (U+0D91)
* ttTthasinh
* pRIsinh
* anusvarayaShUsinh
* trademark (U+2122)
* lIitaml
* uni0DC2 (U+0DC2)
* jRsinh
* chUsinh
* Yacute (U+00DD)
* dcaron (U+010F)
* nnIsinh
* yIisinh
* nna2utaml
* Ntilde (U+00D1)
* Oslash (U+00D8)
* paragraph (U+00B6)
* Eth (U+00D0)
* multiply (U+00D7)
* Racute (U+0154)
* pRasinh
* yasign_usignsinh
* product (U+220F)
* bBUsinh
* ssRIisinh
* Iacute (U+00CD)
* tThIisinh
* K (U+004B)
* uni0BF3 (U+0BF3)
* cItaml
* uni0BF2 (U+0BF2)
* ghRIisinh
* uni0D9A (U+0D9A)
* bhRIisinh
* uni0136 (U+0136)
* fsinh.hist
* nna2iitaml
* kRsinh
* w (U+0077)
* ttItaml
* llUutaml
* mIitaml
* nyRIisinh
* nDaae._csinh
* Atilde (U+00C3)
* dhRsinh
* kUtaml
* uni021A (U+021A)
* kSsIisinh
* nnIisinh
* bBUusinh
* mUtaml
* uni0DA1 (U+0DA1)
* hUtaml
* H (U+0048)
* ngIisinh
* ngIsinh
* ttUusinh
* nacute (U+0144)
* gsinh
* anusvarayaShasinh
* hsinh
* gUsinh
* dRIsinh
* hItaml
* ddRasinh
* f (U+0066)
* ecircumflex (U+00EA)
* adieresis (U+00E4)
* kRIsinh
* uni0BEA (U+0BEA)
* jsinh
* hRIsinh
* f_f_i
* mbUusinh
* rrUutaml
* vRIsinh
* ngsinh
* nnUsinh
* bBsinh
* uni0B92 (U+0B92)
* ttUutaml
* dIisinh
* kUusinh
* nDaa_virama._csinh
* uni0BF7 (U+0BF7)
* llUtaml
* Uogonek (U+0172)
* psinh
* uni20BD (U+20BD)
* Nacute (U+0143)
* less (U+003C)
* phUusinh
* nVUusinh
* bBIisinh
* sRsinh [code: no-overlaps-bit]
  
  

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
* eight.tf has a counter-clockwise outer contour
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
* two (U+0032): Line(Line { p0: (30.0, 20.0), p1: (80.0, 70.0) }) has the same coordinates as a previous segment.
* three (U+0033): Line(Line { p0: (171.0, 233.0), p1: (149.0, 251.0) }) has the same coordinates as a previous segment.
* three (U+0033): Line(Line { p0: (427.0, 510.0), p1: (330.0, 460.0) }) has the same coordinates as a previous segment.
* two.tf: Line(Line { p0: (35.0, 20.0), p1: (89.0, 68.0) }) has the same coordinates as a previous segment.
* three.tf: Line(Line { p0: (171.0, 303.0), p1: (149.0, 321.0) }) has the same coordinates as a previous segment.
* three.tf: Line(Line { p0: (427.0, 580.0), p1: (330.0, 530.0) }) has the same coordinates as a previous segment.
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
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'MNIK' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[2] fonts/variable</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. (googlefonts/glyph_coverage)</summary>
    <div>








- 🔥 **FAIL** fonts/variable/AbhayaLibre[wght].ttf missing required codepoints:

* 0x010A: LATIN CAPITAL LETTER C WITH DOT ABOVE
* 0x010B: LATIN SMALL LETTER C WITH DOT ABOVE
* 0x0120: LATIN CAPITAL LETTER G WITH DOT ABOVE
* 0x0121: LATIN SMALL LETTER G WITH DOT ABOVE
* 0x0126: LATIN CAPITAL LETTER H WITH STROKE
* 0x0127: LATIN SMALL LETTER H WITH STROKE
* 0x0174: LATIN CAPITAL LETTER W WITH CIRCUMFLEX
* 0x0175: LATIN SMALL LETTER W WITH CIRCUMFLEX
* 0x0176: LATIN CAPITAL LETTER Y WITH CIRCUMFLEX
* 0x0177: LATIN SMALL LETTER Y WITH CIRCUMFLEX
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x0300: COMBINING GRAVE ACCENT
* 0x0301: COMBINING ACUTE ACCENT
* 0x0302: COMBINING CIRCUMFLEX ACCENT
* 0x0303: COMBINING TILDE
* 0x0304: COMBINING MACRON
* 0x0306: COMBINING BREVE
* 0x0307: COMBINING DOT ABOVE
* 0x0308: COMBINING DIAERESIS
* 0x030A: COMBINING RING ABOVE
* 0x030B: COMBINING DOUBLE ACUTE ACCENT
* 0x030C: COMBINING CARON
* 0x0326: COMBINING COMMA BELOW
* 0x0327: COMBINING CEDILLA
* 0x0328: COMBINING OGONEK
* 0x1E80: LATIN CAPITAL LETTER W WITH GRAVE
* 0x1E81: LATIN SMALL LETTER W WITH GRAVE
* 0x1E82: LATIN CAPITAL LETTER W WITH ACUTE
* 0x1E83: LATIN SMALL LETTER W WITH ACUTE
* 0x1E84: LATIN CAPITAL LETTER W WITH DIAERESIS
* 0x1E85: LATIN SMALL LETTER W WITH DIAERESIS
* 0x1E9E: LATIN CAPITAL LETTER SHARP S
* 0x1EF2: LATIN CAPITAL LETTER Y WITH GRAVE
* 0x1EF3: LATIN SMALL LETTER Y WITH GRAVE [code: missing-codepoints]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** fonts/variable/AbhayaLibre[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi
* U+2010 HYPHEN: try adding one of: hebrew, cham, kharoshthi, coptic, armenian, kaithi, kayah-li, lisu, sora-sompeng, sundanese, syloti-nagri, yi, arabic
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2126 OHM SIGN: try adding math
* U+212E ESTIMATED SYMBOL: try adding math
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham
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






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 8 | 20 | 13 | 114 | 62 | 
| 4% | 9% | 6% | 53% | 29% | 



