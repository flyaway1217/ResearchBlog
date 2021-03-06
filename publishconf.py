#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'http://research.zhouyichu.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_DOMAIN=SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "research-yichu"
GOOGLE_ANALYTICS = "UA-146436790-1"


