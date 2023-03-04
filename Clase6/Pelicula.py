class Pelicula:
    def __init__(self, titulo, duracion, director, anio):
        self.titulo = titulo
        self.duracion = duracion
        self.director = director
        self.anio = anio

        self.siguiente = None
        self.anterior = None