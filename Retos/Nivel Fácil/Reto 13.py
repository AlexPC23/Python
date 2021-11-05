#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
altura = float(input('¿Cual es la altura del triangulo?: '))
base = float(input('¿Cual es la base del triangulo?: '))
area_triangulo = base * altura / 2
print('La area del triangulo es ' + str(area_triangulo))

import math
radio = float(input('¿Cual es el radio del circulo?: '))
area_circulo = math.pi * (radio**2)
print('El area del circulo es: ' + str(area_circulo))