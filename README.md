
අභය ලිබ්රේ අකුරු මුහුණත / Abhaya Libre Font
==============

Abhaya Libre - is the unicode compliant, complete libre version of FM Abhaya font. 
Designed by Pushpanada Ekanayake with Sol Matas.

එෆ් එම් අභය අකුරු මුහුණතේ යුනිකේත අනුකූල නිදහස් නිකුතුව.


See the discussions on [Googel Fonts mailing list ](https://groups.google.com/d/topic/googlefonts-discuss/ET5kBjYxDiY/discussion)
See the [video discussions](https://www.youtube.com/playlist?list=PLpw12zH02-An-6i79877NUi_ld3U_4tmv)

Now use on your website from [Google Fonts](https://fonts.google.com/specimen/Abhaya+Libre)

##

At the present, ‘FM Abhaya’ designed in 1996, is the most widely used Sinhala typeface in all around contexts. FM Abhaya is an interpretation of the earliest Sinhala letterpress typefaces. The name ‘Abhaya’ comes after the King Abhaya (474 BCE to 454 BCE) who reigned Sri Lanka from the ancient kingdom of Upatissa Nuwara. The ‘Abhaya Libre’ is the Unicode compliant, complete libre version of the most popular Sinhala typeface on Earth.

In the Unicode adaptation process, the FM Abhaya font was completely redrawn from the scratch to suit the modern usages in Web, Tab and smaller sizes for Smartphones. Abhaya Libre comes in 5 weights which enables designers to build sophisticated typographic layouts. Lighter weights suites mostly for body text and heavier weights do best in title settings.

Each of those weights contains 925 glyphs that enables clean and precise rendering for Sinhala, Pali and Sanskrit texts. The Custom compact ‘Da’ forms can be enabled using stylistic sets.

It comes with a Latin set designed by Sol Matas to match the aesthetics of Abhaya Libre Sinhala. The Latin set was inspired by the style of the original Sinhala, with the notable inherent contrast in between thick and thin strokes, was modified to tally with the visualization logics of Latin typefaces. The ductus references according to the lines of a Didone typeface add some Sinhala forms to certain terminations.

After several tests and discussions we agreed on the height for uppercase and lowercase to match harmoniously with Sinhala. The width of each character and its position on the baseline have been carefully designed to get a nice balance between both writing systems. Adding large counters for optimizing on screen viewing and small ascenders and descenders.

The project was funded by Google, being led by Mooniak, a collaborative collective of designers based in Colombo Sri Lanka with the cooperation of Mr. Pushpananda Ekanayake, the designer  of the FM Abhaya font and Sol Matas as the Latin designer.


## Repository Structure

- See [Realases](https://github.com/mooniak/abhaya-libre-font/releases) to Download released clean font versions, sources and specimens at the relase point.

- See `/fonts` in `gh-pages` branch contains draft fonts which are dirty, generated for design testing.
- See `/sources/` contains dirty and incomplete `.ufo` files which opens in all major font editors. These files are generated in intervals in between development. See [Realases](https://github.com/mooniak/abhaya-libre-font/releases) for clean sources.
- See `/sources/sfd` contains source `.sfd` files which opens in [FontForge](http://fontforge.github.io/en-US/). These files are under active developemnt.
- See `/sources/glyphs` contains source `.glyphs` files which opens in [Glyphs](https://glyphsapp.com/). These files are under active developemnt.

## How To Build 

If you want your way around fonts and terminal, you can use our build system to fonts.To generate fonts we use a virtual enviromant created with Vagrant. See [WeliPilla](https://github.com/mooniak/WeliPilla) for more info.

Once you have Welipilla set up, do the following..

- Run Vagrant box, this will take a few minuits to set up the build enviroment.

```shell
$vagrant up
```

- SSH into vagrant box.(Use putty on Windows)
```shell
$vagrant ssh
```

- Run builder script.
```shell
$cd /vagrant/scripts && sh builder.sh
```


## Credits

See `FONTLOG.md` for details on contributions.

- Pushpanada Ekanayake (Sinhala)
- Sol Matas(Latin)
- Pathum Egodawatta (Refactoring and Project coordination)
- Ayantha Randika (Opentype features and engineering)
- Kosala Senvirathne (Documentation)


Special thanks to Dave Crossland, Sumantri Samarawickrama, Liang Hai for consultancy and support. And thanks to all the tweeps who helped to spot errors and bugs.



## License

Abhaya Libre font is released under the  [SIL Open Font License](http://scripts.sil.org/OFL)

For information on what you're allowed to change or modify, consult the
OFL-1.1.txt and OFL-FAQ.txt files. The OFL-FAQ also gives a very general
rationale and various recommendations regarding why you would want to
contribute to the project or make your own version of the font.


