# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:30:28 2021

@author: Alex
"""

reset -f
import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos

#change working directory
os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()

wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape
wbr.head
wbr.tail()


#QC OK

wbr.cnt.describe()
x=wbr['cnt']

plt.hist(x,edgecolor='black', bins=10) #borde de color negro 
plt.xticks(np.arange(0,10000, step=1000)) #eje X 
plt.title('Figure 1. Daily Bicycle rentals in Washington') #poner titulo 
plt.ylabel('Frequency') #dar nombre al eje y 
plt.xlabel('Number of rented bicycles') #dar nombre al eje x
plt.show()

#Guardar los resultados descriptivos en una lista
res = wbr.cnt.describe()
res[1]
m = res[1]
sd = res[2]
n = res[0]

#Subsetting (Elegir variables)
my_vars=['temp_celsius','cnt']
#Extraer variables y guardarlas
wbr_minimal=wbr[my_vars]

#Explore year
mytable = wbr.groupby(['yr']).size()
print(mytable)
wbr_2011 = wbr[wbr.yr == 0]
wbr_2011.cnt.describe()
plt.hist(wbr_2011.cnt)

#Ejercicio 1 (Ventas del invierno 2012)
wbr_winter_12 = wbr[(wbr.yr == 1) & (wbr.season == 1)] #subseting con dos condiciones PONER PARENTESIS
wbr_winter_12.shape
wbr_winter_12.cnt.describe()
plt.hist(wbr_winter_12.cnt)

#Ejercicio 1B (Describir ventas invierno y otoño)
wbr_fall_winter = wbr[(wbr.season ==1) | (wbr.season ==4)]
wbr_fall_winter.shape
wbr_fall_winter.cnt.describe()
plt.hist(wbr_fall_winter.cnt)

#Ejercicio 2 ()
import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos

os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()
wbr_ue = pd.read_csv('wbr_ue.csv', sep=';', decimal=',')
wbr_ue.temp_celsius.describe()

#Limpiar el dataset
wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99, np.nan)
wbr_ue.temp_celsius_c.describe()
plt.hist(wbr_ue.temp_celsius_c)

#Para las evita que salga error por los nan (dropna)
wbr_ue.temp_celsius_c.dropna()

#Nueva columna
wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)
plt.hist(wbr.cs_ratio)

wbr['cnt'] = (wbr.casual) + (wbr.registered)

#Recodificar variable (darle nombre a las estaciones del año)
wbr.loc[(wbr['season'] ==1), "season_cat"] = "Winter"
wbr.loc[(wbr['season'] ==2), "season_cat"] = "Spring"
wbr.loc[(wbr['season'] ==3), "season_cat"] = "Summer"
wbr.loc[(wbr['season'] ==4), "season_cat"] = "Fall"
#Despues de recodificar hacer QC
pd.crosstab(wbr.season, wbr.season_cat)

#Recodificar 2
wbr.cnt.describe()
wbr.loc [(wbr['cnt']<2567), "cnt_cat2"] = "1: Low rentals"
wbr.loc [(wbr['cnt']>=2567) & (wbr['cnt']<6442), "cnt_cat2"] = "2: Average rentals"
wbr.loc [(wbr['cnt']>=6442), "cnt_cat2"] = "3: High rentals"
#QC?
plt.scatter(wbr.cnt, wbr.cnt_cat2)
