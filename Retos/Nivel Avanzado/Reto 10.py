#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
import math

def max_comun_div(numero_a, numero_b) -> int:
    while numero_b:
        numero_a,numero_b = numero_b, numero_a % numero_b
    return numero_a

def min_comun_mult(numero_a, numero_b) -> int:
    return abs(numero_a*numero_b)

print(f"El Máximo Común Divisor de 15 es: {max_comun_div(15, 30)}")
print(f"El Mínimo Común Múltiplo de 15 es: {max_comun_div(15, 30)}")
print(f"El Máximo Común Divisor de 15 es: {math.gcd(15, 30)}")