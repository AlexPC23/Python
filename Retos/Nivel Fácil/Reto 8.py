#Escribe un programa que pueda decirte si un número (número entero) es primo o no
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True
def app():
    num = int(input("Introduce un número entero: "))
    result = es_primo(num)
if __name__ == '__main__':
    app()