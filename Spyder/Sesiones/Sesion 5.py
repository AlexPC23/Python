# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:06:51 2021

@author: Alex
"""

import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos

os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
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
#QC
plt.scatter(wbr.cnt, wbr.cnt_cat2)

#Porcentajes

mytable = wbr.groupby(['cnt_cat2']).size()
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
bar_list = ['Low rentals', 'Average rentals', 'High rentals']
plt.bar(bar_list, mytable2)

#Recodificar 3
wbr.cnt.describe()
wbr.loc [(wbr['cnt']<2567), "cnt_cat3"] = "Low rentals"
wbr.loc [(wbr['cnt']>=2567) & (wbr['cnt']<6442), "cnt_cat3"] = "Average rentals"
wbr.loc [(wbr['cnt']>=6442), "cnt_cat3"] = "High rentals"
#Porcentajes

mytable = wbr.groupby(['cnt_cat3']).size()
print(mytable)
mytable.sum()

#Porcentajes
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)


#Grafica
plt.bar(mytable.index, mytable2)

wbr.dtypes #descripción de las columnas

#Para definir variables categoricas
#Importar funcionalidad
from pandas.api.types import CategoricalDtype
#Definir la categoria especifica para nosotros
#1º Lisra de las categorias ordenada
my_categories = ['Low rentals', 'Average rentals', 'High rentals']
#2º Definir nuevo tipo de datos
my_rentals_type = CategoricalDtype(categories=my_categories, ordered = True)
wbr['cnt_cat4'] = wbr.cnt_cat3.astype(my_rentals_type)


mytable = wbr.groupby(['cnt_cat4']).size()
print(mytable)
mytable.sum()

#Porcentajes
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)
#Grafica de barras
plt.bar(mytable.index, mytable2)




