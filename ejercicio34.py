
#Pide la categoría del cliente y calcula el descuento en base a la categoría.

print ( "porcentajes de descuento por categorias ") 
print("categoria A = 50 %")
print("categoria B = 25 %")
print("categoria C = 10 %") 
print("categoria D = 5 %")

print("escoja una categoria")
print("A, B, C, D:")

categoria = input("ingrese la categoria del cliente (A, B, C, D):").upper()
compra = float(input("ingrese el valor de la compra:"))

if categoria == "A":
    descuento = 0.50
    print("el descuento aplicado es 50 %:")

elif categoria == "B":
    descuento = 0.25
    print("el descuento aplicado es 25 %:")
    
elif categoria == "C":
    descuento = 0.10
    print("el descuento aplicado es 10 %:")

elif categoria == "D":
    descuento = 0.05
    print("el descuento aplicado es 5 %:")

else: 
    print("no esta dentro de la categoria no tiene descuento el total de la compra es:", compra)
    descuento = 0.0

valordescuento = compra * descuento
total = compra - valordescuento

print(f"descuento aplicado: {valordescuento:.2f}")
print(f"total a pagar: {total:.2f}")



