class Animal:
    
    totalAnimales = 0
    mamifero = 0
    ave = 0
    reptil = 0
    pez = 0
    anfibio = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
    
    def setEdad(self, edad):
        self._edad = edad
        
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
        
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero
    
    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona = zona
        
    def getZona(self):
        return self._zona  
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre
    
    @classmethod
    def totalPorTipo(cls):
        men = (f"Mamiferos : {str(cls.mamifero)}\nAves : {str(cls.ave)}\nReptiles : {str(cls.reptil)}\nPeces : {str(cls.pez)}\nAnfibios : {str(cls.anfibio)}")
        
        return men

    def toString(self):
        if self.__zona != [] and self.__zona[0].getZoo() != None:
            men = f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero} la zona en la que me ubico es {self.__zona} en el {self.__zona[0].getZoo()}"
            return men
        else:
            men = f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero}"
            return men