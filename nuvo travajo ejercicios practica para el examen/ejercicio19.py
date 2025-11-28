# Calcular la suma de los números del 1 al 100 que son múltiplos de 5 o 7.

suma = 0 

for i in range(1,101):
    if i % 5 == 0 or i % 7 == 0:
        suma += i
print(suma)