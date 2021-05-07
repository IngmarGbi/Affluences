# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:19:19 2021

@author: ingma
"""
import pandas as pd
import math

data = pd.read_csv("data.csv")
time = pd.read_csv("timetables.csv")
'''
print(type(data))
print(data.head(10))
print(time.head(10))
total = pd.merge(data,time, on="site_id",how="left")
#print(total.head(10))
print(len(data.index))
print(len(total.index))
print(data.site_id.unique())
total.sort_values(by=['site_id'])


print(len(data.sensor_identifier.unique()))
print(total.sensor_identifier.unique())

total.groupby(['sensor_identifier'],sort=False)['last_record_datetime'].max()

'''

total_df = data.groupby('sensor_identifier')
maximums = total_df.max()
maximums = maximums.reset_index()
print(maximums)

total = pd.merge(maximums,time, on="site_id",how="left")
print(total)

print(type(total.iloc[2]['opening_datetime']))

#for row in total.iterrows():
for row in total.head(5):
    value = row['opening_datetime']=='Nan'
    print(value)
        