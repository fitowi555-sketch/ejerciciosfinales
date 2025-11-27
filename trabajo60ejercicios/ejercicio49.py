
#Pide un día de la semana y determina si es fin de semana o día laboral.

dia_semana =input("dijita el dia de la semana: ").lower()

if dia_semana in ["lunes","martes","miercoles","jueves","viernes"]:
    print("es un dia laboral")

elif dia_semana in ["sabado","domingo"]:
    print("es fin de semana")

else:
    print("no es un dia valido ingresar un dia de semana valido:")
