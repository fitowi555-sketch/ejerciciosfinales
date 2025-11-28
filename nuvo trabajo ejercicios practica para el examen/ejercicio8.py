# Eliminar duplicados de una lista. (lista = [1, 2, 2, 3, 4, 4, 5]

entrada = input("digite la lista separada por comas: ")

lista = [int(num) for num in entrada.split(",")]

resultado = []

for num in lista:
    if num not in resultado:
        resultado.append(num) 

print("lista sin duplicados:",resultado)