# Osbaldo Esquivel
# 10AUG2016

from google.appengine.ext import ndb

class Aircraft(ndb.Model):
	type = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    num = ndb.IntegerProperty(required=True)
    active = ndb.BooleanProperty(required=True, default=True)
    user = ndb.IntegerProperty()
	id = ndb.IntegerProperty()
	
class User(ndb.Model):
	name = ndb.StringProperty(required=True)
	pwd = ndb.StringProperty(required=True)
	email = ndb.StringProperty(default="None")
	aircraft = ndb.StringProperty(default="None")