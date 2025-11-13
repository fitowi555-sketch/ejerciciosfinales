
#Pide la edad y determina el descuento: 50% si es menor de 12, 20% si es mayor de 65, y sin descuento para los demás.

edad = int(input("ingrese la edad:"))
descuento1 = 0.50
descuento2 = 0.20

if edad <= 12:
    print("el descuento es del 50% :", descuento1)

elif edad >= 65:
    print("el descuento es de 20%:", descuento2)

else:
    print("no tiene descuento:")