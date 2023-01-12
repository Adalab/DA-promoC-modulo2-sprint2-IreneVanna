from IPython.core.interactiveshell import InteractiveShell 
InteractiveShell.ast_node_interactivity = "all"

import requests
import pandas as pd
import numpy as np

import mysql.connector

pd.options.display.max_columns = None

class crear_insertar:

    def __init__(self,bbdd, contraseña):

        self.bbdd = bbdd
        self.contraseña = contraseña

    def crear_bbdd(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password= self.contraseña
        )
        print("Conexión realizada con éxito")
    
        mycursor = mydb.cursor()

        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.bbdd};")
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            
    def insertar_tabla(self, query):
        
        self.query = query 
    
        cnx = mysql.connector.connect(user='root', password=f"{self.contraseña}",
                                     host='127.0.0.1', database=f"{self.bbdd}")

        mycursor = cnx.cursor()
    
   
        try: 
            mycursor.execute(query)
            cnx.commit() 
    
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            

            #df_clima = pd.read_csv('datos/datos_clima.csv', index_col = 0)

def printear():
    
    df_ataque = pd.read_csv('DA-promoC-modulo2-sprint2-IreneVanna/datos/datos_limpiezaV.csv', index_col = 0)
    
    print(df_ataque.head(2))