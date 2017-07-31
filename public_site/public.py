""" Public facing site """

import os
import urllib

from webapp2_extras import routes

import jinja2
import webapp2
import logging

# Custom imports
#from database_site.google.appengine.ext import ndb
#from database_site.admin_models import *
#from database_site.admin_category import *

from site_database import *
from public_site import *
from methodology import *


from backend_tools.tool import MainPage as ToolPage
from backend_tools.tool import *
from backend_tools.learning_goals import LearningGoalHandler as LearningGoalHandler
from backend_tools.nodes import NodesPage as NodesPage
from backend_tools.visualization import VisualizationHandler as VisualizationHandler
from backend_tools import *


from site_database.article_handler import ArticleInsertHandler as ArticleInsertHandler
from site_database.article_goals import ArticleGoalHandler as ArticleGoalHandler
from site_database.admin_category import ArticleCategoryEditHandler as ArticleCategoryEditHandler
from site_database.admin_category import ArticleCategoryHandler as ArticleCategoryHandler
from site_database.resource_handler import ResourceHandler as ResourceHandler
from site_database.main import GoalHandler as GoalHandler
from site_database.resource_handler import ResourceHandler as ResourceHandler
from site_database import *
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

    template = JINJA_ENVIRONMENT.get_template('templates/public_home.html')
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
    template = JINJA_ENVIRONMENT.get_template('templates/public_about.html')
    self.response.write(template.render(template_values))


################################################################################
class PageLiterature(webapp2.RequestHandler):
  """ About the project page for the public facing website

    """

  def get(self):
    # Fetch all articles
    articles_query = Article.query()#.order(-Article.timestamp.created)
    articles = articles_query.fetch()

    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
      }

    template = JINJA_ENVIRONMENT.get_template('templates/public_literature_query.html')
    self.response.write(template.render(template_values))

################################################################################
#
#
#
#
################################################################################
class PageMethodology(webapp2.RequestHandler):
  """ Search and filtering for the Methodology database """
  def get(self):
    query = Methodology.query()#.order(-Article.timestamp.created)
    results = query.fetch()

    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'results': results,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public_methodology_query.html')
    self.response.write(template.render(template_values))

################################################################################
#
################################################################################
class PageGoalsCluster(webapp2.RequestHandler):
  """ About the project page for the public facing website

  """
  def post(self):
    selected=self.request.get_all('selected')
    logging.info(selected)

    objects = ndb.get_multi([ndb.Key(urlsafe=k) for k in selected])
    logging.info(objects)
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'objects': objects,
      'selected': selected,
      'articles': None,
      'params': self.request,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public_goals_cluster.html')
    self.response.write(template.render(template_values))


  def get(self):
    """ Show a list of all the clusters
    """
    # Fetch all articles
    query = LearningGoal.query()#.order(-Article.timestamp.created)
    goals = query.fetch()

    cluster_dict = dict()

    clusters = []
    for goal in goals:
      for cluster in goal.cluster:
        clusters.append(cluster)
        if cluster in cluster_dict:
          # append to existing array
          cluster_dict[cluster].append(goal)
        else:
          # create new key
          cluster_dict[cluster] = [goal]

    clusters = list(set(clusters))
    logging.info(cluster_dict)

    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'clusters': cluster_dict,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }
    template = JINJA_ENVIRONMENT.get_template('templates/public_cluster_list.html')
    self.response.write(template.render(template_values))



################################################################################
#
################################################################################
class PageGoalsClusterInsert(webapp2.RequestHandler):
  """ About the project page for the public facing website

  """
  def post(self):
    cluster_name=self.request.get('cluster_name')
    selected=self.request.get_all('selected')
    logging.info("HERE")
    logging.info(selected)
    logging.info(cluster_name)

    # Go through and add the cluster to each one
    objects = ndb.get_multi([ndb.Key(urlsafe=k) for k in selected])
    for goal in objects:
      goal.cluster.append(cluster_name)
      goal.put()
    self.redirect("/goals/")


################################################################################
#
# Cluster Creator
#
################################################################################
class PageGoals(webapp2.RequestHandler):
  """ About the project page for the public facing website
  """
  def post(self):
    domain=int(self.request.get('domain'))
    grade_level=int(self.request.get('grade_level'))
    concept=int(self.request.get('concept'))

    query = LearningGoal.query(LearningGoal.domainFromLiteratureReview==domain,LearningGoal.age_level==grade_level,LearningGoal.domain==concept)
    #.order(-Article.timestamp.created)
    articles = query.fetch()
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      'params': self.request,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public_literature_goals.html')
    self.response.write(template.render(template_values))


  def get(self):
    """ Fetch all learning goals and fill out search table."""

    query = LearningGoal.query()#.order(-Article.timestamp.created)
    articles = query.fetch()

    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
        }

    template = JINJA_ENVIRONMENT.get_template('templates/public_literature_goals.html')
    self.response.write(template.render(template_values))

################################################################################
#
################################################################################
# added application handlers for all backend tools
""" WSGI Application
"""
APP = webapp2.WSGIApplication([
                               webapp2.Route('/', handler=HomePage, name='home'),
                               webapp2.Route('/about/', handler=AboutPage, name='home'),
                               webapp2.Route('/literature/', handler=PageLiterature),
                               webapp2.Route('/methodology/', handler=PageMethodology),
                               webapp2.Route('/goals/', handler=PageGoals),
                               webapp2.Route('/goals/cluster/', handler=PageGoalsCluster),
                               webapp2.Route('/goals/cluster/insert/', handler=PageGoalsClusterInsert),
                               routes.PathPrefixRoute('/tools/trajectory', [
                                                                  webapp2.Route('/', handler=ToolPage),
                                                                  webapp2.Route('/<key>/', handler=TrajectoryHandler),
                                                                  webapp2.Route('/<key>/nodes/', handler=NodesPage),
                                                                  webapp2.Route('/<trajectory_key>/node/<node_key>/learning_goals/', handler=LearningGoalHandler),
                                                                  webapp2.Route('/node/<node_key>/', handler=NodeHandler),
                                                                  webapp2.Route('/<key>/visualization/', handler=VisualizationHandler),
                               ]),
                               routes.PathPrefixRoute('/resource', [
                                                                   webapp2.Route('/', ResourceHandler, 'user-overview'),
                                                                   webapp2.Route('/article/insert/', ArticleInsertHandler, 'user-projects'),
                                                                   webapp2.Route('/article/<key>/', ArticleCategoryHandler, 'user-profile'),
                                                                   webapp2.Route('/article/', ArticleHandler, 'user-overview'),
                                                                   webapp2.Route('/article/goal/<task:(insert|edit|delete)>/<article_key>/', ArticleGoalHandler, 'user-projects'),
                                                                   webapp2.Route('/article/goal/<article_key>/<learning_goal_key>/', ArticleGoalHandler, 'user-projects'),
                                                                   webapp2.Route('/article/edit/<category>/<key>/', ArticleCategoryEditHandler, 'user-projects'),
                                                                   webapp2.Route('/goals/', GoalHandler, 'user-projects'),
                                                                   ]),
                               ], debug=True)
