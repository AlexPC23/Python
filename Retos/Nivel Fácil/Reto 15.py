#Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrados (lista:(int) -> (int):
    for i, numero in enumerate(lista):
        lista[i] *=2

    miLista = [10,50,100]
  cuadrados(miLista)
  print(f"Lista Original Modificada: {miLista}")