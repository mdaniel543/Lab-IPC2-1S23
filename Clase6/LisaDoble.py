from Pelicula import Pelicula

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarFinal(self, titulo, duracion, director, anio):
        pelicula = Pelicula(titulo, duracion, director, anio)
        if self.primero is None:
            self.primero = pelicula
            self.ultimo = pelicula
        else:
            pelicula.anterior = self.ultimo
            self.ultimo.siguiente = pelicula
            self.ultimo = pelicula

    def insertarOrdenado(self, titulo, duracion, director, anio):
        pelicula = Pelicula(titulo, duracion, director, anio)
        if self.primero is None:
            self.primero = pelicula
            self.ultimo = pelicula
        else:
            if pelicula.duracion < self.primero.duracion:
                pelicula.siguiente = self.primero
                self.primero.anterior = pelicula
                self.primero = pelicula
            elif pelicula.duracion > self.ultimo.duracion:
                pelicula.anterior = self.ultimo
                self.ultimo.siguiente = pelicula
                self.ultimo = pelicula
            else:
                aux = self.primero
                while aux.duracion < pelicula.duracion:
                    aux = aux.siguiente
                pelicula.anterior = aux.anterior
                pelicula.siguiente = aux
                aux.anterior.siguiente = pelicula
                aux.anterior = pelicula

    def eliminar(self, titulo):
        if self.primero is None:
             print("la lista esta vacia")
        else:
            aux = self.primero
            while aux is not None:
                if aux.titulo == titulo:
                    #INICIO
                    if aux == self.primero:
                        self.primero = self.primero.siguiente
                        self.primero.anterior = None
                    #FIN
                    elif aux == self.ultimo:
                        self.ultimo = self.ultimo.anterior
                        self.ultimo.siguiente = None
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                    print("ELIMINADO")
                    return
                aux = aux.siguiente
            print("Pelicula NO encontrada")

    def mostrar(self):
        if self.primero is None:
            print("la lista vacia")
        else:
            aux = self.primero
            while aux is not None:
                print(aux.titulo, aux.director, aux.anio,  aux.duracion)
                aux = aux.siguiente

    def mostrarInverso(self):
        if self.ultimo is None:
            print("la lista esta vacia")
        else:
            aux = self.ultimo
            while aux is not None:
                print(aux.titulo, aux.director, aux.anio,  aux.duracion)
                aux = aux.anterior

    def ordenarBurbuja(self):
        aux = self.primero
        while aux is not None:
            aux2 = aux.siguiente
            while aux2 is not None:
                if aux.duracion > aux2.duracion:
                    temp = aux.titulo
                    aux.titulo = aux2.titulo
                    aux2.titulo = temp

                    temp = aux.duracion
                    aux.duracion = aux2.duracion
                    aux2.duracion = temp

                    temp = aux.director
                    aux.director = aux2.director
                    aux2.director = temp

                    temp = aux.anio
                    aux.anio = aux2.anio
                    aux2.anio = temp
                aux2 = aux2.siguiente
            aux = aux.siguiente

    def escribirXML(self):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("peliculas.xml", "w")
            archivo.write("<LitadoPeliculas>\n")

            aux = self.primero
            while aux is not None:
                archivo.write("\t<Pelicula>\n")
                archivo.write("\t\t<Titulo>" + aux.titulo + "</Titulo>\n")
                archivo.write("\t\t<Duracion>" + str(aux.duracion) + "</Duracion>\n")
                archivo.write("\t\t<Director>" + aux.director + "</Director>\n")
                archivo.write("\t\t<Anio>" + str(aux.anio) + "</Anio>\n")
                archivo.write("\t</Pelicula>\n")
                aux = aux.siguiente
            archivo.write("</LitadoPeliculas>")
            archivo.close()
