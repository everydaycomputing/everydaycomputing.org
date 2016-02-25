from google.appengine.api import users
from google.appengine.ext import ndb
import logging

class Creator(ndb.Model):
  """
    Sub model for representing an the person who actually entered the data
    """
  identity = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)

#
#
#
#
#
class Greeting(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  author = ndb.StructuredProperty(Creator)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)


#
#
#
#
#
class Author(ndb.Model):
  """ Author of a paper """
  # As written in a bibtex format
  # Parsed from bibpy [{"author":[{"family": "Wing", "given": "Jeannette M"}],
  family_name = ndb.StringProperty(indexed=True)
  given_name = ndb.StringProperty(indexed=True)

  # This is redundant
  articles = ndb.KeyProperty(kind='Article', repeated=True)

  @property
  def name(self):
    return self.given_name+" "+self.family_name

class Article(ndb.Model):
  # Sub model for representing an author.
  # Note: The key is the "id" from bibtex
  #
  #creator = ndb.StructuredProperty(Creator)
  timestamp = ndb.DateTimeProperty(auto_now_add=True)
  
  authors = ndb.KeyProperty(kind='Author', repeated=True)
  
  title = ndb.StringProperty(indexed=False)
  journal = ndb.StringProperty(indexed=False)
  volume = ndb.StringProperty(indexed=False)
  number = ndb.StringProperty(indexed=False)
  pages = ndb.StringProperty(indexed=False)
  year = ndb.IntegerProperty(indexed=True)
  publisher =  ndb.StringProperty(indexed=False)
  
  @property
  def author_names(self):
    return ndb.get_multi(self.authors)
    #.query().filter(Person.guilds == self.key)


class AuthorArticle(ndb.Model):
  #
  #
  author = ndb.KeyProperty(kind=Author,required=True)
  article = ndb.KeyProperty(kind=Article,required=True)




