import numpy as np
from codigo.metodos_numericos import (
    trapecio,
    simpson_1_3,
    cuadratura_gaussiana,
    romberg,
)
from codigo.ayudas.utilidades import graficacion, graficacion_gaussiana
from math import e, exp, sin, sqrt, cos


def fx1(x):
    return sqrt(x) * sin(x)


def fx2(x):
    return x * sin(4 * x)


print("Función 1 a 4 tramos")

trapecio(fx1, 0, 2, 4)
simpson_1_3(fx1, 0, 2, 4)
cuadratura_gaussiana(fx1, 0, 2, 4)
romberg(fx1, 0, 2, 4, 0.001)

graficacion(fx1, 0, 2, 4)

print("Función 1 a 64 tramos")

trapecio(fx1, 0, 2, 64)
simpson_1_3(fx1, 0, 2, 64)
cuadratura_gaussiana(fx1, 0, 2, 64)
romberg(fx1, 0, 2, 64, 0.001)

graficacion(fx1, 0, 2, 64)
print("Función 2 a 4 tramos")

trapecio(fx2, 0, 4, 4)
simpson_1_3(fx2, 0, 4, 4)
cuadratura_gaussiana(fx2, 0, 4, 4)
romberg(fx2, 0, 4, 4, 0.001)

graficacion(fx1, 0, 4, 4)
print("Función 2 a 64 tramos")

trapecio(fx2, 0, 4, 64)
simpson_1_3(fx2, 0, 4, 64)
cuadratura_gaussiana(fx2, 0, 4, 64)
romberg(fx2, 0, 4, 64, 0.001)
graficacion(fx1, 0, 4, 64)
