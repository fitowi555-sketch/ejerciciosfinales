
#Pide dos números y muestra cuál está más cerca de 100.

num1 = int(input("ingresa el primer numero:"))
num2 = int(input("ingresa el segundo numero:"))

dis1 = abs(num1 -100)
dis2 = abs(num2 - 100)

if dis1 < dis2:
    print("el numero", num1 , "esta mas cerca del 100:")

elif dis2 < dis1:
    print("el numero", num2 , "esta mas cerca del 100:")

else:
    print("ambos numeros estan a la misma distancia de 100:")
