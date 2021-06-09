'''Escribir una función contar(x,y) que cuente cuántas veces aparece un carácter x dado en
una cadena y.'''

def contar(caracter, cadena):
    ''' La funcion contar cuenta cuántas
    ocurrencias del caracter dado hay en la cadena indicada.'''

    contador = 0;
    for letra in cadena:
        if letra == caracter:
            contador += 1
    return(contador)


#MAIN
cadena = input("Ingrese una cadena de caracteres: ")
caracter = input("Ingrese el caracter del que desea conocer la cantidad de ocurrencias: ")
cantidad = (contar(caracter, cadena))
print(f"El caracter {caracter} aparece en la cadena {cadena} {cantidad} veces.")