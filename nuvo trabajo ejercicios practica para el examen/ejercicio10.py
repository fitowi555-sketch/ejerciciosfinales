# Imprimir la primera y última letra de cada palabra en una frase. frase = Este es un ejemplo


frase = input("escriba una frace: ").strip()
palabras = frase.split()

for p in palabras:
    primeras = p[0]
    ultima = p[-1]
    print(f"{p} -> {primeras}{ultima}")