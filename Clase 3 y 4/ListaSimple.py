import os

class ListaSimple():
    def __init__(self):
        self.inicio = None
        self.fin = None
        # OPCIONAL
        self.tamanio = 0

    def insertarFin(self, objeto):
        if self.inicio == None:
            self.inicio = objeto
            self.fin = objeto
        else:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = objeto
        self.tamanio += 1

    def insertarInicio(self, objeto):
        if self.inicio == None:
            self.inicio = objeto
            self.fin = objeto
        else:
            objeto.siguiente = self.inicio
            self.inicio = objeto
        self.tamanio += 1

    def recorrer(self):
        aux = self.inicio
        while aux != None:
            print(aux)
            aux = aux.siguiente

    def buscar(self, id):
        aux = self.inicio
        while aux != None:
            if aux.id == id:
                return aux
            aux = aux.siguiente
        return None

    def graphviz(self):
        aux = self.inicio
        cadena = "digraph G {\n"
        cadena += "rankdir=LR;\n"
        cadena += "node [shape=record];\n"
        #creando el cuadro
        while aux != None:
            cadena += "node" + str(aux.id) + " [label=\"{" + str(aux.id) + "|" + str(aux.nombre) + "}\"];\n"
            aux = aux.siguiente
        aux = self.inicio
        #creando flecha
        while aux != None:
            if aux.siguiente != None:
                cadena += "node" + str(aux.id) + " -> node" + str(aux.siguiente.id) + ";\n"
            aux = aux.siguiente
        cadena += "}"

        file = open("listaSimple.dot", "w")
        file.write(cadena)
        file.close()
        os.system("dot -Tpng listaSimple.dot -o listaSimple.png")
