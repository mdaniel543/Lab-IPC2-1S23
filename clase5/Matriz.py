from NodoEncabezado import NodoEncabezado
from ListaEncabezado import ListaEncabezado
from NodoInterno import NodoInterno
import os

class Matriz:
    def __init__(self) -> None:
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()

    def insertar(self, pfila, pcol, valor):
        nuevo = NodoInterno(pfila, pcol, valor)

        if self.filas.buscar(pfila) == None:
            self.filas.insertar(NodoEncabezado(pfila))

        if self.columnas.buscar(pcol) == None:
            self.columnas.insertar(NodoEncabezado(pcol))

        fila = self.filas.buscar(pfila)
        col = self.columnas.buscar(pcol)

        if fila.acceso == None:
            fila.acceso = nuevo
        else:
            if nuevo.col < fila.acceso.col:
                nuevo.derecha = fila.acceso
                fila.acceso.izquierda = nuevo
                fila.acceso = nuevo
            elif nuevo.col > fila.acceso.col:
                actual = fila.acceso
                while actual.derecha != None:
                    actual = actual.derecha
                actual.derecha = nuevo
                nuevo.izquierda = actual

        if col.acceso == None:
            col.acceso = nuevo
        else:
            if nuevo.fila < col.acceso.fila:
                nuevo.abajo = col.acceso
                col.acceso.arriba = nuevo
                col.acceso = nuevo
            elif nuevo.fila > col.acceso.fila:
                actual = col.acceso
                while actual.abajo != None:
                    actual = actual.abajo
                actual.abajo = nuevo
                nuevo.arriba = actual


    def graficar(self):
        if self.filas.primero == None:
            return
        if self.columnas.primero == None:
            return

        file = open("Matriz.dot", "w")
        file.write("digraph G{\n")
        file.write("node [shape=plaintext];\n")
        file.write("rankdir=LR;\n")
        file.write("Matriz [\n")
        file.write("label=<<table border='0' cellborder='1' cellspacing='0'> \n")

        file.write("<tr>\n")
        file.write("<td></td>\n")

        actual = self.columnas.primero
        while actual != None:
            file.write("<td bgcolor=\"#DE0039\">" + str(actual.id) + "</td>\n")
            actual = actual.siguiente
        file.write("</tr>\n")

        actual = self.filas.primero
        while actual != None:
            file.write("<tr>\n")
            file.write("<td bgcolor=\"#0062DE\">" + str(actual.id) + "</td>\n")

            aux = self.columnas.primero
            while aux != None:
                if actual.acceso != None:
                    if actual.acceso.col == aux.id:
                        file.write("<td>" + str(actual.acceso.valor) + "</td>\n")
                        actual.acceso = actual.acceso.derecha
                    else:
                        file.write("<td></td>\n")
                else:
                    file.write("<td></td>\n")
                aux = aux.siguiente

            file.write("</tr>\n")
            actual = actual.siguiente

        file.write("</table>>];\n")
        file.write("}")
        file.close()
        os.system("dot -Tpng Matriz.dot -o Matriz.png")





