from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import csv
import json
import sys
import time

geolocator = Nominatim()
with open('trip_data_example.csv', 'r') as csvin:
	with open('new_trip_data.csv', 'w') as csvout:
		reader = csv.DictReader(csvin)
		fieldnames=['medallion','hack_license','vendor_id','rate_code','store_and_fwd_flag','pickup_datetime','dropoff_datetime','passenger_count','trip_time_in_secs','trip_distance','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude', 'pickup_postcode', 'pickup_neighborhood', 'pickup_hour', 'dropoff_postcode', 'dropoff_neighborhood', 'dropoff_hour']
		writer = csv.DictWriter(csvout, fieldnames=fieldnames, delimiter=',')
		writer.writeheader()
		timeouterrors = 0
		locationerrors = 0
		rowcount = 0 if len(sys.argv) == 1 else int(sys.argv[1])
		for i in range(0,rowcount):
			print(i)
			row = next(reader)
		#row = next(reader)
		for row in reader:
			try:
				rowcount = rowcount + 1
				if rowcount % 1000 == 0:
					print('sleeping for 2 minutes pls wait')
					time.sleep(120)
				print(rowcount)
				pickup_location = geolocator.reverse(row['pickup_latitude'] + ', ' + row['pickup_longitude'])
				dropoff_location = geolocator.reverse(row['dropoff_latitude'] + ', ' + row['dropoff_longitude'])
				if 'pickup_datetime' in row:
					row['pickup_hour'] = row['pickup_datetime'].split(' ')[1].split(':')[0]
				if 'dropof_datetime' in row:
					row['dropoff_hour'] = row['dropoff_datetime'].split(' ')[1].split(':')[0]
				
				if 'error' in pickup_location.raw or 'error' in dropoff_location.raw:
					locationerrors = locationerrors + 1
					print('location finding error, continuing')
					continue

				if 'postcode' in pickup_location.raw['address']:	
					row['pickup_postcode'] = pickup_location.raw['address']['postcode']
				if 'postcode' in dropoff_location.raw['address']:
					row['dropoff_postcode'] = dropoff_location.raw['address']['postcode']

				if 'neighbourhood' in pickup_location.raw['address']:
					row['pickup_neighborhood'] = pickup_location.raw['address']['neighbourhood']
				if 'neighbourhood' in dropoff_location.raw['address']:
					row['dropoff_neighborhood'] = dropoff_location.raw['address']['neighbourhood']

				writer.writerow(row)
			except GeocoderTimedOut:
				timeouterrors = timeouterrors + 1
				print('geocoder timed out, continuing')
				continue
		print('timeout errors', timeouterrors)
		print('location errors', locationerrors)