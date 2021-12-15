# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:59:03 2021

@author: Alex
"""

import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos
import scipy.stats as stats                  #Tests estadisticos
from pandas.api.types import CategoricalDtype

os.chdir('C:/Programacion Estadistica PEP/ejercicio correlacion')
os.getcwd()
wbr = pd.read_csv('auto-mpg.csv', sep=',', decimal='.')

#Describimos la variable cuantitativa horsepower
wbr.horsepower.describe()
wbr.info()
wbr['horsepower'].astype(object).astype(int)
x = wbr['horsepower']
plt.hist(x, bins=15, edgecolor='black')
plt.xlabel('Horse Power')
plt.xticks(np.arange(46, 230, step=25))
plt.ylabel('Frequency')
props = dict(boxstyle= 'round', facecolor='white', lw=0.5)
plt.text(180,60,'Mean:104.47''\n''n:392' '\n' 'std: 38.49', bbox=props)
plt.title('Figure: Number of cars by horsepower ''\n')
plt.show()

#Describimos la variable cuantitativa aceleración (cuanto tiempo tardan en llegar a 100 km/h)
wbr.acceleration.describe()
y = wbr['acceleration']
plt.hist(y, bins=15, edgecolor='black')
plt.xlabel('Acceleration')
plt.xticks(np.arange(8, 25, step= 3))
plt.ylabel('Frequency')
props = dict(boxstyle= 'round', facecolor='white', lw=0.5)
plt.text(21.5,40,'Mean:132.99''\n''n:46376' '\n' 'std: 75.45', bbox=props)
plt.title('Figure: Number of cars by acceleration ''\n')
plt.show()

plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')

#CORRELACION (primer numero correlacion lineal, el segundo p-value)
from scipy.stats.stats import pearsonr
pearsonr(x,y)
r, p_val = pearsonr(x,y)
print (r,p_val)
n = len (wbr)

#Tabla completa
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')
plt.title('Acceleration by horse power') #poner titulo 
plt.ylabel('Acceleration (time to reach 100 km/h)') #dar nombre al eje y 
plt.xlabel('Horse Power') #dar nombre al eje x
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (180,20.5, textstr , bbox=props)
plt.show()

