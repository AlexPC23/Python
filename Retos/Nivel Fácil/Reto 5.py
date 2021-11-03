#Escribe un programa que sea capaz de pedirle a un usuario por consola que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
key = "admin"
password:str = input("Introduce la contraseña: ")
while key == password.lower():
    print("Bienvenido al programa señor ADMIN")
    break
while key != password.lower():
    print("Prueba de nuevo")
    break
   

    

    
    


