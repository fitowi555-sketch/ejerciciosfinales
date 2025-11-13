
#Pide dos números y un operador, y realiza una operación considerando casos especiales de división.

num1 = int(input("ingrese el primer numero:"))
operador =input("ingrese el operador, +, -, *, /, %, :").strip()
num2 = int(input("ingrese el segundo numero:"))


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
    resultado = (num1 * num2) / 100  
    print(f"{num1} % {num2} = {resultado}")


elif operador == "/":
    if num2  == 0:
        print("SintaxERROR:" "no se puede dividir entre cero")

    else:
        resultado = num1 / num2 
        div_entera = num1 // num2
        residuo = num1 % num2
        
        print(f"{num1} / {num2} = {resultado}:")
        print(f"divicion entera: {div_entera}")
        print(f"residuo:{residuo}")

else:
    print("operador no valido")