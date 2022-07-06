from re import X
import numpy as np
import matplotlib.pyplot as plt


def trapecio(fx, a, b, tramos, graficacion=True):
    h = (b - a) / tramos
    xi = a
    suma = fx(xi)

    for i in range(0, tramos - 1):
        xi = xi + h
        suma += 2 * fx(xi)

    suma += fx(b)
    area = h * (suma / 2)

    if graficacion:
        # SALIDA
        print("\n Trapecio \n")
        print("Segmentos:", tramos)
        print("Integral: ", area)
        print("\n")

    return area


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
    plt.title("Integral: Regla de Trapecios")
    plt.legend()

    # Trapecios
    plt.fill_between(xi, 0, fi, color="g")
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color="w")

    plt.show()
