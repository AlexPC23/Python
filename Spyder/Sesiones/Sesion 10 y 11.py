# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:02:27 2021

@author: Alex
"""

import os                                    #sistema operativo
import pandas as pd                          #gestionar datframes
import numpy as np                           #numeric python (vectores, matrices,...)
import matplotlib.pyplot as plt              #graficos
import scipy.stats as stats                  #Tests estadisticos
import seaborn as sns
from pandas.api.types import CategoricalDtype
!pip install stargazer
from stargazer.stargazer import Stargazer #Para comparar modelos de regresion 

os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')

x = wbr['temp_celsius']
y = wbr['cnt']

plt.scatter(x,y, s=20, facecolors='none', edgecolors='C0')

#REGRESION
from statsmodels.formula.api import ols

#MODELOS
model1 = ols('cnt ~ temp_celsius', data = wbr).fit()
print(model1.summary2())
#intercept es la prediccion para cuando el valor es 0
#el segundo coeficiente es cuanto se incrementa la variable target por cada incremento en 1 ud
#El p-value del segundo coeficiente IMPORTANTE

wbr.windspeed_kh.hist()
model2 = ols ('cnt~temp_celsius + windspeed_kh', data=wbr).fit()

model3 = ols('cnt~temp_celsius + windspeed_kh + hum', data=wbr).fit()

model4 = ols('cnt~temp_celsius + windspeed_kh + yr', data=wbr).fit()

model5 = ols ('cnt~temp_celsius + hum + workingday + windspeed_kh + yr', data=wbr).fit()

#STARGAZER
stargazer = Stargazer([model1,model2,model3])
stargazer.render_html()

dummies = pd.get_dummies(wbr.weathersit)
colnames = {1:'sunny', 2:'cloudy', 3:'rainy'}
dummies.rename(columns = colnames, inplace = True)
wbr = pd.concat([wbr,dummies], axis=1)

model6 = ols ('cnt~temp_celsius + hum + workingday + windspeed_kh + yr + cloudy + rainy', data=wbr).fit()
print(model6.summary2())

#
m=4500
print(m)
wbr.loc[(wbr['cnt']<m), 'goal'] = 0
wbr.loc[(wbr['cnt']>=m), 'goal'] = 1
plt.scatter(wbr.cnt, wbr.goal)

from statsmodels.formula.api import logit
model_l1 = logit('goal~temp_celsius', data=wbr).fit()
print(model_l1.summary2())

model_l7 = logit('goal~temp_celsius + hum + workingday + windspeed_kh + yr + cloudy + rainy', data=wbr).fit()
print(model_l7.summary2())
#aqui hay que mirar el coef y la P para ver la significatividad de que la probabilidad aumente o disminuya

#Ajustamos mejor la regresion 
wbr['temp_2'] = wbr.temp_celsius * wbr.temp_celsius
model_8 = ols('cnt~temp_celsius + hum + temp_2 + workingday + windspeed_kh + yr + cloudy + rainy', data=wbr).fit()
print(model_8.summary2())
