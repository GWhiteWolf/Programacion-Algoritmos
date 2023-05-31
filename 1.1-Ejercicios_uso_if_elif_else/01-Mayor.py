"""Numero mayor"""
# Ingrese por teclado dos números enteros e indique cuál de ellos es el mayor.

num1 = int(input("Ingrese primer número : "))
num2 = int(input("Ingrese segundo número : "))

if num1 == num2:
    print(f"Ambos numeros son iguales : {num1}")
elif num1 > num2:
    print(f"El numero mayor es {num1}")
else:
    print(f"El numero mayor es {num2}")
