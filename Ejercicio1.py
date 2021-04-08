from math import sqrt

class Punto:
    # Crea una clase llamada Punto con sus dos coordenadas X e Y.

    def __init__(self, coord_x=0, coord_y=0):
        #Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        # Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
        punto = (self.coord_x,self.coord_y)
        #return f'El punto ingresado es: ({self.coord_x},{self.coord_y})'
        return punto

    def cuadrante(self):
        # Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0
        #se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
        if (self.coord_x > 0):
            if (self.coord_y > 0):
                print(f'El punto ({self.coord_x},{self.coord_y}) pertenece al primer cuadrante')
            elif (self.coord_y < 0):
                print(f'El punto ({self.coord_x},{self.coord_y}) pertenece al cuarto cuadrante')
            else:
                (f'El punto ({self.coord_x},{self.coord_y}) pertenece al eje de las ordenadas')
        else:
            if(self.coord_x < 0):
                if (self.coord_y > 0):
                    print(f'El punto ({self.coord_x},{self.coord_y}) pertenece al segundo cuadrante')
                elif (self.coord_y < 0):
                    print(f'El punto ({self.coord_x},{self.coord_y}) pertenece al tercer cuadrante')
                else:
                    (f'El punto ({self.coord_x},{self.coord_y}) pertenece al eje de las ordenadas')
            else:
                if (self.coord_y > 0) or (self.coord_y < 0):
                    print(f'El punto ({self.coord_x},{self.coord_y}) pertenece al eje de las abscisas')
                else:
                    print('El punto (0,0) pertenece al origen de coordenadas')

    def vector(self, punto2):
        # Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
        resultante_x = punto2.coord_x - self.coord_x
        resultante_y = punto2.coord_y - self.coord_y
        return f'El vector resultante es ({resultante_x},{resultante_y})'

    def distancia(self, punto2):
        # Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre
        # por pantalla.
        distancia = sqrt((punto2.coord_x - self.coord_x)**2 + (punto2.coord_y - self.coord_y)**2)
        #return f'La distancia entre los puntos es {distancia:1.2f}'
        return distancia


class Rectangulo(Punto):
    # Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.

    def __init__(self, punto1=Punto(), punto2=Punto()):
        # Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por
        # defecto.
        self.inicial = punto1
        self.final = punto2

    def base(self):
        # Añade al rectángulo un método llamado base que muestre la base.
        self.base = abs(self.final.coord_x - self.inicial.coord_x)
        return f'La base del rectángulo mide {self.base:10.2f} unidades.'

    def altura(self):
        # Añade al rectángulo un método llamado altura que muestre la altura.
        self.altura = abs(self.final.coord_y - self.inicial.coord_y)
        return f'La altura del rectángulo mide {self.altura:10.2f} unidades.'

    def area(self):
        # Añade al rectángulo un método llamado area que muestre el area.
        self.area = self.base*self.altura
        return f'El rectángulo tiene una área de {self.area:10.2f} unidades cuadradas.'


# main1 Ingreso por teclado
#tengo problemas con los tipos, covierto el input a float pero luego no me toma los valores por defecto
'''
coord_x = float(input('Ingrese la coordenada x del primer punto: '))
coord_y = float(input('Ingrese la coordenada y del primer punto: '))
punto1 = Punto(coord_x, coord_y)
print(f'El punto ingresado es: {punto1.__str__()}')
punto1.cuadrante()
coord_x = float(input('Ingrese la coordenada x del segundo punto: '))
coord_y = float(input('Ingrese la coordenada y del segundo punto: '))
punto2 = Punto(coord_x, coord_y)
print(f'El punto ingresado es: {punto2.__str__()}')
punto2.cuadrante()
print(punto1.vector(punto2))
print(f'La distancia entre los puntos es {punto1.distancia(punto2):10.2f} unidades')

rectangulo = Rectangulo(punto1, punto2)
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())'''


# main2 Ingreso para test
'''
# Test 1: No se ingresan coordenadas
print('Test 1: sin ingreso de coordenadas')
punto1 = Punto()
print(f'El punto ingresado es: {punto1.__str__()}')
punto1.cuadrante()
punto2 = Punto()
print(f'El punto ingresado es: {punto2.__str__()}')
punto2.cuadrante()
print(punto1.vector(punto2))
print(f'La distancia entre los puntos es {punto1.distancia(punto2):10.2f} unidades')
rectangulo = Rectangulo(punto1, punto2)
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())

print()

# Test 2: Se ingresan coordenadas para un punto
# No se ingresan coordenadas
print('Test 2: ingreso de coordenadas para un punto')
punto1 = Punto(4.5,10)
print(f'El punto ingresado es: {punto1.__str__()}')
punto1.cuadrante()
punto2 = Punto()
print(f'El punto ingresado es: {punto2.__str__()}')
punto2.cuadrante()
print(punto1.vector(punto2))
print(f'La distancia entre los puntos es {punto1.distancia(punto2):10.2f} unidades')
rectangulo = Rectangulo(punto1, punto2)
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())

print()

# Test 3: Se ingresan coordenadas para ambos puntos
# No se ingresan coordenadas
print('Test 3: ingreso de coordenadas para ambos puntos')
punto1 = Punto(-2.3,4)
print(f'El punto ingresado es: {punto1.__str__()}')
punto1.cuadrante()
punto2 = Punto(9.2,-6)
print(f'El punto ingresado es: {punto2.__str__()}')
punto2.cuadrante()
print(punto1.vector(punto2))
print(f'La distancia entre los puntos es {punto1.distancia(punto2):10.2f} unidades')
rectangulo = Rectangulo(punto1, punto2)
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())'''

print()

#PARA ENTREGAR

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto()
print(f'Los puntos ingresados son: A = {A.__str__()}, B = {B.__str__()}, C = {C.__str__()}, D = {D.__str__()}')
A.cuadrante()
C.cuadrante()
D.cuadrante()
print(A.vector(B))
print(B.vector(A))
print(f'La distancia entre los puntos A y B es {A.distancia(B):10.2f} unidades')
print(f'La distancia entre los puntos B y A es {B.distancia(A):10.2f} unidades')
rectangulo = Rectangulo(A, B)
print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())