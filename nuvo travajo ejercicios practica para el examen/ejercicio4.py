#Crar un algoritmo que nos premita contar las vocales de la palabra tecnología  

palabra = "tecnologia"
vocales = "aeiouáéíóú"
contador = 0
vocales_encontradas = []

for letra in palabra:
    if letra in vocales:
        contador += 1
        
        vocales_encontradas.append(letra)
vocales_unicas = set(vocales_encontradas)

print(f"la palabra {palabra} tiene {contador} vocales.")
print(f"las vocales que contiene son: {",".join(vocales_unicas)}")