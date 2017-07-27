Start the Development Server
================================================================================
```
dev_appserver.py app.yaml
dev_appserver.py --clear_datastore=yes app.yaml
```

This was for the modules version (its somewhere in the git repo, possibly
  before the first big merge with dev (August 2, 2016)
dev_appserver.py dispatch.yaml app.yaml mobile_frontend.yaml static_backend.yaml admin.yaml

```
lsof -P | grep '8080' | awk '{print $2}' | xargs kill -9
```

Update Server
================================================================================
`cd` to the directory containing everydaycomputing.org/
  (probably ~/Development/GitHub)

```
cd ~/Development/GitHub
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.pyc update everydaycomputing.org/
appcfg.py update everydaycomputing.org/
```

## FOR MICROSERVICE ##
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py update backend-tools.yaml -A everydaycomputingorg -V 0

Set Credentials for Remote API
================================================================================
The .json file was downloaded from the console

```
export GOOGLE_APPLICATION_CREDENTIALS=/Users/tbinkowski/Development/GitHub/EverydayComputing/everydaycomputing.org/EverydayComputingOrg-a3501e320e92.json
```

Download the Datastore
================================================================================
```

export GOOGLE_APPLICATION_CREDENTIALS=./EverydayComputingOrg-a3501e320e92.json
/Applications/google-cloud-sdk/platform/google_appengine/appcfg.py
appcfg.py download_data --application=everydaycomputingorg --url=http://everydaycomputingorg.appspot.com/_ah/remote_api --filename=data.sql3
```

Upload the Datastore Backup to Local Development Server
================================================================================
You have to start the server to upload to the API.

```
dev_appserver.py --clear_datastore=yes app.yaml

gcloud auth login
gcloud auth print-access-token

appcfg.py upload_data  --oauth2_access_token=<oauth2_access_token> --filename=data_updated.sql3 --application=dev~everydaycomputingorg --url=http://localhost:58151/_ah/remote_api
```

Example
> With microservice do not need to specify the application.  It doesn't work.  I don't know
why.
```
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py upload_data --filename=data.sql3 --url=http://localhost:62342/_ah/remote_api --oauth2_access_token=ya29.Glz8A5pSeSMRAcZugWcS4fOgZi1OnGEPSMXdPvQlLynQQ2IHLvni6EiOF4CIz10gAn0WPhiS1EsZEFj6F17tvUC_GcQqJjWipMB2cVZVdwVCqjBvwC8YYnNbexOHDg
```
> Single service
```
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py upload_data --filename=data.sql3 --application=dev~everydaycomputingorg --url=http://localhost:52900/_ah/remote_api --oauth2_access_token=ya29.Glz8A5pSeSMRAcZugWcS4fOgZi1OnGEPSMXdPvQlLynQQ2IHLvni6EiOF4CIz10gAn0WPhiS1EsZEFj6F17tvUC_GcQqJjWipMB2cVZVdwVCqjBvwC8YYnNbexOHDg
 ```
# Update Downloaded Data to the Development Server #
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py upload_data --filename=data.sql3  --url=http://localhost:54606/_ah/remote_api --oauth2_access_token=ya29.Glz8A5pSeSMRAcZugWcS4fOgZi1OnGEPSMXdPvQlLynQQ2IHLvni6EiOF4CIz10gAn0WPhiS1EsZEFj6F17tvUC_GcQqJjWipMB2cVZVdwVCqjBvwC8YYnNbexOHDg



Post from Command Line
======================
curl -XPOST -H "Content-Type: application/json" --data @test.json http://localhost:8081


 {"items": [{"number": "1", "title": "A multidisciplinary approach towards computational thinking for science majors", "booktitle": "ACM SIGCSE Bulletin", "volume": "41", "issued": {"literal": "2009"}, "type": "inproceedings", "id": "hambrusch2009multidisciplinary", "author":
 [{"given": "Susanne", "family": "Hambrusch"},
  {"given": "Christoph", "family": "Hoffmann"},
  {"given": "John T", "family": "Korb"},
  {"given": "Mark", "family": "Haugan"},
  {"given": "Antony L", "family": "Hosking"}],
 "organization": "ACM", "page": "183-187"}]}



{u'booktitle': u'ACM SIGCSE Bulletin', u'title': u'Thinking about computational thinking', u'number': u'1', u'organization': u'ACM', u'author': [{u'family': u'Lu', u'given': u'James J'}, {u'family': u'Fletcher', u'given': u'George HL'}], u'id': u'lu2009thinking', u'type': u'inproceedings', u'page': u'260-264', u'issued': {u'literal': u'2009'}, u'volume': u'41'}
{u'number': u'1', u'title': u'Computational Thinking in K--12 A Review of the State of the Field', u'publisher': u'SAGE Publications', u'page': u'38-43', u'type': u'article', u'id': u'grover2013computational', u'author': [{u'family': u'Grover', u'given': u'Shuchi'}, {u'family': u'Pea', u'given': u'Roy'}], u'volume': u'42', u'issued': {u'literal': u'2013'}, u'journal': u'Educational Researcher'}


@article{crooks2004weblogo,
  title={WebLogo: a sequence logo generator},
  author={Crooks, Gavin E and Hon, Gary and Chandonia, John-Marc and Brenner, Steven E},
  journal={Genome research},
  volume={14},
  number={6},
  pages={1188--1190},
  year={2004},
  publisher={Cold Spring Harbor Lab}
}

@article{wing2006computational,
  title={Computational thinking},
  author={Wing, Jeannette M},
  journal={Communications of the ACM},
  volume={49},
  number={3},
  pages={33--35},
  year={2006}
}

@article{barr2011bringing,
  title={Bringing computational thinking to K-12: what is Involved and what is the role of the computer science education community?},
  author={Barr, Valerie and Stephenson, Chris},
  journal={Acm Inroads},
  volume={2},
  number={1},
  pages={48--54},
  year={2011},
  publisher={ACM}
}

##
#
# {"items": [{"author":
#  [{"family": "Wing", "given": "Jeannette M"}], "volume": "49", "page": "33-35", "journal":
# "Communications of the ACM", "issued": {"literal": "2006"}, "title": "Computational thinking",
# "id": "wing2006computational", "type": "article", "number": "3"}]}






#


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
  """
    Constructs a Datastore key for a Guestbook entity.
    We use guestbook_name as the key.
    """
  return ndb.Key('Guestbook', guestbook_name)

def article_key():
  """
    Constructs a Datastore key for a Guestbook entity.
    We use guestbook_name as the key.
    """
  return ndb.Key('Article', 'article')



#
#
# Main Page
#
#
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
    articles_query = Article.query().order(-Article.timestamp)
    articles = articles_query.fetch(10)
    logging.info("All articles")
    logging.info(articles)

    user = users.get_current_user()
    template_values = {
      'user': user,
      'articles': articles,
      #'greetings': greetings,
      #'guestbook_name': urllib.quote_plus(guestbook_name),
      'url': users.create_logout_url(self.request.uri),
      'url_linktext': "Logout"
    }

    template = JINJA_ENVIRONMENT.get_template('templates/admin.html')
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

    #guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
    #greeting = Greeting(parent=guestbook_key(guestbook_name))
    #greeting.content = self.request.get('content')

    if users.get_current_user():
      researcher = Researcher(identity=users.get_current_user().user_id(),email=users.get_current_user().email())

    self.bib2data(self.request.get('content'))
    researcher.put()

    query_params = {'guestbook_name': "guestbook_name"}
    self.redirect('/')#?' + urllib.urlencode(query_params))



  def bib2data(self,string):
    logging.info("enter bib2")
    # Parse the bibtex formatted string that is coming in from the request.
    # - Convert it to json
    # - Create Article
    # - Iterate through authors and create Author object
    # - Create the relationship between them in the AuthorArticle object
    bib = bibpy.Parser(self.request.get('content'))
    bib.parse()
    items = json.loads(bib.json())
    data = items["items"][0]
    logging.info(data)

    (article_key,article) = self.articleFromJSON(data)
    logging.info(article)
    """
      # Loop through and add all the authors
      for author in data['author']:
      # The unique key the author record can be referred by family_given
      key_name = author['family']+"_"+author['given']
      k = ndb.Key('Author',key_name)
      a = Author.get_or_insert(k.id(),family_name=author['family'],given_name=author['given'])
      if not article_key in a.articles:
      logging.info("HERE")
      a.articles.append(article_key)
      a.put()

      # Relationship stuff
      AuthorArticle(author=a.key,article=article.key).put()
      if not a.key in article.authors:
      article.authors.append(a.key)
      article.put()
      """


  def articleFromJSON(self,json):
    # Return the article_key and article object from a JSON dictionary.
    # Unique (I think) article name from bibtex
    #
    article_key = ndb.Key(Article,json['id'])
    article = Article.get_or_insert(article_key.id(),parent=article_key)

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
      # The unique key the author record can be referred by family_given
      #key_name = author['family']+"_"+author['given']
      #k = ndb.Key('Author',key_name)
      #a = Author.get_or_insert(k.id(),family_name=author['family'],given_name=author['given'])
      a = self.authorObjectFromName(author)
      if not article_key in a.articles:
        a.articles.append(article_key)
      a.put()

      # Relationship stuff
      AuthorArticle(author=a.key,article=article.key).put()
      if not a.key in article.authors:
        article.authors.append(a.key)

    article.put()
    return (article_key,article)


  def authorObjectFromName(self,author):
    key_name = author['family']+"_"+author['given']
    k = ndb.Key('Author',key_name)
    author = Author.get_or_insert(k.id(), family_name=author['family'],given_name=author['given'])
    return author




APP = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/sign', Guestbook),
                               ], debug=True)