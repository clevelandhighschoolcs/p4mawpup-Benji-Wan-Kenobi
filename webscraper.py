import urllib2
import time
from twilio.rest import Client

def WebData():
	
	link = raw_input ("Paste URL here:")
	sec = int(raw_input("How many seconds do you want to test for?"))
    
	while (test == False):
		my_phone_number = raw_input("input phone number for twilio to text (just numbers)")
		twilio_phone_number = raw_input("input phone number that twilio texts from (just numbers)")
		account_sid = raw_input("input account_sid")
		auth_token = raw_input("input auth_token")
		try:
			client = Client(account_sid, auth_token)
			client.messages.create(
				body='Test!',
				to=my_phone_number,
				from_=twilio_phone_number
			)
			test = True
		except Exception:
			print "Test message didn't work!"
	
	URL = urllib2.urlopen(link)
	data = URL.read()
	datastring = str(data)
	lengthB = len(datastring)
	
	timeT = 0
	
	while timeT < sec:
	
		URL = urllib2.urlopen(link)
		data = URL.read()
		datastring = str(data)
		lengthA = len(datastring)
		
		print("Testing...")
		if lengthB != lengthA:
			print("The site has changed!")
			client = Client(account_sid, auth_token)
			client.messages.create(
				body='There has been a change!',
				to=my_phone_number,
				from_=twilio_phone_number
			)
			break
		else:
			lengthA = lengthB
			timeT += 1
			time.sleep(1)
			
		if timeT == sec:
			print ("No changes were made.")
	
WebData()
