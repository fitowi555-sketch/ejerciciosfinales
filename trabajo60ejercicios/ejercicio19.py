
#Pide una velocidad y clasifícala en "Baja", "Normal" o "Alta".

velocidad = int(input("ingrese la velocidad:"))

if velocidad < 30:
    print("la velocidad es baja:", velocidad)

elif velocidad >= 30 and velocidad < 80:
    print("la velocidad es normal:", velocidad)

else: 
    print("la velocidad es alta:", velocidad)
