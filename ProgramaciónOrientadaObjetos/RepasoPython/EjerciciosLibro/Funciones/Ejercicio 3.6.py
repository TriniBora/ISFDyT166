'''Ejercicio 3.6. Corregir el programa tarifador.py para que:
Imprima el costo en pesos y centavos, en lugar de un número decimal.
Informe además cuál fue el total facturado en la corrida.'''

def asegundos (horas, minutos, segundos):
        segsal = 3600 * horas + 60 * minutos + segundos
        return segsal

def main():

    """ El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo. """

    f = float(input("¿Cuánto cuesta 1 segundo de comunicacion?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))

    for x in range(n):

        horas = float(input("Ingrese la cantidad de horas: "))
        minutos = float(input("Ingrese la cantidad de minutos: "))
        segundos = float(input("Ingrese la cantidad de segundos: "))

        segcalc = asegundos(horas, minutos, segundos)

        costo = segcalc * f
        pesos = int(costo)
        centavos = costo - pesos

        print ("Duracion: ", segcalc, "segundos. Costo: $",pesos, "pesos con ", format(centavos, '0.2f'), " centavos.")

    print (f"El costo total de las {n} comunicaciones fue de $ {pesos} pesos con {centavos:0.2f} centavos.")

main()