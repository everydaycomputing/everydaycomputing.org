
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



def trajectory_node_key(trajectory_key):
  return ndb.Key('TrajectoryNode',trajectory_key)

def trajectory_key():
  return ndb.Key('Trajectory','TRAJECTORY')

def trajectory_arrow_key(trajectory_key):
  return ndb.Key('TrajectoryArrow',trajectory_key)

class NodeLearningGoal(ndb.Model):
    goal = ndb.StringProperty()
    text = ndb.StringProperty()
    support = ndb.IntegerProperty()
    notes = ndb.TextProperty()

    @property
    def _support(self):
        if self.support == 1: return "direct"
        if self.support == 2: return "inferred"
        if self.support == 3: return "collected"
        return "unknown"


class Trajectory(ndb.Model):
    name = ndb.StringProperty(default="")
    summary = ndb.StringProperty(default="")
    status = ndb.IntegerProperty(default=0)
    summar2 = ndb.StringProperty(default="test")
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    #nodes = ndb.KeyProperty(kind='TrajectoryNode',repeated=True)
    #articles = ndb.KeyProperty(kind='Article', repeated=True)


class TrajectoryArrow(ndb.Model):
    uuid = ndb.StringProperty()
    start_node = ndb.StringProperty()
    end_node = ndb.StringProperty()
    explination = ndb.StringProperty()
    description = ndb.StringProperty()
    url = ndb.StringProperty()
    pdf = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    color = ndb.IntegerProperty(default=0)
    unplugged = ndb.IntegerProperty(indexed=True,default=False)
    activies = ndb.StringProperty(repeated=True)

    @classmethod
    def _arrowColor(self):
        return 'gray'



class TrajectoryNode(ndb.Model):
    """ """
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    summary = ndb.StringProperty()
    uuid = ndb.StringProperty()
    goals_in_lesson_plans = ndb.IntegerProperty(default=0)
    unplugged = ndb.IntegerProperty(default=0)
    level = ndb.IntegerProperty(default=0)


    understanding = ndb.StringProperty()
    understanding_learning_goals = ndb.KeyProperty(repeated=True)

    action = ndb.StringProperty()
    action_learning_goals = ndb.KeyProperty(repeated=True)

    action_activity = ndb.StringProperty()
    action_activity_url = ndb.StringProperty()
    action_activity_pdf = ndb.StringProperty()

    @property
    def _understanding_learning_goal_score(self):
        evidence_types = []
        for goal in ndb.get_multi(self.understanding_learning_goals):
            learning_goal = ndb.Key(urlsafe=goal.goal)
            lg = learning_goal.get()

            evidence_types.append(lg._support)
            logging.info(goal._support)
        pretty = dict((x,evidence_types.count(x)) for x in set(evidence_types))
        logging.info(pretty)
        return pretty


    @property
    def _action_learning_goal_score(self):
        evidence_types = []
        for goal in ndb.get_multi(self.action_learning_goals):
            learning_goal = ndb.Key(urlsafe=goal.goal)
            lg = learning_goal.get()

            evidence_types.append(lg._support)
            logging.info(goal._support)
        pretty = dict((x,evidence_types.count(x)) for x in set(evidence_types))
        logging.info(pretty)
        return pretty


        keys = []
        evidence_types = []
        for k in self.action_learning_goals:
            keys.append(ndb.Key(urlsafe=k))

        for goal in ndb.get_multi(keys):
            evidence_types.append(goal._support)
        pretty = dict((x,evidence_types.count(x)) for x in set(evidence_types))
        return pretty
