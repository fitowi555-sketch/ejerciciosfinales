# Encontrar el número más grande en una lista de números. (numeros = [3, 15, 8, 23, 42, 16])

entrada = input("ingresa numeros separados por comas: ") 

lista = [int(num.lstrip("0") or "0") for num in entrada.split(",")]

mayor = max(lista)

print("el numero mas grande es:", mayor)