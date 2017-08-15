# api.py

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
from nodes import *
from learning_goals import *
from visualization import *

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)



class NodeHandler(webapp2.RequestHandler):
    def get(self,trajectory_key):
        logging.info("Hi")
        trajectory = ndb.Key(urlsafe=trajectory_key).get()
        #logging.info(trajectory)
        template_values = {
            'trajectory': trajectory
            }
        template = JINJA_ENVIRONMENT.get_template('templates/nodes.html')
        self.response.write(template.render(template_values))

    def post(self,node_key):
        data = self.request
        logging.info(data)
        #node = TrajectoryNode()

        node = ndb.Key(urlsafe=node_key).get()
        node.summary = data.get('summary')
        node.understanding = data.get('understanding')
        node.action = data.get('action')
        #logging.info(data.get('goals_in_lesson_plans'))
        node.goals_in_lesson_plans = data.get('goals_in_lesson_plans') != ''
        arrow_in = ndb.KeyProperty()
        arrow_out = ndb.KeyProperty()
        node.put()

        self.redirect(self.request.uri) # + article_key + "/")
    
    




class MainPage(webapp2.RequestHandler):
    def get(self):
        if self.request.get("mode") == "new":
            trajectory = Trajectory(parent=trajectory_key())
            trajectory.put()
            self.redirect("/tools/trajectory/")
        else:
            logging.info("Redirect")
            trajectories = Trajectory.query(ancestor=trajectory_key()).order(-Trajectory.timestamp).fetch()
            template_values = {
                'trajectories': trajectories,
                'user': users.get_current_user(),
                'url' : users.create_logout_url(self.request.uri),
                'url_linktext' : "Logout"
                }
            template = JINJA_ENVIRONMENT.get_template('templates/trajectories.html')
            self.response.write(template.render(template_values))

    def post(self):
        trajectory = Trajectory()
        trajectory.name = self.request.get('name')
        trajectory.summary = self.request.get('summary')
        trajectory.put()
        self.redirect(self.request.uri)

class TrajectoryHandler(webapp2.RequestHandler):
    def get(self,key):
        trajectory = ndb.Key(urlsafe=key).get()
        if self.request.get("mode") == "delete":
            trajectory.key.delete()
            self.redirect("/tools/trajectory/")
        else:
            logging.info(trajectory)
            template_values = { 'trajectory': trajectory }
            template = JINJA_ENVIRONMENT.get_template('templates/trajectories.html')
            self.response.write(template.render(template_values))

    def post(self,key):
        """This is optimized for x-editable"""
        data = self.request
        logging.info(data)
        trajectory = ndb.Key(urlsafe=key).get()
        if data.get('name') == 'name':
            trajectory.name = data.get('value')
        if data.get('name') == 'summary':
            trajectory.summary = data.get('value')
        if data.get('name').startswith('status'):
            trajectory.status = int(data.get('value'))
        trajectory.put()
        self.redirect(self.request.uri)

        
##
##
##

# unused, all web handlers now registered in public site
app = webapp2.WSGIApplication([
                            webapp2.Route('/tools/trajectory/', MainPage),
                            webapp2.Route('/tools/trajectory/<key>/', handler=TrajectoryHandler),
                            webapp2.Route('/tools/trajectory/<key>/nodes/', handler=NodesPage),
                            webapp2.Route('/tools/trajectory/<trajectory_key>/node/<node_key>/learning_goals/', handler=LearningGoalHandler),
                            webapp2.Route('/tools/trajectory/node/<node_key>/', handler=NodeHandler),
                            webapp2.Route('/tools/trajectory/<key>/visualization/', handler=VisualizationHandler),
                            webapp2.Route('/tools/trajectory/<trajectory_key>/visualization/<node_key>/understanding/', handler=UnderstandingGoalsHandler),
                            webapp2.Route('/tools/trajectory/<trajectory_key>/visualization/<node_key>/action/', handler=ActionGoalsHandler)
], debug=True)
