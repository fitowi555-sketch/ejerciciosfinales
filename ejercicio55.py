
#Crea un programa que pida la edad de una persona y determine su fase de vida: "Infancia" (0-12), "Adolescencia" 
# (13-17), "Adultez" (18-59) y "Vejez" (60 o más).

edad = int(input("ingrese la edad:"))

if 0 <= edad <= 12:
    fase = "infancia"

elif 13 <= edad <= 17:
    fase = "adolecente"

elif 18 <= edad <= 59:
    fase = "adultez"

elif edad >= 60:
    fase = "vejez"
    
else: 
    fase = "edad invalida"

print("fase de vida:", fase)