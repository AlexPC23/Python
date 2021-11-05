#Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. La función debe tener la siguiente firma:
def eliminar(str, n):
    inicio = str[:n] 
    final = str[n+1:]
    return inicio + final

print(eliminar('Madrid', 0))
print(eliminar('Madrid', 3))
print(eliminar('Madrid', 5))