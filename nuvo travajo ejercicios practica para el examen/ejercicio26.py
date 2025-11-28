# Encontrar los valores comunes entre dos listas.

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = []

for num in lista1:
    if num in lista2:
        comunes.append(num)

print("valores comunes:", comunes)