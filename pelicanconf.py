#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import environ

AUTHOR = u'Efficient Era'
SITENAME = u'Efficient Era'
SITEURL = 'http://127.0.0.1:8080'
#SITEURL = 'https://efficientera.com'
OPEN_GRAPH_IMAGE ='images/pages/dashboard.png'

# URLS
TAGS_URL = 'tags'
CATEGORIES_URL = 'categories'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DIRECT_TEMPLATES = ['categories', 'index', 'archives', 'authors', 'tags', 'search', 'sitemap']

GOOGLE_ANALYTICS = 'UA-73097851-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Menu
MENUITEMS_RIGHT = (
                    ('Features', '/features/'),
                    ('Pricing', '/pricing/'),
                    ('Blog', '/blog/'),
                    ('Clients', '/clients/'),
                    ('Resources', '/resources/'),
                    ('Support', '/support/'),
                    ('Affiliate', '/pages/affiliate')
                   )
# Removed:  ('About', '/about/')

# Post Settings
DEFAULT_PAGINATION = 8
DEFAULT_DATE = 'fs'

# Share Buttons
ADDTHIS_PROFILE = 'ra-53cd839229a71296'
# SHARIFF = True
# SHARIFF_LANG = 'en'
# SHARIFF_THEME = 'grey'
# TWITTER_USERNAME = ''
# SHARIFF_TWITTER_VIA = True

# Paths
PATH = 'content'
STATIC_PATHS = ['blog', 'images', 'pages']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'
TEMPLATE_PAGES = {
    'templates/google96a16df7dbeb77e9.html': 'google96a16df7dbeb77e9.html',
    'templates/flywheels.html': 'flywheels.html',
    'templates/index.html': 'index.html',
    'templates/atlassian-domain-verification.html': 'atlassian-domain-verification.html',
}
SITEMAP_SAVE_AS = 'sitemap.xml'

# Theme
THEME = "themes/bootstrap3"
BOOTSTRAP_THEME = 'effera'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = True
SHOW_TAGS = True
DISPLAY_SUMMARY = True
SUMMARY_MAX_LENGTH = 25
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
SITELOGO = 'images/logo_name.png'
SITELOGO_SIZE = '140px'
HIDE_SITENAME = True
FAVICON = 'images/logo_e.png'
BACK_TO_TOP = False

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["thumbnailer", "tipue_search", "i18n_subsites"]

# Thumbnailer
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images/thumbnails/'
THUMBNAIL_SIZES = {'small': '250x?',
                   'medium': '500x?',
                   'large': '800x?'}

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
