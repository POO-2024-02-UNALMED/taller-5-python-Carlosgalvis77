from .animal import Animal

class Pez(Animal):
    _listado = []
    bacalaos = 0
    salmones = 0
    
    def __init__(self, nombre='', edad=0, habitat='', genero='', colorEscamas = '', cantidadAletas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def cantidadPeces(self):
        return len(Pez._listado)
    @classmethod
    def crearSalmon(cls, nombre='', edad=0, genero=''):
        Pez.salmones += 1
        return Pez(nombre, edad, habitat='océano', genero=genero,  colorEscamas='Rojo', cantidadAletas=6)
    @classmethod
    def crearBacalao(cls, nombre='', edad=0, genero=''):
        Pez.bacalaos += 1
        return Pez(nombre, edad, habitat='océano', genero=genero,  colorEscamas='gris', cantidadAletas=6)
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, largo):
        self._cantidadAletas = largo
    def getCantidadAletas(self):
        return self._cantidadAletas