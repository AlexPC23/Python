# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:54:52 2021

@author: Alex
"""

import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos
import scipy.stats as stats                  #Tests estadisticos
import seaborn as sns                        #Graficos pro

os.chdir('C:/Programacion Estadistica PEP/ejercicio comparacion medias')
os.getcwd()
wbr = pd.read_csv('USA_cars_datasets.csv', sep=',', decimal='.')
#Media del precio de los coches
wbr.price.describe()
plt.hist(wbr.price)
plt.xlabel('Price')
plt.ylabel('Frequency')
props = dict(boxstyle= 'round', facecolor='white', lw=0.5)
plt.text(55000,550,'Mean:18767.67''\n''n:2499' '\n' 'std:12116.09', bbox=props)
plt.title('Number of cars sold by price ''\n')
plt.show()


wbr.mileage.describe()
#Kilometraje coches
wbr.loc [(wbr['mileage']<50000), "mileage_cat2"] = "1: Poco kilometraje"
wbr.loc [(wbr['mileage']>=50000) & (wbr['mileage']<150000), "mileage_cat2"] = "2: Kilometraje normal"
wbr.loc [(wbr['mileage']>=150000), "mileage_cat2"] = "3: Alto kilometraje"

mytable = pd.crosstab(index=wbr["mileage_cat2"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

#2º Hacer el test
#Comparacion descriptiva:
wbr.groupby('mileage_cat2').price.mean()

#Comparacion estadistica:
#Extraer las muestras y guardalas en objetos:
price_pocoskm=wbr.loc [(wbr['mileage']<50000), "price"] 
price_normalkm=wbr.loc [(wbr['mileage']>=50000) & (wbr['mileage']<150000), "price"] 
price_muchoskm=wbr.loc [(wbr['mileage']>=150000), "price"]

#Hacer F DE FISHER de las medias para comparar
res = stats.f_oneway(price_pocoskm, price_normalkm, price_muchoskm)
#pvalue= 5.077309184346995e-110
print(res)
print('F:', round(res[0],3), 'PValue:', round(res[1],3))


#COMPARACION GRAFICA: intervalos de confianza para las medias

plt.figure(figsize=(7,5))
ax = sns.pointplot(x="mileage_cat2", y="price", data=wbr, capsize=0.05, ci=95, join=0)
ax.set_ylabel('')

plt.axhline(y=wbr.price.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.5, 5000, 'Mean:18767.67''\n''n:2499' '\n' 'F: 278.83''\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Kilometraje')
plt.title('Average rentals by mileage''\n')



