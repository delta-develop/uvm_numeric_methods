import numpy as np
from codigo.metodos_numericos import (
    trapecio,
    simpson_1_3,
    cuadratura_gaussiana,
    romberg,
)
import math


def fx(x):
    return np.sqrt(x) * np.sin(x)


def fx2(x):
    return np.sqrt(x) * -np.sin(x)


trapecio(fx, 2, 8, 8, graficacion=False)
# simpson_1_3(fx,2,8,8)
# cuadratura_gaussiana(fx,2,8,8)
fx = lambda x: math.exp(x)
romberg(fx, 0, 1, 8, 0.001)
