class Persona():
    def __init__(self, nombre, cui, edad):
        self.nombre = nombre
        self.cui = cui
        self.edad = edad

    def __str__(self):
        return "Nombre PERSONA: " + self.nombre + " CUI: " + str(self.cui) + " Edad: "+ str(self.edad)

    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getCui(self):
        return self.cui
    def setCui(self, cui):
        self.cui = cui
    def setNombre(self, nombre):
        self.nombre = nombre

