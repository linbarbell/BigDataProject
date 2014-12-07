
# coding: utf-8

# In[ ]:

import pandas as pd
import os


# In[2]:

trip_data = pd.read_csv("trip_data_with_geo_1.csv")
trip_fare = pd.read_csv("trip_fare_1.csv")


# Create unique trip_id for each row in both datasets for merging

# In[8]:

trip_data['trip_id'] = trip_data['medallion'] + '_' + trip_data['pickup_datetime']
trip_fare['trip_id'] = trip_fare['medallion'] + '_' + trip_fare['pickup_datetime']


# Merge both data sets

# In[15]:

merged_data = trip_data.merge(trip_fare, on="trip_id")


# In[35]:

merged_data.to_csv("merged_data_1.csv")


# Make column for fare percentage

# In[18]:

merged_data['fare_p'] = merged_data['tip_amount'] / merged_data['fare_amount']


# Find basic information about taxi rides in current data sets

# In[20]:

merged_data.describe()


# Find basic information about rides who pay with credit card (and, thus, tips)

# In[26]:

data_descr = merged_data.query("payment_type == 'CRD'").describe()


# In[25]:

neighborhood_descr = merged_data.groupby("pickup_neighborhood").describe()


# In[27]:

data_descr
neighborhood_descr


# Find basic information about rides by hour

# In[28]:

hour_descr = merged_data.groupby("pickup_hour").describe()


# In[34]:

hour_descr


# In[ ]:



