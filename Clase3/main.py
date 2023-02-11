import xml.sax

from elemento import Elemento

class Manejador( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""  #DEFAULT
        self.id = ""
        self.nombre = ""

    # Se llama cuando se encuentra un elemento de apertura
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "elemento":
            print("***** Elemento *****")

    # Se llama cuando se encuentra contenido entre elementos
    def characters(self, content):
        if self.CurrentData == "id":
            self.id = content
        elif self.CurrentData == "nombre":
            self.nombre = content

    # Se llama cuando se encuentra un elemento de cierre
    def endElement(self, tag):
        if tag == "elemento":
            elemento = Elemento(self.id, self.nombre)
            print(elemento)
        self.CurrentData = ""



if __name__ == '__main__':
    print("XML")

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # CLASE
    Handler = Manejador()

    parser.setContentHandler(Handler)

    parser.parse("info.xml")

    print("TERMINO")