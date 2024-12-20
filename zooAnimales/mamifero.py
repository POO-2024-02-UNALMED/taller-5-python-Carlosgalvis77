from .animal import Animal

class Mamifero(Animal):
    
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre='', edad=0, habitat='', genero='', pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def crearCaballo (cls, nombre = '' , edad = 0, genero = ''):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, habitat= 'pradera', genero = genero, pelaje= True, patas= 4)

    @classmethod
    def crearLeon (cls, nombre = '' , edad = 0, genero = ''):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, habitat= 'selva', genero = genero, pelaje= True, patas= 4)
    
    def cantidadMamiferos(self):
        return len(Mamifero._listado)
    
    def isPelaje(self):
        return(self._pelaje)
    
    def setPatas(self, patas):
        self._patas = patas

    def getPatas(self):
        return self._patas