from codigo.metodos_numericos import newton_raphson, secante, secante_modificado


def raiz(x):
    return 0.95 * x**3 - 5.9 * x**2 + 10.9 * x - 6


def raiz_derivada(x):
    return 3 * 0.95 * x**2 - 2 * 5.9 * x + 10.9


if __name__ == "__main__":

    newton_raphson(raiz, raiz_derivada, 3.5, 1e-2, 100)
    secante(raiz, 2.5, 3.5, 1e-8, 10)
    secante_modificado(raiz, 3.5, 0.01, 1e-8, 10)
