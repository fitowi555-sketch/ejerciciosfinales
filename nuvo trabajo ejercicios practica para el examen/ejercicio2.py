#Imprimir  un triangulo de asteriscos de n filas
for i in range(5):
  for k in range(5-i-1):
    print(" ", end="")

  for j in range(i+1+i):
    print("*", end="")
  print()