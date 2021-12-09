# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:53:13 2021

@author: Alex
"""

import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos
import scipy.stats as stats                  #Tests estadisticos
from pandas.api.types import CategoricalDtype

#Cambiar el directorio donde esta el dataset
os.chdir('C:/Programacion Estadistica PEP/ejercicio comparacion medias')
os.getcwd()
wbr = pd.read_csv('USA_cars_datasets.csv', sep=',', decimal='.')

#HISTOGRAMA
plt.hist(rentals_2011.cnt) #Histograma (Variable cuantitativa)
rentals_2011.cnt.hist()

plt.hist(x,edgecolor='black', bins=20) #borde de color negro 
plt.xticks(np.arange(0,7000, step=1000)) #eje X 
plt.title('Figure 1. Registered rental in Washington') #poner titulo 
plt.ylabel('Frequency') #dar nombre al eje y 
plt.xlabel('Number of rentals') #dar nombre al eje x
plt.show()

#MERGE =unir, juntar dos archivos
rentals_weather_2011=pd.merge(weather_2011, rentals_2011, on='day')
del rentals_weather_2011['dteday_y'] #borrar columna

#Renombrar. Cambiar el nombre
rentals_weather_2011 = rentals_weather_2011.rename(columns={'dteday_x': 'dteday'})

#Añadir nuevas filas
rentals_weather_2012 = pd.read_csv('rentals_weather_2012.csv', sep=';', decimal= ',')

#Unir por abajo 
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012)

#Describir variable nominal 
mytable = wbr.groupby(['weathersit']).size()

#PORCENTAJES
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)

#GRAFICA DE BARRAS
plt.bar(mytable.index, mytable2)
#Hacer categorias
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2)
plt.ylabel('Percentage')
plt.title('Figure 1. Percentage of weather situation')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text(2,50, textstr, bbox=props)

#GUARDAR FIGURAS COMO FOTOS
plt.savefig('bar1.eps')
plt.savefig('bar1.jpg')
plt.savefig('bar1.svg')
plt.show()

#SUBSETTING (Elegir variables)
my_vars=['temp_celsius','cnt']

#LIMPIAR DATASET
wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99, np.nan)
wbr_ue.temp_celsius_c.describe()
plt.hist(wbr_ue.temp_celsius_c)

#Para las evita que salga error por los nan (dropna)
wbr_ue.temp_celsius_c.dropna()

#Nueva columna
wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)

#RECODIFICAR VARIABLE (darle nombre a las estaciones del año)
wbr.loc[(wbr['season'] ==1), "season_cat"] = "Winter"
wbr.loc[(wbr['season'] ==2), "season_cat"] = "Spring"
wbr.loc[(wbr['season'] ==3), "season_cat"] = "Summer"
wbr.loc[(wbr['season'] ==4), "season_cat"] = "Fall"
#Recodificar 2
wbr.cnt.describe()
wbr.loc [(wbr['cnt']<2567), "cnt_cat2"] = "1: Low rentals"
wbr.loc [(wbr['cnt']>=2567) & (wbr['cnt']<6442), "cnt_cat2"] = "2: Average rentals"
wbr.loc [(wbr['cnt']>=6442), "cnt_cat2"] = "3: High rentals"
#Recodificar a string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
#Despues de recodificar hacer QC

#ORDENAR LISTA PARA GRAFICA
#Definir la categoria especifica para nosotros
#1º Lista de las categorias ordenada
my_categories = ['Low rentals', 'Average rentals', 'High rentals']
#2º Definir nuevo tipo de datos
my_rentals_type = CategoricalDtype(categories=my_categories, ordered = True)
wbr['cnt_cat4'] = wbr.cnt_cat3.astype(my_rentals_type)

#COMPARACION DE MEDIAS  (Contraste entre variales cualitativas y cuantitativas)
#1º Describimos las variables
wbr.cnt.describe()
plt.hist(wbr.cnt)

mytable = pd.crosstab(index=wbr["workingday"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

#2º Hacer el test
#Comparacion descriptiva:
wbr.groupby('workingday').cnt.mean()
#Comparacion estadistica:
#Extraer las muestras y guardalas en objetos:
cnt_wd=wbr.loc[wbr.workingday==1, "cnt"] #primero variable nominal y luego la cuantitativa
cnt_nwd=wbr.loc[wbr.workingday==0, "cnt"]
#Hacer T TEST de las medias para comparar
#Importar la libreria scipy
res = stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
print (res[1]) #te da el p value (probabilidad de que no haya ninguna diferencia entre los grupos)

#Representar graficamente
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="workingday", y="cnt", data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle= 'round', facecolor='white', lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')

#COMPARCION CON MAS DE DOS GRUPOS

#Comparacion descriptiva:
wbr.groupby('weathersit').cnt.mean()

#Comparacion estadistica:
#Extraer las muestras y guardalas en objetos:
cnt_sunny=wbr.loc[wbr.weathersit==1, 'cnt']
cnt_cloudy=wbr.loc[wbr.weathersit==2, 'cnt']
cnt_rainy=wbr.loc[wbr.weathersit==3, 'cnt']
#Representamos en grafico de barras
mytable = pd.crosstab(index=wbr["weathersit"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])
#Hacer F DE FISHER de las medias para comparar
res = stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)
print(res)
print('F:', round(res[0],3), 'PValue:', round(res[1],3))

#BOXPLOT GRAFICO
ax = sns.boxplot(x="weathersit", y="cnt", data=wbr)

#CROSSTABULATION (el orden importa)
##Primero  la variable dependiente y luego la independiente
pd.crosstab(wbr.cnt_cat, wbr.weather_cat, normalize='columns', margins=True)*100
my_ct = pd.crosstab(wbr.cnt_cat, wbr.weather_cat, normalize='columns', margins=True)*100
round (my_ct,1) #Redondear función
my_ct.round(1) #Redondear, objeto
my_ct = round (my_ct,1)

#Test estadístico
ct = pd.crosstab(wbr.cnt_cat, wbr.weather_cat) #Tabla de contingencia
stats.chi2_contingency(ct)

#Transpose and plot
my_ct2 = my_ct.transpose()

#V de Cramer
from scipy.stats.contingency import association