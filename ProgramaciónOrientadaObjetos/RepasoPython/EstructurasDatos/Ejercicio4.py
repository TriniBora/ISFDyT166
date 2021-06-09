'''Escribir una función que reciba como parámetro una cadena de palabras separadas por
espacios y devuelva, como resultado, cuántas palabras de más de cinco letras tiene la
cadena dada.'''

def contar_palabras(cadena):
    ''' La funcion contar_palabras convierte la cadena en una lista y verifica cuantos de
    sus elementos tienen una longitud mayor que cinco.
    Devuelve la cantidad de ocurrencias.'''

    contador=0

    lista_cadena = cadena.split()

    for palabra in lista_cadena:
        if len(palabra)>5:
            contador += 1

    return(contador)

#main
cadena = input("Ingrese una cadena de palabras separadas por espacios: ")
cantidad = contar_palabras(cadena)
print(f"En la cadena '{cadena}' hay {cantidad} palabras con más de cinco letras.")