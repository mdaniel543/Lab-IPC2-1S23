class NodoInterno:
    def __init__(self, fila = None, col = None, valor = None) -> None:
        self.fila = fila
        self.col = col
        self.valor = valor

        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None