from google.appengine.api import users
from google.appengine.ext import ndb
import logging



class Researcher(ndb.Model):
  """ Sub model for representing an the person who actually entered the data """
  identity = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)

class Greeting(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  author = ndb.StructuredProperty(Researcher)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)

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
  type = ndb.StringProperty(choices=['Article','Presentation','Standards Document','Curricular Materials','Link', 'Other'], repeated=True)
  researcher = ndb.KeyProperty(kind='Researcher')
  created = ndb.DateTimeProperty(auto_now_add=True)
  created_by = ndb.KeyProperty(kind='Researcher')
  audience = ndb.StringProperty(choices=['Practitioner', 'Researcher', 'Developer', 'Administrator', 'Other'], repeated=True)

class Article(ndb.Model):
  """ Sub model for representing an author.
  "   Note: The key is the "id" from bibtex
  """
  created = ndb.DateTimeProperty(auto_now_add=True)
  created_by = ndb.KeyProperty(kind='Researcher')
  updated = ndb.DateTimeProperty(auto_now=True)
  updated_by = ndb.KeyProperty(kind='Researcher')

  # Article fields
  authors = ndb.KeyProperty(kind='Author', repeated=True)
  title = ndb.StringProperty(indexed=False)
  journal = ndb.StringProperty(indexed=False)
  volume = ndb.StringProperty(indexed=False)
  number = ndb.StringProperty(indexed=False)
  pages = ndb.StringProperty(indexed=False)
  year = ndb.IntegerProperty(indexed=True)
  publisher =  ndb.StringProperty(indexed=False)
  
  #
  # Summary
  #
  star = ndb.BooleanProperty(indexed=True,default=False)
  purpose = ndb.TextProperty(default="")
  findings = ndb.TextProperty(default="")
  recommendations = ndb.TextProperty(default="")
  audience = ndb.StringProperty(choices=['Practitioner', 'Researcher', 'Developer', 'Administrator', 'Other'], repeated=True)
  #rating = ndb.StringProperty(choices=['Poor','OK','Good','Very Good','Great'])
  
  @property
  def author_names(self):
    return ndb.get_multi(self.authors)
    #.query().filter(Person.guilds == self.key)


class LearningGoal(ndb.Model):
  """
  "
  """
  created = ndb.DateTimeProperty(auto_now_add=True)
  created_by = ndb.KeyProperty(kind='Researcher')
  updated = ndb.DateTimeProperty(auto_now=True)
  updated_by = ndb.KeyProperty(kind='Researcher')



