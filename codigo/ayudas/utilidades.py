import numpy as np
import matplotlib.pyplot as plt


def imprimir(iteracion, p, decimales=16):
    print("Iteración:", "%03d" % iteracion, " raiz:", f"%.{decimales}f" % p)


def imprimir_matriz(matriz):
    for fila in matriz:
        print("".join(str(fila)))


def comprobar_vector_resultado(matriz, x, b, elementos_vector):
    """Realiza la operación Ax = b

    Args:
        matriz: Matriz de entrada
        x: Vector de resultados de los cálculos
        b: Vector solución
        elementos_vector: Cantidad de elementos del vector x
    """
    i = 0
    vector_comprobacion = [0.0 for _ in range(elementos_vector)]
    for fila in matriz:
        for indice, columna in enumerate(fila):
            vector_comprobacion[i] += float(x[indice]) * float(columna)

        i += 1

    return vector_comprobacion


def resolver_sistema_ecuaciones(metodo_numerico, A, b, x0, tolerancia, max):
    """Realiza todas las operaciones de cálculos e impresión para el
    método numérico elegido

    Args:
        metodo_numerico: Función del método numérico a implementar
        A: Matriz de entradas
        b: Vector solución
        x0: Aproximación inicial
        tolerancia: Tamañod el error aceptable
        max: Cantidad máxima de iteraciones soportadas
    """
    print(f"\nMétodo: {metodo_numerico.__name__}")
    print("\nMatriz A")
    imprimir_matriz(A)

    print(f"\nVector b = {b}")

    print(f"\nAproximación inicial x0 = {x0}\n")

    vector_resultado = metodo_numerico(A, b, x0, tolerancia, max)
    vector_comprobacion = comprobar_vector_resultado(A, vector_resultado, b, 3)

    print(f"\nVector solución x = {vector_resultado}")

    print(f"\nComprobación: \nVector b = {b} \nProducto Ax = {vector_comprobacion}\n")
    diferencias = [abs(x - y) for (x, y) in zip(b, vector_comprobacion)]
    print(f"Diferencias: {diferencias}\n")


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
    plt.title("Integral")
    plt.legend()

    # Trapecios
    plt.fill_between(xi, 0, fi, color="g")
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color="w")

    plt.show()


def graficacion_gaussiana(fx, a, b, tramos):
    # GRAFICAR por cada Segmento
    # para concepto con pocos segmentos
    x0 = -1 / np.sqrt(3)
    x1 = 1 / np.sqrt(3)

    # arregos para gráficas
    xi = np.array([])
    fi = np.array([])

    xat = np.array([])
    xbt = np.array([])

    recta = np.array([])

    muestrastramo = 10
    muestras = tramos + 1
    subtramo = np.linspace(a, b, muestras)

    for i in range(0, tramos, 1):
        at = subtramo[i]
        bt = subtramo[i + 1]

        xit = np.linspace(at, bt, muestrastramo)
        fit = fx(xit)

        xi = np.concatenate((xi, xit))
        fi = np.concatenate((fi, fit))

        # puntos xa y xb por tramo
        xa = (bt + at) / 2 + (bt - at) / 2 * (x0)
        xb = (bt + at) / 2 + (bt - at) / 2 * (x1)

        xat = np.concatenate((xat, [xa]))
        xbt = np.concatenate((xbt, [xb]))

        # Recta entre puntos x0 y x1 por tramo
        m = (fx(xb) - fx(xa)) / (xb - xa)
        b0 = fx(xa) - m * xa
        linea = b0 + m * xit
        recta = np.concatenate((recta, linea))

    # Marcadores 'o' de xa y xb por tramos
    puntox = np.concatenate((xat, xbt))
    puntoy = fx(puntox)

    # Graficando
    # Trazado de lineas
    plt.plot(xi, recta, label="grado 1", color="tab:orange")
    plt.fill_between(xi, 0, recta, color="tab:olive")
    plt.plot(xi, fi, label="f(x)", color="blue")

    # Verticales para dividir los tramos
    for j in range(0, len(subtramo), 1):
        plt.axvline(subtramo[j], color="tab:gray")

    # Marcadores de puntos xa y xb por tramos
    for j in range(0, len(xat), 1):
        plt.axvline(xat[j], color="w")
        plt.axvline(xbt[j], color="w")

    plt.plot(puntox, puntoy, "o", color="g")

    plt.title("Integral: Cuadratura Gauss")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    plt.show()
