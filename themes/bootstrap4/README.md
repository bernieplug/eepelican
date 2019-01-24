# bootstrap4 #

This was inspired by the [Bootstrap theme](https://github.com/pelican-themes/bootstrap), by [getpelican](https://github.com/getpelican).

Relies on bootstrap, Jquery and dependent libraries.


## contents ##

- changelog
- features
    + translations
    + general
    + optional settings
    + custom color scheme
- contributing to translations
- screenshots


## changelog ##

12/14/2018
- *New Beta, for sites using the i18n plugin.*

11/12/2018
- *Changed default color scheme, preparation for next release.*
- *removed custom social icons. Using icons through font-awesome.*

11/11/2018
- *Preparing new version, 'vanilla', to have no SCSS or webassets requirements.*
- *Fixed bug with loading sidebars and menus.*
- *removed snippets and card-image CSS classes, as existing bootstrap classes make these redundant.*

10/13/2018
- *Updated to use webassets, and SCSS*

09/21/2018
- *Updated to Bootstrap 4.1.3.*
- *Changing behaviour to not need as many pelicanconf.py variables, and no custom colours.*

06/10/2018
- *Updated to Bootstrap 4.1.1.*

02/20/2018:
- *Updated to Bootstrap 4.0.0.*

12/20/2017:
- *Added capability to override color scheme.*

12/11/2017:

- *Working when optional settings are missing.*
- *New options to place category, tag, author and blogroll menus in navbar.*
- *Social media now only icons on footer.*

11/29/2017:

- *Check and Test against mock site, preparation for beta.*
- *Test behaviour if new optional settings are missing.*

11/03/2017:

- *Updated to Bootstrap v4.0.0.beta.2.*
- *Moved sidebar to right.*
- *Broke sidebar into sections: blogroll, social media links, and optional authors, categories, and tags.*
- *Archives moved to top navigation menu, far right*
- *no categories, authors or tags pages used, no such pages listed in top navigation menu*
- *Replaced home link in top navigation menu with image link to home page.*
- *added arias for accessibility and screen readers.*
- *added social icons for links referring meetup.com, anaconda.org and instagram.com. Updated reference for del.icio.us*


## features ##

### translations ###

Releases marked *i18n* are designed for use with the i18n (localisation) plugin. 

The default language is English.

Currently supported languages are (code, language):

|code | language         |
|-----|------------------|
|es   | Spanish, Español |


### general ###

- In most cases, the default behaviour of the bootstrap 4 theme has been followed. Differences are in font weight of lead paragraphs, and appearance of nav and metadata links.
- Additionally the theme should be reasonably accessible for the visually impaired and for screen readers.
- if an image `home.png` is placed in the content/images directory, it will be used as the navbar logo and home button.
- background images can be shown. These backgrounds use the filenames `background-lg.png`, `background-md.png`, `background-sm.png`, `background-xs.png` in the content/images directory. The breakpoint widths of each are, respectively: above 1800px, 1800px - 800px, 800px - 520px, and under 520px. 
- The archives are always available in the top menu.
- Blogroll, Social Links, Categories, Tags and Authors can be shown in the top menu, sidebar, or both.
- Social media links can have associated icons. visit [font-awesome](fontawesome.com) and look up the brand icons, to see if an icon is available for your preferred platforms.


### optional settings ###

Your pelican settings file may use the following additional settings (default values are shown):

`SITE_DESCRIPTION = ''`, for the description meta tag.

`SHOW_AUTHORS = False`, If categories are to be shown in the sidebar.
`DISPLAY_AUTHORS_ON_MENU = False`, put a link to the authors index page in the menu.
Note that if all articles only ever have one author, an Author sidebar will never be shown anyway.

`SHOW_CATEGORIES = False`, If categories are to be shown in the sidebar.
`DISPLAY_CATEGORIES_ON_MENU = False`, put a link to the categories index page in the menu.

`SHOW_TAGS = False`, If tags are to be shown in the sidebar.
`DISPLAY_TAGS_ON_MENU = False`, put a link to the tags index page in the menu.

`SHOW_BLOGROLL = False`, If Blogroll links are to be shown in the sidebar.
`DISPLAY_BLOGROLL_ON_MENU = False`, show a dropdown menu with blogroll links.

`SHOW_SOCIAL = False`, If Blogroll links are to be shown in the sidebar.
`DISPLAY_SOCIAL_ON_MENU = False`, show a dropdown menu with blogroll links.
`SOCIAL_FOOTER = False`, show social media links in the footer. Only items with a third (font-awesome) field will be shown (see `SOCIAL` below).

Additionally, the `SOCIAL` setting may list social media items with a third field, the class of a font-awesome brand icon. For example:
```
SOCIAL = (
    ('Facebook', 'facebook.com/username/'),
    ('Twitter', 'twitter.com/user/', 'fa-twitter'),
)
```

Will show Links to facebook and twitter accounts, but only the twitter account will show an icon next to it.


## Custom Color Scheme ##

It is possible to change some of the default color scheme. 

The base template loads the default CSS, then looks for a file at `theme/colors.css` which can redefine the
color scheme.

The following CSS variables are used in `:root` to define colors:

`--main-background`,
`--general-background`,
`--general-border-color`,
`--bright-foreground`,
`--link-color`,
`--link-hover-color`,
`--pre-color`,
`--code-color`,
`--table-color`,

When redefining the color scheme, the `STATIC_PATHS` and `EXTRA_PATH_METADATA` options will need to be updated. For example:

```
STATIC_PATHS = [ 'extras/colors.css', 'images' ]

EXTRA_PATH_METADATA = {
    'extras/colors.css':  {'path': 'theme/colors.css'},
}
```

Assuming your custom scheme is at the file `contents/extras/colors.css`, this tells Pelican to look for it as a static file, then copy it into the output website at `theme/colors.css`, which the base template will recognise and load accordingly.


### contributing to translations ###

Volunteer contributions are welcome. To contribute:

1. Prepare a virtual environment with babel installed.
1. Download and unzip this theme.
1. Open a terminal, and activate the virtual environment. Change directory to the root directory of the theme. You should be in the same directory as the `messages.pot` file.
1. In the `translations` directory, check for the language code of the language you want to translate to. If there is no directory for this language code, no translations for this language have been created yet.
1. Preparing or finding translations:
    1. For new translations, run the command `pybabel init --input-file messages.pot --output-dir translations/ --locale <code> --domain messages` where `<code>` is the language code you are working on. A new language code directory will be created. OR
    1. For existing translations, go to the language code directory of the language you are editing.
1. In the `LC_MESSAGES` directory, edit the `messages.po` file to make the translations. Comments and `msgid` strings should be left alone. `msgstr` strings should be changed to a suitable translation.
1. Finally, send me the `messages.po` file, and the language and language code. I will compile and update the content when i have time.


## Screenshots ##

![screenshot 1](screenshot1.png)
![screenshot 2](screenshot2.png)
![screenshot 3](screenshot3.png)
![screenshot 4](screenshot4.png)
