# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:33:13 2021

@author: Alex
"""

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


# Change working directory
os.chdir('C:/Programacion Estadistica PEP/code_and_data')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK


#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])

#######################
# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

#Crosstabultation (el orden importa)
##Primero  la variable dependiente y luego la independiente
pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins=True)*100
my_ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins=True)*100
round (my_ct,1) #Redondear función
my_ct.round(1) #Redondear, objeto
my_ct = round (my_ct,1)

#Test estadístico
ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat) #Tabla de contingencia
stats.chi2_contingency(ct)

#Transpose and plot
my_ct2 = my_ct.transpose()

my_ct2.plot(kind='bar', edgecolor = 'black', colormap = 'Blues')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.4, 81, 'Chi2: 4983''\n''n: 731' '\n' 'Pval.: 0.083', bbox=props)
plt.xlabel('Working Day')
plt.legend(['Low rentals','Average rentals','High rentals'])
plt.ylim(0,100)
plt.title('Figure. Percentage of Rental level, by Working Day.' '\n')
plt.xticks(rotation='horizontal')
