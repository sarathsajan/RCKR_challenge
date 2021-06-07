from math import radians, cos, sin, asin, sqrt
import requests
r = requests.get('https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json')

#print (r.json())
pop_limit = 1000
top_20 = []
for i in range(len(r.json())):
    if (r.json()[i]['population'] > pop_limit):
        top_20.append(r.json()[i])

top_20 = sorted(top_20, key=lambda x: x['population'], reverse=False)

top_20 = top_20[:20]

#for i in top_20:
    #print (i['population'], i['latlng'], i['name'])

#print ('\n\n\n')
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

distance_sum = 0.0
while top_20:
    country = top_20.pop(0)
    for i in top_20:
        #print (distance_sum)
        distance_sum = distance_sum + distance(round(country['latlng'][0], 2), round(i['latlng'][0], 2), round(country['latlng'][1], 2), round(i['latlng'][1], 2))
print (round(distance_sum, 2))
