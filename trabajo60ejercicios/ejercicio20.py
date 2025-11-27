
#Pide un mes (número) e indica a qué trimestre del año pertenece.

MES2 = int(input("ingrese el mes:"))
MES1 = input(("ingrese el numero que corresponde al mes:"))

if MES2 >= 1 and MES2 <= 3:
    print("el mes", MES2 , MES1 , "pertenece al primer trimestre (T1)")

elif MES2 >= 4 and MES2 <= 6:
     print("el mes", MES2 , MES1 , "pertenece al segundo trimestre (T2)")


elif MES2 >= 7 and MES2 <= 9:
     print("el mes", MES2 , MES1 , "pertenece al tercer trimestre (T3)")


elif MES2 >= 10 and MES2 <= 12:
     print("el mes", MES2 , MES1 , "pertenece al cuarto trimestre (T4)")

else:
     print("numero de" "MES" "invalido ingrese un numero de 1 a 12")