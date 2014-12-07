import pandas as pd
import os

trip_data = pd.read_csv("trip_data_with_geo_1.csv")
trip_fare = pd.read_csv("trip_fare_1.csv")

# Create unique trip_id for each row in both datasets for merging
trip_data['trip_id'] = trip_data['medallion'] + '_' + trip_data['pickup_datetime']
trip_fare['trip_id'] = trip_fare['medallion'] + '_' + trip_fare['pickup_datetime']

# Merge both data sets
merged_data = trip_data.merge(trip_fare, on="trip_id")
merged_data.to_csv("merged_data_1.csv")

# Make column for fare percentage
merged_data['fare_p'] = merged_data['tip_amount'] / merged_data['fare_amount']

# Find basic information about taxi rides in current data sets
merged_data.describe()

# Find basic information about rides who pay with credit card (and, thus, tips)
data_descr = merged_data.query("payment_type == 'CRD'").describe()
neighborhood_descr = merged_data.groupby("pickup_neighborhood").describe()

data_descr
neighborhood_descr

# Find basic information about rides by hour
hour_descr = merged_data.groupby("pickup_hour").describe()
hour_descr