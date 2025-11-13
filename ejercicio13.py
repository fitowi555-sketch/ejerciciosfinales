
#Pide dos letras e indica si son iguales o cuál es mayor alfabéticamente.

letra1 =input("ingrese la primer letra:") .lower()
letra2 =input("ingrese la segunda letra:").lower()

if letra1 == letra2:
    print("las letras son iguales")

else:
    print("las letras son diferntes")

    if letra1 > letra2:
        print("la letra mayor alfavetica mente es:", letra1)
        print("la letra que va primero en el alfabeto es:", letra2)

    else:
        print("la letra mayor alfabetica mente es:", letra2)
        print("la letra que va primero en el alfabeto es:", letra1)