'''Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con
los elementos de la lista que devuelvan True al aplicarles la función booleana.'''

def lista_positivos(nro):
    '''La funcion es_positivo verifica si el número recibido es
    mayor que 0 y retorna True si lo es o False si no lo es.'''
    if nro > 0:
        return True
    else:
        return False

def aplicar_funcion_booleana(lista_nros, es_positivo):
    '''La funciona aplicar_funcion_boolena recibe la funcion es_positivo y una lista de numeros y devuelva otra lista con
los elementos de la lista que devuelvan True al aplicarles la función booleana, es decir, elementos positivos.'''
    lista_positivos = []

    for nro in lista_nros:
        if es_positivo(nro):
            lista_positivos.append(nro)

    return lista_positivos

#MAIN
lista_numeros1 = [23, 45, 9, 0, 8]
print(aplicar_funcion_booleana(lista_numeros1, lista_positivos))

lista_numeros2 = []
print(aplicar_funcion_booleana(lista_numeros2, lista_positivos))

lista_numeros3 = [0]
print(aplicar_funcion_booleana(lista_numeros3, lista_positivos))

lista_numeros4 = [-3, 4.88, 0, -5.6]
print(aplicar_funcion_booleana(lista_numeros4, lista_positivos))