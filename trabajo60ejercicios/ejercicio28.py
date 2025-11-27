
#Pide un mes y determina si está dentro del ciclo escolar o en vacaciones.

mes = int(input("ingrese el mes (1-12):"))

if mes == 12 or mes == 1:
    print("vacaciones")

elif 2 <= mes <= 11:
    print("ciclo escolar")

else:
    print("mes invalido:")