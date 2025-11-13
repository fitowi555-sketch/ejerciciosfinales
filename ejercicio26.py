
#Pide el número de horas trabajadas y calcula el salario con 50% más para horas extra.

horas_laboradas = int(input("ingrese el total de horas trabajadas:"))
horas_extras = 0.50

mul = horas_laboradas * 6.189

suma = mul * (1 + 0.50)

if horas_laboradas > 44:
    print(f"su sueldo es de, mas las horas extras: , {suma:.2f}")

else:
    print(f"su sueldo es: , {mul:.2f}")


