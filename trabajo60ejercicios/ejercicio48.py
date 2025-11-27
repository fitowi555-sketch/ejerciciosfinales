
#Pide un tipo de sangre y determina a qué grupos puede donar y recibir.

tipo = input("digite el tipo de sangre (A+,A-,B+,B-,AB+,AB-,O+,O-): ").upper()

if tipo == "A+":
    print(" A+ puede donar a: A+,AB+")
    print("Y puede recibir de: A+,A-,O+,O-")

elif tipo == "A-":
    print("A- puede donar a: A+,A-,AB+,AB-")
    print("Y puede recibir de: A-,O-")

elif tipo == "B+":
    print("B+ puede doar a: B+,AB+")
    print("Y puede recibir: B+,B-,O+,O-")

elif tipo == "B-":
    print("B- puede donar a: B+,B-,AB+,AB-")
    print("Y puede recibir de: B-,O-")

elif tipo == "AB+":
    print("AB+ puede donar solo a: AB+ ")
    print("Y puede recibir de: TODOS LOS TIPOS (RECEPTOR UNIVERSAL)")

elif tipo == "AB-":
    print("AB- puede donar a: AB+,AB-")
    print("Y puede recibir de: A-,B-,AB- Y O-")

elif tipo == "O+":
    print("O+ puede donar a: O+,A+,B+,AB+")
    print("Y puede recibir de: O+,O-")

elif tipo == "O-":
    print("O- puede donar a: TODOS LOS TIPOS (DONANTE UNIVERSAR)")
    print("Y puede recibir solo de: O-")

else:
    print("tipo de sangre no valido por favor ingrese un tipo valido:")