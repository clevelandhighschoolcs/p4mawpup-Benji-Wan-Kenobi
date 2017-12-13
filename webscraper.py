import urllib2
import time

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
			print "The site has changed!"
			break
		else:
			lengthA = lengthB
			timeT += 1
			time.sleep(1)
			
		if timeT == sec:
			print "No changes were made."
	
WebData()
