import cgi
import datetime
import urllib
import webapp2
import json
import logging
import jinja2
import os

#from google.appengine.api import mail
#from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.api import taskqueue
from google.appengine.ext import deferred

from models import *
from site_database import *

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)



class LearningGoalHandler(webapp2.RequestHandler):

    @staticmethod
    def get_learning_goals():
        data = memcache.get('LEARNING-GOALS')
        if data is not None:
            logging.info("CACHE HIT")
            return data
        else:
            data = LearningGoal.query().fetch()
            memcache.add('LEARNING-GOALS', data, 3600)
        return data

    def get(self,trajectory_key,node_key):
        logging.info("--------------- GET ------------------")
        logging.info("Learning Goal Handler Get")
        logging.info(self.request)

        current_goal = None
        if self.request.get("mode") == "edit":
            lg = ndb.Key(urlsafe=self.request.get("goal"))
            current_goal = lg.get()
            logging.info(current_goal)

        template_values = {
            'trajectory_key': trajectory_key,
            'node_key': node_key,
            'learning_goals': self.get_learning_goals(),
            'type': self.request.get("type"),
            'current_goal': current_goal,
            'mode': self.request.get("mode")
            }
        template = JINJA_ENVIRONMENT.get_template('templates/learning_goals.html')
        self.response.write(template.render(template_values))

    def post(self,trajectory_key,node_key):
        logging.info("---------------POST------------------")
        logging.info(self.request)

        # if edit just update
        if self.request.get("mode") == "edit":
            logging.info("============EDIT=============")
            logging.info(self.request.get("current_goal"))

            # Node Learning Goal
            goal_key = ndb.Key(urlsafe=self.request.get("current_goal"))
            node_learning_goal = goal_key.get()
            logging.info("============NL Goal=============")
            logging.info(node_learning_goal)

            # Update the values
            node_learning_goal.support = int(self.request.get('support'))
            node_learning_goal.goal = self.request.get('lg') # key value from select box
            node_learning_goal.notes = self.request.get('notes')
            g = ndb.Key(urlsafe=node_learning_goal.goal)
            real_goal = g.get()
            node_learning_goal.text = real_goal.goal

            # save it
            node_learning_goal.put()

            logging.info("============Goal after =============")
            logging.info(node_learning_goal)

        else:
            #trajectory = ndb.Key(urlsafe=key).get()
            node_key2 = ndb.Key(urlsafe=node_key)
            node = node_key2.get()
            logging.info(node)

            # Create a new goal record
            lg = NodeLearningGoal()
            lg.support = int(self.request.get('support'))
            lg.goal = self.request.get('lg')
            lg.notes = self.request.get('notes')

            # Add reference to lgs
            g = ndb.Key(urlsafe=lg.goal)
            real_goal = g.get()
            lg.text = real_goal.goal
            lg.put()

            if self.request.get("type") == "understanding":
                node.understanding_learning_goals.append(lg.key)
            elif self.request.get("type") == "action":
                node.action_learning_goals.append(lg.key)
            #learning_goals.append(lg.key)
            node.put()
        self.redirect("/tools/trajectory/%s/nodes/" % (trajectory_key))
