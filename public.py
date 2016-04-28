"""Hello world application."""

import os
import urllib

from webapp2_extras import routes

import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


class HomePage(webapp2.RequestHandler):
  
  def get(self):
    """ """
    template_values = {
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/public/public_home.html')
    self.response.write(template.render(template_values))
    
  
  def post(self):
    self.response.write("-------------------------------------------------")
    #self.response.write(structured_dictionary)
    
    # structured_dictionary is the body of the post (which is the json file)
    structured_dictionary = json.loads(self.request.body)
    
    # Loop through the dictionary and print out some basic info (for debugging)
    self.response.write(structured_dictionary)


class AboutPage(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = JINJA_ENVIRONMENT.get_template('templates/public/public_about.html')
    self.response.write(template.render(template_values))


APP = webapp2.WSGIApplication([
                               webapp2.Route('/', handler=HomePage, name='home'),
                               webapp2.Route('/about/', handler=AboutPage, name='home'),
                               ], debug=True)



