#Pide las edades de tres personas y determina quién es el mayor y quién el menor.

edad1 = int(input("ingrese la primera edad:"))
edad2 = int(input("ingrese la segunda edad:"))
edad3 = int(input("ingrewse la tercera edad:"))

if edad1 > edad2 and edad1 > edad3:
    print("la edad mayor es", edad1)
    print("la edad de", edad2 , "y la edad de", edad3, "son menores" )

elif edad2 > edad1 and edad2 > edad3:
    print("la edad mayor es",edad2)
    print("la edad de", edad1 , "y la edad de", edad3, "son menores" )

else:
    print("la edad mayor es",edad3)
    print("la edad de", edad1 , "y la edad de", edad2, "son menores" )