
#Un supermercado ofrece descuentos en función de la hora de compra. Si la compra es
#antes de las 12:00 p.m., se aplica un 10% de descuento. Si la compra es después de las
#6:00 p.m., el descuento es del 20%. En otros horarios, no hay descuento. Escribe un
#programa que determine el descuento aplicable y el total a pagar

producto =input("ingrese el producto:")

precio = int(input("ingrese el valor del producto:"))

hora =int(input("ingrese la hora de la compra (1 pm a 12 pm):"))

if hora >= 12:
    descuento = 0.10

elif hora < 18:
    descuento = 0.20

else:
    descuento = 0

valor_descuento = precio * descuento
total = precio - valor_descuento

print(f"\nproducto: {producto}")
print(f"precio normal: ${precio}")
print(f"descuento aplicado: {descuento*100}%")
print(f"total a pagar: ${total}")
