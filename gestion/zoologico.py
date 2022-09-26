class Zoologico:
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]
    
    def agregarZonas(self,zonas):
        self._zonas.append(zonas)
        
    def cantidadTotalAnimales(self):
        acumulador=0
        for i in self._zonas:
            cantidad=i.cantidadAnimales()
            acumulador=acumulador+cantidad
        return acumulador

    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getUbicacion(self):
        return self._ubicacion
    
    def setZona(self, zonas):
        self._zonas = zonas
        
    def getZona(self):
        return self._zonas