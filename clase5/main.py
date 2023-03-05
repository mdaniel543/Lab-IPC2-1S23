from Matriz import Matriz

if __name__ == '__main__':
    matriz = Matriz()

    matriz.insertar(4, 2, "z")

    matriz.insertar(2, 1, "d")
    matriz.insertar(2, 2, "e")
    matriz.insertar(2, 3, "f")
    #matriz.insertar(3, 1, "g")
    matriz.insertar(3, 2, "h")
    matriz.insertar(3, 3, "i")

    matriz.insertar(1, 1, "a")
    # matriz.insertar(1, 2, "b")
    # matriz.insertar(1, 3, "c")

    matriz.recorrer()
    print("-----------------")
    matriz.graficar()
    matriz.recorrer()



