# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:45:59 2021

@author: Alex
"""

import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos
import scipy.stats as stats                  #Tests estadisticos
import seaborn as sns
from pandas.api.types import CategoricalDtype

os.chdir('C:/Programacion Estadistica PEP/Trabajo final Spoty')
os.getcwd()
df_1 = pd.read_csv('spotify edited.csv', sep=';')

#Describimos la variable cuantitativa lyrics
df_1.lyrics.describe()

x = df_1['lyrics']
plt.hist(x, bins=15, edgecolor='black')
plt.xlabel('Lyrics')
plt.xticks(np.arange(0, 48, step=5))
plt.ylabel('Frecuencia')
props = dict(boxstyle= 'round', facecolor='white', lw=0.5)
plt.text(35,200,'Mean:8.36''\n''n:603' '\n' 'std: 7.48', bbox=props)
plt.title('Figura: Número de canciones por  ''\n')
plt.axvline(8.36, linewidth=1, linestyle='solid', color = 'red')
plt.axvline(0.88, linewidth=1, linestyle= 'dashed', color= 'green')
plt.axvline(15.84, linewidth=1, linestyle= 'dashed', color= 'green')
plt.show()

#Describimos la variable cuantitativa popularidad
df_1.popu.describe()

y = df_1['popu']
plt.hist(y, bins=15, edgecolor='black')
plt.xlabel('Popularidad')
plt.xticks(np.arange(0, 100, step= 10))
plt.ylabel('Frequency')
props = dict(boxstyle= 'round', facecolor='white', lw=0.5)
plt.text(12.5,100,'Mean:66.52''\n''n:603' '\n' 'std: 14.52', bbox=props)
plt.title('Figura: Número de canciones por popularidad ''\n')
plt.axvline(66.52, linewidth=1, linestyle='solid', color = 'red')
plt.axvline(52, linewidth=1, linestyle= 'dashed', color= 'green')
plt.axvline(81.04, linewidth=1, linestyle= 'dashed', color= 'green')
plt.show()

#CORRELACION (primer numero correlacion lineal, el segundo p-value)
from scipy.stats.stats import pearsonr
pearsonr(x,y)
r, p_val = pearsonr(x,y)
print (r,p_val)
n = len (df_1)

#Tabla completa
plt.figure(figsize=(5,5))
plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')
plt.title('Figura: Popularidad de las canciones por sus lyrics') #poner titulo 
plt.ylabel('Popularidad') #dar nombre al eje y 
plt.xlabel('Lyrics') #dar nombre al eje x
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (14,6, textstr , bbox=props)
plt.show()

