from google.appengine.api import users
from google.appengine.ext import ndb
import logging

# from article_goals import *
from article_methodology import *

# class LearningGoal(ndb.Model):
#   """Learning Goals that are identified in article resource.
#   """
#   # The original domain is now referred to as a `concept`
#   domain = ndb.IntegerProperty(default=9)
#   # This is referred to as a domain
#   domainFromLiteratureReview = ndb.IntegerProperty(default=4)
#   page_number = ndb.StringProperty(default="")
#   goal = ndb.TextProperty(default="")
#   age_level = ndb.IntegerProperty(choices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], repeated=True)
#   #empirical_support = ndb.BooleanProperty(default=False)
#   support = ndb.IntegerProperty(default=3)
#   subgoals = ndb.TextProperty(default="")
#   relationships_goals = ndb.TextProperty(default="")
#   activity_origin = ndb.StringProperty(choices=['Custom','Pre-existing'], repeated=True)
#   activity_source = ndb.TextProperty(default="")
#   ccssm_domains = ndb.StringProperty(choices=['CC','OA','NBT','NF','MD','G'], repeated=True)
#   ccssm_cotent_standards = ndb.StringProperty(default="") # repeated??
#   ccssm_practice_standards = ndb.IntegerProperty(choices=[1,2,3,4,5,6,7,8], repeated=True)
#   ccssm_grades = ndb.IntegerProperty(choices=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], repeated=True)
#   cluster = ndb.StringProperty(repeated=True)
#   article = ndb.KeyProperty(kind='Article')

#   # new
#   programming_environment = ndb.TextProperty(default="")
#   contextual_approach = ndb.StringProperty(choices=['game design', 'storytelling', 'simulations', 'world-building'])
#   student_experience_level = ndb.StringProperty(choices=['none','some'])
#   duration_of_intervention = ndb.StringProperty(choices=["0-2", "3-10", "11-20", "21+"])
#   pacing_of_intervention = ndb.StringProperty(choices=["daily", "weekly", "monthly", "less than monthly"])
#   student_evidence_type = ndb.StringProperty(choices=["program analysis", "other work analysis", "performance on programming challenges", "paper and pencil assessment", "attitude surveys", "observation data", "interviews", "focus groups"])
#   experiment_duplication = ndb.BooleanProperty(default=False)
#   instructor = ndb.StringProperty(choices=["no instructor", "classroom teacher", "researcher"])
#   structured_vs_open_ended = ndb.StringProperty(choices=["structured", "hybrid", "open-ended projects"])

  # @staticmethod
  # def _pretty_grades(code):
  #     """Convert the numeric grade levels into a string"""
  #     if code == 0: return "K"
  #     if code > 0 and code < 13: return str(code)
  #     if code == 13: return "Elementary School"
  #     if code == 14: return "Junior High"
  #     if code == 15: return "Middle School"
  #     if code == 16: return "High School"

  # @property
  # def _domainFromLiteratureReview(self):
  #   """ Mapping of emergent domains (those that came from the literature review
  #       after the name "domain" was previously applied to the Grover and Pea
  #       domains
  #   """
  #   if self.domainFromLiteratureReview == 0: return 'Program development (Iterative development of computational solutions)'
  #   if self.domainFromLiteratureReview == 1: return 'Computing languages, environments, and constructs'
  #   if self.domainFromLiteratureReview == 2: return 'Algorithms (Flow of control)'
  #   if self.domainFromLiteratureReview == 3: return 'Applications of computing (Recognizing computational problems and interpreting computational results)'
  #   if self.domainFromLiteratureReview == 4: return 'None'

  # @property
  # def _article(self):
  #   """ Mapping of goal back to article.
  #   This should have been done initially as a many-to-many, but wasn't
  #   """

  #   #select * from Article WHERE learning_goals CONTAINS Key(LearningGoal, 4786706423218176)
  #   #article = ndb.GqlQuery("SELECT * from Article").fetch()
  #   art = ndb.gql("SELECT __key__ from Article WHERE learning_goals = :1", self.key).get()
  #   #.fetch()
  #   #"SELECT __key__ FROM Article WHERE learning_goals CONTAINS :1", self.key)

  #   return art.get().key.urlsafe()

  # @property
  # def _domain(self):
  #   """ Mapping so that we can freely change names at a later time

  #     Note: In all the documents moving forward from June, 2016,

  #     these are
  #     referred to as the "Concepts"
  #     """
  #   if self.domain == 0: return "Abstraction and pattern generalization"
  #   if self.domain == 1: return "Systematic processing of data"
  #   if self.domain == 2: return "Symbol systems and representations"
  #   if self.domain == 3: return "Algorithmic notions of flow of control"
  #   if self.domain == 4: return "Structured problem decomposition (modularizing)"
  #   if self.domain == 5: return "Iterative, recursive, and parallel thinking"
  #   if self.domain == 6: return "Conditional logic"
  #   if self.domain == 7: return "Efficiency and performance constraints"
  #   if self.domain == 8: return "Debugging and systematic error detection"
  #   if self.domain == 9: return "None"

  # @property
  # def _support(self):
  #   if self.support == 0: return 'Classroom Evidence'
  #   if self.support == 1: return 'Theoretical Evidence'
  #   if self.support == 2: return 'Theoretical Evidence'
  #   if self.support == 3: return 'None'

  # @staticmethod
  # def _ccssm_practice_standards(code):
  #   if code == 1: return "1. Make sense of problems and persevere in solving them."
  #   if code == 2: return "2. Reason abstractly and quantitatively."
  #   if code == 3: return "3. Construct viable arguments and critique the reasoning of others."
  #   if code == 4: return "4. Model with mathematics."
  #   if code == 5: return "5. Use appropriate tools strategically."
  #   if code == 6: return "6. Attend to precision."
  #   if code == 7: return "7. Look for and make use of structure."
  #   if code == 8: return "8. Look for and express regularity in repeated reasoning."



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
  """Model representing a resource type article
    Note: The key is the "id" from bibtex
"""
  # Entry metadata
  timestamp = ndb.KeyProperty(kind='Timestamp', repeated=True)

  # Article metadata
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

  # Summary data
  type = ndb.StringProperty(indexed=True,choices=['Theoretical','Empirical','Review Article','Taxonomy Development','Practitioner', 'Other'], repeated=True)
  star = ndb.BooleanProperty(indexed=True,default=False)
  purpose = ndb.TextProperty(default="")
  findings = ndb.TextProperty(default="")
  recommendations = ndb.StringProperty(default="")
  citation = ndb.TextProperty(default="")
  audience = ndb.StringProperty(choices=['Practitioner', 'Researcher', 'Developer', 'Administrator', 'Other'], repeated=True)
  #rating = ndb.StringProperty(choices=['Poor','OK','Good','Very Good','Great'])

  # Methodology
  methodology = ndb.KeyProperty(kind='Methodology')
  # learning_goals = ndb.KeyProperty(kind='LearningGoal', repeated=True)

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


  # @property
  # def _learning_goal(self):
  #   """
  #     if self.learning_goal == None:
  #     learning_goal = LearningGoal()
  #     else:
  #     learning_goal = self.learning_goal.get_multi()

  #     return learning_goal
  #     """
  #   return ndb.get_multi(self.learning_goal)




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
