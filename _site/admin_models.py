from google.appengine.api import users
from google.appengine.ext import ndb
import logging


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

  # Learning Goals
  domain = ndb.StringProperty(default="")
  goal = ndb.TextProperty(default="")
  age_level = ndb.IntegerProperty(choices=[0,1,2,3,4,5,6,7,8], repeated=True)
  empirical_support = ndb.BooleanProperty(default=False)
  subgoals = ndb.TextProperty(default="")
  relationships_goals = ndb.TextProperty(default="")
  activity_origin = ndb.StringProperty(choices=['Custom','Pre-existing'], repeated=True)
  activity_source = ndb.TextProperty(default="")
  ccssm_domains = ndb.StringProperty(choices=['CC','OA','NBT','NF','MD','G'], repeated=True)
  ccssm_cotent_standards = ndb.StringProperty(default="") # repeated??
  ccssm_practice_standards = ndb.IntegerProperty(choices=[1,2,3,4,5,6,7,8], repeated=True)


  # Methodology
  sample_size = ndb.IntegerProperty(default=0)
  sample_gender = ndb.StringProperty(choices=['Female','Male'], repeated=True)
  sample_ses = ndb.StringProperty(default="")
  sample_disability_status = ndb.StringProperty(choices=['Mild','Moderate','Severe'], repeated=True)
  sample_ethnicity = ndb.StringProperty(choices=['Caucasian', 'African American', 'Hispanic', 'Asian PI', 'Native American', 'Multiracial', 'Other'], repeated=True)
  sample_notes = ndb.StringProperty(default="")
  sample_participant_type = ndb.StringProperty(default="")
  sample_environment = ndb.StringProperty(choices=['in school', 'after school', 'informal setting'], repeated=True)
  sample_setting = ndb.StringProperty(choices=['rural', 'urban', 'public', 'private'], repeated=True)

  sample_size_of_school = ndb.IntegerProperty()
  sample_design = ndb.StringProperty(choices=['case study', 'qualitative', 'quanitative', 'other'], repeated=True)

  sample_data_collection_instrument = ndb.StringProperty(default="")
  sample_data_collection_procedure = ndb.StringProperty(default="")

  sample_data_analytic_technique = ndb.StringProperty(choices=['t-test', 'anova', 'regression', 'factor analysis', 'interviews', 'artifacts', 'other'], repeated=True)

  sample_effect_size = ndb.StringProperty(default="")
  sample_agreement = ndb.StringProperty(default="")



  @property
  def author_names(self):
    return ndb.get_multi(self.authors)
    #.query().filter(Person.guilds == self.key)





class LearningGoal(ndb.Model):
  """ 
  ""
  ""
  ""
  """
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








