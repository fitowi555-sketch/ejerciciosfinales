
#Pide una temperatura y verifica si está en rango de ebullición o congelación.

temperatura =float(input("ingrese la tempratura :"))

if temperatura <= 0:
    print("la temperatura esta en grado de congelacion", temperatura,"°C")

elif temperatura >= 100:
    print("la tempreatura esta en grado de ebullicion", temperatura,"°C")

else:
    print("la tempratura esta nula a un nivel templado", temperatura,"°C")