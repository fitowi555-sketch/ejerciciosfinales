
#Pide un número entre 1 y 7 y muestra el día correspondiente.

num = int(input("ingrese un numero entre 1 y 7: "))

if num == 1:
    print("el dia es LUNES")

elif num == 2:
    print("el dia es MARTES")

elif num == 3:
    print("el dia es MIERCOLES")

elif num == 4:
    print("el dia es JUEVES")

elif num == 5:
    print("el dia es VIERNES")

elif num == 6:
    print("el dia es SABADO")

elif num == 7:
    print("el dia es DOMINGO")                

else:
    print("el numero ingresado no corresponde a ningun dia de la semana digite un numero de (1 a 7)")

