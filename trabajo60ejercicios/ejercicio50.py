
#Pide dos números y determina si son pares o impares y si uno es múltiplo del otro.

num1 = int(input("digite el primer numero: "))
num2 = int(input("digite el segundo numero: "))

if num1 % 2 == 0 :
    print(f" el numero {num1} es par")
else:
    print(f"es numero {num1} impar")

if num2 % 2 == 0:
    print(f"el numero  {num2} es par")
else:
    print(f"es numero  {num2} impar")

if num1 % num2 == 0:
    print(f"{num1} es multiplos de {num2}")

elif num2 % num1 == 0:
    print(f" {num2} es multiplo de {num1}")

else: 
    print("nimguno es multiplo de otro")