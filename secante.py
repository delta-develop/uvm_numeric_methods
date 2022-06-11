from utilidades import imprimir


def secante(f, p0, p1, tolerancia, max_iteraciones):
    iteracion = 2

    print(f"\n Función: {f.__name__} \n")

    while iteracion <= max_iteraciones:

        p = p1 - (f(p1) * (p1 - p0)) / (f(p1) - f(p0))

        imprimir(iteracion, p)

        if abs(p - p1) < tolerancia:
            return p

        p0 = p1
        p1 = p
        iteracion += 1

    print("Iteraciones agotadas")
    return
