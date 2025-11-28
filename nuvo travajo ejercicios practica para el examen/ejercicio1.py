
#Utilizando funciones y ciclos for determinar si una lista esta ordenada 

def listaordenada(lista):
    
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1 ]:
            return False
    return True

def verificar_y_ordenar(lista):
    if listaordenada(lista):
        print("la lista ya esta ordenada",lista)

    else:
        print("la lista no esta ordenada",lista)
        print("lista ornenada correctamente", sorted(lista))

entrada =input("ingrese la lista separadas por coma: ")
lista_usuario = list(map(int,entrada. split(",")))

verificar_y_ordenar(lista_usuario)