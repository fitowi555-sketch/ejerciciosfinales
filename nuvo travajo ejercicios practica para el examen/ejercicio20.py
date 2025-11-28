# Invertir una cadena usando un ciclo for.

texto = input("ingrese la cadena: ")
invertida = ""

for letra in texto:
    invertida = letra + invertida
print("la cadena invertida queda asi:",invertida)