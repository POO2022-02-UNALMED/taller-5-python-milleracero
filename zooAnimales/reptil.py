from zooAnimales.animal import Animal

class Reptil(Animal):
    
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Animal.reptil += 1
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero,"blanco", 1)
        cls._listado.append(serpiente)
        cls.serpientes += 1
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero,"verde", 3)
        cls._listado.append(iguana)
        cls.iguanas += 1
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def setListado(self, listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
        
    def getLargoCola(self):
        return self._largoCola
    

    