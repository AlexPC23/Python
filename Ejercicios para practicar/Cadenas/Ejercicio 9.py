#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha_nacimiento = input('¿Que dia naciste? (formato dd/mm/aa): ')
dia = fecha_nacimiento[:fecha_nacimiento.find('/')]
mesaño = fecha_nacimiento[fecha_nacimiento.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)