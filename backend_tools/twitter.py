import cgi
import datetime
import urllib
import webapp2
import json
import logging
import jinja2
import os
import random

from webapp2_extras import routes
from google.appengine.api import mail
from google.appengine.ext import vendor
from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.api import taskqueue
from google.appengine.ext import deferred

# Add any libraries install in the "lib" folder.
vendor.add('lib')
import tweepy

class TweetHandler(webapp2.RequestHandler):
    """Send a daily tweet everymorning to keep on top of the timeline"""

    token = "4877256413-KTBnxOxciPxJCsO120O9G4flzX4mofC97NFnKJM"
    token_secret = "S94iIiawQu3ipCP6Zdrv5paeuUS4kAw2eLAC21ZAKnNWJ"
    consumer_key = "QuOJBKX2FRsUPk9drwg2YOyE0"
    consumer_secret = "MGTBmDPn3NiNXhzqJbX2yCzyWzQrIiPrK8l4MQyvfPFIil6AgM"

    status = ["What is going on at Everyday Computing?  Read our latest blog post:  https://blog.everydaycomputing.org/",\
    "Kids. Computers. Math. Read more about it at https://blog.everydaycomputing.org",\
    "Everyday Computing news: https://blog.everydaycomputing.org"]

    def post(self):
        """Tasks are only made on get() requests"""
        self.abort(405,hedears=[('Allow', 'GET')])

    def get(self):
        """Make sure requests coming from app engine"""
        if 'X-AppEngine-Cron' not in self.request.headers:
            self.error(403)

        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.token, self.token_secret)

        # Creation of the actual interface, using authentication
        api = tweepy.API(auth)

        # Sample method, used to update a status
        random_status = random.choice(self.status)
        api.update_status(random_status)

        sender = "Everyday Computing Bot <bot@everydaycomputingorg.appspotmail.com>"
        subject = "Tweet Sent - Daily"
        body = "Daily tweet sent: http://twitter.com/everydaycs/"
        try:
            mail.send_mail(sender=sender, to="abinkowski@uchicago.edu", subject=subject, body=body)
        except:
            logging.error(traceback.extract_stack())
