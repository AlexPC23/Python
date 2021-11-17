# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:27:18 2021

@author: Alex
"""

reset -f

import os                                    
import pandas as pd                          
import numpy as np                           
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

#change working directory
os.chdir('C:/Programacion Estadistica PEP/tarea 1_data')
os.getcwd()

sales= pd.read_csv('vgsales.csv')

sales.dropna(subset=["Publisher"], inplace=True)
sales["Year"].fillna(sales["Year"].median(), inplace=True)
sales["Year"] = sales["Year"].astype("int64")

#Juegos producidos por año
plt.figure(figsize = (9,3.50))
plt.bar(sales["Year"].value_counts().index, sales["Year"].value_counts(), edgecolor='black', color='navy')
plt.title("Figura 1: Juegos producidos por año", fontsize=18)
plt.ylabel('Nuevos lanzamientos', fontsize=12.5) #dar nombre al eje y 
plt.xlabel('Años', fontsize=12.5) #dar nombre al eje x
plt.xticks(rotation=30)
plt.yticks(rotation=30)
plt.show()

#Géneros con el mayor número de juegos
plt.figure(figsize=(12,10))
plt.bar(sales["Genre"].value_counts().index, sales["Genre"].value_counts())
plt.xticks(rotation=45)
plt.title("Genres", size=15)
plt.show()

#Juegos producidos chulo
plt.figure(figsize=(18,6))
sns.countplot(sales["Year"])
plt.xticks(rotation=45, size=12)
plt.yticks(rotation=45, size=12)
plt.title("Figura 1: Juegos producidos por año", size=35)
plt.ylabel('Nuevos lanzamientos', fontsize=16.6) #dar nombre al eje y 
plt.xlabel('Años', fontsize=16.5) #dar nombre al eje x
plt.savefig('bar1.svg')
plt.show()


#Genero con mayor numero de juegos chulo
plt.figure(figsize=(18,6))
sns.countplot(sales["Genre"])
plt.xticks(rotation=0, size=10)
plt.yticks(rotation=45, size=12)
plt.title("Figura 2: Géneros con mayor número de juegos", size=35)
plt.ylabel('Número de juegos', fontsize=16.5) #dar nombre al eje y 
plt.xlabel('Géneros', fontsize=14) #dar nombre al eje x
plt.savefig('bar2.svg')
plt.show()


