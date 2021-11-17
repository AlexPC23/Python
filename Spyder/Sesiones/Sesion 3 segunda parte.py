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