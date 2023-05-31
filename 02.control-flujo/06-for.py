buscar = int(input("Ingrese numero entre 1 y 5"))
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado!", buscar)
        break
else:
    print("no se encontró el numero buscado")

for char in "Ultimate python":
    print(char)
