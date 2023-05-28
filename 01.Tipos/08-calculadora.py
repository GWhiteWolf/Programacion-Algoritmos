num1 = int(input("Ingrese el primero numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
poten = num1 ** num2

mensaje = f"""
Para los números {num1} y {num2},
El resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multiplicacion es {multi}.
El resultado de la división es {div}.
El resultado de la potencia es {poten}.
"""

print(mensaje)
