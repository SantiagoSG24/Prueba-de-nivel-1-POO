from superclases.vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)
    
    def catalogar(self, vehiculos):
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__,vehiculo)