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
    ''' Dado un archivo csv, retorna una lista cuyos elementos
    son cada una de las filas del archivo'''
    archivo = open(archivo, 'r',encoding='latin-1') #con utf-8 habia error. Si el programa no corre, eliminar el encoding='latin-1'
    archivo_reader= csv.reader(archivo, delimiter = ',')
    next(archivo_reader, None)

    lista = []

    for row in archivo_reader:
        lista.append(row)

    return lista
    archivo.close()

archivo = open("C:/Users/Trinidad/Documents/Proyectos/ISFDyT166/Covid19VacunasaAgrupadas.csv")
#MAIN
#lista_vacunas = archivo_csv_a_lista("Covid19VacunasAgrupadas.csv")
#print(lista_vacunas)
#lista_cabañas = archivo_csv_a_lista("cabañas.csv")
#print(lista_cabañas)