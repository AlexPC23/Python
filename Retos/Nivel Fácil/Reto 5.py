#Escribe un programa que sea capaz de pedirle a un usuario por consola que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
acierto: bool = False
valor_introducido: str = ''

while not acierto:
      valor_introducido = input('Introduzca una contraseña: ')
      if(valor_introducido == 'admin'):
          acierto = True
          print(f"Contraseña correcta")
          break
      else:
          print("¡Contraseña incorrecta!")
   

    

    
    


