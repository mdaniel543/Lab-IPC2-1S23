import xml.sax

from ListaSimple import ListaSimple

from ListaDoble import ListaDoble

from SubElemento import SubElemento

from elemento import Elemento


listaEjemplo = ListaSimple()


class Manejador( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""  #DEFAULT

        self.elemento = None
        self.id = ""
        self.nombre = ""

        self.codigo = ""
        self.apellido = ""
        self.subelementos = None

    # Se llama cuando se encuentra un elemento de apertura
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "elemento":
            self.subelementos = ListaDoble()

    # Se llama cuando se encuentra contenido entre elementos
    def characters(self, content):
        if self.CurrentData == "id":
            self.id = content
        elif self.CurrentData == "nombre":
            self.nombre = content

        elif self.CurrentData == "codigo":
            self.codigo = content
        elif self.CurrentData == "apellido":
            self.apellido = content

    # Se llama cuando se encuentra un elemento de cierre
    def endElement(self, tag):
        if tag == "elemento":
            elemento = Elemento(self.id, self.nombre, self.subelementos)
            listaEjemplo.insertarFin(elemento)

        if tag == "subelemento":
            sub = SubElemento(self.codigo, self.apellido)
            self.subelementos.insertarFin(sub)
        self.CurrentData = ""



if __name__ == '__main__':
    print("XML")

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # CLASE
    Handler = Manejador()

    parser.setContentHandler(Handler)

    parser.parse("info.xml")

    print("inicio lista")

    listaEjemplo.recorrer()

    print("fin de lista")

    listaEjemplo.graphviz()

    temporal = listaEjemplo.buscar("1")

    temporal.subElementos.graphviz()

