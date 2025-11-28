# Contar cuántos números del 1 al 100 son divisibles por 3.

numeros = list(range(1,11))
divisible = []

for n in numeros:
    if n % 3 == 0:
        divisible.append(n)

print("cantidad:", len(divisible))
print("numeros:", divisible)