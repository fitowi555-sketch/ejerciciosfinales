
#Pide el número de días de retraso en la devolución de un libro y calcula la multa.

dias = int(input("ingrese el dia de retraso del libro: "))

if dias <= 5:
    multa = 0
    print("el libro fue entregado a tiempo no se aplican multas")
else:
    dias_con_multas = dias - 5
    multa = dias_con_multas * 20000
    print(f"la multa por {dias} dias de retraso a pagar es: $ {multa}")
