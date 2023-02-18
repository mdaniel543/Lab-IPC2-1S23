class Elemento():
    def __init__(self, id, nombre, subElementos):
        self.id = id
        self.nombre = nombre
        self.subElementos = subElementos
        self.siguiente = None

    def __str__(self):
        return "id: " + self.id + " nombre: " + self.nombre + " subelementos: \n" + str(self.subElementos.recorrer())


