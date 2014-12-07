import csv
import math

def distance(x1,y1,x2,y2):
	dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return dist

with open('trip_data_1.csv', 'r') as csvin, \
	 open('trip_data_example3.csv', 'w') as csvout:
		reader = csv.DictReader(csvin)
		fieldnames=['medallion','hack_license','vendor_id','rate_code', \
			'store_and_fwd_flag','pickup_datetime','dropoff_datetime', \
			'passenger_count','trip_time_in_secs','trip_distance','pickup_longitude', \
			'pickup_latitude','dropoff_longitude','dropoff_latitude', \
			'pickup_neighborhood', 'pickup_hour', 'dropoff_neighborhood', 'dropoff_hour']
		writer = csv.DictWriter(csvout, fieldnames=fieldnames, delimiter=',')
		writer.writeheader()
		rowcount = 0
		for row in reader:
			rowcount = rowcount + 1
			print(rowcount)
			if float(row['pickup_latitude']) == 0 \
				or float(row['pickup_longitude']) == 0 \
				or float(row['dropoff_latitude']) == 0 \
				or float(row['dropoff_longitude']) == 0 \
				or float(row['trip_time_in_secs']) == 0:
				continue

			min_pickup_distance = 100
			min_dropoff_distance = 100
			pickup_neighborhood = ''
			dropoff_neighborhood = ''
			with open('geolocator_data.csv', 'r') as geodata:
				data_reader = csv.DictReader(geodata)
				for data in data_reader:
					pickup_distance = distance(float(row['pickup_latitude']),\
						float(row['pickup_longitude']), float(data['latitude']), \
						float(data['longitude']))
					dropoff_distance = distance(float(row['dropoff_latitude']),\
						float(row['dropoff_longitude']), float(data['latitude']), \
						float(data['longitude']))
					
					if min_pickup_distance >= pickup_distance:
						min_pickup_distance = pickup_distance
						pickup_neighborhood = data['neighborhood']
					if min_dropoff_distance >= dropoff_distance:
						min_dropoff_distance = dropoff_distance
						dropoff_neighborhood = data['neighborhood']
			row['pickup_neighborhood'] = pickup_neighborhood
			row['dropoff_neighborhood'] = dropoff_neighborhood

			if 'pickup_datetime' in row:
				row['pickup_hour'] = row['pickup_datetime'].split(' ')[1].split(':')[0]
			if 'dropof_datetime' in row:
				row['dropoff_hour'] = row['dropoff_datetime'].split(' ')[1].split(':')[0]
			writer.writerow(row)