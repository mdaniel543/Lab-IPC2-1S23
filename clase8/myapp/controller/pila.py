from .Nodo import Persona

class Pila:
    def __init__(self):
        self.top = None
        
    def apilar(self, nombre, email, edad, genero, mensaje):
        print(nombre, email, edad, genero, mensaje)
        persona = Persona(nombre, email, edad, genero, mensaje)
        persona.siguiente = self.top
        self.top = persona
        
    def desapilar(self):
        if self.top == None:
            return None
        else: 
            aux = self.top
            self.top = self.top.siguiente
            return aux
    
    def estaVacia(self):
        return self.top == None