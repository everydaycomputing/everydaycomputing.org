import cgi
import datetime
import urllib
import webapp2
import json
import logging
import jinja2
import os
import HTMLParser 

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
        try:
            trajectory = ndb.Key(urlsafe=key).get()
            
        except TypeError:
            logging.info('Only string allowed as urlsafe input')
            return
        except ProtocolBufferDecodeError:
            logging.info('Urlsafe string invalid')
            return
        nodes_query = TrajectoryNode.query(ancestor=trajectory_node_key(key)).order(TrajectoryNode.timestamp)
        nodes = nodes_query.fetch()
        arrows = TrajectoryArrow.query(ancestor=trajectory_node_key(key)).order(TrajectoryArrow.timestamp).fetch()
        elements = []
        parser = HTMLParser.HTMLParser()
        for node in nodes:
            uuid = str(node.uuid)
            summary = str(node.summary)
            understanding = node.understanding
            action = node.action
            name = str(understanding) + '\n\n' + str(action)
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
            data = {'id' : uuid, 'name' : name, 'temp_name' : name, 'clicked_var' : clicked_var, 'href': []}
            # unescaped_data = {}
            # for key in data:
            #     unescaped_data[parser.unescape(key)] = parser.unescape(data[key])

            # data = unescaped_data
            elements.append(json.dumps({'data' : data, 'classes' : classes}))
        for arrow in arrows:
            uuid = arrow.uuid
            key = arrow.start_node
            logging.info(key)
            logging.info("\n\n")
            source = nodes_query.filter(TrajectoryNode.uuid == key).fetch()[0].uuid
            key = arrow.end_node
            target = nodes_query.filter(TrajectoryNode.uuid == key).fetch()[0].uuid
            unplugged = ''
            if arrow.unplugged == 0: 
                unplugged = 'unplugged'
            else:
                unplugged = 'programming'
            data = {'source' : source, 'target' : target, 'label' : uuid, 'unplugged' : unplugged}
            # unescaped_data = {}
            # for key in data:
            #     unescaped_data[parser.unescape(key)] = parser.unescape(data[key])
            # data = unescaped_data
            elements.append(json.dumps({'data' : data}))
        # elements = json.dumps(elements).replace(u'<', u'\\u003c').replace(u'>', u'\\u003e').replace(u'&', u'\\u0026').replace(u''', u'\\u0027')
        template_values = {
            'elements' : elements,
            'trajectory' : key
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        # json_values = json.dumps(template_values).replace(u'<', u'\\u003c').replace(u'>', u'\\u003e').replace(u'&', u'\\u0026').replace(u''', u'\\u0027')
        #logging.info('json values')
        #logging.info(json_values)
        #logging.info('\n\n\n\n')
        self.response.write(template.render(template_values, name=template_values))
        
        return
        # self.redirect('/tools/trajectory/%s/visualization/' % (key))
    