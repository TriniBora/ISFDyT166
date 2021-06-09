'''Escribir una función que reciba una muestra de números en una lista y devuelva su media.'''

def calcular_media(lista_numeros):
    '''La funcion calcular_media llama a la funcion agregar_numeros y si tiene elementos, calcula el promedio y retorna este valor. Si la lista está vacía, retorna cero.'''
    suma = 0

    if len(lista_numeros) > 0:
        for numero in lista_numeros:
            suma += int(numero)
        return suma / len(lista_numeros)
    else:
        return 0

#MAIN
test1 = calcular_media([1,2,3,4])
print(f'La media de la lista de números es {test1:.2f}.')

test2 = calcular_media([])
print(f'La media de la lista de números es {test2:.2f}.')

test3 = calcular_media([0])
print(f'La media de la lista de números es {test3:.2f}.')

test4 = calcular_media([-1,2.7,3.99,4])
print(f'La media de la lista de números es {test4:.2f}.')

test5 = calcular_media([235])
print(f'La media de la lista de números es {test5:.2f}.')
