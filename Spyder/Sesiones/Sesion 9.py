# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:07:07 2021

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

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')

wbr.cnt.describe()

plt.hist(wbr['cnt'],edgecolor='black', bins=10) #borde de color negro 
plt.xticks(np.arange(0,10000, step=1000)) #eje X 
plt.title('Figure 1. Daily Bicycle rentals in Washington') #poner titulo 
plt.ylabel('Frequency') #dar nombre al eje y 
plt.xlabel('Number of rented bicycles') #dar nombre al eje x
plt.show()

#Descripcion temperatura

plt.hist(wbr['temp_celsius'],edgecolor='black', bins=10) #borde de color negro 
plt.title('Figure. Temperature in celsius') #poner titulo 
plt.ylabel('Frequency') #dar nombre al eje y 
plt.xlabel('Temperature in celsius') #dar nombre al eje x
plt.show()


x = wbr['temp_celsius']
y = wbr['cnt']

plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')

#CORRELACION (primer numero correlacion lineal, el segundo p-value)
from scipy.stats.stats import pearsonr
pearsonr(x,y)
r, p_val = pearsonr(x,y)
print (r,p_val)
n = len (wbr.cnt)

#Tabla completa
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')
plt.title('Daily bicycle rentals by temperature') #poner titulo 
plt.ylabel('Daily rentals') #dar nombre al eje y 
plt.xlabel('Temperature in celsius') #dar nombre al eje x
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

#Poner colores segun el año (c=wbr.yr)
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', c=wbr.yr)
plt.title('Daily bicycle rentals by temperature') #poner titulo 
plt.ylabel('Daily rentals') #dar nombre al eje y 
plt.xlabel('Temperature in celsius') #dar nombre al eje x
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()
#Por season
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', c=wbr.season)
plt.title('Daily bicycle rentals by temperature') #poner titulo 
plt.ylabel('Daily rentals') #dar nombre al eje y 
plt.xlabel('Temperature in celsius') #dar nombre al eje x
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

#Mismo ejercicio pero con windspeed
z = wbr['windspeed_kh']
plt.scatter(z,y, s=20, facecolors='none', edgecolors='C0')
pearsonr(z,y)
r, p_val2 = pearsonr(z,y)
print (r,p_val2)

plt.figure(figsize=(5,5))
plt.scatter(z,y, s=20, facecolors='none', c=wbr.yr)
plt.title('Daily bicycle rentals by windspeed') #poner titulo 
plt.ylabel('Daily rentals') #dar nombre al eje y 
plt.xlabel('Windspeed') #dar nombre al eje x
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (25,7000, textstr , bbox=props)
plt.show()