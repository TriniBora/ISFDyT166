def print_asegundos (horas, minutos, segundos):

    """ Transforma en segundos una medida de tiempo
    expresada en 3 horas, minutos y segundos """

    segsal = 3600 * horas + 60 * minutos + segundos# regla de transformación
    return segsal

def main():

    """ Lee tres tiempos expresados en horas, minutos y segundos, e imprime
    el valor retornado por calc_asegundos, mostrando en pantalla la conversión a segundos """

    for x in range(3):
        horas = float(input("Ingrese la cantidad de horas: "))
        minutos = float(input("Ingrese la cantidad de minutos: "))
        segundos = float(input("Ingrese la cantidad de segundos: "))

        print(print_asegundos(horas, minutos, segundos), "segundos")

main()