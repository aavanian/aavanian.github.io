#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# While developping:
LOAD_CONTENT_CACHE = False

AUTHOR = 'Alexandre Avanian'
SITENAME = '@/dev/null'
SITEURL = 'http://aavanian.github.io'

# Possibly useful to set as true but need more thinking
USE_FOLDER_AS_CATEGORY = False
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'en'
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'

THEME = 'alchemy'
# Alchemy theme configuration
EXTRA_FAVICON = ''
LICENSE_NAME = ''
LICENCE_URL = ''
MENU_ITEMS = {}
META_DESCRIPTION = ''
PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True
ARCHIVES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
PROFILE_IMAGE = ''
SHOW_ARTICLE_AUTHOR = False
SITE_SUBTEXT = 'Random rants & thoughts'

EMAIL_ADDRESS = 'alexandre.avanian@gmail.com'
FB_ADDRESS = ''
GITHUB_ADDRESS = 'https://www.github.com/aavanian'
SO_ADDRESS = ''
TWITTER_ADDRESS = 'http://www.twitter.com/aavanian'

DISQUS_SITENAME = ''
GOOGLE_ANALYTICS_DOMAIN = ''
GOOGLE_ANALYTICS_ID = ''

NOTEBOOK_DIR = 'notebooks'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plug-ins
PLUGIN_PATHS = ['.']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

# for notebook rendering
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html', encoding = 'utf-8').read()
    # EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
