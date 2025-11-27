
#Pide calificaciones de tareas, proyectos y exámenes y calcula la nota final.

tareas =float(input("ingrese la nota de la tarea:"))
proyectos = float(input("ingrese la nota del proyecto:"))
examenes = float(input("ingrese la nota del examen:"))

suma = tareas + proyectos + examenes

nota_final = suma / 3

if nota_final < 3.0:
    print("el estudiante peridio con una  nota final de", nota_final)

else:
    print("el estudiante gano con una nota final de", nota_final)