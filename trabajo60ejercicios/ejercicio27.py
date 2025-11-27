
#Pide peso y altura, calcula el IMC y clasifícalo en "Bajo peso", "Normal", "Sobrepeso" o "Obesidad".

peso = float(input("ingrese el peso:"))
altura =float(input("ingrese la altura en metros:"))


IMC = peso / (altura ** 2)



if IMC < 18.5:
    clasificacion = "Bajo de peso"

elif IMC < 25:
  clasificacion = "Peso nolmal"

elif IMC < 30:
    clasificacion = "Sobrepeso"

else: 
  clasificacion = "Obeso"

print(f"su IMC es:, {IMC:.2f}")
print(f"clasificacion:,{clasificacion}")