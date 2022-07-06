# Integración: Regla Simpson 1/3
# Validar cantidad de tramos pares
import numpy as np
import matplotlib.pyplot as plt


def simpson_1_3(fx, a, b, tramos):
    h = (b - a) / tramos
    xi = a
    area = 0
    for i in range(0, tramos, 2):
        deltaA = (h / 3) * (fx(xi) + 4 * fx(xi + h) + fx(xi + 2 * h))
        area = area + deltaA
        xi = xi + 2 * h

    # SALIDA
    print("\n Simpson 1/3 \n")
    print("Segmentos:", tramos)
    print("Integral: ", area)
    print("\n")


def graficacion(f, a, b, tramos):
    muestras = tramos + 1
    xi = np.linspace(a, b, muestras)
    fx = np.vectorize(f)
    fi = fx(xi)

    linea_muestras = tramos * 10 + 1
    xk = np.linspace(a, b, linea_muestras)
    fk = fx(xk)

    plt.plot(xk, fk, label="f(x)")
    plt.plot(xi, fi, marker="o", color="orange", label="muesras")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Integral: Regla de Simpson 1/3")
    plt.legend()

    # Trapecios
    plt.fill_between(xi, 0, fi, color="b")
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color="w")

    plt.show()
