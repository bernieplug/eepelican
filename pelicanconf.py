#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import environ

AUTHOR = u'Efficient Era'
SITENAME = u'Efficient Era'

if 'ONLOCAL' in environ:
    SITEURL = 'http://127.0.0.1:8000'
else:
    SITEURL = 'https://efficientera.com'
    DISQUS_SITENAME = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Menu
MENUITEMS = (('Blog', '/blog'),
             ('Support', '/support'),)
MENUITEMS_RIGHT = (('Log In', 'https://efficientera.com/login/'),
                   ('Register', 'https://efficientera.com/register/'),)

# Post Settings
DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'

# Paths
PATH = 'content'
STATIC_PATHS = ['blog', 'images', 'pages']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%b}/{slug}.html'
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
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# Plugins
PLUGIN_PATHS = ["plugins", "plugins"]
PLUGINS = []
