
#Pide una temperatura y clasifícala como "Muy frío", "Frío", "Tibio", "Caliente", o "Muy caliente".

temperatura = int(input("ingrese la temperatura:"))

if  temperatura <= 5:
    print(f"temperatura es muy fria:{temperatura } °C")

elif temperatura <= 11:
      print(f"temperatura es fria :{temperatura } °C")

elif temperatura <= 16:
       print(f"temperatura es tibio:{temperatura } °C")

elif  temperatura <= 31:
        print(f"temperatura es templado:{temperatura } °C")

elif temperatura  <= 36:
        print(f"temperatura es caliente:{temperatura } °C")

elif temperatura <= 41:
        print(f"temperatura es muy caliente:{temperatura } °C")

else:
    print(f"temperatura fuera de los rangos completados: {temperatura}°C")

          