# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:19:19 2021

@author: ingmar
"""
import pandas as pd
from MySqlConnexion import Connexion
from datetime import datetime,timedelta

class Alerte :
    
    def __init__(self,analyseDate) :
        self.DB = Connexion()
        self.analyseDate = analyseDate
        self.setAlerte()

    #Execution de requete et sauvegarde du resultat
    def createDF(self,file,columns) :
        query = self.DB.queryFromFile(file)
        result = self.DB.executeQuery(query)
        df = pd.DataFrame(columns = columns)
        for row in result:
            df = df.append(pd.Series(row,index=columns),ignore_index=True)
        return df
    
    def mergeDF(self,data,timetables,columnJoin) :
        #Fonction à faible valeur ajoutée => peut être supprimée ?
        #Les requêtes ont déjà permis les actions de la V1 : 
        #récupération dernière donnée des capteurs et des lieux non vide
        total = pd.merge(data,timetables, on=columnJoin,how="left")
        #Suppression des capteurs avec aucun établissement récupéré
        isNa = pd.isna(total['opening_datetime'])
        total= total[~isNa]
        return total
    
    def addDelay(self,data) :
        data['delay'] = self.analyseDate - data['last_record_datetime']
        #On trie par ordre croissant pour avoir les alarmes les plus importantes affichées en dernière 
        #donc lisible immédiatement
        data = data.sort_values(by='delay')
        return data
   
    def setAlerte(self) :
        #On considerera toujours les délais en heures, le délai le plus court = alerte niveau 1 ...Etc
        #Pourra être appelé et variabiliser si besoin
        #Considéré en Heures uniquement
        self.alertes = [2,24,48]
        self.alertes.sort()
        
    #ERREUR SUR ALERTE
    def analyseAlerte(self,data):
        self.setAlerte()
        data = self.addDelay(data)
        for indice,row in data.iterrows():
            #Etablissement ouvert
            if self.analyseDate > datetime.strptime(row['opening_datetime'], '%Y-%m-%d %H:%M:%S') and self.analyseDate < datetime.strptime(row['closing_datetime'], '%Y-%m-%d %H:%M:%S') :
                #Une alerte a lieu 
                index = 0
                while index < len(self.alertes) :
                    if row['delay'] > timedelta(hours = self.alertes[index]) :
                        index+=1
                    else :
                        break
                #Au moins 1 niveau d'alerte
                if index != 0 :
                    print("Sensor {} with identifier {} triggers an alerte at {} with level {}  with last data recorded at {}".format(row['sensor_name'],row['sensor_identifier'],self.analyseDate, index,row['last_record_datetime']))

if __name__ == "__main__":
    #Piste à améliorer : Colonnes des DF à récupérer via la requête
    columnsData = ["sensor_identifier","sensor_name","site_id","last_record_datetime"]
    columnsTimeTables = ["site_id","opening_datetime","closing_datetime"]
    alerte = Alerte(datetime(2021, 5, 6, 16,0,0))
    data = alerte.createDF('data.sql',columnsData)
    timetables = alerte.createDF('timetables.sql',columnsTimeTables)
    total = alerte.mergeDF(data,timetables,'site_id')
    alerte.analyseAlerte(total)
    
