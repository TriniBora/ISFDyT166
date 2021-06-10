'''Búsqueda binaria: este tipo de búsqueda es usado en listas que estén previamente
ordenadas, ya que su método de búsqueda es la de dividir los datos en dos grupos,
eligiendo el grupo en el cual debería estar el dato buscado (supone que está
ordenado alfabéticamente o numéricamente), volviendo a aplicar la división, y así
sucesivamente hasta verificar si existe o no existe el dato buscado. Aplicar en este
caso recursividad.'''

def ordenar_lista(lista_nros):
    lista_nros.sort()
    lista_ordenada = lista_nros
    return lista_ordenada


def busqueda_binaria_recursiva(lista_ordenada_nros, buscado, i, k):
    '''La funcion busqueda_binaria_recursiva recibe una lista de numeros, el numerosa buscar en la lista y dos valores i, k que indican los extremos del intervalo donde se va a buscar.
    Retorna -1 si el número buscado no está en la lista o el índice del elemnto correspondiente, en caso de que sí esté.'''

    if i > k:
        #si los extremos se "cruzan" quiere decir que se terminó la búsqueda
        return -1

    j = (i + k) // 2
    #j es el índice del elemento medio de la lista de numeros en el intervalo de extremos i, k

    mitad = lista_ordenada_nros[j]
    #mitad es el elemento medio de la lista de numeros en el intervalo

    if mitad == buscado:
        #si el numero buscado coincide con el elemento medio dle intervalo, se retorna ese indice
        return j

    if buscado < mitad:
        #si el numero buscado es menor que el elemento medio del intervalo, se vuelve a llamar a la funcion pero esta vez el extremo superior del intervalo sera el indice del elemento anterior al elemento medio
        return busqueda_binaria_recursiva(lista_ordenada_nros, buscado, i, j - 1)
    else:
        #si el numero buscado es mayor que el elemento medio del intervalo, se vuelve a llamar a la funcion pero esta vez el extremo inferior del intervalo sera el indice del elemento siguiente al elemento medio
        return busqueda_binaria_recursiva(lista_ordenada_nros, buscado, j + 1, k)


def mostrar_mensaje(lista_nros, buscado, encontrado):
    if encontrado == -1:
        print(f'El número {buscado} no está en la lista {lista_nros}.')
    else:
        print(f'El número {buscado} está en la lista {lista_nros}.')


#MAIN
lista_nros = [23, -45, 9, 0, 8, 6.4]
lista_ordenada = ordenar_lista(lista_nros)

nro_buscado = 0
encontrado = busqueda_binaria_recursiva(lista_ordenada, nro_buscado, 0, len(lista_nros))
mostrar_mensaje(lista_ordenada, nro_buscado, encontrado)

nro_buscado = 4
encontrado = busqueda_binaria_recursiva(lista_ordenada, nro_buscado, 0, len(lista_nros))
mostrar_mensaje(lista_ordenada, nro_buscado, encontrado)
