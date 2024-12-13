from gestion.zona import Zona
class Animal:
    _totalAnimales = 0

    def __init__(self, nombre = '', edad= 0, habitat = '', genero =''):
        self._nombre = nombre
        self._edad = edad
        self._habitat =habitat
        self._zona = []
        self._genero = genero
        Animal._totalAnimales += 1

    def setNombre (self, nombre):
        self._nombre = nombre
    def getNombre (self):
        return self._nombre

    def setEdad(self, edad):
        self._edad = edad
    def getEdad (self):
        return self._edad
    
    def setHabitat (self, habitat):
        self._habitat =habitat
    def getHabitat (self):
        return self._habitat
    
    def setZona (self, zona):
        self._zona =zona
    def getZona (self):
        return self._zona
    
    def setGenero (self, genero):
        self._genero = genero
    def getGenero(self):
        return self._genero

    def movimiento(self):
        from ave import Ave
        from reptil import Reptil
        from pez import Pez
        from anfibio import Anfibio
        if isinstance(self):
            return 'desplazarse'
        
        if isinstance (self, Ave):
            return 'volar'
        
        if isinstance (self, Reptil):
            return 'reptar'
        
        if isinstance (self, Pez):
            return 'nadar'
        
        if isinstance (self, Anfibio):
            return 'saltar'
        
    def toString(self):
        if self._zona == []:
            return (f'Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}')
        else:
            return (f'Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el zoo {self._zona._zoo._nombre}')    
    
    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio

        return (f'Mamiferos : {len(Mamifero._listado)}\nAves : {len(Ave._listado)}\nReptiles : {len(Reptil._listado)}\nPeces : {len(Pez._listado)}\nAnfibios : {len(Anfibio._listado)}')
        