def contarA(x):
    """ La funcion contarA(x) cuenta cuántas
    letras "A" aparecen en la cadena x ."""

    contador = 0;
    for letra in x:
        if letra == "A":
            contador = contador + 1
    return(contador)

cadena = input("Ingrese una cadena de caracteres: ")
print (contarA(cadena))