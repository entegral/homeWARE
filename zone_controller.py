__author__ = "Brewski"

import models, database, zone_view, house_controller


# Create new zones
def createNewZone():
	name = input('What would you like to call the new zone?\n')
	gpio = input('What gpio would you like to give the new zone?\n')
	newZone = models.Zone(name= name, channel= gpio)
	database.addZone(newZone)
	message = " '%s' zone has been added to the database.\n " % (name)
	print (message)

def setupZones():
	# input specific data for each zone  
	numberofzones = input('how many zones would you like to setup?\n')
	current_zone = 0
	while current_zone <= int(numberofzones) - 1:
	    createNewZone()
	    current_zone = current_zone + 1


# Display/print Zone functions
def listAllZones():
	zones = database.getAllZones()
	zone_view.printZoneNames(zones)

def listFirstZone():
	zone = database.getFirstZone()
	zone_view.printZoneName(zone)

def listZoneByName():
	listAllZones()

	zone = database.getZoneByName(name)
	zone_view.printZoneName(zone)


# Read and/or return zone functions
def returnAllZones():
	zones = database.getAllZones()
	return zones

def returnZoneByName():
	listAllZones()
	name = input('What is the name of the zone you would like to get?\n')
	zone = database.getZoneByName(name)
	return zone	


# Update Zone functions
def updateZoneName():
	listAllZones()
	zone = database.getZoneByName()
	name = input("What would you like to rename '%s' to?\n" % (zone.name))
	zone.name = name
	database.db_session.commit()


# Delete Zone Functions
def deleteZone():
	name = input('What is the name of the zone you would like to delete?\n')
	database.deleteZone(name)



# zone monitor functions

def startZoneMonitor():
	
	zones = database.returnAllZones
	for zone in zones:
		GPIO.add_event_detect(zone.channel, GPIO.RISING, callback=doorClosed())
		GPIO.add_event_detect(zone.channel, GPIO.FALLING, callback=doorOpened())
	while True:
		time.sleep(300)





def doorOpened(residents_at_home):
	datapoint = Data_Point()
	print ("AYYYYE, THE BLAST DOOR HAS BEEN BREACHED!!!")
	residents_at_home = resident_controller.residentsAtHome()
	if residents_at_home == False:
		print ('Flint be taking the ship! Arm yourself laddies!')
		house_controller.broadcastSMS('Wake up lads! Flint has boarded the ship!', database.getAllResidents())
		# house = House()  <-------- eventually this will take a snapshot of every camera and sensor of the house and persist it to the database
	else:
		pass


def doorClosed():
	print ("Ayyyyyyye, de doors be more lonely than a whooooores tit.")



