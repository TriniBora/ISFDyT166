'''Escribir otra función repite_hola que reciba como parámetro un número entero n y
retorne la cadena formada por n concatenaciones de "Hola". Invocarla con distintos
valores de n.'''

def repite_hola(n):
    print("Hola "*n)

#MAIN
repite_hola(int(input("Ingrese un número entero mayor que 0: ")))