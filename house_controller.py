import models, database, resident_controller, zone_controller

import time
import datetime
from twilio.rest import TwilioRestClient



# house alarm related functions:

def sendSMS(note, residents):

	"""
	This function receives a string and sends it to residents as a text message.
	"""

	accountSID = 'AC4ef5b1267687ff3f1984829aa9e13f8b'
	authToken = 'afbcc30cede0b005efa5b9c20e365749'
	twilioCli = TwilioRestClient(accountSID, authToken)
	myTwilioNumber = '+15415000742'
	for resident in residents:
		mobile = str(resident.phone)
		message = twilioCli.messages.create(body = note, from_ = myTwilioNumber, to = mobile)
		time.sleep(0.01)


# house obj related functions:

def securityLogger():
	"""
	This function should take a data point every time its called.
	"""
	# take snapshot of every sensor and save their states/values
	timestamp = datetime.datetime.now()
	open_doors = zone_controller.doorCheck()
																	# take pictures with all cameras and sensors

	dp = models.Security_Data_Point(timestamp, open_doors)
	database.addDataPoint(dp)

def animals_are_fed(fed_am, fed_pm):
	feedpoint = models.Pet(fed_am, fed_pm)
	database.fedAnimals(feedpoint)

def createNewHouse(name, address):
	house = models.House(name, address)
	database.addHouse(house)
