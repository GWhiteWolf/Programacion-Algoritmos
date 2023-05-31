"""Empresa zapatos"""

# La empresa dedicada a la venta de zapatos, ha decidido
# fabricar zapatos de hombre para la venta online. Los zapatos
# tienen un valor de $20.000 (cualquier número), pero podría
# variar según la demanda.
# Si la compra es igual o superior a $40.000 el envío es gratis,
# en caso contario, debe cancelar un monto extra de $3.000
# Determine el total a pagar por una persona que requiere X
# cantidad de zapatos.

cantidad = int(input("Ingrese cantidad de zapatos a comprar : "))
valor = cantidad * 20000

if valor <= 0:
    print("Ingrese una cantidad valida")
elif valor >= 40000:
    print(f"El total a pagar es {valor}")
else:
    print(f"El total a pagar es {valor+3000}")
