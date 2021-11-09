#Actualiza la lista sin aquellas tuplas que estén vacías.
miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
miLista = [tupla for tupla in miLista if tupla]
print(miLista)