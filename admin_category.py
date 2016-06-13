import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import logging

from admin_models import *

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


class ArticleCategoryHandler(webapp2.RequestHandler):
  def get(self,key):
    """ This is """
    article = ndb.Key(urlsafe=key).get()
    
    template_values = {
      'key': key,
      'application_url': self.request.application_url,
      'user': users.get_current_user(),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout",
      'article': article,
      'categories': ['summary','learning-goals','methodology']
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/admin_category.html')
    self.response.write(template.render(template_values))



class ArticleCategoryEditHandler(webapp2.RequestHandler):
  
  def post(self,category,key):
    # Get the correct category from ndb
    if category == 'summary':
      self.updateSummary(key,self.request)
    elif category == 'learning-goals':
      self.updateLearningGoals(key,self.request)
    elif category == 'methodology':
      self.updateMethodology(key,self.request)

    self.redirect("/resource/article/" + key + "/")


  def get(self,category,key):
    """
    "
    """
    article = ndb.Key(urlsafe=key).get()
    #learning_goal = ndb.Key(urlsafe=key).get()
    template_values = {
      'key': key,
      'category': category,
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout",
      'article': article,
      #'learning_goal': learning_goal
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/admin_%s.html' % category)
    self.response.write(template.render(template_values))
  
  
  def updateSummary(self,key,data):
    """ """
    summary = data.get('summary')
    article = ndb.Key(urlsafe=key).get()
    article.findings = data.get('findings')
    article.purpose = data.get('purpose')
    article.recommendations = data.get('recommendations')
    article.star = data.get('star') != ''
    article.audience = data.get_all('audience')
    article.put()



  def updateLearningGoals(self,key,data):
    """ """
    article = ndb.Key(urlsafe=key).get()
    learning_goal_key = data.get('learning_goal_key')
    logging.info("HI" + learning_goal_key)
    learning_goal = ndb.Key(urlsafe=learning_goal_key).get()

    learning_goal.domain = data.get('domain')
    learning_goal.goal = data.get('goal')
    learning_goal.age_level = map(int, data.get_all('age_level'))
    learning_goal.empirical_support = data.get('empirical_support') != ''
    learning_goal.subgoals = data.get('subgoals')
    learning_goal.relationships_goals = data.get('relationships_goals')
    learning_goal.activity_origin = data.get_all('activity_origin')
    learning_goal.activity_source = data.get('activity_source')
    learning_goal.ccssm_domains = data.get_all('ccssm_domains')
    learning_goal.ccssm_cotent_standards = data.get('ccssm_cotent_standards')
    learning_goal.ccssm_practice_standards = map(int, data.get_all('ccssm_practice_standards'))
    learning_goal.put()
    #article.learning_goal = learning_goal.key
    #article.put()



  def updateMethodology(self,key,data):
    """ """
    article = ndb.Key(urlsafe=key).get()
    methodology = article._methodology
    logging.info("METHODOLOGY: ")
    logging.info(methodology)

    methodology.sample_size = int(data.get('sample_size'))
    methodology.sample_gender = data.get_all('sample_gender')
    methodology.sample_ses = data.get('sample_ses')
    methodology.sample_disability_status = data.get_all('sample_disability_status')
    methodology.sample_ethnicity = data.get_all('sample_ethnicity')
    methodology.sample_notes = data.get('sample_notes')
    methodology.sample_participant_type = data.get('sample_participant_type')
    methodology.sample_environment = data.get_all('sample_environment')
    methodology.sample_setting = data.get_all('sample_setting')
    methodology.sample_size_of_school = int(data.get('sample_size_of_school'))
    methodology.sample_design = data.get_all('sample_design')
    methodology.sample_data_collection_instrument = data.get('sample_data_collection_instrument')
    methodology.sample_data_collection_procedure = data.get('sample_data_collection_procedure')
    methodology.sample_data_analytic_technique = data.get_all('sample_data_analytic_technique')
    methodology.sample_data_analytic_technique_note = data.get('sample_data_analytic_technique_note')
    methodology.sample_effect_size = data.get('sample_effect_size')
    methodology.sample_agreement = data.get('sample_agreement')

    methodology.put()
    article.methodology = methodology.key
    article.put()


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





