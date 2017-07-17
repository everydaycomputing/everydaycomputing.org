import os
import urllib

from webapp2_extras import routes

import jinja2
import webapp2
import logging

# Custom imports
from site_database import *
from public_site import *
from methodology import *

#
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


class PageMethodology(webapp2.RequestHandler):
  """ Search and filtering for the Methodology database """

  def get(self):
    query = Methodology.query()#.order(-Article.timestamp.created)
    results = query.fetch()

    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'results': results,
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/public_methodology_query.html')
    self.response.write(template.render(template_values))
