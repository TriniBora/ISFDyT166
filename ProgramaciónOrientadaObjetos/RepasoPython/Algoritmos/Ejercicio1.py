'''Implementar un algoritmo de ordenamiento  por burbuja de una lista numérica.'''

def ordenamiento_por_burbuja(lista_nros):

    for i in range(len(lista_nros)):
        for j in range(0, len(lista_nros)-i-1):
            if lista_nros[j] > lista_nros[j+1]:#intercambio si el nro es más grande que el siguiente
                lista_nros[j], lista_nros[j+1] = lista_nros[j+1], lista_nros[j]

    print ("Lista ordenada:")
    for nro in lista_nros:
        print (nro)

#MAIN
lista_nros1 = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_por_burbuja(lista_nros1)
