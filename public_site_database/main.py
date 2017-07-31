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

def article_ancestor_key():
  """
  Constructs a Datastore key for a Guestbook entity.
  We use guestbook_name as the key.
  """
  return ndb.Key(Article, 'article')

################################################################################
class PublicResourcePage(webapp2.RequestHandler):

  def get(self):
    """ """
    #self.response.headers['Content-Type'] = 'text/plain'
    #self.response.write('Everyday computing')

    template_values = {
    }

    template = JINJA_ENVIRONMENT.get_template('templates/home.html')
    self.response.write(template.render(template_values))

  def post(self):
    self.response.write("-------------------------------------------------")
    #self.response.write(structured_dictionary)

    # structured_dictionary is the body of the post (which is the json file)
    structured_dictionary = json.loads(self.request.body)

    # Loop through the dictionary and print out some basic info (for debugging)
    self.response.write(structured_dictionary)


""" Handle a print out of the goals in CSV, JSON, etc. """
class PublicArticlePage(webapp2.RequestHandler):
  def get(self):
    """ """
    articles_query = Article.query(ancestor=article_ancestor_key())#.order(-Article.timestamp.created)
    articles = articles_query.fetch()

    template_values = {
      'articles': articles
    }
    template = JINJA_ENVIRONMENT.get_template('templates/public_article.html')
    self.response.write(template.render(template_values))



class PublicArticleCategoryHandler(webapp2.RequestHandler):
  def get(self,key):
    article = ndb.Key(urlsafe=key).get()
    
    template_values = {
      'article': article,
      'categories': ['summary','methodology']
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/public_category.html')
    self.response.write(template.render(template_values))
#
#
APP = webapp2.WSGIApplication([
                               routes.PathPrefixRoute('/public/resource', [
                                                                  webapp2.Route('/', PublicResourcePage),
                                                                  webapp2.Route('/article/', PublicArticlePage),
                                                                  webapp2.Route('/article/<key>/', PublicArticleCategoryHandler)
                               ])
                               ], debug=True)
