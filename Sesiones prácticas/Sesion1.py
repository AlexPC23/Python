nombre:str = "Alex"
saludo = f'¡Hola, {nombre}!'

print ("¡Hola, " +nombre+"!")
print (f"¡Hola, {nombre}!")
print (saludo)

'''
Esto es un comentario
multilínea
'''

# Esto sería una línea de comentario 
# TODO: Tarea pendiente de hacer
# FIXME: Correcciones de código necesarias


'''
TIPOS DE DATOS EN PYTHON
'''

print('------CADENAS DE TEXTO------')

#STR
miCadena: str = "Hola mundo"
miCadena2: str = '''Hola mundo'''

primeros_dos_caracteres= miCadena[0:2]

print(f'PRIMEROS DOS CARACTERES: {primeros_dos_caracteres}')

print(f'Texto Con mayúsculas: {miCadena.upper()}')
print(f'Texto Con mayúscula: {miCadena.capitalize()}')
print(f'Texto Con minúsculas: {miCadena.lower()}')

'''
BOOL
'''
casado: bool = False

print (f'¿Casado? {casado}')

'''
LISTAS de Datos
'''

miLista: [str] = ['Martin', 'Juan', 'Ana']
print(miLista)
print(*miLista)
print(miLista[2])

#RANGO
miRango = range(1, 10, 2)
miRango2 = range(10, 1, -2)
miRango3 = range(-10, 10, 2)

print(*miRango)
print(*miRango2)
print(*miRango3)

'''
diccionarios
'''

persona = {
  "nombre": "Martin", 
  "edad": 30,
  "email": "martin@imaginagroup.com"
}

print(persona)
print(*persona)

print(f'La edad de {persona["nombre"]} es {persona.get("edad")}')


misNumeros = [1,2,3,4,5,1,5]
print(*misNumeros)

miSetDeNumeros = set([1,2,3,4,5,1,5])
print(miSetDeNumeros)
miOtroSetDeDatos = {1,2,2,5,5,'a', False}
print(miOtroSetDeDatos)
miSetDeNumeros2 = set(misNumeros)
print(miSetDeNumeros2)

miSetCongelado = frozenset(misNumeros)

miValorNone = None

print(miValorNone)



'''
str
int
float
complex
listas
tuple
range
dict
set
frozenset
bool
bytes
bytearray
memoryview
'''



'''
RETO 1

Operación aritmetica que realice 

(6-2)
----
(5)    ^2

'''
result:float = ((6-2)/5)**2
print(result)

print(result.__round__(4))
print(round(result,4))

'''
RETO GRUPAL

Partiendo de:
-Cantidad a invertir
-El interés anual
-El número de años

Calcular el capital obtenido y guardarlo en una variable

Se tiene que mostrar por consola
"El capital obtenido por tu inversión asciende a "capital_obtenido" euros
'''

inv = 10000
rent = 10
n = 40

Patrimonio= inv * (1+(rent/100))**n

print(round(Patrimonio,2))

'''
RETO 2
Producto: 14,99
Los que no son de temporada tendrán 30% descuento
Reciba un número de productos en temporada. Otro número de productos de la temporada pasada y aplicar el descuento obtener el gasto total en productos
Hay que indicar la cantidad ahorrada gracias al descuento
'''

Producto= 14-.99
Descuento= 0.3

Temporada= int(input("Número de productos que son de temporada"))

noTemporada= int(input("Número de productos que no son de temporada"))

total= (Temporada*Producto) + (noTemporada*Producto*(1-Descuento))


print("El precio total de la venta sería",total)

'''
RETO
Pedir al usuario un año y si es bisiesto o no que pida años hasta que salga
'''

year= int(input("Introduce un año"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('El año es bisiesto')
    else:
        print('El año es bisiesto.')