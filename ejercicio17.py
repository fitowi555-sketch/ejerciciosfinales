
#Pide dos números y determina si el primero es múltiplo del segundo.

num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))

MOD = num1 % num2

if num1 % num2 == 0:
    print("los numero si son multiplos entre si su resultado es:",MOD)

else:
    print("no son multiplos entre si su resultado es:", MOD) 