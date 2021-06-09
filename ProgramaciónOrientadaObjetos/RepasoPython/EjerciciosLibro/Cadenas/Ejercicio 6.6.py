'''Ejercicio 6.6.Escribir un programa que cuente cúantas veces aparecen cada una de las
vocales en una cadena. No importa si la vocal aparece en mayúscula o en minúscula.'''

def contar_vocales(cadena):
    """ La funcion contar_vocales cuenta cuántas
    ocurrencias de cada vocal hay en la cadena indicada y devuelve
    la cantidad de ocurrencias."""

    cadena = cadena.lower()

    vocales=["a","e","i","o","u"]
    contador = {}

    for letra in cadena:
        if letra in vocales:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    for letra in contador:
        frecuencia = contador[letra]

    print(contador)

#main
cadena = input("Ingrese una cadena de caracteres: ")
contar_vocales(cadena)
