"""Public facing site that contains the landing page and about page."""

import os
#import tweepy
import jinja2
import webapp2
import logging

from google.appengine.ext import vendor
from webapp2_extras import routes

# Custom imports
from public_site_database import *
from landing import AboutPage, HomePage, ProfessionalDevelopmentPage, HomePageExample
from public_site import *
from site_database import *
from methodology import *

from backend_tools.tool import MainPage as ToolPage
from backend_tools.tool import *
from backend_tools.learning_goals import LearningGoalHandler as LearningGoalHandler
from backend_tools.nodes import NodesPage as NodesPage
from backend_tools.visualization import VisualizationHandler as VisualizationHandler
from backend_tools.visualization import ActionGoalsHandler as ActionGoalsHandler
from backend_tools.visualization import UnderstandingGoalsHandler as UnderstandingGoalsHandler
from backend_tools import *


from site_database.article_handler import ArticleInsertHandler as ArticleInsertHandler
from site_database.article_goals import ArticleGoalHandler as ArticleGoalHandler
from site_database.admin_category import ArticleCategoryEditHandler as ArticleCategoryEditHandler
from site_database.admin_category import ArticleCategoryHandler as ArticleCategoryHandler
from site_database.resource_handler import ResourceHandler as ResourceHandler
from site_database.main import GoalHandler as GoalHandler
from site_database.resource_handler import ResourceHandler as ResourceHandler
from site_database import *


# from public_site_database.main import PublicResourcePage as PublicResourcePage
from public_site_database.main import PublicArticlePage as PublicArticlePage
from public_site_database.main import PublicArticleCategoryHandler as PublicArticleCategoryHandler

# Add any libraries install in the "lib" folder.
vendor.add('lib')

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)


################################################################################
class PageLiterature(webapp2.RequestHandler):
  """ About the project page for the public facing website."""
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
# Cluster Creator
################################################################################
class PageGoals(webapp2.RequestHandler):
  """The Goals sort and filter utility.
  Located at: everydaycomputing.org/goals/
  """
  def post(self):
    # Get the values from the filtering form on the website
    domain=int(self.request.get('domain'))
    grade_level=int(self.request.get('grade_level'))
    concept=int(self.request.get('concept'))

    # Construct the query
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

class PublicResourcePage(webapp2.RequestHandler):
  def get(self):
    template_values = {
    }

    template = JINJA_ENVIRONMENT.get_template('templates/resource_home.html')
    self.response.write(template.render(template_values))

class PublicVisualizationPage(webapp2.RequestHandler):
  def get(self):
    """ """
    #self.response.headers['Content-Type'] = 'text/plain'
    #self.response.write('Everyday computing')

    template_values = {
    }

    template = JINJA_ENVIRONMENT.get_template('templates/vis_home.html')
    self.response.write(template.render(template_values))


################################################################################
#
################################################################################
# added application handlers for all backend tools
""" WSGI Application
"""
APP = webapp2.WSGIApplication([
                               webapp2.Route('/', handler=HomePage, name='home'),
                               webapp2.Route('/home-example/<style_id>/<example_id:\d+>/', handler=HomePageExample, name='home'),
                               webapp2.Route('/about/', handler=AboutPage, name='home'),
                               webapp2.Route('/pd/', handler=ProfessionalDevelopmentPage, name='home'),
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
                                                                  webapp2.Route('/<trajectory_key>/visualization/<node_key>/understanding/', UnderstandingGoalsHandler),
                                                                  webapp2.Route('/<trajectory_key>/visualization/<node_key>/action/', ActionGoalsHandler)
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
                               webapp2.Route('/public/visualization/', PublicVisualizationPage),
                               routes.PathPrefixRoute('/public/resource', [
                                                                  webapp2.Route('/', PublicResourcePage),
                                                                  webapp2.Route('/article/', PublicArticlePage),
                                                                  webapp2.Route('/article/<key>/', PublicArticleCategoryHandler)
                               ])
                               ], debug=True)
