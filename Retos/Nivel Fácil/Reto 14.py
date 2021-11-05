#Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
import math
radio = float(input('¿Cual es el radio del circulo?: '))
area_circulo = math.pi * (radio**2)
altura_cilindro = float(input('¿Cual es la altura del cilindro?: '))
volumen_cilindro = area_circulo * altura_cilindro
print('El volumen del cilindro es ' + str(volumen_cilindro))