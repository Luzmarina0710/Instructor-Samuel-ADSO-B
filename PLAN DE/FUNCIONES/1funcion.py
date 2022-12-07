"""Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
n = int(input('Escriba un numero entero '))

def factorial(n):
    fact = 1
    for i in range(n):
        fact *= i+1
    return fact

print(factorial(n))