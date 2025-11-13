
#Pide un número y muestra la raíz cuadrada si es positivo. Si es negativo, muestra un mensaje diciendo que no tiene raíz real.

import math

num = int(input("ingrese un numero:"))

if num >= 0:
    raiz = math.sqrt(num)
    print("el numero" , num , "tiene raiz exacta:",raiz)

else:
    print("el numero" , num , "tiene NO raiz real:")

