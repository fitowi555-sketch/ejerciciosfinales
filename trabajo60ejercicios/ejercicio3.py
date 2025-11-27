
#Crea un programa que pida la edad de una persona y determine si es un niño (0-12 años), un adolescente (13-17 años), un adulto (18-64 años) o un adulto mayor (65 años o más).

edad = int(input("ingrese la edad:"))


if edad <= 12:
    print("es un niño:", edad)

elif edad <= 17:
    print("es un adolecente:", edad)

else:
    print("es un adulto:" , edad)