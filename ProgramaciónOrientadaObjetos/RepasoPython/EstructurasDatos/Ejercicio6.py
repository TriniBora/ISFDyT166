'''Implementar un diccionario Inglés – Español, permitiendo agregar una palabra en inglés
y su traducción al español, consultar la traducción de una palabra en ambos sentidos
(inglés a español y español a inglés) contar la cantidad de palabras y mostrar el
diccionario ordenado de la Z a la A.'''

def agregar(palabra, diccionario1, diccionario2):
    '''La función agregar inserta en el diccionario pasado como segundo parámetro, como clave
    la palabra ingresada por el ususario, cuyo valor es la traducción ingresada por el ususario.
    Luego inserta la traducción como clave del otro diccionario, cuyo valor será la palabra original.
    Si la palabra ya estuviera en el primer diccionario, sale un mensaje por pantalla que muestra
    palabra y traducción.'''

    if palabra in diccionario1:
        print(f'La palabra "{palabra}" ya está en el diccionario. Su traducción es "{diccionario1[palabra]}".')
    else:
        traduccion = (input("Ingrese la traducción en español: ")).upper()
        diccionario1[palabra]=traduccion
        diccionario2[traduccion]=palabra
        print(f'La palabra "{palabra}" se agregó al diccionario, y su traducción es "{traduccion}"')
    print()
    menu(diccionario1, diccionario2)

def traducir(palabra, diccionario1, diccionario2):
    '''La función traducir busca, dentro de las claves del primer diccionario, si está la palabra ingresada por el ususario. Si está, muestra el valor asociado a esa clave, que es la traducción de la palabra.
    Si no está, sale un mensaje por pantalla lo indica.'''

    if palabra in diccionario1:
        print(f'La traducción de "{palabra}" es "{diccionario1[palabra]}".')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el diccionario.')
    print()
    menu(diccionario1, diccionario2)

def modificar_palabra(palabra, diccionario1, diccionario2):
    '''La función modificar_palabra busca, dentro de las claves del primer diccionario, si está la palabra ingresada por el ususario. Si está, guarda la traduccion, solicita la nueva palabra, inserta la nueva palabra  y su traduccion original y elemina la palabra anterior del primer diccionario. Luego actualiza
    clave y valor en el segundo diccionario.
    Si la palabra ingresada por el usuario no está, sale un mensaje por pantalla lo indica.'''

    if palabra in diccionario1:
        traduccion = diccionario1.get(palabra)
        nueva_palabra = (input("Ingrese la nueva palabra: ")).upper()
        diccionario2[traduccion]=nueva_palabra
        del diccionario1[palabra]
        diccionario1[nueva_palabra]=traduccion
        print(f'La palabra "{palabra}" se modificó por "{nueva_palabra}"')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el diccionario.')
    print()
    menu(diccionario1, diccionario2)

def modificar_traduccion(palabra, diccionario1, diccionario2):
    '''La función modificar_traduccion busca, dentro de las claves del primer diccionario, si está la palabra ingresada por el ususario. Si está, modifica el valor correspondiente a la clave, que es la nueva traducción. Luego actualiza clave y valor en el segundo diccionario.
    Si la palabra ingresada por el usuario no está, sale un mensaje por pantalla lo indica.'''

    if palabra in diccionario1:
        traduccion = (input("Ingrese la nueva traducción en español: ")).upper()
        diccionario1[palabra]=traduccion
        diccionario2[traduccion]=palabra
        print(f'La palabra "{palabra}" modificó su traducción a "{traduccion}"')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el diccionario.')
    print()
    menu(diccionario1, diccionario2)

def eliminar(palabra, diccionario1, diccionario2):
    '''La función eliminar busca, dentro de las claves del primer diccionario, si está la palabra ingresada por el ususario. Si está, guarda la traducción y elimina clave y valor del primer diccionario. Luego actualiza elimina clave y valor en el segundo diccionario, valiendose de la traducción guardada.
    Si la palabra ingresada por el usuario no está, sale un mensaje por pantalla lo indica.'''

    if palabra in diccionario1:
        traduccion = diccionario1[palabra]
        del diccionario1[palabra]
        del diccionario2[traduccion]
        print(f'La palabra "{palabra}" se eliminó del diccionario.')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el diccionario.')
    print()
    menu(diccionario1, diccionario2)

def mostrar(diccionario1, diccionario2):
    '''La función mostrar almacena en una lista todos los pares clave valor del primer diccionario. Luego los ordena de forma descendente y muestra por pantalla cada par.'''
    lista_dic=[]

    for palabra,traduccion in diccionario1.items():
        lista_dic.append((palabra, traduccion))
    lista_dic.sort(reverse=True)
    for elemento in lista_dic:
        print(elemento)
    print()
    menu(diccionario1, diccionario2)

def contar(diccionario1, diccionario2):
    '''La función contar muestra por pantalla la cantidad de elementos del primer diccionario.'''

    cantidad = len(diccionario1)
    print(f"El diccionario tiene ingresadas {cantidad} palabras.")
    print()
    menu(diccionario1, diccionario2)


def menu_agregar(diccionario1, diccionario2):
    ''' La funcion menu_agregar solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Agregar palabra en inglés \n2: Salir "))

    if(opcionNro == 1):
        palabra = input("Ingrese la palabra en inglés que quiere agregar al diccionario: ").upper()
        agregar(palabra, diccionario1, diccionario2)
    elif(opcionNro == 2):
        menu(diccionario1, diccionario2)
    else:
        print("La opción ingresada no es válida.")

def menu_traducir(diccionario1, diccionario2):
    ''' La funcion menu_traducir solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Traducir palabra a ingles \n2: Traducir palabra a español \n3: Salir "))

    if(opcionNro == 1):
        palabra = input("Ingrese la palabra en español que quiere traducir a inglés: ").upper()
        traducir(palabra, diccionario2, diccionario1)
    elif(opcionNro == 2):
        word = input("Ingrese la palabra en inglés que quiere traducir a español: ").upper()
        traducir(word, diccionario1, diccionario2)
    elif(opcionNro == 3):
        menu(diccionario1, diccionario2)
    else:
        print("La opción ingresada no es válida.")

def menu_modificar_palabra(diccionario1, diccionario2):
    ''' La funcion menu_modificar_palabra solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Modificar una palabra en inglés \n2: Modificar una palabra en español \n3: Salir "))

    if(opcionNro == 1):
        word = input("Ingrese la palabra en inglés que quiere modificar: ").upper()
        modificar_palabra(word, diccionario1, diccionario2)
    elif(opcionNro == 2):
        palabra = input("Ingrese la palabra en español que quiere modificar: ").upper()
        modificar_palabra(palabra, diccionario2, diccionario1)
    elif(opcionNro == 3):
        menu(diccionario1, diccionario2)
    else:
        print("La opción ingresada no es válida.")

def menu_modificar_traduccion(diccionario1, diccionario2):
    ''' La funcion menu_modificar_traduccion solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Modificar traducción de una palabra en inglés \n2: Modificar traducción de una palabra en español \n3: Salir "))

    if(opcionNro == 1):
        word = input("Ingrese la palabra en inglés de la cual quiere modificar su traducción: ").upper()
        modificar_traduccion(word, diccionario1, diccionario2)
    elif(opcionNro == 2):
        palabra = input("Ingrese la palabra en español de la cual quiere modificar su traducción: ").upper()
        modificar_traduccion(palabra, diccionario2, diccionario1)
    elif(opcionNro == 3):
        menu(diccionario1, diccionario2)
    else:
        print("La opción ingresada no es válida.")

def menu_eliminar(diccionario1, diccionario2):
    ''' La funcion menu_eliminar solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Eliminar palabra en español \n2: Eliminar palabra en inglés \n3: Salir "))

    if(opcionNro == 1):
        palabra = input("Ingrese la palabra en español que quiere eliminar: ").upper()
        eliminar(palabra, diccionario2, diccionario1)
    elif(opcionNro == 2):
        word = input("Ingrese la palabra en inglés que quiere eliminar: ").upper()
        eliminar(word, diccionario1, diccionario2)
    elif(opcionNro == 3):
        menu(diccionario1, diccionario2)
    else:
        print("La opción ingresada no es válida.")

def menu(diccionario1, diccionario2):
    ''' La funcion menu solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta se imprime un mensaje de error. Si elige la opción 8, se termina la ejecución dle programa.'''

    opcionNro = int(input(
        "Ingrese la opción: \n1: Agregar palabra \n2: Traducir palabra \n3: Modificar palabra \n4: Modificar traducción \n5: Eliminar palabra \n6: Mostrar diccionario \n7: Mostrar cantidad de palabras ingresadas \n8: Salir "))

    if(opcionNro == 1):
        menu_agregar(diccionario1, diccionario2)
    elif(opcionNro == 2):
        menu_traducir(diccionario1, diccionario2)
    elif(opcionNro == 3):
        menu_modificar_palabra(diccionario1, diccionario2)
    elif(opcionNro == 4):
        menu_modificar_traduccion(diccionario1, diccionario2)
    elif(opcionNro == 5):
        menu_eliminar(diccionario1, diccionario2)
    elif(opcionNro == 6):
        mostrar(diccionario1, diccionario2)
    elif(opcionNro == 7):
        contar(diccionario1, diccionario2)
    elif(opcionNro == 8):
        exit()
    else:
        print("La opción ingresada no es válida.")

    print()


# MAIN
dic_ing_esp = {"SUN":"SOL","APPLE":"MANZANA"}
dic_esp_ing = {"SOL":"SUN","MANZANA":"APPLE"}
menu(dic_ing_esp, dic_esp_ing)
