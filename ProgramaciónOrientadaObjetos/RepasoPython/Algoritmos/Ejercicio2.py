'''Implementar un algoritmo de ordenamiento  por inserción de una lista numérica.'''

def ordenamiento_por_insercion(lista_nros):

    for i in range(1, len(lista_nros)):
        marcador = lista_nros[i]

        j = i-1
        while j >= 0 and marcador < lista_nros[j]:
            lista_nros[j + 1] = lista_nros[j]
            j -= 1
            lista_nros[j + 1] = marcador

    print ("Lista ordenada por inserción:",lista_nros)


#MAIN
lista_nros1 = [23, 45, 9, 0, 8]
ordenamiento_por_insercion(lista_nros1)

lista_nros2 = []
ordenamiento_por_insercion(lista_nros2)

lista_nros3 = [0]
ordenamiento_por_insercion(lista_nros3)

lista_nros4 = [-3, 4.88, 0, -5.6]
ordenamiento_por_insercion(lista_nros4)
