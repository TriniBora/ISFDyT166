def aHsMinSeg(x):
    """ Dada una duración en segundos sin fracciones
    (la función debe invocarse con números enteros)
    se la convierte a horas, minutos y segundos """

    horas = x / 3600
    minutos = (x % 3600) / 60
    segundos = (x % 3600 ) % 60

    return(horas, minutos, segundos)


#main
(h, m, s) = aHsMinSeg(3660)
print("Son",int(h),"horas",int(m),"minutos",int(s),"segundos")
