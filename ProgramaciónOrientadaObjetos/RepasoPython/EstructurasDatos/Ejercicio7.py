'''Implementar una lista de precios que permita grabar el precio de un producto, consultar
el precio de un producto consultar todos los productos cuto precio sea mayor a un valor
ingresado y mostrar los productos ordenados del más barato al más caro.'''

def agregar(nombre, lista_precios):
    '''La funcion agregar verifica que el nombre del producto esté ya en la lista de precios.
    Si no está en la lista, solita el precio y lo agrega, mostrando por pantalla la modificación realizada.
    Si ya está en la lista de precios informa al usuario mediante un mensaje en pantalla.'''

    if nombre in lista_precios:
        print(f'El producto "{nombre}" ya está en la lista de precios. Su precio es "{lista_precios[nombre]}".')
    else:
        precio = float((input("Ingrese el precio del producto: ")))
        lista_precios[nombre]=precio
        print(f'El producto "{nombre}" se agregó a la lista de precios, y su precio es ${precio:.2f}')
    print()
    menu(lista_precios)

def actualizar(nombre, lista_precios):
    '''La funcion actualizar verifica que el nombre del producto esté ya en la lista de precios. Si ya está en la lista solicita el nuevo precio y lo modifica, mostrando por pantalla la modificación realizada.
    Si no está en la lista de precios informa al usuario mediante un mensaje en pantalla.'''

    if nombre in lista_precios:
        precio = float(input("Ingrese el nuevo precio: "))
        lista_precios[nombre]=precio
        print(f'El producto "{nombre}" modificó su precio a ${precio:.2f}')
    else:
        print(f'El producto "{nombre}" no se encuentra en la lista de precios.')
    print()
    menu(lista_precios)

def consultar(nombre, lista_precios):
    '''La funcion consultar verifica que el nombre del producto esté ya en la lista de precios.
    Si ya está en la lista muestra por pantalla un mensaje con el precio.
    Si no está en la lista de precios informa al usuario mediante un mensaje en pantalla.'''

    if nombre in lista_precios:
        print(f'El precio del producto "{nombre}" es ${lista_precios[nombre]:.2f}.')
    else:
        print(f'El producto "{nombre}" no se encuentra en la lista de precios.')
    print()
    menu(lista_precios)


def menu_agregar(lista_precios):
    ''' La funcion menu_agregar solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Agregar nuevo producto \n2: Salir "))

    if(opcionNro == 1):
        nombre = (input("Ingrese el nombre del producto: ")).upper()
        agregar(nombre, lista_precios)
    elif(opcionNro == 2):
        menu(lista_precios)
    else:
        print("La opción ingresada no es válida.")


def menu_actualizar(lista_precios):
    ''' La funcion menu_agregar solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Actualizar precio de un producto existente \n2: Salir "))

    if(opcionNro == 1):
        nombre = input("Ingrese el nombre del producto del cual quiere actualizar el precio: ").upper()
        actualizar(nombre, lista_precios)
    elif(opcionNro == 2):
        menu(lista_precios)
    else:
        print("La opción ingresada no es válida.")

def menu_consultar(lista_precios):
    ''' La funcion menu_agregar solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada
    no es correcta se imprime un mensaje de error.'''

    opcionNro = int(input(
        "Ingrese la opcion: \n1: Consultar precio de un producto existente \n2: Salir "))

    if(opcionNro == 1):
        nombre = input("Ingrese el nombre del producto del cual quiere consultar el precio: ").upper()
        consultar(nombre, lista_precios)
    elif(opcionNro == 2):
        menu(lista_precios)
    else:
        print("La opción ingresada no es válida.")


def mostrar_productos(lista_precios):
    '''La funcion mostrar_productos lista por pantalla cada uno de los pares producto-precio de la lista de precios, ordenados desde el menor precio hasta el mayor.'''

    lista_prod=[]

    for nombre,precio in lista_precios.items():
        lista_prod.append((precio, nombre))
    lista_prod.sort()
    for producto in lista_prod:
        print(producto)
    print()
    menu(lista_precios)


def mostrar_mayores(lista_precios):
    '''La funcion mostrar_mayores lista por pantalla aquellos pares producto-precio de la lista de precios cuyo precio sea mayor al precio de referencia ingresado por el usuario, ordenados desde el menor precio hasta el mayor.'''

    precio_ref = float(input("Ingrese el precio de referencia: "))

    lista_prod=[]
    hay_mayores = False

    for nombre,precio in lista_precios.items():
        lista_prod.append((precio, nombre))
    lista_prod.sort()
    for producto in lista_prod:
        if producto[0] > precio_ref:
            print(producto)
            hay_mayores = True
    if not hay_mayores:
        print(f'No se econtraron productos cuyo precio sea mayor que ${precio_ref:.2f}')
    print()
    menu(lista_precios)


def menu(lista_precios):
    ''' La funcion menu solicita al usuario que ingrese una de las opciones indicadas.
    Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta se imprime un mensaje de error. Si elige la opción 6, se termina la ejecución dle programa.'''

    opcionNro = int(input(
        "Ingrese la opción: \n1: Agregar precio \n2: Actualizar precio \n3: Consultar precio \n4: Mostrar precios mayores \n5: Mostrar productos \n6: Salir "))

    if(opcionNro == 1):
        menu_agregar(lista_precios)
    elif(opcionNro == 2):
        menu_actualizar(lista_precios)
    elif(opcionNro == 3):
        menu_consultar(lista_precios)
    elif(opcionNro == 4):
        mostrar_mayores(lista_precios)
    elif(opcionNro == 5):
        mostrar_productos(lista_precios)
    elif(opcionNro == 6):
        exit()
    else:
        print("La opción ingresada no es válida.")

    print()


#MAIN
lista_precios = {"GALLETITAS":75.0,"AGUA MINERAL":120.5}
menu(lista_precios)