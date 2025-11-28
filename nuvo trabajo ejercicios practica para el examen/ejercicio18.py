# Calcular la suma de los dígitos de un número (ejemplo, 12345).

numero = input("ingrese un numero: ")
suma = 0

print("proceso de suma:")

for digito in numero:
    print(f"{suma} + {digito} = {suma + int(digito)}")
    suma += int(digito)

print("\nla suma de los digitos es:", suma)