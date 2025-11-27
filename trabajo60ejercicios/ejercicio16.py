
#Pide una calificación y clasifícala en "Excelente", "Buena", "Regular" o "Mala".

calificacion = float(input("in grese la calificacion:"))

if calificacion < 3.0:
    print("la calificacion es mala")

elif calificacion >= 3.0 and calificacion < 4.0:
    print("la calificacion es regular")

elif calificacion >= 4.0 and calificacion < 5.0:
    print(":la calificacion es buena")    

else:
    print("la calificacion es exelente")