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


def actividad_4(metodo_numerico, A, b, x0, tolerancia, max):
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
    print(f"Diferencias: {diferencias}")
