'''Escribir un programa que lea un archivo de texto y escriba en otro archivo, una lista con las 10 palabras con mayor ocurrencia ordenadas por cantidad de ocurrencias, tener en cuenta una lista de palabras ignoradas en el análisis de ocurrencias.'''

def archivo_txt_a_lista(archivo):
    ''' Dado un archivo txt, lo abre, retorna una lista cuyos elementos contienen listas de palabras de cada una de las filas del archivo y cierra el archivo.'''

    lista_lineas = []

    with open(archivo, "r") as archivo:
        contenido = archivo.readlines() #separo el contenido del archivo en lineas
        for linea in contenido: #itero a través de las líneas
            lista_lineas.append(linea.split()) #separo la línea en palabra y la agrego a la lista de lineas

    return lista_lineas

    archivo.close()


def contar_palabras(lista_contenido):

    '''La función contar_palabras recibe la lista de palabras obtenida a partir del archivo de texto origen y
    crea un diccionario cuyos pares clave - valor son las palabras que están en dicha lista (pero que no están)
    en la lista de "palabras ignoradas" y sus respectivas ocurrencias.
    Retorna este diccionario.'''

    dict_contenido={}
    palabras_ignoradas = ["a","ante","bajo","cabe","con","contra","de","desde","en","entre","hacia","hasta","para","por","según","sin","so","sobre","tras","durante","mediante","vía","versus","el","la","lo","las","los","un","una","unos","unas","yo","tú","él","usted","ustedes","nosotros","nosotras","vosotros","vosotras","ellos","ellas","me","te","nos","se","mi","mis","mío","mía","míos","mías","tu","tus","tuyo","tuya","tuyos","tuyas","su","sus","suyo","suya","suyos","suyas","nuestro","nuestra","nuestros","nuestras","vuestro","vuestra","vuestros","vuestras","este","ese","aquél","esta","esa","aquella","estos","esos","aquellos","estas","esas","aquellas","esto","eso","aquello","que","quien","quienes","cuyo","cuyos","cuyas","cuya","donde","qué","quién","quiénes","cuál","cuáles","cuánto","cuántos","cuánta","cuántas","dónde","cómo","mucho","muchos","mucha","muchas","poco","pocos","poca","pocas","tanto","tantos","tanta","tantas","bastante","bastantes","demasiado","demasiados","demasiada","demasiadas","alguno","algunos","alguna","algunas","ninguno","ninguna","algo","nada","y","ni","pero","aunque","o","que","aunque","pero","e","pues","puesto","por","porque","sea","dado","embargo","pesar","cambio","sino","no","es","al","de","del"]#ignoro proposiciones, artículos, pronombres y conjunciones

    for linea in lista_contenido:
        for palabra in linea:
            palabra = palabra.lower()#convierte a minúscula todas las palabras para evitar duplicados
            if palabra in dict_contenido and palabra not in palabras_ignoradas:
                dict_contenido[palabra] += 1
            else:
                dict_contenido[palabra] = 1

    return dict_contenido


def ranking_mayor_ocurrencia (lista_contenido):
    '''Esta función recibe un diccionario con la totalidad de palabras y sus ocurrencias obtenida a
    partir del archivo de texto origen y retorna un diccionario ordenado en forma decreciente de acuerdo
    a las ocurrencias de cada palabra.'''

    dict_contenido={}

    dict_contenido = contar_palabras(lista_contenido)
    ranking = sorted(dict_contenido.items(), key=lambda x: x[1], reverse=True)

    return ranking


def mostrar_ranking(lista_contenido):
    '''La función mostrar_ranking escribe en un archivo de texto un ranking de las 10
    palabras con mayor ocurrencia en la lista de palabras obtenida a partir del archivo de texto origen.'''

    archivo = open("mayor_ocurrencia.txt", "a")
    #si el archivo de texto existe, se posiciona al final, de modo que no sobreescribe los datos existentes

    ranking = ranking_mayor_ocurrencia (lista_contenido)

    archivo.write('Las 10 palabras con mayor ocurrencia son:\n ')

    for item in range(10):
        archivo.write(f'{item+1}: {ranking[item][0]}: {ranking[item][1]}\n')

    archivo.close()


#MAIN

lista_texto = archivo_txt_a_lista("./Delicatessen.txt")

mostrar_ranking(lista_texto)