
#Pide tres lados y verifica si pueden formar un triángulo.

A = float(input("ingrese el primer lado:"))
B = float(input("ingrese el segundo lado:"))
C = float(input("ingrese el tercer numero:"))

if A + B > C and A + C > B and B + C > A:
    print("si se puede formar un triangulo")

else:
    print("los lados no coinciden para formar un triangulo")