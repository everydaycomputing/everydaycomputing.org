"""Hello world application."""

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import routes

import jinja2
import webapp2
import json
import logging

# Custom imports
from admin_models import *
from article_handler import *
from admin_category import *

#
#
#
APP = webapp2.WSGIApplication([
                               #webapp2.Route('/', handler=MainPage, name='home'),
                                routes.PathPrefixRoute('/article', [
                                  webapp2.Route('/', ArticleHandler, 'user-overview'),
                                  webapp2.Route('/insert/', ArticleInsertHandler, 'user-projects'),
                                  webapp2.Route('/category/<key>/', ArticleCategoryHandler, 'user-profile'),
                                  webapp2.Route('/category/<category>/edit/<key>', ArticleCategoryEditHandler, 'user-projects'),
                                  ]),
                               #webapp2.Route('/article/<operation:.*?>/<:/?>/', handler=ArticleHandler, name='insert'),
                               #webapp2.Route('/article/edit/<key>/', handler=ArticleHandler, name='edit'),
                               #webapp2.Route('/sign', handler=Guestbook),
                               ], debug=True)
