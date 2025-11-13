
#Pide una temperatura en grados Celsius y convierte a Fahrenheit o Kelvin.

celsius = float(input("ingrese la temperatura en grados celsius:"))

print("a que unidad quiere convertir")
print("1. fahrenheit")
print("2. kelvin")

opccion =input("seleccione la opccion (1 o 2):")

if opccion == "1":
    fahrenheit = (celsius * 9/5) + 32 
    print(f"la temperatura en fahrenheit es: {fahrenheit} °F")

elif opccion == "2":
    kelvin = celsius + 273.15
    print(f"la temperatura en kelvin es: {kelvin} K")

else:
    print("no se encuentran datos valido elija la opccion 1 o 2") 