'''Escribir una función repite_saludo que reciba como parámetro un número
entero n y una cadena saludo y escriba por pantalla el valor de saludo n veces. Invocarla
con distintos valores de n y de saludo.'''

def repite_saludo(n, saludo):

    for i in range(0, n):
        print(saludo, i+1 )
        i+=1

#MAIN
repite_saludo(int(input("Ingrese un número entero mayor que 0: ")), input("Ingrese el saludo: "))