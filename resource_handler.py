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

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
DEFAULT_ARTICLE_KEY = 'article'


class ResourceHandler(webapp2.RequestHandler):
  """ """
  
  def get(self):
    """ """
    # Fetch all articles
    #articles_query = Article.query(ancestor=article_ancestor_key()).order(-Article.timestamp)
    #articles = articles_query.fetch(10)
    
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'types': Resource.types,
      #'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/resource.html')
    self.response.write(template.render(template_values))

