
#Calcula el promedio de tres notas y determina si el estudiante aprueba o reprueba (mínimo 60).

nota1 = float(input("ingrese la primera nota:"))
nota2 = float(input("ingrese la segunda nota:"))
nota3 = float(input("ingrese la tercer nota:"))

suma = nota1 + nota2 + nota3

promedio = suma / 3 

if promedio < 3.0:
    print(f"el estudiante repueba con una nota de: {promedio:.2f}")

else:
    print(f"el estudiante aprueba con una nota de {promedio:.2f}")