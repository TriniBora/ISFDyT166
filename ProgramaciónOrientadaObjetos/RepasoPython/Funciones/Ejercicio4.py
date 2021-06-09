'''Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
resultado de aplicar la función dada a cada uno de los elementos de la lista. '''

def calcular_cuadrados(lista_nros):
    '''La funcion calcular_cuadrados reciba una lista de numeros de la listay retorna otra lista con los cuadrados de cada uno de los numeros de la lista original'''
    lista_cuadrados = []
    for nro in lista_nros:
        lista_cuadrados.append(nro**2)

    return lista_cuadrados

def aplicar_funcion(lista_nros, calcular_cuadrados):
    '''La funciona aplicar_funcion recibe la funcion calcular_cuadrados y una lista de numeros y retorna
    precisamente el resultado de esta funcion recibida, aplicada  a lista de numeros.'''
    return calcular_cuadrados(lista_nros)

#MAIN
lista_numeros1 = [23, 45, 9, 0, 8]
print(aplicar_funcion(lista_numeros1,calcular_cuadrados))

lista_numeros2 = []
print(aplicar_funcion(lista_numeros2,calcular_cuadrados))

lista_numeros3 = [0]
print(aplicar_funcion(lista_numeros3,calcular_cuadrados))

lista_numeros4 = [-3, 4.88, 0, -5.6]
print(aplicar_funcion(lista_numeros4,calcular_cuadrados))