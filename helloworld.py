"""Hello world application."""


import webapp2
import json


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, webapp2 World! This is the default module.')

    def post(self):
        self.response.write("-------------------------------------------------")
        #self.response.write(structured_dictionary)

        # structured_dictionary is the body of the post (which is the json file)
        structured_dictionary = json.loads(self.request.body)
        
        # Loop through the dictionary and print out some basic info (for debugging)
        self.response.write(structured_dictionary)
        #for item in structured_dictionary:
        #    self.response.write("%s %s - %s\n" % (item['lessonNumber'],item['title'],item['parentCourse']))



APP = webapp2.WSGIApplication([('/', MainPage),], debug=True)
