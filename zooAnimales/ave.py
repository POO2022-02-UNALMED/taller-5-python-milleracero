from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0
    
     
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Animal.ave += 1
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero,"blanco y amarillo")
        cls._listado.append(aguila)
        cls.aguilas +=1

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero,"cafe glorioso")
        cls._listado.append(halcon)
        cls.halcones += 1
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def setListado(self, listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
        
    def getColorPlumas(self):
        return self._colorPlumas