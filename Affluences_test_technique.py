# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:19:19 2021

@author: ingma
"""
import pandas as pd
import math
from datetime import datetime

analyse_date = datetime(2021, 5, 6, 16,0,0)
print(analyse_date)
data = pd.read_csv("data.csv")
time = pd.read_csv("timetables.csv")


total_df = data.groupby('sensor_identifier')
maximums = total_df.max()
maximums = maximums.reset_index()
print(maximums)

total = pd.merge(maximums,time, on="site_id",how="left")
print(total)

print(type(total.iloc[2]['opening_datetime']))

test.head()

for indice,row in test.iterrows():
    #établissement sans info
    if math.isnan(row['opening_datetime']) or math.isnan(row['closing_datetime']) :
        continue
    
    '''
    else :
        delay = analyse_date - row['last_record_datetime']
        if delay > 7200 and analyse_date > row['opening_datetime'] and analyse_date < row['closing_datetime'] :
            if delay > 7200 * 24 :
                   print("Sensor "+ row['']+"with identifier {identifier} triggers an
                          alert at {alert datetime} with level {alert level} with last
                          data recorded at {last record datetime})#alerte 3
                   
            else :
                if delay > 7200 * 12 :
                    #alerte 2
'''
            