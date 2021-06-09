'''Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario
generado con la función anterior y devuelva una tupla con la palabra más repetida y su
frecuencia. '''


def contar_palabras(cadena):
    ''' La funcion contar_vocales cuenta cuántas
    ocurrencias de cada vocal hay en la cadena indicada y devuelve
    la cantidad de ocurrencias.'''

    lista_cadena = cadena.split()

    contador = {}

    for palabra in lista_cadena:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return(contador)

def palabra_mas_repetida(dic_cadena):

    lista_cadena=[]

    for palabra,cantidad in dic_cadena.items():
        lista_cadena.append((cantidad, palabra))
    lista_cadena.sort(reverse=True)
    mayor_frecuencia = lista_cadena[0] #guardo en una variable el primer elemento de la lista, el que más ocurrencias tiene
    for elemento in lista_cadena: #recorro todas las tuplas palabra-cantidad
      if elemento[0] == mayor_frecuencia[0]: #imprimo solo las tuplas cuya cantidad es la misma que la de mayor frecuencia
        print(elemento)


#MAIN
cadena = input("Ingrese una cadena de caracteres: ")
dic_cadena = contar_palabras(cadena)
print(f'La/s palabra/s más repetida/s en la cadena "{cadena}" es/son: ')
palabra_mas_repetida(dic_cadena)
