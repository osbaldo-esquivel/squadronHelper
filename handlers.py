# Osbaldo Esquivel
# 14JUL2016

import webapp2
import json
import models
from google.appengine.ext import ndb

# Function: Add an aircraft to the database
# Required: name, tail number, type
def addAircraft(name, num, type):
    key = ndb.Key(models.Aircraft, 'unit-info')
    newAir = models.Aircraft(parent=key)
    newAir.num = num
    newAir.type = type
	newAir.name = name
	
    keyAir = newAir.put()
    newAir.id = keyAir.id()
    keyAir = newAir.put()
    return keyAir.id()
	
def addUser(name,pwd,email,aircraft):
	key = ndb.Key(models.User, 'unit-info')
	newUser = models.User(parent=key)
	newUser.name = name
	newUser.pwd = pwd
	newUser.email = email
	newUser.aircraft = aircraft
	
	newUser.put()
	
# Function: Delete an aircraft from the database
# Required: id, type
def deleteAircraft(self, id, type):
    find = models.Aircraft.query(models.Aircraft.id == int(id)).get()
    if find:
        if find.type == int(type):
            request = models.Squadron.query(models.Squadron.request == int(id)).fetch()
            for r in request:
                for i, x in enumerate(r.request):
                    if x == int(id):
                        r.request.pop(i)
                        r.requester.pop(i)
                        r.put()
            find.key.delete()
            msg(self, 200, "The aircraft has been deleted")
        else:
            msg(self, 406, "That aircraft does not exist")
    else:
        msg(self, 404, "That aircraft does not exist")
    return
	
'''
# Function: Add a squadron to the database
# Required: name, city
def addSquadron(name, city):
    key = ndb.Key(models.Squadron, 'unit-info')
    newSquad = models.Squadron(parent=key)
    newSquad.name = name
    newSquad.city = city
	
    keySq = newSquad.put()
    newSquad.id = keySq.id()
    keySq = newSquad.put()
    return keySq.id()
'''

'''
# Class to define DELETE handler for a squadron
class squadrondelete(webapp2.RequestHandler):
    def delete(self):
        id = self.request.get('id')
        
		# if the id exists
        if id:
            find = models.Squadron.query(models.Squadron.id == int(id)).get()
            if find:
				# find the aircraft
                airFind = models.Aircraft.query(models.Aircraft.type == int(id)).fetch()
				# delete from database all aircraft
                if airFind:
                    for a in airFind:
                        deleteAircraft(self, a.id, int(id))
 
                request = models.Squadron.query(models.Squadron.requesters == int(id)).fetch()
				
				# delete squadron
                for r in request:
                    for i, x in enumerate(r.requesters):
                        if x == int(id):
                            r.requesters.pop(i)
                            r.request.pop(i)
                            r.put()
							
                find.key.delete()
				
                msg(self, 200, "The squadron has been deleted.") 
            else:
                msg(self, 404, "That squadron does not exist")
        else:
            msg(self, 406, "Error: You must provide the squadron ID")
'''

# Class to define the DELETE handler for aircraft
class aircraftdelete(webapp2.RequestHandler):
    def delete(self):
        type = self.request.get('id')
        id = self.request.get('aircraft')
        
		# if aircraft exists, delete it
        if id and type:
            deleteAircraft(self, id, type)
        else:
            msg(self, 406, "ID and type required")

'''
# Class to define GET handler for a squadron
class squadronget(webapp2.RequestHandler):
    def get(self):
        id = self.request.get('id')
        
		# if squadron exists, return info
        if id:
            find = models.Squadron.query(models.Squadron.id == int(id)).fetch()
            if find:
                find = models.Aircraft.query(models.Aircraft.type == int(id)).fetch()
                if find:
                    info = {}
                    for i, x in enumerate(find):
                        entry = x.to_dict()
                        del entry['type']
                        del entry['user']
                        info[i] = entry
                    self.response.status = 200
                    self.response.write(json.dumps(info))
                else:
                     info = {}
                     self.response.status = 200
                     self.response.write(json.dumps(info))
            else:
                msg(self, 404, "That squadron does not exist")
        else:
            msg(self, 406, "Error: You must provide a squadron ID")
'''

class userget(webapp2.RequestHandler):
	def get(self):
		name = self.request.get('name')
		pwd = self.request.get('pwd')
		
		find = models.User.query(models.User.name == name).fetch()
		
		if find:
			info = {}
			temp = 0
			for i, x in enumerate(find):
				entry = x.to_dict()
				info[temp] = entry
				temp += 1
			self.response.write(json.dumps(info))
		else:
			msg(self,404,"That user does not exist")
			
# Class to define GET handler for aircraft			
class aircraftget(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        active = self.request.get('active')
        id = self.request.get('id')
        
		# return if aircraft is active or return all
        if active:
            if name:
                find = models.Aircraft.query(models.Aircraft.active == True, models.Aircraft.name == name).fetch()
            else:
                find = models.Aircraft.query(models.Aircraft.active == True).fetch()
        else:
            if name:
                find = models.Aircraft.query(models.Aircraft.name == name).fetch()
            else:
                find = models.Aircraft.query().fetch()
        
		# return aircraft info
        if find:
            info = {}
            temp = 0
            for i, x in enumerate(find):
                entry = x.to_dict()
                if entry['type'] == int(id):
                    del entry
                else:
                    del entry['user']
                    del entry['type']
                    info[temp] = entry
                    temp += 1
            self.response.write(json.dumps(info))
        else:
            msg(self, 404, "Nothing to return")
 
''' 
# Class for POST handler for a squadron
class squadronpost(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        city = self.request.get('city')
		
		# if name and city provided, add squadron
        if name and city:
            key = addSquadron(name, city)
            msg(self, 200, key)

        elif name:
            msg(self, 406, "Error: You must provide a city")
        else:
            msg(self, 406, "Error: You must provide a name")
'''

class userpost(webapp2.RequestHandler):
	def post(self):
		name = self.request.get('name')
		pwd = self.request.get('pwd')
		email = self.request.get('email')
		aircraft = self.request.get('air')
		
	if name and pwd:
		addUser(name,pwd,email,aircraft)
		mess = "Added " + name
		msg(self,200,mess)
	else:
		msg(self, 406, "You must enter a name and password")
			
# Class for POST handler for aircraft
class aircraftpost(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        num = self.request.get('num')
        type = self.request.get('id')
        
		# if name, tail number, and type provided, add aircraft
        if name and num and type:
            addAircraft(name, int(num), int(type))
            mess = "Added " + name + " #" + num
            msg(self, 200, mess) 
        else:
            msg(self, 406, "You must provide the name, tail number, and type")

'''
# Class for PUT handler for a squadron
class squadronput(webapp2.RequestHandler):
    def put(self):
        name = self.request.get('name')
        city = self.request.get('city')
        id = self.request.get('id')
         
		 # if ID is provided, update name and/or city
        if id:
            find = models.Squadron.query(models.Squadron.id == int(id)).get()
            if find:
                if name:
                    find.name = name
                if city:
                    find.city = city
                find.put()
                msg(self, 200, "Squadron has been updated")
            else:
                msg(self, 404, "That squadron does not exist")
        else:
            msg(self, 406, "Error: You must provide a squadron ID")
'''

# Class for PUT handler for aircraft			
class aircraftput(webapp2.RequestHandler):                 
    def put(self):
        type = self.request.get('type')
        id = self.request.get('id')
        name = self.request.get('name')
        num = self.request.get('num')
        active = self.request.get('active')
    
		# if id and type provided, update name, active, or tail number
        if id and type:
            find = models.Aircraft.query(models.Aircraft.id == int(id)).get()
            if find:
                if find.type == int(find):
                    if name:
                        find.name = name
                    if num:
                        find.num = int(num)
                    if active:
                        if active == "True" or active == "true":
                            find.active = True
                        elif active == "False" or active == "false":
                            find.active = False
                        else:
                            msg(self, 400, "Active has an invalid status")
                    find.put()
                    msg(self, 200, "Aircraft has been updated")
                else:
                    msg(self, 406, "IDs could not be found")
            else:
                msg(self, 404, "That aircraft does not exist")
        else:
            msg(self, 406, "Error: You must provide an ID and type")
		
# Function: Display error message
# Required: error and message	
def msg(self, error, message):
    self.response.status = error
    self.response.write(message)
    return

# Class to display a basic message when user is at base page
class basepage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Nothing to display on base page. All your base are belong to us.")