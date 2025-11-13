
#Pide un usuario y contraseña y verifica si coinciden con valores predeterminados.

usuario_correcto = "administrado"
contraseña_correcta = "andres2905"

usuario =input("ingrese el usuario:")
contraseña =input("ingrese una contraseña:")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("acceso permitido")

else: 
    print("usuario o contraseña incorrectos:")


