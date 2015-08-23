#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Site generation behavior
LOAD_CONTENT_CACHE = True
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

# Site configuration
AUTHOR = 'Alexandre Avanian'
SITENAME = '@/dev/null'
SITE_SUBTEXT = 'Random rants & thoughts'
SITEURL = 'http://aavanian.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/custom.css', 'extra/robots.txt', 'extra/favicon.ico', '../.travis.yml', '../.gitmodules']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    '../.travis.yml': {'path': '.travis.yml'},
    '../.gitmodules': {'path': '.gitmodules'},
    'extra/custom.css': {'path': 'theme/css/custom.css'}
}

DEFAULT_LANG = 'en'
TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'

# Metadata stuff
# Possibly useful to set as true but need more thinking
USE_FOLDER_AS_CATEGORY = False

# Plug-ins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']
NOTEBOOK_DIR = 'notebooks'
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html', encoding = 'utf-8').read()

# Theme
THEME = 'themes/bootstrap3'
BOOTSTRAP_THEME = 'spacelab' # Yeti is also a good candidate
PYGMENTS_STYLE = 'tango'
CUSTOM_CSS = 'theme/css/custom.css'

FAVICON = 'images/favicon.png'
#SITELOGO = 'images/logo.png'
#SITELOGO_SIZE = '128px'
#HIDE_SITENAME = True
BANNER = 'images/banner.png'
BANNER_SUBTITLE = SITE_SUBTEXT
PROFILE_IMAGE = ''
DEFAULT_PAGINATION = 10
CC_LICENSE = "CC-BY"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
MENU_ITEMS = {}

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_TAGS_INLINE = True
TAGS_URL = 'tags.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
TWITTER_USERNAME = 'aavanian'
SOCIAL =   (('twitter', 'http://twitter.com/aavanian'),
            ('linkedin', 'http://www.linkedin.com/in/alexandreavanian'),
            ('github', 'http://github.com/aavanian'),
            ('stackoverflow', 'http://stackoverflow.com/users/5190136/alexandre-avanian', 'stack-overflow'))
SHARIFF = True
SHARIFF_BACKEND_URL = ''
SHARIFF_LANG = 'en'
SHARIFF_SERVICES = "[&quot;twitter&quot;linkedin&quot;googleplus&quot;mail&quot;info&quot;]"

DISQUS_SITENAME = ''
GOOGLE_ANALYTICS = ''
GOOGLE_ANALYTICS_DOMAIN = ''
GOOGLE_ANALYTICS_UNIVERSAL = ''
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = ''
GOOGLE_ANALYTICS_ID = ''

DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = ''
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
