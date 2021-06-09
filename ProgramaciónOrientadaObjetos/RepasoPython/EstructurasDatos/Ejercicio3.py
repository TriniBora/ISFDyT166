'''Escribir un programa que cuente cuantas veces aparecen cada una de las vocales en una
cadena. No importa si la vocal aparece en mayúscula o en minúscula.'''

def contar_vocales(cadena):
    ''' La funcion contar_vocales cuenta cuántas
    ocurrencias de cada vocal hay en la cadena indicada y devuelve
    la cantidad de ocurrencias.'''

    cadena = cadena.lower()

    vocales=["a","e","i","o","u","á","é","í","ó","ú"]
    contador = {}

    for letra in cadena:
        if letra in vocales:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    for letra in contador:
        frecuencia = contador[letra]

    return(contador)


#main
cadena = input("Ingrese una cadena de caracteres: ")
cantidad = contar_vocales(cadena)

print(f"Cantidad de ocurrencias de cada vocal en {cadena}: ")
for clave,valor in cantidad.items(): print(clave, valor)
