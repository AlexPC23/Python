#Realiza un script que permita encontrar dentro de la lista aquellos elementos que sean tuplas. Cada vez que encuentre una tupla, deberá incrementarse la variable cantidad.
numeros = [10,20,(1,3),30,50,69,(10,20),40]
cantidad = 0

for numero in numeros:
      if isinstance(numero, tuple):  
        cantidad += 1

print(f"Cantidad de tuplas: {cantidad}") 