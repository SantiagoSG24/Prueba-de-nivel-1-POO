from subclases.coche import Coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ", Carga: {} kg".format(self.carga)
    
    def catalogar(self, vehiculos):
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__,vehiculo)