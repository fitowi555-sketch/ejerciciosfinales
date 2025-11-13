
#Pide un código de descuento y aplica un descuento específico si es válido.

codigos_validados = {"DES10": 10, "DES20": 20, "SEPER50": 50, "ULTRA100": 100}

precio = float(input("el ingrese el precio:"))
codigo =input("ingrese el codigo de descuento:").upper()

if codigo in codigos_validados:
    descuento = codigos_validados[codigo]
    precio_final = precio - (precio * descuento / 100)

    print(f"codigo valido. descuento aplicado: {descuento}%.")
    print(f"total a pagar: $ {precio_final}")

else:
    print("codigo invalido. no se aplica descuento")
    print(f"total a pagar: ${precio}")
