
# Imprimir la suma de los números pares del 1 al 100.

suma = 0

for i in range(1,101):
    if i % 2 == 0:
        suma += i
    print("la suma de los numero pares de 1 al 100 es: ", suma)

