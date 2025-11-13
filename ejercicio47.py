
#Pide el precio de un producto y si es esencial o no, y aplica IVA según el tipo.

producto = input("ingrese el producto:")

precio = float(input("ingrese el precio del producto:"))

tipo = input("el producto es esencial (si/no):").lower()

if tipo == "si":
    iva = 0

elif tipo == "no":
    iva = 0.19

else:
    print("respuesta no valida debe escribir (si/no)")
    iva = 0

precio_final = precio * (1+iva)

print(f"\nprecio sin iva: $ {precio:.2f}")
print(f"iva aplicado {iva + 100}%")
print(f"precio final con iva: ${precio_final:.2f}")