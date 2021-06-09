'''Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
que una palabra fue cortada con el agregado de una arroba). Por otro lado cobra un valor
para las palabras cortas y otro valor para las palabras largas (que deben ser cortadas).
Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de
cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
telegrama y el costo del mismo.'''


def cortar_palabra(palabra, long_max):
    '''La funcion cortar_palabra recibe una cadena de caracteres y si tiene
    más de la longitud maxima indicada, corta la cadena añadiendole una "@" al final.
    Devuelve la cadena modificada.'''

    palabra_cortada = ""
    lista_palabra = []

    for i in range(0, long_max):
        lista_palabra.append(palabra[i])
    lista_palabra.append("@")
    palabra_cortada = "".join(lista_palabra)

    return palabra_cortada


def procesar_texto(texto, long_max):
    '''La función procesar texto recibe un texto y una longitud máxima de palabra. Recorre todo el texto y si la palabra tiene una longitud mayor a la indicada se llama a la función cortar_palabra.
    Retorna el texto procesado.'''

    lista_palabras = texto.split()
    texto_procesado = []

    for palabra in lista_palabras:
        if len(palabra) > 5:
            palabra = cortar_palabra(palabra, long_max)
        texto_procesado.append(palabra)

    texto_procesado = " ".join(texto_procesado)

    return texto_procesado


def calcular_total(texto_procesado, long_max, costo_pal_corta, costo_pal_larga):
    '''La función calcular_total recorre el texto procesado y contabiliza la cantidad de palabras cuya longitid es menor o igual a la longitud máxima indicada y la cantidad de palabras cuya longitud es mayor.
    Luego calcula el costo total de acuerdo a los precios deingresados por el usuario y retorna el costo_total.'''

    total = 0.0
    cont_pal_corta = 0
    cont_pal_larga = 0
    for palabra in texto_procesado:
        if len(palabra) <= long_max:
            cont_pal_corta += 1
        else:
            cont_pal_larga += 1
    total = costo_pal_corta*cont_pal_corta + costo_pal_larga*cont_pal_corta
    return total


def procesamiento_de_telegrama(texto, long_max, costo_pal_corta, costo_pal_larga):
    '''La función procesamiento_de_telegrama recibe un texto, la longitud máxima de las palabras, el costo de cada palabra corta, el costo de cada palabra larga, y retorna una impresión por pantalla con el texto del telegrama y el costo del mismo'''
    texto_procesado = procesar_texto(texto, long_max)
    costo_total = calcular_total(texto_procesado, long_max, costo_pal_corta, costo_pal_larga)
    return print(f"El texto del telegrama es:\n {texto_procesado} \nEl costo del telegrama es ${costo_total:.2f}")


# MAIN
texto = input("Ingrese una cadena de palabras separadas por espacios: ")
long_max = int(
    input("Ingrese la longitud máxima que puede tener la palabra: "))
precio_pal_corta = float(input(
    f"Ingrese el costo de cada palabra de hasta {long_max} caracteres inclusive: "))
precio_pal_larga = float(
    input(f"Ingrese el costo de cada palabra más de {long_max} caracteres: "))
procesamiento_de_telegrama(texto, long_max, precio_pal_corta, precio_pal_larga)
