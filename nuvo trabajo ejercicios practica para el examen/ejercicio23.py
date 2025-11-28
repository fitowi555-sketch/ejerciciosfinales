# Contar cuántas veces aparece cada letra en una cadena.

texto = input("escribe una cadena: ")

solo_letras = " ".join(ch.lower() for ch in texto if ch.isalpha())

contador = {}
for ch in solo_letras:
    if ch in contador:
        contador[ch] += 1
    else:
        contador[ch] = 1

if contador:
    print("\nletras encontras y sus cantidades")

    for letra in sorted(contador):
        print(f"{letra}: {contador[letra]}")
        print(f"\nTotal de letras distintas: {len(contador)}")
    else:
        print("no se dectetaron letras en la entrada")
