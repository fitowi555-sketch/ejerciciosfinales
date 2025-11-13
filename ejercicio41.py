
#Pide cinco calificaciones y calcula el promedio, luego muestra el nivel de desempeño (bajo, medio, alto).

calificacion1 =float(input("ingrese la primer calificacion: "))
calificacion2 =float(input("ingrese la segunda calificacion: "))
calificacion3 =float(input("ingrese la tercera calificacion: "))
calificacion4 =float(input("ingrese la cuarta calificacion: "))
calificacion5 =float(input("ingrese la quinta calificacion: "))

suma = calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5 

promedio = suma / 5

if promedio < 3.0:
    print(f" el promedio es: {promedio:.2f} tiene un desempeño muy bajo")

elif promedio <= 4.0:
    print(f" el promedio es: {promedio:.2f} tiene un desempeño medio")

elif promedio == 5.0:
    print(f" el promedio es: {promedio:.2f} tiene un desempeño alto")

else:
    print("promedio no valido ya perdio el año")
