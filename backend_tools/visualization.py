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

class VisualizationHandler(webapp2.RequestHandler):
    def get(self, key):
        # checks to make sure key is urlsafe
        try:
            trajectory = ndb.Key(urlsafe=key).get()
        except TypeError:
            logging.info('Only string allowed as urlsafe input')
            return
        except ProtocolBufferDecodeError:
            logging.info('Urlsafe string invalid')
            return

        # queries for nodes and arrows
        nodes_query = TrajectoryNode.query(ancestor=trajectory_node_key(key)).order(TrajectoryNode.timestamp)
        nodes = nodes_query.fetch()
        arrows = TrajectoryArrow.query(ancestor=trajectory_node_key(key)).order(TrajectoryArrow.timestamp).fetch()
        lg_query = LearningGoal.query()
        elements = []
        
        # initializes nodes to be sent to jinja template
        for node in nodes:
            uuid = (node.uuid).encode('utf-8')
            summary = (node.summary).encode('utf-8')
            understanding = node.understanding
            action = node.action
            name = uuid + 'U: ' + (understanding).encode('utf-8') + '\n\n' + uuid + 'A: ' + (action).encode('utf-8')
            clicked_var = 0
            classes = ''
            if node.level == 0:
                classes += 'beginning'
            elif node.level == 1:
                classes += 'intermediate'
            else:
                classes += 'advanced'
            if node.unplugged == 0:
                classes += ' programming'
            else: 
                classes += ' unplugged'
            ulg_check = 0
            alg_check = 0
            if node.understanding_learning_goals != []:
                ulg_check = 1
            if node.action_learning_goals != []:
                alg_check = 1
            # ulgs = []
            # algs = []
            # for lg in node.understanding_learning_goals:
            #     lg_text = lg.get().text
            #     lg_support = lg.get()._support
            #     # lg_article = lg_query.filter(LearningGoal.goal == lg_text).fetch()[0].article
            #     lg_article_key = ndb.Key(urlsafe=lg.get().goal).get().article.urlsafe()
            #     logging.info("\nLG INFO:")
            #     logging.info(lg.get().goal)
            #     logging.info(lg_article_key)
            #     logging.info("\n")
            #     ulgs.append([lg_text, lg_support, lg_article_key])
            # for lg in node.action_learning_goals: 
            #     lg_text = lg.get().text
            #     lg_support = lg.get()._support
            #     lg_article_key = ndb.Key(urlsafe=lg.get().goal).get().article.urlsafe()
            #     logging.info("\nLG INFO:")
            #     logging.info(lg.get().goal)
            #     logging.info(lg_article_key)
            #     logging.info("\n")
            #     # lg_article = lg_query.filter(LearningGoal.goal == lg_text).fetch()[0].article
            #     algs.append([lg_text, lg_support, lg_article_key])

            data = {'id' : uuid, 'summary' : summary, 'name' : name, 'temp_name' : name, \
                'clicked_var' : clicked_var, 'href': [], 'ulg_check' : ulg_check, 'alg_check' : alg_check,\
                'node_urlsafe' : node.key.urlsafe(), 'trajectory_urlsafe' : key}
            elements.append(json.dumps({'data' : data, 'classes' : classes}))
        
        # initializes arrows to be sent to jinja template
        for arrow in arrows:
            uuid = arrow.uuid
            color = ''
            color_id = arrow.color
            if color_id == 0:
                color = 'black'
            else:
                color = 'silver'
            # causing NeedIndexError            
            key = arrow.start_node
            source = nodes_query.filter(TrajectoryNode.uuid == key).fetch()[0].uuid
            key = arrow.end_node
            target = nodes_query.filter(TrajectoryNode.uuid == key).fetch()[0].uuid

            unplugged = ''
            if arrow.unplugged == 0: 
                unplugged = 'unplugged'
            else:
                unplugged = 'programming'
            data = {'source' : source, 'target' : target, 'label' : uuid, 'unplugged' : unplugged, 'color' : color}
            elements.append(json.dumps({'data' : data}))
            
        template_values = {
            'elements' : elements,
            'trajectory' : key
        }

        # renders template values
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values, name=template_values))
        
        return

class UnderstandingGoalsHandler(webapp2.RequestHandler):
    def get(self, trajectory_key, node_key):
        node_entity = ndb.Key(urlsafe=node_key).get()
        node_ulgs = node_entity.understanding_learning_goals
        node_uuid = node_entity.uuid
        node_cg = node_entity.understanding
        trajectory_entity = ndb.Key(urlsafe=trajectory_key).get()
        trajectory_title = trajectory_entity.name
        understanding_lgs = []
        for lg in node_ulgs:
            lg_text = lg.get().text
            lg_support = lg.get()._support
            lg_key = ndb.Key(urlsafe=lg.get().goal)
            lg_article_key = lg_key.get().article.urlsafe()
            lg_evidence = lg_key.get()._support
            lg_support = lg_evidence + " - " + lg_support
            understanding_lgs.append([lg_text, lg_support, lg_article_key])
        template_values = {
            'lgs' : understanding_lgs,
            'trajectory_key' : trajectory_key,
            'node_key' : node_key,
            'node_uuid' : node_uuid,
            'trajectory_title' : node_cg
        }
        template = JINJA_ENVIRONMENT.get_template('templates/public_node_lg_list.html')
        self.response.write(template.render(template_values, name=template_values))
        return

class ActionGoalsHandler(webapp2.RequestHandler):
    def get(self, trajectory_key, node_key):
        node_entity = ndb.Key(urlsafe=node_key).get()
        node_algs = node_entity.action_learning_goals
        node_uuid = node_entity.uuid
        node_cg = node_entity.action
        trajectory_entity = ndb.Key(urlsafe=trajectory_key).get()
        trajectory_title = trajectory_entity.name
        action_lgs = []
        for lg in node_algs:
            lg_text = lg.get().text
            lg_support = lg.get()._support
            lg_key = ndb.Key(urlsafe=lg.get().goal)
            lg_article_key = lg_key.get().article.urlsafe()
            lg_evidence = lg_key.get()._support
            lg_support = lg_evidence + " - " + lg_support
            action_lgs.append([lg_text, lg_support, lg_article_key])
        template_values = {
            'lgs' : action_lgs,
            'trajectory_key' : trajectory_key,
            'node_key' : node_key,
            'node_uuid' : node_uuid,
            'trajectory_title' : node_cg
        }
        template = JINJA_ENVIRONMENT.get_template('templates/public_node_lg_list.html')
        self.response.write(template.render(template_values, name=template_values))
        return