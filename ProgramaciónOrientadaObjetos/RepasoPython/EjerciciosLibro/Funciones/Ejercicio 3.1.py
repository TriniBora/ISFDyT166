'''Escribir una función repite_hola que reciba como parámetro un número entero n y
escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de
n.'''

def repite_hola(n):

    for i in range(0, n):
        print("Hola", i+1 )
        i+=1

#MAIN
repite_hola(int(input("Ingrese un número entero mayor que 0: ")))