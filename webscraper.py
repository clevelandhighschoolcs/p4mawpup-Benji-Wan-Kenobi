import urllib2
import time
import requests
from twilio.rest import Client

account_sid = 'AC767817a5c1ed3e223e922a4927f402f4'
auth_token = '4c36bb4c4ea20b9ee027df992ed49de5'
twilio_phone_number = '+19718034163'
my_phone_number = '+15035454979'

def WebData():
	
	link = raw_input "Paste URL here:"
	sec = int(raw_input("How many seconds do you want to test for?"))
	
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
		
		print "Testing..."
		if lengthB != lengthA:
			body = "The site has changed!"
			client = Client(account_sid, auth_token)
			client.messages.create(
			body=body,
			to=my_phone_number,
			from_=twilio_phone_number
			)
			break
		else:
			lengthA = lengthB
			timeT += 1
			time.sleep(1)
			
		if timeT == sec:
			print "No changes were made."
	
WebData()
