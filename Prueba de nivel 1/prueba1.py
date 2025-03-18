class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color: {}, Ruedas: {}".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", Tipo: {}".format(self.tipo)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ", Carga: {} kg".format(self.carga)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in filtrados:
            print(type(vehiculo).__name__, ":", vehiculo)
    else:
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__, ":", vehiculo)

# Creación de objetos y lista de vehículos
vehiculos = [
    Coche("Rojo", 4, 180, 2000),
    Bicicleta("Azul", 2, "Urbana"),
    Camioneta("Blanco", 4, 160, 2500, 1000),
    Motocicleta("Negro", 2, "Deportiva", 220, 1000)
]

# Pruebas de catalogar
print("\nTodos los vehículos:")
catalogar(vehiculos)
print("\nVehículos con 2 ruedas:")
catalogar(vehiculos, 2)
print("\nVehículos con 4 ruedas:")
catalogar(vehiculos, 4)
