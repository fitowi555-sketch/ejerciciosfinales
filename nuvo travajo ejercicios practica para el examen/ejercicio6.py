# Encontrar el segundo número más grande en una lista de números. (10,15, 20, 25, 5)

lista = list(map(int,input("ingresa numeros separados por espacios: ").split()))

mayor = float("-inf")
segundo_mayor =float("-inf")

for num in lista:
    if num > mayor:
        segundo_mayor = mayor 
        mayor = num
    elif num > segundo_mayor and num != mayor: 
        segundo_mayor = num

print("el segundo numero mas grande es:", segundo_mayor)