'''Implementar los algoritmos de búsqueda simple y binaria.
1. Búsqueda simple: busca desde el primer dato hasta el último, uno a uno comparando
sucesivamente todos los datos en memoria hasta localizar el dato que queramos
localizar. Este algoritmo puede usarse en cualquier situación, pero se recomienda
usarlo solo en listas que no estén ordenadas.'''

def busqueda_simple(lista_nros, nro):

    encontrado = False

    for elemento in lista_nros:
        if nro == elemento:
            encontrado = True

    return encontrado


#MAIN
lista_nros1 = [23, -45, 9, 0, 8, 6.4]

nro_buscado1 = 0
nro_buscado2 = 4

encontrado = busqueda_simple(lista_nros1, nro_buscado1)
print(f'El número {nro_buscado1} está en la lista {lista_nros1}?: {encontrado}')

encontrado = busqueda_simple(lista_nros1, nro_buscado2)
print(f'El número {nro_buscado2} está en la lista {lista_nros1}?: {encontrado}')

lista_nros2 = []

encontrado = busqueda_simple(lista_nros2, nro_buscado1)
print(f'El número {nro_buscado1} está en la lista {lista_nros2}?: {encontrado}')

lista_nros3 = [0]

encontrado = busqueda_simple(lista_nros3, nro_buscado1)
print(f'El número {nro_buscado1} está en la lista {lista_nros3}?: {encontrado}')

encontrado = busqueda_simple(lista_nros3, nro_buscado2)
print(f'El número {nro_buscado2} está en la lista {lista_nros3}?: {encontrado}')
