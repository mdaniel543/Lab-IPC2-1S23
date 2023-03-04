from LisaDoble import ListaDoble
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse("file.xml")
    root = tree.getroot()

    lista = ListaDoble()

    for pelicula in root.findall('Pelicula'):
        titulo = pelicula.find('Titulo').text
        duracion = pelicula.find('Duracion').text
        director = pelicula.find('Director').text
        anio = pelicula.find('Anio').text

        lista.insertarOrdenado(titulo, duracion, director, anio)

    lista.mostrar()
    print("-----------------")
    #lista.ordenarBurbuja()
    #lista.mostrar()

    lista.escribirXML()
