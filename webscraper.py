import urllib2
import time

def WebData():
	
	link = raw_input "Paste URL here:"
	sec = int(raw_input("How many seconds do you want to test for? If you would like to run until a change is detected enter 0."))
	
	URL = urllib2.urlopen(link)
	data = URL.read()
	datastring = str(data)
	lengthA = len(datastring) # rename this to lengthA as in the algorithim it is first and is not consistent the alphabet sequentially 
	
	timeT = 0
	
	if sec == 0:
		while True:
	
			URL = urllib2.urlopen(link)
			data = URL.read()
			datastring = str(data)
			lengthB = len(datastring) # change to lengthB
		
			print "Testing..."
			if lengthA != lengthB:# respective A and B 
				print "The site has changed!"
				break
			else:
			 # this code is redundant, because length A does not equal lenght B  
				timeT += 1
				time.sleep(1)
		
	else:
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
				 # same here redundancy 
				timeT += 1
				time.sleep(1)
			
			if timeT == sec:
				print "No changes were made."
	
WebData()
