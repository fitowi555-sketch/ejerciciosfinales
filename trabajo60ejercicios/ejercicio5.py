#Escribe un programa que le pida al usuario dos números y un operador (+, -, *, /) y realice la operación correspondiente.

num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))

operador =input("ingrese el operador, +, -, *, /, %, :").strip()

if operador == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operador == "-":
    resultado = num1 - num2 
    print(f"{num1} - {num2} = {resultado}")

elif operador == "*":
    resultado = num1 * num2 
    print(f"{num1} * {num2} = {resultado}")

    
elif operador == "%":
    resultado = num1 % num2 
    print(f"{num1} % {num2} = {resultado}")


elif operador == "/":
    if num2  == 0:
        print("SintaxERROR:" "no se puede dividir entre cero")

    else:
        resultado = num1 / num2 
        print(f"{num1} / {num2} = {resultado}:")
    
