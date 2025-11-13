
#Pide una letra y determina si es vocal o consonante.

letra = input("ingrese una letra:").lower()

if letra in "a,e,i,o,u":
    print("la letra", letra, "es vocal")

else:
    print("la letra", letra , "es una consonante")