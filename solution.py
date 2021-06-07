from math import radians, cos, sin, asin, sqrt
import requests
r = requests.get('https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json')


#print (r.json())
pop_limit = 9856000
top_20 = []
for i in range(len(r.json())):
    if (r.json()[i]['population'] >= pop_limit):
        top_20.append(r.json()[i])

	
########################################################################################################
#TITLE : Ways to sort list of dictionaries by values in Python – Using lambda function
#SOURCE : https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/

top_20 = sorted(top_20, key=lambda x: x['population'], reverse=False)
########################################################################################################


top_20 = top_20[:20]
#for i in top_20:
    #print (i['population'], i['latlng'], i['name'])


#########################################################################################################
#TITLE : Program for distance between two points on earth
#SOURCE : https://www.geeksforgeeks.org/program-distance-two-points-earth/

def distance(lat1, lat2, lon1, lon2):
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * asin(sqrt(a))
	r = 6371
	return(c * r)
#########################################################################################################


distance_sum = 0.0
while top_20:
    country = top_20.pop(0)
    for i in top_20:
        #print (distance_sum)
        distance_sum = round(distance_sum + distance(country['latlng'][0], (i['latlng'][0]), country['latlng'][1], i['latlng'][1]), 2)

#Solution
print (round(distance_sum, 2))
