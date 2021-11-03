#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
def main():
    print("PARES E IMPARES")
    numero_1 = int(input("Escriba un número entero: "))
    numero_2 = int(input(f"Escriba un número entero mayor o igual que {numero_1}: "))
    if numero_2 < numero_1:
        print(f"¡Le he pedido un número entero mayor o igual que {numero_1}!")
    else:
        for i in range(numero_1, numero_2):
            if i % 2 != 0:
                print(f"El número {i} es impar.")
if __name__ == "__main__":
    main()