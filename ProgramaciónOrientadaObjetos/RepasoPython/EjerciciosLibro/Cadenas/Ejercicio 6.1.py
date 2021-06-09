'''Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres de una cadena del ﬁnal al
principio.'''

cadena = input("Ingrese una cadena de caracteres: ")

i = -1;

while i >= -len(cadena):
    print(cadena[i])
    i -= 1
