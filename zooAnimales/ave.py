from .animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre='', edad=0, habitat='', genero='', colorPlumas = ''):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas= colorPlumas
        Ave._listado.append(self)

    @classmethod
    def crearHalcon(cls, nombre='', edad=None, genero='' ):
        Ave.halcones += 1
        return Ave(nombre, edad, habitat = 'montañas', genero = genero, colorPlumas= 'café glorioso' )
    
    @classmethod
    def crearAguila (cls, nombre='', edad=None, genero='' ):
        Ave.aguilas += 1
        return Ave(nombre, edad, habitat = 'montañas', genero = genero, colorPlumas= 'blanco y amarillo' )

    def setColorPlumas(self, color):
        self._colorPlumas = color
    def getColorPlumas(self):
        return self._colorPlumas
    
    def cantidadAves(self):
        return len(Ave._listado)  
    