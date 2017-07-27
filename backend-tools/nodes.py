
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

class NodesPage(webapp2.RequestHandler):
    """Handle the nodes updat"""

    def get(self,key):
        logging.info("?????????")
        trajectory = ndb.Key(urlsafe=key).get()
        logging.info(trajectory)
        if self.request.get("mode") == "new":
            node = TrajectoryNode(parent=trajectory_node_key(key))
            node.put()
            #trajectory.nodes.append(node.key)
            self.redirect("/tools/trajectory/%s/nodes/" % (key))

        elif self.request.get("mode") == "new_arrow":
            arrow = node = TrajectoryArrow(parent=trajectory_node_key(key))
            arrow.put()
            self.redirect("/tools/trajectory/%s/nodes/" % (key))
        else:
            nodes = TrajectoryNode.query(ancestor=trajectory_node_key(key)).order(TrajectoryNode.timestamp).fetch()
            arrows = TrajectoryArrow.query(ancestor=trajectory_node_key(key)).order(TrajectoryArrow.timestamp).fetch()
            #learning_goals =  LearningGoal.query().fetch()
            #logging.info(learning_goals)

            template_values = {
                'trajectory': trajectory,
                'nodes': nodes,
                'arrows': arrows,
                #'learning_goals': learning_goals
                }
            logging.info("?????????")
            template = JINJA_ENVIRONMENT.get_template('templates/nodes.html')
            self.response.write(template.render(template_values))

    def post(self,key):
        """This is optimized for x-editable"""
        data = self.request
        node_key = data.get('pk')
        logging.info("HERE")
        logging.info(data)
        node = ndb.Key(urlsafe=node_key).get()
        if data.get('name') == 'summary':
            node.summary = data.get('value')
        if data.get('name').startswith('level'):
            node.level = int(data.get('value'))
        if data.get('name').startswith('learning_goals'):
            node.learning_goals = data.get_all('value[]')
            logging.info(data.get_all('value[]'))
        if data.get('name').startswith('understanding_learning_goals'):
            node.understanding_learning_goals = data.get_all('value[]')

        if data.get('name').startswith('action_learning_goals'):
            node.action_learning_goals = data.get_all('value[]')

        if data.get('name').startswith('node_unplugged'):
            node.unplugged= int(data.get('value'))

        if data.get('name') == 'uuid':
            node.uuid = data.get('value')
        if data.get('name') == 'understanding':
            node.understanding = data.get('value')
        if data.get('name') == 'understanding_score':
            node.understanding_score = float(data.get('value'))
        if data.get('name').startswith('understanding_support'):
            node.understanding_support = int(data.get('value'))
        if data.get('name') == 'action':
            node.action = data.get('value')
        if data.get('name') == 'action_activity_text':
            node.action_activity_text = data.get('value')
        if data.get('name') == 'action_activity_url':
            node.action_activity_url = data.get('value')
        if data.get('name') == 'action_activity_pdf':
            node.action_activity_pdf = data.get('value')
        if data.get('name').startswith('action_support'):
            node.action_support = int(data.get('value'))
        if data.get('name').startswith('goals_in_lesson_plans'):
            node.goals_in_lesson_plans = int(data.get('value'))
        node.put()

        if data.get('name') == 'arrow_uuid':
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.pdf  = data.get('value')
            arrow.put()

        if data.get('name') == 'arrow_explination':
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.explination  = data.get('value')
            arrow.put()

        if data.get('name') == 'arrow_description':
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.description  = data.get('value')
            arrow.put()

        if data.get('name') == 'arrow_url':
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.url  = data.get('value')
            arrow.put()

        if data.get('name') == 'arrow_pdf':
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.pdf  = data.get('value')
            arrow.put()

        if data.get('name') == 'arrow_unplugged':
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.unplugged  = data.get('value')
            arrow.put()

        if data.get('name').startswith('arrow_color'):
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.color  = int(data.get('value'))
            arrow.put()

        if data.get('name').startswith('arrow_start_node'):
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.start_node= data.get('value')
            arrow.put()

        if data.get('name').startswith('arrow_end_node'):
            arrow = ndb.Key(urlsafe=node_key).get()
            arrow.end_node= data.get('value')
            arrow.put()

        self.redirect(self.request.uri)
