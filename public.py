"""Hello world application."""

import os
import urllib

from webapp2_extras import routes

import jinja2
import webapp2
import logging

# Custom imports
from google.appengine.ext import ndb
from admin_models import *
from admin_category import *

#
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)



class HomePage(webapp2.RequestHandler):
  """ Handlers for the public facing website.

  """
  
  
  def get(self):
    """ 
    """
    template_values = {}
    
    template = JINJA_ENVIRONMENT.get_template('templates/public/public_home.html')
    self.response.write(template.render(template_values))
    
  
  def post(self):
    self.response.write("-------------------------------------------------")
    #self.response.write(structured_dictionary)
    
    # structured_dictionary is the body of the post (which is the json file)
    structured_dictionary = json.loads(self.request.body)
    
    # Loop through the dictionary and print out some basic info (for debugging)
    self.response.write(structured_dictionary)


class AboutPage(webapp2.RequestHandler):
  """ About the project page for the public facing website
    
  """
  def get(self):
    template_values = {}
    template = JINJA_ENVIRONMENT.get_template('templates/public/public_about.html')
    self.response.write(template.render(template_values))



class PageLiterature(webapp2.RequestHandler):
  """ About the project page for the public facing website

  """
  
  def get(self):
    # Fetch all articles
    articles_query = Article.query()#.order(-Article.timestamp.created)
    articles = articles_query.fetch(500)
    
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public/public_literature_query.html')
    self.response.write(template.render(template_values))



class PageGoals(webapp2.RequestHandler):
  """ About the project page for the public facing website

  """
  def post(self):
    domain=int(self.request.get('domain'))
    grade_level=int(self.request.get('grade_level'))
    concept=int(self.request.get('concept'))
  
    query = LearningGoal.query(LearningGoal.domainFromLiteratureReview==domain,LearningGoal.age_level==grade_level,LearningGoal.domain==concept)
    #.order(-Article.timestamp.created)
    articles = query.fetch(500)
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      'params': self.request,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public/public_literature_goals.html')
    self.response.write(template.render(template_values))


  def get(self):
    # Fetch all articles
    query = LearningGoal.query()#.order(-Article.timestamp.created)
    articles = query.fetch(500)
    
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public/public_literature_goals.html')
    self.response.write(template.render(template_values))

APP = webapp2.WSGIApplication([
                               webapp2.Route('/', handler=HomePage, name='home'),
                               webapp2.Route('/about/', handler=AboutPage, name='home'),
                               webapp2.Route('/literature/', handler=PageLiterature),
                               webapp2.Route('/goals/', handler=PageGoals),
                               ], debug=True)



