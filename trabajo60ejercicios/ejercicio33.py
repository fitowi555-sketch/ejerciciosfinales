
#Pide un puntaje de examen y determina en qué rango cae (por ejemplo, A, B, C, D, o F).

examen = float(input("ingrese el puntaje del examen:"))

if examen < 3.0:
    print("el estudiante tiene (F) su calificacion es muy mala:")

elif examen >= 3.0 and examen < 3.5:
    print("el estudiante tiene (D) su calificacion es mala:")

elif examen >= 3.5 and examen < 4.0:
    print("el estudiante tiene (C) su calificacion es aceptable:")

elif examen >= 4.0 and examen < 4.5:
    print("el estudiante tiene (B) su calificacion buena:")

elif examen >= 4.5 and examen <= 5.0:
    print("el estudiante tiene (A) su calificacion es exelente:")

else:
    print("no se emcontraron resultados")