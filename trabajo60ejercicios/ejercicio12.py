
#Pide tres números y muestra si son todos pares, todos impares, o hay mezcla.

num1 =int(input("ingrese el primer numero:"))
num2 =int(input("ingrese el segundo numero:"))
num3 =int(input("ingrese el tercer numero:"))

p1 = num1 % 2
p2 = num2 % 2
p3 = num3 % 2

if p1 == 0 and p2 == 0 and p3 == 0:
    print("todos son pares")

elif p1 != 0 and p2 != 0 and p3 != 0:
    print("todos son impares")

else: 
    print("hay mezcla")