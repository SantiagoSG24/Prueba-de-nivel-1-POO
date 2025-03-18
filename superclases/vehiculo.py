class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color: {}, Ruedas: {}".format(self.color, self.ruedas)
    
def catalogar(self, vehiculos):
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__,vehiculo)