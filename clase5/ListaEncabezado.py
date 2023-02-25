from NodoEncabezado import NodoEncabezado

class ListaEncabezado:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def insertar(self, nuevo: NodoEncabezado):
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                nuevo.anterior = self.ultimo
                self.ultimo.siguiente = nuevo
                self.ultimo = nuevo
            else:
                actual = self.primero
                while actual != None:
                    if nuevo.id < actual.id:
                        nuevo.siguiente = actual
                        nuevo.anterior = actual.anterior
                        actual.anterior.siguiente = nuevo
                        actual.anterior = nuevo
                        break
                    actual = actual.siguiente

    def buscar(self, id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print(actual.id)
            actual = actual.siguiente
