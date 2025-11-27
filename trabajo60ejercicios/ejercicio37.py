
#Pide el monto de una transferencia y el saldo disponible, y detecta si la transacción es fraudulenta.

saldo_disponible = 300000

transferencia = int(input("ingrese el monto de la tranferencia:"))

RESTA = saldo_disponible - transferencia

if saldo_disponible >= transferencia: 
    print("la transferencia se realizo con exito saldo disponible:",RESTA)

else:
    print("saldo insuficiente:")
    print("pesible transaccion fraudulenta verifique los movimiento y si no es usted reportelo:")
