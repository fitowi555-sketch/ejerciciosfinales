
#Pide un año y determina si es bisiesto.

año = int(input("ingrese el año:"))

if (año % 4 == 0) and (año % 100 != 0):
    print("el año" , año ,"es bisiesto")

else:
    print("el año" , año , "NO es bisiesto:")
