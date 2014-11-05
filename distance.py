#!/usr/bin/env python
# gives the distance between two places in kilometers
import simplejson, urllib
import sys

try:
	place1 = sys.argv[1]
	place2 = sys.argv[2]
except:
	print "Did you fill out two places as parameter?"
	sys.exit(1)

url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(place1,place2)
result= simplejson.load(urllib.urlopen(url))
#print result

#driving_time = result['rows'][0]['elements'][0]['duration']['value']
distance_meter = result['rows'][0]['elements'][0]['distance']['value']

print place1 + " ; " + place2 + " ; " + str(int(distance_meter / 1000))


