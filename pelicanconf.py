#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yichu Zhou'
SITENAME = "Yichu Zhou | Research Blog"
SITEURL = ''

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['post_stats', 'better_tables',  'tipue_search',
        'neighbors', 'pelican-cite', 'render_math',
        'simple_footnotes', 'share_post',
        'better_figures_and_images', 'series']

THEME='elegant'

READING_TIME_LOWER_LIMIT = 1

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/flyaway1217'),
        ('Email', 'flyaway1217@gmail.com', 'My Email Address'),
        ('RSS', 'http://research.zhouyichu.com/feeds/atom.xml'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL='{slug}.html'
DRAFT_URL='drafts/{slug}.html'
PAGE_URL='{slug}.html'
PAGE_SAVE_AS='{slug}.html'
AUTHOR_SAVE_AS=''

LANDING_PAGE_TITLE="Welcome to My Research Blog"

PROJECTS = [{
    'name': 'PYEVALB',
    'url': 'https://github.com/flyaway1217/PYEVALB',
    'description': 'is a python version of Evalb which is used to score the bracket tree banks.'},
    {'name': 'ExAssist',
    'url': 'http://exassist.zhouyichu.com/en/latest/',
    'description': 'is an light-weight assist tool that can save your time from doing experiments.'},
    {'name': 'FeVER', 
        'url': 'https://github.com/flyaway1217/FeVER',
        'description':'implementation of the paper Beyond Context: A New Perspective for Word Embeddings'
        }]

PROJECTS_TITLE = "My Projects"

PUBLICATIONS_SRC = 'content/pubs.bib'

SITE_LICENSE = """Content licensed under <a rel="license"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""

SITESUBTITLE = "Computers are useless. they can only give you answers."

HOSTED_ON = {
    "name": "Digital Ocean",
    "url": "https://www.digitalocean.com/"
    }

ARTICLE_URL = '{slug}.html'

AUTHORS = {
    "Yichu Zhou": {
        "url": "http://research.zhouyichu.com/",
        "blurb": "is the owner of this blog.",
    },
}

AUTHOR='Yichu Zhou'
PDF_STYLE_PATH = 'output/pdf/'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.legacy_attrs': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.def_list': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.toc': {
            'title': 'Table of Contents:',
            'anchorlink': True,
            'permalink': True},
        'markdown.extensions.meta': {},
        'markdown.extensions.extra': {},
        'markdown_image_caption.plugin': {},
        # 'markdown_captions': {}
        }
  }

COMMENTS_INTRO='So what do you think? Did I miss something? Is any part unclear? Leave your comments below'

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}
