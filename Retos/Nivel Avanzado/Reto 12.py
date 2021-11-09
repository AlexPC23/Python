#Escribe un script de código que haga al usuario introducir 8 alturas de edificios (deben ser float) y que saque por consola las 3 más altas (haz uso de sorted).
print("Introduce la altura de 8 edificios:")
alturas = [int(input()) for i in range(8)]

print("Las tres alturas más altas:")
alturas = sorted(alturas)

print(*alturas[:4:-1], sep='\n')