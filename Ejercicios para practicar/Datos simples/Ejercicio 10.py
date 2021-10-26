#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
precio_pan = 3.49
descuento = 0.6
barras_vendidas = int(input("¿Cuantas barras que no son del día se han vendido hoy?"))
coste = barras_vendidas * precio_pan * (1-descuento)
print("El coste de la barra de pan es " + str(precio_pan) + "$")
print("El descuento para las barras de pan que no son del día es del " + str(descuento * 100) + "%")
print("El coste final es de " + str(round(coste, 2)))  
