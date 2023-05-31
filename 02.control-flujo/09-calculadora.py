"""CALCULADORA"""

print("""Bienvenido a la calculadora
Las operaciones son SUMA, RESTA, MULTI, DIV
Para salir escribe SALIR
""")

num1 = int(input("Ingrese primer numero : "))

while True:
    if not num1:
        num1 = input("Ingrese un numero")
        if num1.upper() == "SALIR":
            break
        num1 = int(num1)
    operacion = input("Ingrese operación a realizar : ")
    if operacion.upper() == "SALIR":
        break
    num2 = int(input("Ingrese segundo numero : "))
    if operacion.upper() == "SALIR":
        break
    num2 = int(num2)

    if operacion.upper() == "SUMA":
        num1 += num2
    elif operacion.upper() == "RESTA":
        num1 -= num2
    elif operacion.upper() == "MULTI":
        num1 *= num2
    elif operacion.upper() == "DIV":
        num1 /= num2
    elif operacion.upper() == "SALIR":
        break
    else:
        print("Ingrese una operación valida")
        break

    print(f"El resultado es {num1}")
