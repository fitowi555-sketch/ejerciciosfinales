
#Pide la edad y determina si la persona puede votar, y si es obligatorio (entre 18 y 70 años).

edad =int(input("ingrese la edad:"))

if edad < 18:
    print("es obligatorio que esta persona vote al cumplir la mayoria de edad, esta persona al ser menor de edad NO PUEDE VOTAR")

elif edad >= 18 and edad <= 70:
    print("es obligatorio que esta persona vote al ser mayor de edad")

else:
    print("no se encuentran resultados:")