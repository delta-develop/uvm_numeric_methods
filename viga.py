from codigo.metodos_numericos import biseccion


def funcion_viga(x):
    return 12 - 10 * x**2 - 185 * x + 1650


if __name__ == "__main__":

    biseccion(funcion_viga, 6.0, 10.0, 1e-2, 100, 7)
