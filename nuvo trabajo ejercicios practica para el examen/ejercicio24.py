# Imprimir un triángulo invertido de asteriscos de 5 filas.

for i in range(5, 0, -1):
    print(" "* (5-i) + "*" * (2*i-1))