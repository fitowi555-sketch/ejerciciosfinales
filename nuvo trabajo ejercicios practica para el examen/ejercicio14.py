# Calcular el factorial de un número dado (por ejemplo, 5).

num = int(input("digita un numero: "))
factorial = 1

for i in range(1,num+1):
    factorial *= i 

    print("el numero factoria de", num, "es:", factorial)