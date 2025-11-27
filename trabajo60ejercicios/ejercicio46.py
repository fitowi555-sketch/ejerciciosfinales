#Pide una contraseña y verifica si cumple ciertos requisitos (mayúsculas, minúsculas, números).

contraseña = input("digite la conttraseña:")

tienemayusculas = False
tieneminuscula = False
tienenumeros = False

for caracter in contraseña:
   if caracter.isupper():
     tienemayuscula = True

   elif caracter.islower():
      tieneminusculas = True

   elif caracter.isdigit():
      tienenumeros = True


if tienemayusculas and tieneminuscula and tienenumeros:
   print("la contraseña cumple con todos los reqisitos")
   
else:
   print("la contraseña no cumple con todos los parametros")
   
   if not tienemayusculas:
      print("falta almenos una letra mayuscula")

   if not tieneminuscula:
      print("falta almenos una letra minuscula")

   if not tienenumeros:
      print("falta almenos un numero")