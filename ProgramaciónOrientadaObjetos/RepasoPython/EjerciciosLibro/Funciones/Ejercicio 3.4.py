'''Escribir otra función repite_saludo que reciba como parámetro un número
entero n y una cadena saludo retorne el valor de n concatenaciones de saludo. Invocarla con
distintos valores de n y desaludo.'''

def repite_saludo(n, saludo):
    print((saludo + " ")*n)

#MAIN
repite_saludo(int(input("Ingrese un número entero mayor que 0: ")), input("Ingrese el saludo: "))