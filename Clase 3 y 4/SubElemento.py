class SubElemento():
    def __init__(self, codigo, apellido):
        self.codigo = codigo
        self.apellido = apellido
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return "codigo: " + self.codigo + " apellido: " + self.apellido