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
  '''
  ''
  ''
  ''
  '''

  def get(self,key):
    '''
    ' This is 
    '''
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
    
    template = JINJA_ENVIRONMENT.get_template('templates/admin_category.html')
    self.response.write(template.render(template_values))



class ArticleCategoryEditHandler(webapp2.RequestHandler):
  """
  "
  "
  """
  
  def post(self,category,key):
    article = ndb.Key(urlsafe=key).get()
    article.findings = self.request.get('findings')
    article.purpose = self.request.get('purpose')
    article.recommendations = self.request.get('recommendations')
    article.star = self.request.get('star') != ''
    article.audience = self.request.get_all('audience')
    article.put()
    
    logging.info(article.audience)
    # Get the correct category from ndb
    #if category == 'summary':
    #  self.updateSummary(self.request)
    #elif category == 'nope':
    #  logging.info("HI")
    self.redirect("/article/category/" + key + "/")

  def get(self,category,key):
    """
    "
    """
    article = ndb.Key(urlsafe=key).get()
    template_values = {
      'key': key,
      'category': category,
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout",
      'article': article
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/admin_%s.html' % category)
    self.response.write(template.render(template_values))
  
  def updateSummary(self,data):
    '''
    ' Update
    ' something
    '''# Update
    summary = data.get('summary')


"""
class ArticleCategoryUpdateHandler(webapp2.RequestHandler):
  ''' 
  '' sdsd
  ''
  ''
  '''

  def post(self,category,key):
    '''
    '''
    article = ndb.Key(urlsafe=key).get()
    # Get the correct category from ndb
    if category == 'summary':
      self.updateSummary(self.request)
    elif category == 'nope':
      logging.info("HI")


    self.redirect(self.request.application_url + "/article/category/" + key + "/")
"""





