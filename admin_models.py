from google.appengine.api import users
from google.appengine.ext import ndb


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
class Author(ndb.Model):
  """ Author of a paper """
  # As written in a bibtex format
  # Parsed from bibpy [{"author":[{"family": "Wing", "given": "Jeannette M"}],
  family_name = ndb.StringProperty(indexed=True)
  given_name = ndb.StringProperty(indexed=True)

  @property
  def name(self):
    return self.given_name+" "+self.family_name


class Greeting(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  author = ndb.StructuredProperty(Creator)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)

##
#
# {"items": [{"author":
#  [{"family": "Wing", "given": "Jeannette M"}], "volume": "49", "page": "33-35", "journal":
# "Communications of the ACM", "issued": {"literal": "2006"}, "title": "Computational thinking",
# "id": "wing2006computational", "type": "article", "number": "3"}]}
#
class Article(ndb.Model):
  """Sub model for representing an author."""
  creator = ndb.StructuredProperty(Creator)
  timestamp = ndb.DateTimeProperty(auto_now_add=True)
  
  author = ndb.KeyProperty(Author)
  
  journal = ndb.StringProperty(indexed=False)
  volume = ndb.StringProperty(indexed=False)
  number = ndb.StringProperty(indexed=False)
  pages = ndb.StringProperty(indexed=False)
  year = ndb.IntegerProperty(indexed=True)
