{
    'name': 'Hello PageCrafter Theme',
    'version': '19.0.1.0.0',
    'summary': 'Minimalist Theme for PageCrafter',
    'description': """
Hello PageCrafter Theme
=======================

A clean, minimalist theme designed specifically for use with PageCrafter.
Inspired by "Hello Elementor" for WordPress, this theme provides a blank
canvas that lets PageCrafter's builder shine without theme conflicts.

Features:
---------
* Minimal, lightweight styling
* Clean base for PageCrafter designs
* Optimized for page builder workflow
* Responsive foundation
* No conflicting styles

This theme works best when used with the PageCrafter module.
    """,
    'category': 'Theme',
    'author': 'Ata Khadivi',
    'website': 'https://github.com/atakhadivi/Hello_PageCrafter',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'pagecrafter',
    ],
    'data': [
        'views/layout.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hello_pagecrafter/static/src/scss/main.scss',
        ],
    },
    'application': True,
    'auto_install': False,
    'installable': True,
}
