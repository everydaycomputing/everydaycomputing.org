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


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, webapp2 World! This is the default module. Hi')

    def post(self):
        self.response.write("-------------------------------------------------")
        #self.response.write(structured_dictionary)

        # structured_dictionary is the body of the post (which is the json file)
        structured_dictionary = json.loads(self.request.body)
        
        # Loop through the dictionary and print out some basic info (for debugging)
        self.response.write(structured_dictionary)
        #for item in structured_dictionary:
        #    self.response.write("%s %s - %s\n" % (item['lessonNumber'],item['title'],item['parentCourse']))

#
#
#
APP = webapp2.WSGIApplication([
                               webapp2.Route('/', handler=MainPage, name='home'),
                                routes.PathPrefixRoute('/article', [
                                  webapp2.Route('/', ArticleHandler, 'user-overview'),
                                  webapp2.Route('/insert/', ArticleInsertHandler, 'user-projects'),
                                  webapp2.Route('/category/<key>/', ArticleCategoryHandler, 'user-profile'),
                                  webapp2.Route('/category/<category>/edit/<key>/', ArticleCategoryEditHandler, 'user-projects'),
                                  ]),
                               #webapp2.Route('/article/<operation:.*?>/<:/?>/', handler=ArticleHandler, name='insert'),
                               #webapp2.Route('/article/edit/<key>/', handler=ArticleHandler, name='edit'),
                               #webapp2.Route('/sign', handler=Guestbook),
                               ], debug=True)



