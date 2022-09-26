from zooAnimales.animal import Animal
class Anfibio(Animal):
    
    _listado = []
    ranas=0
    salamandras=0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Animal.anfibio += 1

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.__listado.append(rana)
        cls.ranas += 1

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.__listado.append(salamandra)
        cls.salamandras += 1

    def setListado(self, listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
        
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
        
    def isVenenoso(self):
        return self._venenoso