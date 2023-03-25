from .Nodo import Persona

class Pila:
    def __init__(self) -> None:
        self.top = None

    def push(self, nombre, email, edad, genero, mensaje):
        persona = Persona(nombre, email, edad, genero, mensaje)
        persona.siguiente = self.top
        self.top = persona
        
    def pop(self):
        if self.top == None: 
            return None
        else:
            aux = self.top
            self.top = self.top.siguiente
            return aux
        
    def estaVacia(self):
        return self.top == None