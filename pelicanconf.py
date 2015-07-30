#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Efficient Era'
SITENAME = u'Efficient Era'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('BOOK OF FACES!', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Menu
MENUITEMS = (('Blog', '/blog'),)
MENUITEMS_RIGHT = (('Register', 'https://efficientera.com/register/'),
                   ('Log In', 'https://efficientera.com/login/'),)

# Post Settings
DEFAULT_DATE = 'fs'

# Paths
PATH = 'content'
STATIC_PATHS = ['blog', 'images', 'pages']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
INDEX_SAVE_AS = 'blog.html'
TEMPLATE_PAGES = {'templates/index.html': 'index.html'}

# Theme
THEME = "themes/bootstrap3"
BOOTSTRAP_THEME = 'paper'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Plugins
PLUGIN_PATHS = ["plugins", "plugins"]
PLUGINS = []
