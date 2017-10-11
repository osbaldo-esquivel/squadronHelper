# Osbaldo Esquivel
# 10AUG2016

import handlers
import webapp2


config = {'unit-info' : 'base-data'}

app = webapp2.WSGIApplication([
	('/', 'handlers.basepage'),
	
	('/aircraft/view', 'handlers.aircraftget'),
	('/aircraft/add', 'handlers.aircraftpost'),
	('/aircraft/update', 'handlers.aircraftput'),
	('/aircraft/delete', 'handlers.aircraftdelete'),
	
	('/user/view', 'handlers.userget'),
	('/user/add', 'handlers.userpost'),
	('/user/update', 'handlers.userput'),
	('/user/delete', 'handlers.userdelete'),
	
], debug=True, config=config)