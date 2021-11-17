# -*- coding: utf-8 -*-

"""
Created on Fri Nov 12 16:48:58 2021

@author: Alex
"""

reset -f

import os                                    
import pandas as pd                          
import numpy as np                           
import matplotlib.pyplot as plt 

#change working directory
os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()

#Read data from CSV file
rentals_2011 = pd.read_csv('washington_bike_rentals_2011.csv', sep=';', decimal=',')

rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()
#QC OK

#Seleccionar las columnas
rentals_2011.cnt
np.mean(rentals_2011.cnt) #media (Variable cuantitativa)
np.std(rentals_2011.cnt)  #desviacion tipica (Variable cuantitativa)

rentals_2011.cnt.mean() #hacerlo directamente
rentals_2011.cnt.describe() #te lo da todo

#Describir  graficamente una variable 
plt.hist(rentals_2011.cnt) #Histograma (Variable cuantitativa)
rentals_2011.cnt.hist()

x=rentals_2011['cnt']

plt.hist(x,edgecolor='black', bins=20) #borde de color negro 
plt.xticks(np.arange(0,7000, step=1000)) #eje X 
plt.title('Figure 1. Registered rental in Washington') #poner titulo 
plt.ylabel('Frequency') #dar nombre al eje y 
plt.xlabel('Number of rentals') #dar nombre al eje x
plt.show()

#Expandiendo el dataset. Leer cdv del tiempo
weather_2011 = pd.read_csv('weather_washington_2011.csv', sep=';', decimal= ',')

del (x)

weather_2011.shape
weather_2011.head()
weather_2011.tail()
#QC OK

weather_2011.dtypes #tipos de datos en el dataframe

#Merge=unir, juntar dos archivos
rentals_weather_2011=pd.merge(weather_2011, rentals_2011, on='day')
rentals_weather_2011.shape
rentals_weather_2011.head()
del rentals_weather_2011['dteday_y'] #borrar columna

#Renombrar. Cambiar el nombre
rentals_weather_2011 = rentals_weather_2011.rename(columns={'dteday_x': 'dteday'})

#Añadir nuevas filas
rentals_weather_2012 = pd.read_csv('rentals_weather_2012.csv', sep=';', decimal= ',')
rentals_weather_2012.shape
rentals_weather_2012.head()

#Unir por abajo 
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012)

rentals_weather_11_12.shape
rentals_weather_11_12.head()
rentals_weather_11_12.tail()

#Simplificar el nombre del dataframe
wbr=rentals_weather_11_12
del rentals_weather_11_12

#Describir variable nominal 
mytable = wbr.groupby(['weathersit']).size()
print(mytable)

mytable.sum()

#Porcentajes
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)


#Grafica
plt.bar(mytable.index, mytable2)

#Barchart
#Hacer categorias
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2)
plt.ylabel('Percentage')
plt.title('Figure 1. Percentage of weather situation')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text(2,50, textstr, bbox=props)

#Guardar figuras
plt.savefig('bar1.eps')
plt.savefig('bar1.jpg')
plt.savefig('bar1.svg')
plt.show()


