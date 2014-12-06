
import csv
import json
import sys
import time

neighborhoods = ['']

# get all the different unqiue neighborhoods and save it in a list

with open('new_trip_data_1_5.csv', 'r') as csvin:
		reader = csv.DictReader(csvin)

		for row in reader:
			found = False
			for hood in neighborhoods:
				if hood == row['dropoff_neighborhood']:
					found = True					
					break
						
			if found == False:
				neighborhoods.append(row['dropoff_neighborhood'])
				# writer.writerow({'neighborhood': row['dropoff_neighborhood']})


longitudes    = []
latitudes	  = []
counts        = []



for index in range(len(neighborhoods)):
	longitudes.append(float(0))
	latitudes.append(float(0))
	counts.append(float(0))

#calculate all the average x and y

with open('new_trip_data_1_5.csv', 'r') as csvin:
	with open('geolocator_data.csv', 'w') as csvout:
		reader = csv.DictReader(csvin)
		fieldnames=['neighborhood','longitude','latitude']
		writer = csv.DictWriter(csvout, fieldnames=fieldnames, delimiter=',')
		writer.writeheader()
		
		#calculation
		for row in reader:
			longitude = float(row['dropoff_longitude'])
			latitude  = float(row['dropoff_latitude'])
			hood      = row['dropoff_neighborhood']
			
			i = neighborhoods.index(hood)

			if counts[i] == 0:
				longitudes[i] = longitude
				latitudes[i] = latitude
				counts [i] = counts[i]+1
			elif counts[i] > 0:
				longitudes[i] = (longitude + (longitudes[i] * counts[i]))/(counts[i]+1)
				latitudes[i] = (latitude + (latitudes[i] * counts[i]))/(counts[i]+1)
				counts [i] = counts[i]+1

		#write into csv		
		for i in range(len(neighborhoods)):
			n =neighborhoods[i]
			lo = longitudes[i]
			la = latitudes[i]
			writer.writerow({'neighborhood': n,'longitude':lo,'latitude':la})

print (counts)
print (latitudes)
print (longitudes)





		