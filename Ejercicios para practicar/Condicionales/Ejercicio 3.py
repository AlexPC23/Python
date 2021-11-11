#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
dividendo = int(input('Introduce un numero: '))
divisor = int(input('Introduce un numero: '))
if divisor == 0:
    print('Error')
else:
    print(dividendo/divisor)




