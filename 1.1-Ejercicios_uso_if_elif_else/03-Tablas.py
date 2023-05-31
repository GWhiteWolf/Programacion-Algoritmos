"""Tablas de multiplicar"""
# Ingrese por teclado un número positivo y muestre su tabla de multiplicar (considere que la tabla sea de 1 a 10)

num1 = int(input("Ingrese un número entero POSITIVO : "))

if num1 < 0:
    print("Ingresó un número invalido")
else:
    for rango in range(1, 11):
        resultado = num1 * rango
        print(f"{num1}*{rango}={resultado}")
