def varibles():
    # ASSIGMENT OPERATORS
    # =	    x = 5	x = 5
    # +=	x += 3	x = x + 3
    # -=	x -= 3	x = x - 3
    # *=	x *= 3	x = x * 3
    # /=	x /= 3	x = x / 3

    a = 1
    b = 'dos'
    c = 12.6
    d = True
    e = 15

    f = [a, b, c, d, e]

    print([x for x in f])

    print(type(c), c)


def sumados(a, b):
    return a + b


def condicionales():
    a = 1
    b = 2

    # Comparison Operators
    # ==	Equal	                    x == y
    # !=	Not equal	                x != y
    # >	    Greater than	            x > y
    # <	    Less than	                x < y
    # >=	Greater than or equal to	x >= y
    # <=	Less than or equal to	    x <= y

    if a > b:
        print('a es mayor que b')
    elif a < b and a == 1:
        print('a es menor que b')
    else:
        print('a es igual a b')

    # Logical Operators
    # and 	    Returns True if both statements are true	                x < 5 and  x < 10
    # or	    Returns True if one of the statements is true	            x < 5 or x < 4
    # not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

    amigos = ['Juan', 'Pedro', 'Pablo']
    if 'Juan' in amigos:
        print('Juan esta en la lista de amigos')


def iteradores():

    while True:
        letra = input('Ingrese una letra: ')
        if letra == 'q':
            break

    for i in range(10):
        print(i)



if __name__ == '__main__':
    varibles()

    if sumados(5, 3) == 8:
        print('Todo bien')
    else:
        print('Todo mal')

    iteradores()

    condicionales()

