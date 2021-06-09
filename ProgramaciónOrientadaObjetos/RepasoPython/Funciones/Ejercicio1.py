'''Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un
cilindro usando la primera función.'''

import math

def calcular_area(radio):
    '''La función calcular_area recibe un valor numérico y devuelve el área del circulo cuyo radio es dicho valor numérico.'''
    return math.pi * math.pow(radio, 2)


def calcular_volumen(radio, altura):
    '''La función calcular_volumen recibe dos valores numéricos, que representan radio y altura de un cilindro respectivamente. Llama a la función calcular_area y luego calcula el volumen del cilindro.'Retorna el volumen del cilindro.'''
    area = calcular_area(radio)
    return area * altura


#MAIN

radio = float(input("Ingrese un valor numérico que indique el radio del círculo: "))
altura = float(input("Ingrese un valor numérico que indique la altura del cilindro: "))

area = calcular_area(radio)
print(f'El área del círculo de radio {radio} es {area:.2f} unidades cuadradadas.')

volumen = calcular_volumen(radio, altura)
print(f'El volumen del cilindro de radio {radio} y altura {altura} es {volumen:.2f} unidades cúbicas.')