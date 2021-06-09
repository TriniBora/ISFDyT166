#OPERACIONES CON CADENAS
#SUMAR CADENAS
print("Un divertido "+"programa "+"de "+ "radio")

#MULTIPLICAR CADENAS
print(3*"programas ")
print("programas "*2)

#LONGITUD DE UNA CADENA
print(len("programas "))

s=""#cadena vacía
print(len(s))

#RECORRER CADENAS
for caracter in"programas ":
    print (caracter)

#ACCEDER A UNA POSICION EN LA CADENA
a="Veronica"
print(a[1])#segundo elemento: "e"
print(a[len(a)-1])#último elemento:"a"
print(a[-1])#último elemento:"a"
print(a[-2])#anteúltimo elemento: "c"
print(a[-len(a)])#primer lemento: "V"

'''Las distintas posiciones de una cadenaase llaman índices. Los índices son números enteros que
pueden tomar valores entre -len(a) y len(a)-1.
Los índices entre 0 y len(a)-1 son lo que ya vimos: los caracteres de la cadena del primero
al útimo. Los índices negativos proveen una notación que hace más fácil indicar cuál es el último
carácter de la cadena: a[-1] es el último carácter de a, a[-2]es el penúltimo carácter de a,
a[-len(a)] es el primer carácter de a.'''

#SEGMENTOS DE CADENAS
print(a[0:2]) #caracteres cuyos índices están en el rango[0,2): "Ve"
print(a[-4:-2]) #caracteres cuyos índices están en el rango[-4,-2): "ni"
print(a[0:8]) #caracteres cuyos índices están en el rango[0,8): "Veronica"

'''Si j es un entero no negativo, se puede usar la notación a[:j] para representar al
segmento a[0:j]; también se puede usar la notación a[j:]para representar al segmento
a[j:len(a)].'''

print(a[:3])#"Ver"
print(a[3:])#"onica"

#PROCESAMIENTO DE cadenas
