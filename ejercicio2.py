
#Escribe un programa que le pida al usuario tres números y determine cuál es el mayor.

num1 =int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))
num3 = int(input("ingrese el tercer numero:"))

if num1 > num2 and  num1 > num3 :
    print("el numero" , num1 , "es mayor:")

elif num2 > num1 and  num2 > num3 :
    print("el numero", num2 , "es mayor")


else:
      print("el numero es mayor:", num3 )
    
