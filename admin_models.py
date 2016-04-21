from google.appengine.api import users
from google.appengine.ext import ndb
import logging

from article_goals import *
from article_methodology import *


class Researcher(ndb.Model):
  """ Sub model for representing an the person who actually entered the data """
  identity = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)


class Timestamp(ndb.Model):
  """ A versatile timestamp we can add to every class """
  created = ndb.DateTimeProperty(auto_now_add=True)
  created_by = ndb.KeyProperty(kind='Researcher')
  updated = ndb.DateTimeProperty(auto_now=True)
  updated_by = ndb.KeyProperty(kind='Researcher')


class Author(ndb.Model):
  """ Author of a resource from the bibtex format
    " As written in a bibtex format
    " Parsed from bibpy [{"author":[{"family": "Wing", "given": "Jeannette M"}],
    """
  family_name = ndb.StringProperty(indexed=True)
  given_name = ndb.StringProperty(indexed=True)
  articles = ndb.KeyProperty(kind='Article', repeated=True)
  
  @property
  def name(self):
    """ Easier way to refer to author """
    return self.given_name+" "+self.family_name


class Resource(ndb.Model):
  """ The base type for all entries in the database """
  types = ['Article','Presentation','Standards Document','Curricular Materials','Link', 'Other']
  timestamp = ndb.KeyProperty(kind='Timestamp', repeated=True)
  type = ndb.StringProperty(choices=types, repeated=True)
#audience = ndb.StringProperty(choices=['Practitioner', 'Researcher', 'Developer', 'Administrator', 'Other'], repeated=True)
#summary = ndb.KeyProperty(kind='Summary')


class Article(ndb.Model):
  """ Sub model for representing an author.
    "   Note: The key is the "id" from bibtex
    """
  timestamp = ndb.KeyProperty(kind='Timestamp', repeated=True)
  
  authors = ndb.KeyProperty(kind='Author', repeated=True)
  title = ndb.StringProperty(indexed=False)
  journal = ndb.StringProperty(indexed=False)
  volume = ndb.StringProperty(indexed=False)
  number = ndb.StringProperty(indexed=False)
  pages = ndb.StringProperty(indexed=False)
  year = ndb.IntegerProperty(indexed=True)
  publisher =  ndb.StringProperty(indexed=False)
  # link =
  # pdf =
  
  # Summary
  star = ndb.BooleanProperty(indexed=True,default=False)
  purpose = ndb.TextProperty(default="")
  findings = ndb.TextProperty(default="")
  recommendations = ndb.TextProperty(default="")
  audience = ndb.StringProperty(choices=['Practitioner', 'Researcher', 'Developer', 'Administrator', 'Other'], repeated=True)
  #rating = ndb.StringProperty(choices=['Poor','OK','Good','Very Good','Great'])
  
  # Methodology
  methodology = ndb.KeyProperty(kind='Methodology')
  learning_goals = ndb.KeyProperty(kind='LearningGoal', repeated=True)
  
  @property
  def author_names(self):
    return ndb.get_multi(self.authors)
  #.query().filter(Person.guilds == self.key)
  
  @property
  def _methodology(self):
    """ A shortcut for the methodology property that can be accessed from a 
    template so that we do not have to call get() in a template.
    """
    if self.methodology == None:
      methodology = Methodology()
      self.methodology = methodology.key
    else:
      methodology = self.methodology.get()
    return methodology
  
  
  @property
  def _learning_goal(self):
    """
    if self.learning_goal == None:
      learning_goal = LearningGoal()
    else:
      learning_goal = self.learning_goal.get_multi()
    
    return learning_goal
    """
    return ndb.get_multi(self.learning_goal)




class Timestamp(ndb.Model):
  """ """
  timestamp = ndb.KeyProperty(kind='Timestamp', repeated=True)
  created = ndb.DateTimeProperty(auto_now_add=True)
  created_by = ndb.KeyProperty(kind='Researcher')
  updated = ndb.DateTimeProperty(auto_now=True)
  updated_by = ndb.KeyProperty(kind='Researcher')


class Greeting(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  author = ndb.StructuredProperty(Researcher)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)




