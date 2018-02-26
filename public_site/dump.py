"""Handle a print out of the goals. This was an example only."""

import os
import urllib
import random

import jinja2
import webapp2
import logging

from google.appengine.api import mail
from google.appengine.ext import vendor
from webapp2_extras import routes

from public_site_database import *
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

from public_site_database.main import PublicArticlePage as PublicArticlePage
from public_site_database.main import PublicArticleCategoryHandler as PublicArticleCategoryHandler


class ArticleDump(webapp2.RequestHandler):

  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write("HI")

    query = Article.query()
    articles = query.fetch()

    for article in articles:
        outputString = ''
        outputString = "> %s | %s | %s \n" % \
            (article.key.urlsafe(), article.title, article.authors)
        self.response.write(outputString)

app = webapp2.WSGIApplication([
                            webapp2.Route('/dump/', handler=ArticleDump)
], debug=True)
