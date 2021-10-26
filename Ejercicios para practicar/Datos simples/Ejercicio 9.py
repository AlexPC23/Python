#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
i = 0.04
dinero_depositado = float(input("¿Cuanto dinero tiene la cuenta de ahorros?"))
año1 = dinero_depositado * (1+i)
print("El primer año su saldo es de " + str(round(año1, 2)))
año2 = año1 * (1+i)
print("El segundo año su saldo es de " + str(round(año2, 2)))
año3 = año2 * (1+i)
print("El tercer año su saldo es de " + str(round(año3, 2)))
