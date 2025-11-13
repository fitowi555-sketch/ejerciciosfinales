#Pide una contraseña y verifica si cumple ciertos requisitos (mayúsculas, minúsculas, números).

contraseña = input("digite la conttraseña:")

mayusculas = False
minuscula = False
numeros = False

for caracter in contraseña:
   if caracter.isupper():
     tienemayuscula = True

   elif caracter.islower():
      tieneminuscula = True

   elif caracter.isdigit():
      tienenumeros = True


if tieneminuscula = 