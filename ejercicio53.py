
#Una empresa de alquiler de autos permite alquilar vehículos solo a personas mayores de
#21 años. Sin embargo, si la persona tiene entre 21 y 25 años, se le cobra un cargo
#adicional del 15%. Si es mayor de 25, no se cobra ningún cargo adicional. Escribe un
#programa que determine si alguien puede alquilar un auto y el costo adicional si aplica.

edad =int(input("ingrese la edad:"))
precio =int(input("ingrese el valor del veiculo:"))

if edad > 21 and edad < 25:
    valor_aplicado = precio * (1+0.15)
    print("se aplica un valor adicionla de 15%:", valor_aplicado)

else:
    print("no se aplica el valor adicional")

