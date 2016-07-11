from google.appengine.api import users
from google.appengine.ext import ndb
from protorpc import messages
import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

################################################################################
#
# Learning Goal
#
################################################################################
class LearningGoal(ndb.Model):
  """ Learning Goals that are identified in article resource. """
  
  # The original domain is not referred to as a `concept`
  domain = ndb.IntegerProperty(default=0)
  # This is referred to as a domain
  domainFromLiteratureReview = ndb.IntegerProperty(default=0)
  
  
  page_number = ndb.StringProperty(default="")
  goal = ndb.TextProperty(default="")
  age_level = ndb.IntegerProperty(choices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], repeated=True)
  #empirical_support = ndb.BooleanProperty(default=False)
  support = ndb.IntegerProperty(default=0)
  subgoals = ndb.TextProperty(default="")
  relationships_goals = ndb.TextProperty(default="")
  activity_origin = ndb.StringProperty(choices=['Custom','Pre-existing'], repeated=True)
  activity_source = ndb.TextProperty(default="")
  ccssm_domains = ndb.StringProperty(choices=['CC','OA','NBT','NF','MD','G'], repeated=True)
  ccssm_cotent_standards = ndb.StringProperty(default="") # repeated??
  ccssm_practice_standards = ndb.IntegerProperty(choices=[1,2,3,4,5,6,7,8], repeated=True)
  ccssm_grades = ndb.IntegerProperty(choices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], repeated=True)
  
  @staticmethod
  def _pretty_grades(code):
    if code == 0: return "K"
    if code > 0 and code < 13: return str(code)
    if code == 13: return "Elementary School"
    if code == 14: return "Junior High"
    if code == 15: return "Middle School"
    if code == 16: return "High School"
  
  @property
  def _domainFromLiteratureReview(self):
    """ Mapping of emergent domains (those that came from the literature review
      after the name "domain" was previously applied to the Grover and Pea
      domains """
    
    if self.domainFromLiteratureReview == 0: return 'Program development (Iterative development of computational solutions)'
    if self.domainFromLiteratureReview == 1: return 'Computing languages, environments, and constructs'
    if self.domainFromLiteratureReview == 2: return 'Algorithms (Flow of control)'
    if self.domainFromLiteratureReview == 3: return 'Applications of computing (Recognizing computational problems and interpreting computational results)'
  
  @property
  def _domain(self):
    """ Mapping so that we can freely change names at a later time
      
      Note: In all the documents moving forward from June, 2016, these are
      referred to as the "Concepts"
      """
    if self.domain == 0: return "Abstraction and pattern generalization"
    if self.domain == 1: return "Systematic processing of data"
    if self.domain == 2: return "Symbol systems and representations"
    if self.domain == 3: return "Algorithmic notions of flow of control"
    if self.domain == 4: return "Structured problem decomposition (modularizing)"
    if self.domain == 5: return "Iterative, recursive, and parallel thinking"
    if self.domain == 6: return "Conditional logic"
    if self.domain == 7: return "Efficiency and performance constraints"
    if self.domain == 8: return "Debugging and systematic error detection"
  
  @property
  def _support(self):
    if self.support == 0: return 'Clasroom Evidence'
    if self.support == 1: return 'Literature Evidence'
    if self.support == 2: return 'Theorectical Evidence'
  
  @staticmethod
  def _ccssm_practice_standards(code):
    if code == 1: return "1. Make sense of problems and persevere in solving them."
    if code == 2: return "2. Reason abstractly and quantitatively."
    if code == 3: return "3. Construct viable arguments and critique the reasoning of others."
    if code == 4: return "4. Model with mathematics."
    if code == 5: return "5. Use appropriate tools strategically."
    if code == 6: return "6. Attend to precision."
    if code == 7: return "7. Look for and make use of structure."
    if code == 8: return "8. Look for and express regularity in repeated reasoning."


################################################################################
#
# ArticleGoalHandler
#
################################################################################
class ArticleGoalHandler(webapp2.RequestHandler):
  
  def post(self,article_key,learning_goal_key):
    """
      article = ndb.Key(urlsafe=key).get()
      article.findings = self.request.get('findings')
      article.purpose = self.request.get('purpose')
      article.recommendations = self.request.get('recommendations')
      article.star = self.request.get('star') != ''
      article.audience = self.request.get_all('audience')
      article.put()
      """
    data = self.request
    article = ndb.Key(urlsafe=article_key).get()
    #learning_goal_key = data.get('learning_goal_key')
    #logging.info("LGK: " + learning_goal_key)
    learning_goal = ndb.Key(urlsafe=learning_goal_key).get()
    learning_goal.domain = int(data.get('domain'))
    learning_goal.domainFromLiteratureReview = int(data.get('domainFromLiteratureReview'))
    learning_goal.support = int(data.get('support'))
    learning_goal.page_number = str(data.get('page_number'))
    learning_goal.goal = data.get('goal')
    learning_goal.age_level = map(int, data.get_all('age_level'))
    learning_goal.empirical_support = data.get('empirical_support') != ''
    learning_goal.subgoals = data.get('subgoals')
    learning_goal.relationships_goals = data.get('relationships_goals')
    learning_goal.activity_origin = data.get_all('activity_origin')
    learning_goal.activity_source = data.get('activity_source')
    learning_goal.ccssm_domains = data.get_all('ccssm_domains')
    learning_goal.ccssm_grades = map(int, data.get_all('ccssm_grades'))
    learning_goal.ccssm_cotent_standards = data.get('ccssm_cotent_standards')
    learning_goal.ccssm_practice_standards = map(int, data.get_all('ccssm_practice_standards'))
    learning_goal.put()
    # Reload
    self.redirect("/resource/article/" + article_key + "/")
  
  
  def get(self,task,article_key):
    """
      " Note: We are using a different key based on the type of task
      """
    article = ndb.Key(urlsafe=article_key).get()
    if task == 'insert':
      # Create a new learing goal
      learning_goal = LearningGoal()
      learning_goal_key = learning_goal.put()
      article.learning_goals.append(learning_goal.key)
      learning_goal_key = learning_goal_key.urlsafe()
    elif task == 'delete':
      learning_goal_key = self.request.get('learning_goal_key')
      learning_goal = ndb.Key(urlsafe=learning_goal_key).get()
      article.learning_goals.remove(learning_goal.key)
      learning_goal.key.delete()
    else:
      learning_goal_key = self.request.get('learning_goal_key')
      learning_goal = ndb.Key(urlsafe=learning_goal_key).get()
    
    # Save any changes we made
    article.put()
    
    if task == 'delete':
      self.redirect("/resource/article/" + article_key + "/")
    else:
      template_values = {
        'url': self.request.application_url,
        'user': users.get_current_user(),
        'url': users.create_logout_url(self.request.uri),
        'url_linktext': "Logout",
        'article': article,
        'article_key': article_key,
        'learning_goal' : learning_goal,
        'learning_goal_key' : learning_goal_key
      }
      logging.info("article")
      logging.info(article_key)
      template = JINJA_ENVIRONMENT.get_template('templates/admin_learning-goals.html')
      self.response.write(template.render(template_values))



