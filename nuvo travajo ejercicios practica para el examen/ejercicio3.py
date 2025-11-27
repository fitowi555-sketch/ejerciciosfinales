#Crear un algoritmo en python con ciclos for que nos imprima las tablas de multiplicar 

for numero in range(1,10):
    print(f"\ntablas del {numero}")

    print("---------------")

    for i in range(1,11):
        resultado = numero*i
        print(f"{numero} x {i} = {resultado}")