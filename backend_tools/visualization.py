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
            ulgs = []
            algs = []
            for lg in node.understanding_learning_goals:
                ulgs.append(lg.get().text)
            for lg in node.action_learning_goals:
                algs.append(lg.get().text)

            data = {'id' : uuid, 'summary' : summary, 'name' : name, 'temp_name' : name, 'ulgs' : ulgs, 'algs' : algs, 'clicked_var' : clicked_var, 'href': []}
            elements.append(json.dumps({'data' : data, 'classes' : classes}))
        
        # initializes arrows to be sent to jinja template
        for arrow in arrows:
            uuid = arrow.uuid
            color = ''
            color_id = arrow.color
            if color_id == 0:
                color = 'black'
            else:
                color = 'gray'
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
    