__author__ = "Brewski"


import models
import database
import resident_view
import os, platform

def createNewResident():
	#need to finish this fucntion to add new residents and then make a function to delete them
	name = input('What is the name of the new resident?')
	email = input('What is the email of the new resident?')
	phone = input('What is the phone number of the new resident?')
	ip = input('What is the static IP address of the new resident?')
	mac = input('What is the mac address of the new resident?')
	newResident = models.Resident(name, email, phone, ip, mac)
	database.addResident(newResident)

def listAllResidents():
	residents = database.getAllResidents()
	resident_view.printAllResidents(residents)

def listFirstResident():
	resident = database.getFirstResident()
	resident_view.printResident(resident)

def listResidentByName():
	listAllResidentsData
	resident = database.getResidentByName(name)
	resident_view.printAllResident(resident)

def returnAllResidents():
	residents = database.getAllResidents()
	return residents

def returnResidentByName():
	name = input('What is the name of the resident you would like to get?')
	resident = database.getResidentByName(name)
	return resident

def updateResidentName():
	resident = database.getResidentByName()
	name = input('What is the new name of this user?')
	resident.name = name
	database.db_session.commit()

def deleteResident():
	database.deleteResident()

# resident monitor function ##############################################################################################################

def startResidentMonitor():

	# get list of residents from the database and iterate through them checking 
	# for their presence on the local network, based on their static IPs and a ping
	residents = database.returnAllResidents
	for resident in residents:
		# send resident to function that pings the IP and waits for a response
		ping(resident.ip)

	while True:
		time.sleep(1/5)

def ping(ipaddress):
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + ipaddress) == 0

