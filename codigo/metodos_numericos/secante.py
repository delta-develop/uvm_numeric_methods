from codigo.ayudas import imprimir


def secante(f, p0, p1, tolerancia, max_iteraciones, decimales=16):
    iteracion = 2

    print(f"\n Función: {f.__name__} \n")

    while iteracion <= max_iteraciones:

        p = p1 - (f(p1) * (p1 - p0)) / (f(p1) - f(p0))

        imprimir(iteracion, p, decimales)

        if abs(p - p1) < tolerancia:
            return p

        p0 = p1
        p1 = p
        iteracion += 1

    print("Iteraciones agotadas")
    return


def secante_modificado(f, p1, delta, tolerancia, max_iteraciones, decimales=16):
    iteracion = 2

    print(f"\n Función: {f.__name__} \n")

    while iteracion <= max_iteraciones:

        p = p1 - ((delta * p1 * f(p1)) / (f(p1 + delta * p1) - f(p1)))

        imprimir(iteracion, p, decimales)

        if abs(p - p1) < tolerancia:
            return p

        p0 = p1
        p1 = p
        iteracion += 1

    print("Iteraciones agotadas")
    return
