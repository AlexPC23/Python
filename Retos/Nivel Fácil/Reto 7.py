#Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
key = 'admin'
password:str = input('Introduce la contraseña: ')
while key == password.lower():
    print('Son iguales')
if key != password.lower():
    print('Son diferentes')
   
