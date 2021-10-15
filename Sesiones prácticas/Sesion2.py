'''¡Palabras clave en Python!
Estas palabras no se deben usar si no es para el uso que tiene el lenguaje establecido

- and
- as
- assert (testing)
- break (para salir del bucle)
- class (declarar clases)
- continue 
- def (definir función)
- del
- elif
- else
- except
- exec
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- return
- try
- while
- with
- yield
- True
- False
- None
'''

'''
OPERADORES
'''
# Operadores Numéricos


# Operadores de Texto

nombre: str = "Martín"
apellidos: str = "San José de Vicente"  
# Concatenación
nombre_completo: str = nombre + " " + apellidos
print(f"> Nombre completo: {nombre_completo}")  
# Repetición
nombre_x5: str = nombre*5
print(f"> Nombre 5 veces: {nombre_x5}")

# Operadores de Comparación y de Identidad
c: int = 3
d: int = 3
e: int = 4

# Igualdad - Nos devolverá True o False
print(f"> ¿3 y 3 son iguales? {c is d}") # Operador Identidad
print(f"> ¿3 y 3 son iguales? {c == d}")
print(f"> ¿3 y 4 son iguales? {c is e}") # Operador Identidad

# Desigualdad - Nos devolverá True o False
print(f"> ¿3 y 3 no son iguales? {c is not d}") # Operador Identidad
print(f"> ¿3 y 4 no son iguales? {c is not e}") # Operador Identidad
print(f"> ¿3 y 3 no son iguales? {c != d}")

# Operadores Lógicos

# And (y)
print(f"> Verdadero y Verdadero = {True and True}")
print(f"> Verdadero y Falso = {True and False}")
print(f"> Verdadero y 1 = {True and 1}")
print(f"> Falso y Falso = {False and False}")
print(f"> Falso y 0 = {False and 0}")
print(f"> Falso y None = {False and None}")

# Operadores de Pertenencia

mi_texto:str = "Lorem ipsum dolor sit amet consectetur adipiscing elit dui odio"
mi_sub_texto: str = "amet"
mi_otro_sub_texto: str = "pepito"

# Pertenece
print(f"> ¿amet está dentro del mi_texto?: {mi_sub_texto in mi_texto}")
# No Pertenece
print(f"> ¿pepito no está dentro de mi_texto?: {mi_otro_sub_texto not in mi_texto}")

# Operadores de Asignación


# Operadores de Bits




'''
CONDICIONALES
'''
# IF


# IF - ELSE


# IF - ELIF - ELSE

'''En Python, la estructura es con "elif" y no con "else if"''' 
miEdad: int = 30
if (miEdad >= 60):
  print('Apuntarse al gym')
elif (miEdad < 60 and miEdad > 30):    
  print ('Adulto maduro')
elif (miEdad == 30):    
  print ('Adulto en su sweet moment')
elif (miEdad < 30 and miEdad >= 18):    
  print ('Adulto joven, todo en orden')
else:    print ('¡A clase!')

# SWITCH CASE ----> ¡¡¡¡¡ PYTHON NO DISPONE DE UN SWITCH CASE como otros lenguajes !!!!!


'''
BUCLES
'''
# Variables Globales para el programa


# Inicialización de Variables


# Bucle FOR para sacar valores del 0 al 100

for i in range (101):
  print (i)

# Bucle FOR sacar los elementos pares e impares de la lista

lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):        
    print(f'{elemento} es par')    
  else:        
    print(f'{elemento} es impar')

# Bucle WHILE para encontrar eliminar elementos hasta que la longitud sea 3

lista = [1,2,3,4,5,6,7,8] 
# Bucle WHILE para encontrar eliminar elementos hasta que la longitud sea 3
while (len(lista) > 3):    
  lista.pop()    
  print(lista)

# Python NO CUENTA con bucles DO - WHILE, pero se pueden simular:

# Bucle WHILE INFINITO - ¡OJO!

# ¡Bucle INFINITO! Mucho cuidado


'''
FUNCIONES
'''
# Funciones básicas

# Función Básica
def miFuncion():  
  print(f"Esto es una función básica") 

  miFuncion()


# Función con Parámetros No Tipados
	
def miFuncionConParametros(a,b):
    print(f"¡{a}, {b}!")
 
 
# llamando la función y pasándole algunos parámetros
miFuncionConParametros('Hola', 'Mundo')
miFuncionConParametros('Adios','Mundo')
miFuncionConParametros(1,2)

# Función con Parámetros Tipados
def miFuncionConParametrosTipados(a: str, b: str) :
    print(f"¡{a}, {b}!")
 
 
# llamando la función y pasándole algunos
# parámetros tipados
miFuncionConParametrosTipados('Hola', 'Mundo')

# Función con parámetros por defecto
# Si un valor no viene, se pone por defecto
def miFuncionConParametrosPorDefecto(a, b = 1) :
    print(f"La división es {a/b}")
 
 
# llamando la función y pasándole los dos parámetros
miFuncionConParametrosPorDefecto(3, 4)
# llamando la función y pasándole un único parámetro
miFuncionConParametrosPorDefecto(3)

''' NOTA: PARÁMETROS OPCIONALES:
    Python NO dispone de parámetros opcionales. Únicamente se hace uso de
    los parámetros por defecto en su lugar.
'''

# Función con muchos parámetros
def miFuncionConMultiplesParametros(*elementos) :
    for elemento in elementos:
        print(f"Elemento: {elemento}")
 
# llamando la función y pasándole una lista de parámetros
lista: [int] = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(*lista)


# Función con Retorno

def miFuncionConRetorno():
    return '¡Hola, Mundo!'
 
# llamando, ejecutando y almacenando el retorno en una variable
# la variable hola_mundo acabará valiendo "¡Hola, Mundo!"
hola_mundo = miFuncionConRetorno()
print(hola_mundo)



# Función con Retorno Tipado
def miFuncionConRetornoTipado(*elementos) -> int :
    # Inicializamos la variable suma a 0 para incrementarla después
    suma: int = 0
 
    # iteramos sobre los elementos y los vamos sumando uno a uno
    # los guardamos en la variable suma que se va incrementando
    for elemento in elementos:
        print(f"Elemento: {elemento}")
        suma += elemento
 
    return suma
 
# llamar, pasarle la lista, ejecutar y almacenar la suma del retorno
# en la variable sumatorio
lista_numeros = [1, 2, 3, 4, 5, 6]
sumatorio = miFuncionConRetornoTipado(*lista_numeros)
print(f"EL sumatorio total es: {sumatorio}")

''' PASO POR REFERENCIA
Paso de parámetros por Referencia
 
Los valores simples se pasan, por defecto, por valor
Los valores complejos se pasan, por defecto, por referencia
 
'''
 
# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen
 
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
	
# definiendo una variable que se va a pasar por referencia
ns = [10,50,100]
doblar_valores(ns)
print(f"Lista Original Modificada: {ns}") #[20, 100, 200]

# SI NO QUEREMOS PASAR UNA LISTA COMO REFERENCIA, DEBEMOS REALIZAR UNA COPIA "AL VUELO"
# Ahora esta no se pasará por referencia, ya que haremos una copia del valor
ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista se realiza con [:]
# Esto hace que la lista original no se vea modificada
print(f"Lista Original No Modificada: {ns}") #[10, 50, 100]
	
# Para aquellos tipos de datos simples, si queremos el mismo comportamiento
# de paso por referencia podemos:
 
# SOBRESCRIBIR EL VALOR ORIGINAL CON EL VALOR DE RETURN DE LA FUNCIÓN
def doblar_valor(numero):
    return numero * 2
 
n = 10
n = doblar_valor(n)
print(f"Valor original Modificado: {n}")

# Pasando Diccionarios por parámetro


# llamando la función y pasándole una diccionario como parámetros


''' FUNCIONES LAMBDA:

Las funciones Lambda de Python son bastante habituales.

Básicamente sirven para definir funciones rápidas para un consumo veloz

Son muy parecidas a las funciones flecha de TypeScript
'''

al_cuadrado = lambda a: a**2
 
# llamando a la función lambda
print(al_cuadrado(2)) # imprimirá un 4


# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen


# definiendo una variable que se va a pasar por referencia


# Para aquellos tipos de datos simples, si queremos el mismo comportamiento
# de paso por referencia podemos:

# SOBRESCRIBIR EL VALOR ORIGINAL CON EL VALOR DE RETURN DE LA FUNCIÓN

# SI NO QUEREMOS PASAR UNA LISTA COMO REFERENCIA, DEBEMOS REALIZAR UNA COPIA "AL VUELO"
# Ahora esta no se pasará por referencia, ya que haremos una copia del valor


# Esto hace que la lista original no se vea modificada



'''
LISTAS
'''

'''
DICCIONARIOS
'''


'''
FECHAS
'''

import datetime
import time
import calendar
import locale

#locale.setlocale(locale.LC_ALL, 'es_ES')

print('Fecha y Hora actual', datetime.datetime.now())
print('Fecha actual', datetime.date.today())
print('Año actual', datetime.date.today().strftime("%Y"))
print('Mes actual', datetime.date.today().strftime("%B"))
print('Mes actual(num)', datetime.date.today().strftime("%m"))
print('Numero de la semana', datetime.date.today().strftime("%W"))
print('Dia del año', datetime.date.today().strftime("%j"))
print('Dia del mes', datetime.date.today().strftime("%d"))
print('Dia de la semana', datetime.date.today().strftime("%A"))

print('Dia', calendar.day_name[0])
print('Mes', calendar.month_name[10])
print('2020 es bisiesto?', calendar.isleap(2020))

ahora= datetime.datetime.now()

timeStamp= time.mktime(ahora.timetuple())

print('TimeStamp', timeStamp)

print('Fecha legible', datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S'))

miFecha = '02/10/2021'

nuevoTimeStamp = time.mktime(datetime.datetime.strptime(miFecha,'%d/%m/%Y').timetuple())

print('Nuevo TimeStamp', nuevoTimeStamp)

print('Fecha Legible:',datetime.datetime.fromtimestamp(nuevoTimeStamp).strftime('%Y-%m-%d %H:%M:%S'))

'''
Ejercicio 1
'''
miSet= {0,1,2,3,4,5,6,7,8,9}
miSet2= {2,4,6,8}

print(miSet.symmetric_difference(miSet2))

precios = [('Producto A', '12.20'), ('Producto B', '15.10'), ('Producto C', '24.50')]
print(sorted(precios,key=lambda x: float(x[1]),reverse=True))