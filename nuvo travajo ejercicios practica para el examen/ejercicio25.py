# Contar cuántos números en una lista son mayores que un valor dado (ej. 10). numeros = [5, 12, 3, 18, 25, 7]

lista = list(map(int,input("digite la lista de numeros separados por comas: ").split(",")))

numero_dado = int(input("digite el numero de referencia: "))

contador = 0 
mayores = []

for n in  lista:
    if n > numero_dado:
        contador += 1
        mayores.append(n)
print("hay", contador, "numeros mayores que", numero_dado)
print("los numero mayores son:", mayores)