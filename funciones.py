from math import sin, cos, pow, exp


def polinomio(x):
    return x**3 + 4 * x**2 - 10


def trigonometrica(x):
    return x * cos(x - 1) - sin(x)


def potencia(x):
    return pow(7.0, x) - 13


def polinomio_2(x):
    return ((-1 / 10) * x**2) + 3


def exponencial(x):
    return x**2 + exp(-2 * x) - 2 * x * exp(-x)


def exponencial_derivada(x):
    return 2 * x - 2 * exp(-2 * x) - 2 * exp(-x) + 2 * x * exp(-x)


def trigonometrica_2(x):
    return cos(x) - x


def trigonometrica_2_derivada(x):
    return -sin(x) - 1


def polinomio_3(x):
    return x**3 - 2


def trigonometrica_3(x):
    return sin(2 / x)
