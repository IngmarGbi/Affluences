# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:19:19 2021

@author: ingma
"""
import pandas as pd
import math
from datetime import datetime, timedelta

#Récupération des données
data = pd.read_csv("data.csv")
time = pd.read_csv("timetables.csv")


analyse_date = datetime(2021, 5, 6, 16,0,0)


test_date = datetime(2021, 5, 6, 17,0,0)
print(test_date - analyse_date > timedelta(minutes=50))


#récupération de la dernière donnée par capteur
#Si un même capteur est placé sur 2 sites qui donnent des informations au même moment, les deux données sont conservées
dataMaxTime = data.groupby('sensor_identifier')['last_record_datetime'].transform(max) == data['last_record_datetime']
total = data[dataMaxTime]
#Jointure avec les horaires d'ouverture
total = pd.merge(total,time, on="site_id",how="left")
#Suppression des établissements sans info
isNa = pd.isna(total['opening_datetime'])
total= total[~isNa]

#Test comparaison date
analyse_date > datetime.strptime("2021-05-06 09:30:00", '%Y-%m-%d %H:%M:%S')
analyse_date < datetime.strptime("2021-05-06 12:30:00", '%Y-%m-%d %H:%M:%S')


#Lors de l'exécution il y a une erreur sur la comparaison des dates d'ouverture/fermeture, a finir

#Traitement des données correctes
for indice,row in total.iterrows():
    #Transtypage de la date de str en datetime
    record_datetime = datetime.strptime(row['last_record_datetime'], '%Y-%m-%d %H:%M:%S')
    delay = analyse_date - record_datetime
    #Etablissement ouvert
    if analyse_date > datetime.strptime(row['opening_datetime'], '%Y-%m-%d %H:%M:%S') and analyse_date < datetime.strptime(row['closing_datetime'], '%Y-%m-%d %H:%M:%S') :
        #Une alerte a lieu 
        if delay > timedelta(hours = 2) :
            msg1 = "Sensor "+ row['sensor_name']+" with identifier "+str(row['sensor_identifier'])+ " triggers an alerte at "+str(analyse_date)+" with level"
            msg2 = "with last data recorded at "+row['last_record_datetime']
            if delay >  timedelta(days=2) :
                print(msg1+" 3 "+msg2)
            elif delay > timedelta(days=1) :
                print(msg1+" 2 "+msg2)
            else :
                print(msg1+" 1 "+msg2)
    
            