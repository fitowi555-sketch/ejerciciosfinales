
#Pide el total de la compra e indica si tiene 10% de descuento si es mayor a 100.

total_compra =int(input("ingrese el toatl de la compra:"))
descuento = 0.10

if total_compra >= 100:
    total_descuento = total_compra * (1-0.10)
    print("el valor a pagar con descuento del 10% por compras iguales o superiores a 100 es:", total_descuento)

else:
    print("no se aplica descuento por compras menores a 100 su total de compra es:", total_compra)