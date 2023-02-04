from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, cui, edad, carnet, carrera):
        super().__init__(nombre, cui, edad)
        self.carnet = carnet
        self.carrera = carrera

    def __str__(self):
        return super().__str__() + " Carnet: " + str(self.carnet) + " Carrera: " + self.carrera



