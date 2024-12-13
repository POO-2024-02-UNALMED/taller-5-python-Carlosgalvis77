from .animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre='', edad=0, habitat='', genero='', colorEscamas = '', largoCola = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def cantidadReptiles(self):
        return len(Reptil._listado)
    
    @classmethod
    def crearIguana(self, nombre='', edad=0, genero=''):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, habitat='humedal', genero=genero, colorEscamas='verde', largoCola=3)
    
    @classmethod
    def crearSerpiente(self, nombre='', edad=0, genero=''):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, habitat='jungla', genero=genero, colorEscamas='blanco', largoCola=1)
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largo):
        self._largoCola = largo
    def getLargoCola(self):
        return self._largoCola