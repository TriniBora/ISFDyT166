#Elementos y segmentos de tuplas
t=(25, "Mayo", 1810)

print(t[0])#25
print(t[1])#’Mayo’
print(t[2])#1810

print(t[:2])#(25, ’Mayo’)

#Las tuplas son inmutables
'''t[2] = 2008
Traceback (most recent call last):
File "<stdin>", line 1,in<module>
TypeError: ’tuple’ object doesnotsupport item assignment'''

#Longitud de tuplas
print(len(t))

#tupla vacía: tupla con 0 componentes
tupla_vacia = 0
#print(len(tupla_vacia))#TypeError: object of type 'int' has no len()

#tupla unitaria: tupla con una componente
tupla_unitaria = ("hola",)
print(len(tupla_unitaria))#1

#Empaquetado y desempaquetado de tuplas
a=125
b="&"
c="Ana"
d=a,b,c
print(d)#(125, '&', 'Ana')
print(len(d))#3

x,y,z = d
print(x)#125
print(y)#&
print(z)#"Ana"