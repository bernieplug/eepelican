#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Efficient Era'
SITENAME = u'Efficient Era'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
MENUITEMS = (('Blog', '/index.html'),
             ('Support', '/support.html'),
             ('About', '/about.html'))
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/bootstrap'
BOOTSTRAP_THEME = 'yeti'

# custom page generated with a jinja2 template
DIRECT_TEMPLATES = ('index', 'categories', 'authors',
                    'archives', 'home', 'about',
                    'support', 'sign-up', 'customer-reviews',
                    'tax', 'seller-feedback', 'products',
                    'pricing-table')
