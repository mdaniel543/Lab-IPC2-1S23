class Persona:
    def __init__(self, nombre, email, edad, genero, mensaje) -> None:
        self.nombre = nombre
        self.email = email 
        self.edad = edad
        self.genero = genero 
        self.mensaje = mensaje
        self.siguiente = None