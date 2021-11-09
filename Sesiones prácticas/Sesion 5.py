import pandas as pd


#CSV
pokemon_df = pd.read_csv('pokemon_data.csv', dtype={'Name': str, 'Type 1':str, 'Speed':int, 'Generation':str})

#EXCEL
#pokemon_df_excel = pd.read_excel('pokemon_data.xlsx')

#TXT con tabulación
#pokemon_df_txt = pd.read_csv('pokemon_data.txt', delimeter='\t')

print(pokemon_df)
print(pokemon_df.head(5))
print(pokemon_df.tail(5))

'''
Obtener nombre de las columnas
'''
print(pokemon_df.columns)

'''
Obtener todos los valores de la columna name
'''
print(pokemon_df['Name'])

'''
Obtener todos los nombres y velocidades
'''
print(pokemon_df[['Name','Speed']])

'''
Los cinco primero nombres
'''
primeros_5 = pokemon_df['Name'][0:5]
print(primeros_5)

'''
Obtener filas
'''
print('Fila 1: ')
print(pokemon_df.iloc[0])

'''
Obtener varias filas
'''
print('Fila 1 hasta la 3: ')
print(pokemon_df.iloc[0:3])

'''
Obtener el nombre de la fila 1
'''
print(pokemon_df.iloc[0][1])

'''
Iterar por todos y mostrar el indice y nombre de cada
'''
for i, pokemon in pokemon_df.iterrows():
  print(i, pokemon['Name'])

'''
Obtener los pokemons tipo agua
'''
print(pokemon_df.loc[pokemon_df['Type 1'] == 'Water'])

'''
Estadisticas
'''
print(pokemon_df.describe())

'''
Ordenacion 
'''
print(pokemon_df.sort_values('Name', ascending= True))

'''
Ordenacion mas compleja
'''
print(pokemon_df.sort_values(['Type 1', 'HP'], ascending=[True, False])[['Name', 'Type 1', 'HP']])

'''
Crear una columna extra calculada
'''
pokemon_df['Total']  = pokemon_df['HP'] + pokemon_df['Attack'] + pokemon_df['Speed']
print(pokemon_df['Total'])