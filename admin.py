"""Hello world application."""

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import json
import logging

# Custom imports
from admin_models import *
import bibpy


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
  """
    Constructs a Datastore key for a Guestbook entity.
    We use guestbook_name as the key.
    """
  return ndb.Key('Guestbook', guestbook_name)



#
#
#
#
#
class MainPage(webapp2.RequestHandler):
  
  def get(self):
    #
    #
    #
    guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
    greetings_query = Greeting.query(ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
    greetings = greetings_query.fetch(10)
    
    user = users.get_current_user()
    if user:
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'
    
    template_values = {
      'user': user,
      'greetings': greetings,
      'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': url,
      'url_linktext': url_linktext,
    }
        
    template = JINJA_ENVIRONMENT.get_template('admin.html')
    self.response.write(template.render(template_values))

#
#
#
#
#
#
class Guestbook(webapp2.RequestHandler):
  
  def post(self):
    # We set the same parent key on the 'Greeting' to ensure each
    # Greeting is in the same entity group. Queries across the
    # single entity group will be consistent. However, the write
    # rate to a single entity group should be limited to
    # ~1/second.
    guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
    greeting = Greeting(parent=guestbook_key(guestbook_name))
        
    if users.get_current_user():
      greeting.author = Creator(identity=users.get_current_user().user_id(),email=users.get_current_user().email())
      
    greeting.content = self.request.get('content')
    self.bib2data(self.request.get('content'))
    greeting.put()
        
    query_params = {'guestbook_name': guestbook_name}
    self.redirect('/?' + urllib.urlencode(query_params))

  def bib2data(self,string):
    """ Bib parsing
    """
    bib = bibpy.Parser(self.request.get('content'))
    bib.parse()
    items = json.loads(bib.json())
    data = items["items"][0]
    logging.info(data)

    # Create article

    # Loop through and add all the authors
    for author in data['author']:
      # The unique key the author record can be referred by
      key_name = author['family']+"_"+author['given']
      k = ndb.Key('Author',key_name)
      a = Author.get_or_insert(k.id(),family_name=author['family'],given_name=author['given'])


APP = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/sign', Guestbook),
                               ], debug=True)
