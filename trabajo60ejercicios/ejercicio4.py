
#4 Escribe un programa que le pida al usuario su calificación y determine si aprobó (60 o más), reprobó (menos de 60), y si es un aprobado especial (90 o más).

nota = int(input("ingrese la calificacion:"))

if nota >= 90:
    print("aprobo con una nota superior a 90 es un aprobado especial su nota es:" , nota)
   

elif nota >= 60:
       print("aprobo con una nota superior a 60 su nota es:" , nota)
     
else:
    print("reprobo con una nota menor que 60 su nota es:" , nota)

