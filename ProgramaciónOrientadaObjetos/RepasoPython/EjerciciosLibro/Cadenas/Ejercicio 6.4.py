'''Ejercicio 6.4. Escribir una función contar(l, x) que cuente cuántas veces aparece un
carácter l dado en una cadena x.'''

def contar_caracter(caracter, cadena):
    """ La funcion contar_caracter cuenta cuántas
    ocurrencias del caracter dado hay en la cadena indicada."""

    contador = 0;
    for letra in cadena:
        if letra == caracter:
            contador += 1
    return(contador)

cadena = input("Ingrese una cadena de caracteres: ")
caracter = input("Ingrese el caracter que desea contar: ")
print (contar_caracter(caracter, cadena))