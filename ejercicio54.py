
#Escribe un programa que reciba una calificación numérica (0 a 100) y determine la
#categoría de la nota: "Muy deficiente" (menos de 50), "Deficiente" (50-64), "Regular"
#(65-74), "Buena" (75-89) y "Excelente" (90-100).

calificacion = int(input("ingrese la calificacion (0-100):"))

if 0 <= calificacion <= 64:
    categoria = "insuficiente"

elif 65 <= calificacion <= 74:
    categoria = "regular"

elif 75 <= calificacion <= 89:
    categoria = "buena"

elif 90 <= calificacion <= 100:
    categoria = "exelente"

else:
    categoria = "calificacion invalida"

print("la calificacion es:",categoria) 