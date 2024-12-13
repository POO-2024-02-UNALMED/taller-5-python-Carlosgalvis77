from animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre='', edad=0, habitat='', genero='', zona=None, colorEscamas = '', largoCola = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def cantidadReptiles(self):
        return len(Reptil._listado)
    
    @classmethod
    def crearIguana(self, nombre='', edad=0, genero='', zona=None):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, habitat='humedal', genero=genero, zona=zona, colorEscamas='verde', largoCola=3)
    
    @classmethod
    def crearSerpientes(self, nombre='', edad=0, genero='', zona=None):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, habitat='jungla', genero=genero, zona=zona, colorEscamas='blanco', largoCola=1)
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largo):
        self._largoCola = largo
    def getLargoCola(self):
        return self._largoCola