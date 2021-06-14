'''1. Escribir un programa que lea la información de vacunación por COVD-19 por provincias y
almacene en estructuras que permitan dar respuestas a las siguientes consultas:
1. Dada una provincia informar total de vacunas aplicadas, tipo de vacuna con mayor
cantidad de aplicaciones, tipo de vacuna con menor cantidad de aplicaciones.
2. Listar un ranking de las 10 provincias con mayor porcentaje de segundas dosis
totales aplicadas
3. Listar un ranking de las vacunas por mayor porcentaje de segundas dosis totales
aplicadas'''

import csv

def archivo_csv_a_lista(archivo):
    ''' Dado un archivo csv, lo abre, retorna una lista cuyos elementos contienen cada una
    de las filas del archivo y cierra el archivo.'''

    lista_datos = []

    with open(archivo) as File:
        reader = csv.reader(File, delimiter = ',')
        next(reader, None)#excluyo el encabezado del archivo
        for row in reader:
            lista_datos.append(row)

    return lista_datos

    archivo.close()


def extraer_datos(lista_datos, nro_columna):
    '''La funcion extraer_datos guarda en una lista los especificados
    por el nro de columna indicado (por ejemplo, provincias, tipos de vacunas, etc).
    Retorna dicha lista de datos especificos.'''

    datos_extraidos = []

    for row in lista_datos:
        if row[2] not in datos_extraidos:
            datos_extraidos.append(row[nro_columna])

    return datos_extraidos


def total_dosis_aplicadas(lista_datos, tipo_dosis):
    '''La funcion total_dosis_aplicadas recibe los datos en forma de lista con toda la
    info obtenida del archivo csv y la dosis de la cual se quiere saber el total.
    Retorna la cantidad total de aplicaciones de dicha dosis.'''

    lista_dosis = extraer_datos(lista_datos, tipo_dosis)
    #recibe la lista con todas las dosis indicadas

    lista_dosis_int = [int(elemento) for elemento in lista_dosis]
    #convierto a int todos los elementos str de la lista para poder sumarlos

    total = sum(lista_dosis_int)#sumo todos los valores de la lista de dosis

    return total


def cantidad_dosis_aplicadas_por_criterio(lista_datos, criterio_seleccion, nro_columna):
    '''La funcion cantidad_dosis_aplicadas_por_criterio recibe la lista de datos, el criterio
    por el cual va a sumar los totales (por provincia o por tipo de vacuna) y el número de
    columna de ese criterio en la lista de datos.
    Retorna una lista de dos elementos, cuyo primer elemento es el total de primeras dosis y
    el segundo elemento, el total de segundas dosis, en base al criterio pasado por parámetro.'''

    total = [0,0]

    for elemento in lista_datos:
        if elemento[nro_columna] == criterio_seleccion:
            total[0] += int(elemento[3])#total de primera dosis
            total[1] += int(elemento[4])#total de segunda dosis

    return total

def tipo_vacuna_cant_aplicaciones(lista_datos, provincia):
    '''Dada una provincia, la funcion tipo_vacuna_cant_aplicaciones retorna una lista
    donde el primer elemento es el tipo de vacuna con mayor cantidad de aplicaciones y
    el segundo es el tipo de vacuna con menor cantidad de aplicaciones en esa provincia'''

    dict_tipos = {}
    tipo_mayor = ""
    tipo_menor = ""

    for elemento in lista_datos:
        if elemento[1] == provincia:
            dict_tipos[elemento[2]] = int(elemento[3]) + int(elemento[4])

    tipo_mayor = max(dict_tipos.keys())#obtengo la clave con mayor valor
    #mayor = dict_tipos.get(tipo_mayor)#obtengo ese valor maximo

    tipo_menor = min(dict_tipos.keys())#obtengo la clave con menor valor

    return [tipo_mayor, tipo_menor]


def info_por_provincia(lista_datos, provincia):
    '''Dada una provincia, la funcion info_por_provincia, muestra por pantalla, 
    el total de vacunas aplicadas, el tipo de vacuna con mayor cantidad de aplicaciones
    y el tipo de vacuna con menor cantidad de aplicaciones'''

    total_por_dosis = []
    cant_total=0
    tipo_mayor=""
    tipo_menor=""

    total_por_dosis = cantidad_dosis_aplicadas_por_criterio(lista_datos, provincia, 1)
    #lista donde el primer elemento es la cantidad total de primeras dosis en la provincia,
    #y el segundo elemento es la cantidad total de segundas dosis

    cant_total = total_por_dosis[0] + total_por_dosis[1]

    tipo = tipo_vacuna_cant_aplicaciones(lista_datos, provincia)

    return print(f'\nEl total de vacunas aplicadas en la provincia de {provincia} es: {cant_total}\nEl tipo de vacuna con mayor cantidad de aplicaciones en {provincia} es: {tipo[0]} \nEl tipo de vacuna con menor cantidad de aplicaciones en {provincia} es: {tipo[1]}')


def dosis_totales_por_criterio(lista_datos, nro_columna):
    '''La funcion dosis_totales_por_criterio recibe la lista de datos y el numero de la
    columa que corresponde al rango de datos seleccionados(provincia o tipo de vacuna y
    retorna un diccionario con los pares clave: tipo de vacuna, valor: una lista de dos
    elementos: cantidad de aplicaciones de primera dosis y cantidad de aplicaciones de
    segunda dosis'''

    dict_elementos_seleccionados = {}

    elementos = extraer_datos(lista_datos, nro_columna)

    for elemento in elementos:
        total_por_criterio = cantidad_dosis_aplicadas_por_criterio(lista_datos, elemento, nro_columna)
        #recibe una lista donde el primer elemento es la cantidad total de primeras dosis de la vacuna
        #indicada, y el segundo elemento es la cantidad total de segundas dosis
        dict_elementos_seleccionados[elemento] = total_por_criterio

    return dict_elementos_seleccionados

def seleccionar_tipo_dosis(tipo_dosis):
    '''La función seleccionar_tipo_datos, dependiendo del tipo de dosis que se está consultando
    (primeras dosis, columna 3 o segundas dosis, columna 4) se elige el valor 0 o 1 para realizar
    el ordenamiento del ranking y convertir a porcentaje y también se elige qué texto mostrar
    en el mensaje de salida.
    Retorna una lista con dos elementos, el primero el índice para ordenar el ranking y el
    segundo el texto que se mostrará en el encabezado del mensaje del ranking.'''

    if tipo_dosis == 3:#3: columna correspondiente a primeras dosis
        i = 0
        dosis = "primeras"
    if tipo_dosis == 4:#4: columna correspondiente a primeras dosis
        i = 1
        dosis = "segundas"

    return [i, dosis]


def ranking_dosis_aplicadas_por_criterio(lista_datos, nro_columna, tipo_dosis):
    '''La funcion ranking_dosis_aplicadas_por_criterio recibe la lista de datos,
    el numero de la columa que corresponde al rango de datos seleccionados(provincia o
    tipo de vacuna) y el tipo de dosis (primeras o segundas) y retorna una lista ordenada
    en forma descendente de acuerdo al tipo de dosis elegido.'''

    dict_dosis_totales = {}

    dict_dosis_totales = dosis_totales_por_criterio(lista_datos, nro_columna)

    i = seleccionar_tipo_dosis(tipo_dosis)[0]

    ranking = sorted(dict_dosis_totales.items(), key=lambda x: x[1][i], reverse=True)
    '''dic.items() devuelve una lista de pares clave-valor del diccionario y el tipo de datos 
    de su elemento es tuple. x es el elemento de esta tupla, donde x[0] es la clave y x[1]
    es el valor. key=lambda x:x[1] indica que la clave de comparación es el valor de los elementos
    del diccionario.El parámetro opcional reverse puede ser establecido como true si los valores
    necesitan ser ordenados en orden descendente.En este caso la clave x[1][i] hace referencia
    al primer o segundo elemento del valor de la clave x.'''

    return ranking


def mostrar_ranking_por_provincia(lista_datos, tipo_dosis):
    '''La función mostrar_ranking_por_provincias muestra por pantalla un ranking de las 10
    provincias con mayor porcentaje de dosis totales aplicadas segun el tipo de dosis indicada.'''

    ranking = ranking_dosis_aplicadas_por_criterio(lista_datos,1, tipo_dosis)

    total = total_dosis_aplicadas(lista_datos, tipo_dosis)

    i = seleccionar_tipo_dosis(tipo_dosis)[0]
    dosis = seleccionar_tipo_dosis(tipo_dosis)[1]

    for item in range(len(ranking)):
        ranking[item][1][i] = ranking[item][1][i]*100/total
        #se convierte a porcentaje la cantidad de dosis

    print (f'Las 10 provincias con mayor porcentaje de {dosis} dosis totales aplicadas son: ')
    for item in range(11):
        print(f'{item}: {ranking[item][0]}: {ranking[item][1][i]:.2f} %')


def mostrar_ranking_por_tipo_vacuna(lista_datos, tipo_dosis):
    '''La función mostrar_ranking_por_tipo_vacuna muestra por pantalla un ranking de las
    vacunas con porcentaje de dosis totales aplicadas, según el tipo de dosis indicada'''

    ranking = ranking_dosis_aplicadas_por_criterio(lista_datos,2, tipo_dosis)

    total = total_dosis_aplicadas(lista_datos, tipo_dosis)

    i = seleccionar_tipo_dosis(tipo_dosis)[0]
    dosis = seleccionar_tipo_dosis(tipo_dosis)[1]

    for item in range(len(ranking)):
        ranking[item][1][i] = ranking[item][1][i]*100/total
        #se convierte a porcentaje la cantidad de dosis

    print (f'Ranking de las vacunas por mayor porcentaje de {dosis} dosis totales aplicadas: ')
    for item in range(len(ranking)):
        print(f'{item+1}: {ranking[item][0]}: {ranking[item][1][i]:.2f} %')


#MAIN

lista_vacunas = archivo_csv_a_lista("./Covid19VacunasAgrupadas.csv")

#CONSULTA 1:
info_por_provincia(lista_vacunas, "San Luis")
print()
info_por_provincia(lista_vacunas, "Buenos Aires")
print()
info_por_provincia(lista_vacunas, "Catamarca")
print()


#CONSULTA 2:
mostrar_ranking_por_provincia(lista_vacunas, 3)
#el 3 corresponde al indice de la columna de las primeras dosis
print()
mostrar_ranking_por_provincia(lista_vacunas, 4)
#el 4 corresponde al indice de la columna de las segundas dosis
print()

#CONSULTA 3:
mostrar_ranking_por_tipo_vacuna(lista_vacunas, 3)
#el 3 corresponde al indice de la columna de las primeras dosis
print()
mostrar_ranking_por_tipo_vacuna(lista_vacunas, 4)
#el 4 corresponde al indice de la columna de las segundas dosis
print()
