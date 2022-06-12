from codigo.metodos_numericos import biseccion


def profundidad_critica(y):
    Q = 20
    g = 9.81
    return 1 - ((Q**2) / (g * Ac(y) ** 3)) * B(y)


def Ac(y):
    return 3 * y + ((y**2) / 2)


def B(y):
    return 3 + y


if __name__ == "__main__":

    biseccion(profundidad_critica, 0.5, 2.5, 1e-4, 100, 10)
