class Zoologico:

    def __init__(self, _nombre = None, _ubicacion = None, _zonas = []):
        self._nombre = _nombre
        self._ubicacion = _ubicacion
        self._zonas = _zonas

    def getNombre(self):
        return self._nombre
    def setNombre (self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion (self, ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas
    def setZonas(self, zonas):
        self._zonas = zonas

    def agregarZonas (self, zona):
        self._zonas.append(zona)
        zona._zoo = self

    def cantidadTotalAnimales (self):
        from zona import Zona
        cantidadAnimales = 0
        for i in self._zonas:
            if isinstance(i, Zona):
                cantidadAnimales += len(i._animales)
        return cantidadAnimales