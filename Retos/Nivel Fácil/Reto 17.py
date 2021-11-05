#Partiendo de la siguiente tupla, realiza las operaciones.
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = tupla[3:5]
print('1-', _slice)

_slice = tupla[:6]
print('2-',_slice)

_slice = tupla[5:]
print('3-',_slice)

_slice = tupla[:]
print('4-',_slice)

_slice = tupla[-8:-4]
print('5-',_slice)

tupla = tuple("HELLO WORLD")
print('6-',tupla)

_slice = tupla[2:9:2]
print('7-',_slice)

_slice = tupla[::4]
print('8-',_slice)

_slice = tupla[9:2:-4]
print('9-',_slice)