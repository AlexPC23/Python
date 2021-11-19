# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:20:27 2021

@author: Alex
"""
import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos
import scipy.stats as stats                  #Tests estadisticos
import seaborn as sns                        #Graficos pro

os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

#Comparacion de medias  (Contraste entre variales cualitativas y cuantitativas)
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

#Ejemplo 2

plt.figure(figsize=(5,5))
ax=sns.pointplot(x="yr",y="cnt",data=wbr,ci=95,join=0)
ax.set_ylabel('')
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.xticks((0,1), ("2011", "2012"))
plt.xlabel('Year')
plt.title('Figure 7. Average rentals by Year.''\n')
plt.text(-0.35,5400,'Mean:4504.3''\n''n:731' '\n' 't:18.6' '\n' 'Pval.: 0.000',bbox=props)

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

#COMPARACION GRAFICA: intervalos de confianza para las medias

plt.figure(figsize=(5,5))
ax = sns.pointplot(x="weathersit", y="cnt", data=wbr, capsize=0.05, ci=99.9, join=0)
ax.set_ylabel('')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.5, 5000, 'Mean: 4504.3''\n''n: 731' '\n' 'F: 40.06''\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 8. Average rentals by Weather Situation.''\n')

#BOXPLOT GRAFICO
ax = sns.boxplot(x="weathersit", y="cnt", data=wbr)