#
#  ENSEMBLE DE FONCTION PERMETTANT DE GERER LA BDD
#  Les variables d'environnements sont dans le fichier env
#
#   EXEMPLE CREATION CONNECTION : engine = create_engine('mysql+mysqlconnector://InfoFlower:Fleurs@127.0.0.1:3636/Data_Mining')
#   EXEMPLE CREATION DE TABLE : myd.to_sql(name='TD_datamining', con=engine, if_exists='replace', index=False)

pip install pandas
pip install mysql.connector
pip install sqlalchemy
import variables
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

engine_connexion= create_engine('mysql+mysqlconnector://InfoFlower:Fleurs@127.0.0.1:3636')