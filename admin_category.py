import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


class ArticleCategoryHandler(webapp2.RequestHandler):
  def get(self,key):
    article = ndb.Key(urlsafe=key).get()
    
    template_values = {
      'key': key,
      'application_url': self.request.application_url,
      'user': users.get_current_user(),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout",
      'article': article,
      'categories': ['summary','learninggoals','methodology']
    }
    
    template = JINJA_ENVIRONMENT.get_template('admin_category.html')
    self.response.write(template.render(template_values))

class ArticleCategoryEditHandler(webapp2.RequestHandler):
  def get(self,category,key):
    article = ndb.Key(urlsafe=key).get()
    logging.info(category)
    
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout",
      'article': article,
      'categories': ['Summary','LearningGoals','Methodology','Learning Goals']
    }
    
    template = JINJA_ENVIRONMENT.get_template('admin_%s.html' % category)
    self.response.write(template.render(template_values))

