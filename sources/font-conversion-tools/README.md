Converting FM fonts to Unicode
=============================

<This was originally published (here)[http://pathnirvana.org/custom/unicode_tools/create_unicode.htm]>

You can convert any Sinhala FM Font to the corresponding Sinhala unicode font by following the set of steps outlined here.

Two FM fonts that we have converted to Unicode using this method are listed below

UN-Abhaya (Unicode equivalent of FM Abahaya font)
UN-Abhaya-Bold (Unicode equivalent of FM AbaBld font - bold version of FM Abhaya)
Someone has converted the rest of FM fonts using the instructions below and posted them online. You can download them here
Steps (You need some knowledge about fonts to follow these steps)

Download and install the required software Fontlab Studio and Microsoft VOLT
Open the FM font you want to convert (e.g. FMMalithi.ttf) and the potha.ttf file in Fontlab. Change the Font Info of 'potha.ttf' to the new Font (e.g. UN-Malithi)
Open the create_glyphs_unicode.py macro in the Fontlab and change the font names at the beginning of the macro (e.g. to FMMalithi and UN-Malithi)
Delete all glyphs from the 'potha.ttf' except for the last 5 glyphs and run the macro.
Some Glyphs are missing and they are marked in red. Create these glyphs by copying over the parts from other glyphs. You can use UN-Abhaya.ttf in Fontlab and use it as an example for this step. Expect to spend at least 15 minutes on this step.
Use "File->Generate Font" in Fontlab to save the font in ttf format (e.g. UN-Malithi.ttf)
Open this font in MS VOLT, then choose "Import Project" and select volt_project.vtp file.
Click "Compile" in MS VOLT (there shouldn't be any errors), then select "Ship Font" from the menu to save the final Sinhala unicode font.
Install this new unicode font. Enjoy!
