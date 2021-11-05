#Escribe un programa que pida al usuario los siguientes datos por consola:Título de la película/Director/Año/País/E introduzca esos valores en una variable GLOBAL llamada "pelicula".
global pelicula 
pelicula: dict = dict()
pelicula['Titulo'] = input('Introduzca el TÍTULO de la película: ')
pelicula['Director'] = input('Introduzca el DIRECTOR de la película: ')
pelicula['Año'] = int(input('Introduzca el AÑO de la película: '))
pelicula['País'] = input('Introduzca el PAÍS de la película: ')

print(pelicula)