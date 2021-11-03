#Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad_usuario = int(input('¿Cuantos años tienes?'))
if edad_usuario >= 18:
    print('Eres mayor de edad')
if edad_usuario < 18:
    print('Eres menor de edad')