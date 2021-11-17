# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:27:41 2021

@author: Alex
"""

#importar librerias 
import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos

#create a dataframe for the class
name = ['Yaling', 'Sofia', 'Maria', 'Pablo', 'Inés']
age = [28, 23, 25, 23, 25]
gender = ['Female', 'Female', 'Female', 'Male', 'Female']

print(name, age, gender)
class2020 = pd.DataFrame({'name' : name, 'age' : age, 'gender' : gender})
#limpieza
del (age, gender, name)
del (a)
del (b)

class2020.shape  #filas y columnas (dimensionalidad)
class2020.head(3)
class2020.tail(2)

#QC OK (para indicar que hasta aquí va bien)

edad = class2020.age
del(edad)

#Get working directory
os.getcwd()

#change working directory
os.chdir('C:/Programacion Estadistica PEP')
os.getcwd()

#Guardar dataframe (Excel)
class2020.to_excel('Class2020.xlsx')
class2020.to_csv('Class2020.csv')
