# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:25:19 2021

@author: ingmar
"""

from mysql.connector import connect, Error

class Connexion:
    def __init__(self):
        self.connexionObject = self.initConnexion()
        
    def initConnexion(self):
        try :
            return connect(
                    host="localhost",
                    user="root",  
                    password="Password0!",
                    database="test_technique",)               
        except Error as e:
            print(e)
            
    def executeQuery(self,query) :
        try :
            with self.connexionObject.cursor() as cursor :
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
    
    def queryFromFile(self,file) :
        buffer = open(file,'r')
        query = buffer.read()
        return query

