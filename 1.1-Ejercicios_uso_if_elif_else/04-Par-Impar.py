"""Par-Impar"""

num1 = int(input("Ingrese un número mayor a 1 y menor a 101 : "))

if 1 > num1 < 101:
    print("Ingrese un número valido")
elif num1 % 2 == 0:
    print(f"El número {num1} es par")
else:
    print(f"El número {num1} es impar")
