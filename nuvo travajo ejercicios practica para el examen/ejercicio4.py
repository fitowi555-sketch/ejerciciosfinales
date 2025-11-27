#Crar un algoritmo que nos premita contar las vocales de la palabra tecnología  

palabra = "tecnologia"
vocales = "aeiouáéíóú"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1


print(f"la palabra {palabra} tiene {contador} vocales.")


