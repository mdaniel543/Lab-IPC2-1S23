from .Nodo import Persona

class Cola:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
        
    def encolar(self, nombre, email, edad, genero, mensaje):
        persona = Persona(nombre, email, edad, genero, mensaje)
        if self.primero == None:
            self.primero = persona
            self.ultimo = persona
        else:
            self.ultimo.siguiente = persona
            self.ultimo = persona
        
    
    def desencolar(self):
        if self.primero == None:
            return None
        else: 
            aux = self.primero
            self.primero = self.primero.siguiente
            return aux
        
    def estaVacia(self):
        return self.primero == None