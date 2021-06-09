'''DOCUMENTACIÓN DE UNA FUNCIÓN
def hola(alguien):
    #Documentación de la función
    """ Imprime por pantalla un saludo, dirigido a la persona que
    se indica por parámetro. """
    print ("Hola ",alguien,"!")
    print ("Estoy programando en Python.")


hola("Trinidad")

#Lectura de la documenttación
help(hola)'''

#PRINT VS RETURN

#IMPRIME
def print_asegundos (horas, minutos, segundos):

    """ Transforma en segundos una medida de tiempo
    expresada en 3 horas, minutos y segundos """

    segsal = 3600 * horas + 60 * minutos + segundos# regla de transformación
    print ("Son", segsal, "segundos")

print_asegundos (1, 10, 10)

#RETORNA
def calc_asegundos (horas, minutos, segundos):

    """ Transforma en segundos una medida de tiempo
    expresada en 3 horas, minutos y segundos """

    segsal = 3600 * horas + 60 * minutos + segundos# regla de transformación
    return segsal

print (calc_asegundos (1, 10, 10))

print ("Son", calc_asegundos (1, 10, 10), "segundos")

y = calc_asegundos(1, 10, 10)
z = calc_asegundos(2, 20, 20)
print (y+z)
