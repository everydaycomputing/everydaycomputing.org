from google.appengine.api import users
from google.appengine.ext import ndb
import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)



class Methodology(ndb.Model):
  """ """
  sample_size = ndb.IntegerProperty(default=0)
  sample_gender = ndb.StringProperty(choices=['female','male'], repeated=True)
  sample_ses = ndb.StringProperty(default="")
  sample_disability_status = ndb.StringProperty(choices=['Mild','Moderate','Severe'], repeated=True)
  sample_ethnicity = ndb.StringProperty(choices=['Caucasian', 'African American', 'Hispanic', 'Asian PI', 'Native American', 'Multiracial', 'Other'], repeated=True)
  sample_notes = ndb.StringProperty(default="")
  sample_participant_type = ndb.StringProperty(default="")
  sample_environment = ndb.StringProperty(choices=['in school', 'after school', 'informal setting'], repeated=True)
  sample_setting = ndb.StringProperty(choices=['rural', 'urban', 'public', 'private'], repeated=True)
  
  sample_size_of_school = ndb.IntegerProperty(default=0)
  sample_design = ndb.StringProperty(choices=['case study', 'qualitative', 'quanitative', 'other'], repeated=True)
  
  sample_data_collection_instrument = ndb.StringProperty(default="")
  sample_data_collection_procedure = ndb.StringProperty(default="")
  
  sample_data_analytic_technique = ndb.StringProperty(choices=['t-test', 'anova', 'regression', 'factor analysis', 'interviews', 'artifacts', 'other'], repeated=True)
  sample_data_analytic_technique_note = ndb.TextProperty(default="")
  
  sample_effect_size = ndb.StringProperty(default="")
  sample_agreement = ndb.StringProperty(default="")






