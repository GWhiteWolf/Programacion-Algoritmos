"""Suma positivos"""
# Ingrese por teclado dos números enteros positivos, súmelos y entregue su resultado.

num1 = int(input("Ingrese primer numero entero positivo : "))
num2 = int(input("Ingrese segundo numero entero positivo : "))

if num1 < 0 or num2 < 0:
    print("Ingrese un numero entero POSITIVO, LEA BIEN")
else:
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es {resultado}")
