from math import pi

from biseccion import biseccion
from funciones import (
    exponencial,
    exponencial_derivada,
    polinomio,
    polinomio_3,
    potencia,
    trigonometrica,
    trigonometrica_2,
    trigonometrica_2_derivada,
    trigonometrica_3,
)
from newthon_raphson import newton_raphson
from regula import regula
from secante import secante

if __name__ == "__main__":

    # biseccion(polinomio,1.0,2.0,1e-8,100)
    # biseccion(trigonometrica, 4.0, 6.0, 1e-8, 100)
    # biseccion(potencia, 0.0, 2.0, 1e-8, 100)

    # regula(polinomio,1.0,2.0,1e-8,100)
    # regula(trigonometrica, 4.0, 6.0, 1e-8, 100)
    # regula(potencia, 0.0, 2.0, 1e-8, 100)

    # newton_raphson(trigonometrica_2, trigonometrica_2_derivada, pi/4, 1e-10,100)

    # newton_raphson(exponencial, exponencial_derivada, 4.0, 1e-8, 100)

    secante(polinomio_3, -3.0, 3.0, 1e-10, 100)
    secante(trigonometrica_3, 1.1, 0.8, 1e-8, 100)
