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
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion
        
    def getUbicacion(self):
        return self.__ubicacion
    
    def setZona(self, zonas):
        self.__zonas = zonas
        
    def getZona(self):
        return self.__zonas