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

        print ("Duracion: ", segcalc, "segundos. Costo: ",costo, "$.")

main()