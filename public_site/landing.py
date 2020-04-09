"""Landing page and about page handlers."""
import os
import jinja2
import webapp2
import random

JINJA_ENVIRONMENT = jinja2.Environment(\
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), \
    extensions=['jinja2.ext.autoescape'], autoescape=True)


class HomePage(webapp2.RequestHandler):
    """Handlers for the public facing website."""

    def get(self):
        # Define possible video IDs
        video_ids = ['164178655','214983140','266544098','332316962']
        # Select random video to display
        video_id = random.choice(video_ids)
        # Pass video ID to template
        template_values = {
            'video_id': video_id
        }
        template = JINJA_ENVIRONMENT.get_template('templates/public_home.html')
        self.response.write(template.render(template_values))

    def post(self):
         """Unused test for the post handler."""

         self.response.write("-------------------------------------------------")
         #self.response.write(structured_dictionary)
         # structured_dictionary is the body of the post (which is the json file)
         structured_dictionary = json.loads(self.request.body)
         # Loop through the dictionary and print out some basic info (for debugging)
         self.response.write(structured_dictionary)


class AboutPage(webapp2.RequestHandler):
    """About the project page for the public facing website."""

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/public_about.html')
        self.response.write(template.render(template_values))

class TeamPage(webapp2.RequestHandler):
    """Team page for the public facing website."""

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/public_team.html')
        self.response.write(template.render(template_values))

class ProfessionalDevelopmentPage(webapp2.RequestHandler):
    """Professional Development page for the public facing website."""

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/public_pd.html')
        self.response.write(template.render(template_values))

class HomePageExample(webapp2.RequestHandler):
    """Professional Development page for the public facing website."""

    def get(self,style_id,example_id):
        template_values = {
            'style_id': style_id,
            'example_id': example_id
        }
        try:
            template = JINJA_ENVIRONMENT.get_template('templates/public_homepage_example_' + style_id + '.html')
        except:
            webapp2.abort(404)
        
        self.response.write(template.render(template_values))

class LessonsPage(webapp2.RequestHandler):
    """Professional Development page for the public facing website."""

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/public_lessons.html')
        self.response.write(template.render(template_values))

class AssessmentsPage(webapp2.RequestHandler):
    """Professional Development page for the public facing website."""

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/public_assessments.html')
        self.response.write(template.render(template_values))

class PublicationsPage(webapp2.RequestHandler):
    """Professional Development page for the public facing website."""

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/public_publications.html')
        self.response.write(template.render(template_values))