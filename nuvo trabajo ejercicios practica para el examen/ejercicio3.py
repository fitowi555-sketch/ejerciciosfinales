#Crear un algoritmo en python con ciclos for que nos imprima las tablas de multiplicar 

numero = int(input("digite el numero: "))

print(f"\ntabla del {numero}")
print("---------------")

for i in range(1,11):
    resultado = numero*i
    print(f"{numero} x {i} = {resultado}")