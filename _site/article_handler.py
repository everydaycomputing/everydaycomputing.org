"""Hello world application."""

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import routes

import jinja2
import webapp2
import json
import logging

# Custom imports
from admin_models import *
from admin_category import *
import bibpy


JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
DEFAULT_ARTICLE_KEY = 'article'

# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
  """Constructs a Datastore key for a Guestbook entity.
  We use guestbook_name as the key.
  """
  return ndb.Key('Guestbook', guestbook_name)

def article_ancestor_key():
  """
  Constructs a Datastore key for a Guestbook entity.
  We use guestbook_name as the key.
  """
  return ndb.Key(Article, 'article')



#
#
# Main Page
#
#
"""
class MainPage(webapp2.RequestHandler):
  
  def get(self):
    #
    #
    #
    #guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
    #greetings_query = Greeting.query(ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
    #greetings = greetings_query.fetch(10)
    #logging.info(greetings)
    
    # Fetch all articles
    articles_query = Article.query(ancestor=article_ancestor_key()).order(-Article.timestamp)
    articles = articles_query.fetch(10)
    
    template_values = {
      'user': users.get_current_user(),
      'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }
    
    template = JINJA_ENVIRONMENT.get_template('admin.html')
    self.response.write(template.render(template_values))
"""
#
#
#
#
#
#
class ArticleInsertHandler(webapp2.RequestHandler):
  def post(self):
    """We set the same parent key on the 'Greeting' to ensure each
    Greeting is in the same entity group. Queries across the
    single entity group will be consistent. However, the write
    rate to a single entity group should be limited to
    ~1/second.
    """
    #guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
    #greeting = Greeting(parent=guestbook_key(guestbook_name))
    #greeting.content = self.request.get('content')
    #greeting.put()
    
    
    researcher = Researcher(identity=users.get_current_user().user_id(),\
      email=users.get_current_user().email())
    researcher.put()
  
    data = self.bib2data(self.request.get('content'))
    (article_key,article) = self.articleFromJSON(data)
    logging.info(article)
    
    query_params = {'guestbook_name': "guestbook_name"}
    self.redirect('/article/')  #?' + urllib.urlencode(query_params))

  
  def bib2data(self,string):
    """
    """
    logging.info("enter bib2")
    # Parse the bibtex formatted string that is coming in from the request.
    # Convert it to json
    # Create Article
    # Iterate through authors and create Author object
    # Create the relationship between them in the AuthorArticle object
    bib = bibpy.Parser(self.request.get('content'))
    bib.parse()
    items = json.loads(bib.json())
    data = items["items"][0]
    return data

  def articleFromJSON(self,json):
    # Return the article_key and article object from a JSON dictionary.
    # Unique (I think) article name from bibtex
    #
    article_key = ndb.Key(Article,json['id'])
    article = Article.get_or_insert(article_key.id(),parent=article_ancestor_key())
    
    if 'title' in json: article.title=json['title']
    if 'journal' in json: article.journal=json['journal']
    if 'volume' in json: article.volume=json['volume']
    if 'number' in json: article.number=json['number']
    if 'page' in json: article.pages=json['page']
    if 'issued' in json: article.year=int(json['issued']['literal'])
    if 'publisher' in json: article.publisher=json['publisher']
    if 'booktitle' in json: article.booktitle=json['booktitle']
    if 'organization' in json: article.organization=json['organization']

    for author in json['author']:
      a = self.authorObjectFromName(author)
      if not article_key in a.articles:
        a.articles.append(article_key)
      a.put()
      
      #AuthorArticle(author=a.key,article=article.key).put()
      if not a.key in article.authors:
        article.authors.append(a.key)

    article.put()
    return (article_key,article)
 
  
  def authorObjectFromName(self,author):
    # Create (or retrieve) an author object from a dictionary of author data
    # that is passed from bibtex input.  The key is contstructed from the
    # name combinations.
    # Todo: There is a chance that someone might have identical names, so we
    # may want to use a unique id instead
    logging.info(author)
    key_name = author['family']+"_"+author['given']
    k = ndb.Key('Author',key_name)
    author = Author.get_or_insert(k.id(), \
      family_name=author['family'], \
      given_name=author['given'])
    return author


class ArticleHandler(webapp2.RequestHandler):
  def get(self):
    """
    """
    # Fetch all articles
    articles_query = Article.query(ancestor=article_ancestor_key())#.order(-Article.timestamp.created)
    articles = articles_query.fetch(10)
    
    template_values = {
      'url': self.request.application_url,
      'user': users.get_current_user(),
      'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }
    
    template = JINJA_ENVIRONMENT.get_template('templates/article.html')
    self.response.write(template.render(template_values))






