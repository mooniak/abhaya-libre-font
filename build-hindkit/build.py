#! /usr/bin/env python

import hindkit as kit
kit.confirm_version('0.1.3')

# - - -

family = kit.Family(
    trademark = 'Abhaya Libre',
    script = 'Sinhala',
    hide_script_name = True,
)

family.set_masters(
    modules = [
        # 'kerning',
        # 'mark_positioning',
        # 'mark_to_mark_positioning',
        # 'devanagari_matra_i_variants',
    ],
)
family.masters[0]._file_name = 'AbhayaLibre-Regular.ufo'
family.masters[1]._file_name = 'AbhayaLibre-ExtraBold.ufo'

family.set_styles([
    ('Regular',     0.0, 400),
    ('Medium',     18.6, 500),
    ('SemiBold',   41.3, 600),
    ('Bold',       67.9, 700),
    ('ExtraBold', 100.0, 800),
])

# - - -

family.output_name_affix = '{} FDK'

# - - -

builder = kit.Builder(family)

builder.fontrevision = '0.100'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    'makeinstances', #!
    'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])

builder.generate_designspace()
builder.generate_fmndb()

builder.build()
