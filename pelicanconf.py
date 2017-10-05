#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Robinson Merillat'
SITENAME = 'Robinson Merillat'
SITEURL = ''
SITETITLE = 'Robinson Merillat'
SITESUBTITLE = 'Senior in Computer Science at Colorado School of Mines'
SITEDESCRIPTION = 'Robinson\'s portfolio, thoughts, and writings'
SITELOGO = SITEURL + '/images/profile.jpg'
#FAVICON = SITEURL + '/images/favicon.ico'

MAIN_MENU = True

PATH = './content'

TIMEZONE = 'America/Denver'

THEME = 'Flex'
CUSTOM_CSS = './static/custom.css'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['./static', './images']

GOOGLE_ANALYTICS = 'UA-104941015-1'
DISQUS_SITENAME = 'robinsonmerillat'

#PLUGIN_PATHS = ['plugins']
#PLUGINS = ['post_stats', 'representative_image', 'neighbors', 'related_posts']
PYGMENTS_STYLE = 'autumn'

IGNORE_FILES = ['.vim-template:.md']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/sumnerevans'),
          ('stack-overflow', 'http://stackoverflow.com/users/2319844/'),
          ('github', 'https://github.com/bloodraine'),
          ('instagram', 'https://www.instagram.com/sumner.evans/'),
          ('facebook', 'https://www.facebook.com/sumner.evans98'),
          ('youtube', 'https://www.youtube.com/channel/UCyrdRO4oJRpszr0ovN1FwBA/'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

LINKS = (('resume', '/static/resume.pdf'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
