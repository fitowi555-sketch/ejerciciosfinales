
#Utilizando funciones y ciclos for determinar si una lista esta ordenada 

def listaordenada(lista):
    
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1 ]:
            return False
    return True

numero = [1,2,3,4,5,6,7,8,9,10]
print(listaordenada(numero))

numero2 = [1,3,2,4,6,5,7,9,8,10] 
print(listaordenada(numero2))

