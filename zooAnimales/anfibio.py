from .animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPiel = None, venenoso = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel= colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def crearRana(cls, nombre='', edad=None, genero='' ):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, habitat = 'selva', genero = genero, colorPiel= 'rojo', venenoso=True )
    
    @classmethod
    def crearSalamandra (cls, nombre='', edad=None, genero='' ):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, habitat = 'selva', genero = genero, colorPiel= 'negro y amarillo', venenoso= False )

    def setColorPiel(self, color):
        self._colorPiel = color
    def getColorPiel(self):
        return self._colorPiel
    
    def cantidadAnfibios(self):
        return len(Anfibio._listado)

    def setVenenoso (self, veneno:bool):
        self._venenoso = veneno

    def getVenenoso (self):
        return self._venenoso