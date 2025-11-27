
#Pide la edad y calcula el año de nacimiento.

edad =int(input("ingrese la edad actual:"))

año_actual = 2025

if edad > 0 and edad <= 10000:
    año_nacimiento = año_actual - edad
    print("tu año de nacimiento es",año_nacimiento)

else: 
    print("error de lectua por favor ingrese un valor logico:")