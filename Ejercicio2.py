class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f", {self.carga} kg"

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", {self.tipo}"

class Motocicleta(Coche, Bicicleta):

    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        Bicicleta.__init__(self, color, ruedas, tipo)

    def __str__(self):
        Coche.__str__(self)
        Bicicleta.__str__(self)

#main
mi_coche = Coche("azul", 4, 150, 1200)
print(mi_coche)

mi_bicicleta = Bicicleta("blanco", 2, "Urbana")
print(mi_bicicleta)

mi_camioneta = Camioneta("rojo", 4, 180, 2000, 1000)
print(mi_camioneta)

mi_motocicleta = Motocicleta("negro", 2, 150, 650, "Deportiva")
print(mi_bicicleta)

#vehiculos = [mi_coche, mi_bicicleta, mi_camioneta, mi_motocicleta]
