# Convertir una lista de números en una lista de sus cuadrados.

entrada = input("digita la lista separadas por espacios: ")
numeros = [int (n) for n in entrada.split()]
cuadrados = [n**2 for n in numeros]

print("lista original:", numeros)
print(":lista de cuadrados:", cuadrados)