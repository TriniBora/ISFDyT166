'''Ejercicio 6.5. ¿Hay más letras “A” o más letras “E” en una cadena? Escribir un programa
que lo decida.'''

def mayor_cantidad_ocurrencias(cadena):
    """ La funcion mayor_cantidad_ocurrencias cuenta cuántas
    ocurrencias de "A" y "E" hay en la cadena indicada y devuelve
    la letra que tiene mayor cantidad de ocurrencias."""

    contadorA = 0;
    contadorE = 0;

    for letra in cadena:
        if letra == "A":
            contadorA += 1
        if letra == "E":
            contadorE += 1

    if contadorA > contadorE:
        return(f"La letra 'A' tiene {contadorA} ocurrencias, más ocurrencias que la letra 'E'" )
    elif contadorA == contadorE:
        return(f"La letra 'A' y la letra 'E' tienen {contadorA} ocurrencias, la misma cantidad." )
    else:
        return(f"La letra 'E' tiene {contadorE} ocurrencias, más ocurrencias que la letra 'A'" )


cadena = input("Ingrese una cadena de caracteres: ")

print (mayor_cantidad_ocurrencias(cadena))