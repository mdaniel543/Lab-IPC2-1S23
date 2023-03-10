import os

class ListaDoble():
    def __init__(self):
        self.inicio = None
        self.fin = None
        # OPCIONAL
        self.tamanio = 0

    def recorrer(self):
        aux = self.inicio
        cadena = ""
        while aux != None:
            cadena += str(aux) + "\n"
            aux = aux.siguiente
        return cadena

    def recorreInverso(self):
        cadena = ""
        aux = self.fin
        while aux != None:
            cadena += str(aux) + "\n"
            aux = aux.anterior
        return cadena

    def insertarFin(self, objeto):
        if self.inicio == None:
            self.inicio = objeto
            self.fin = objeto
        else:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = objeto
            objeto.anterior = aux
        self.tamanio += 1

    def insertarInicio(self, objeto):
        if self.inicio == None:
            self.inicio = objeto
            self.fin = objeto
        else:
            objeto.siguiente = self.inicio
            self.inicio.anterior = objeto
            self.inicio = objeto
        self.tamanio += 1

    def eliminar(self, codigo):
        aux = self.inicio
        while aux != None:
            if aux.codigo == codigo:
                if aux.anterior == None:
                    self.inicio = aux.siguiente
                    self.inicio.anterior = None
                elif aux.siguiente == None:
                    self.fin = aux.anterior
                    self.fin.siguiente = None
                else:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior
                self.tamanio -= 1
                return True
            aux = aux.siguiente
        return False

    def graphviz(self):
        aux = self.inicio
        cadena = "digraph G {\n"
        cadena += "rankdir=LR;\n"
        cadena += "node [shape=record];\n"
        # info cuadrado
        while aux != None:
            cadena += "node" + str(aux.codigo) + " [label=\"{" + str(aux.codigo) + "|" + str(aux.apellido) + "}\"];\n"
            aux = aux.siguiente
        aux = self.inicio
        # flechas, siguiente y anterior
        while aux != None:
            if aux.siguiente != None:
                cadena += "node" + str(aux.codigo) + " -> node" + str(aux.siguiente.codigo) + ";\n"
            if aux.anterior != None:
                cadena += "node" + str(aux.codigo) + " -> node" + str(aux.anterior.codigo) + ";\n"
            aux = aux.siguiente
        cadena += "}"
        archivo = open("listaDoble.dot", "w")
        archivo.write(cadena)
        archivo.close()
        os.system("dot -Tpng listaDoble.dot -o listaDoble.png")