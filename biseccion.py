from utilidades import imprimir


def biseccion(f, a, b, tolerancia, max_iteraciones):
    iteracion = 1

    print(f"\n Función: {f.__name__} \n")

    while iteracion <= max_iteraciones:
        p = a + (b - a) / 2.0
        imprimir(iteracion, p)

        if abs(f(p)) <= 1e-15 or (b - a) / 2.0 < tolerancia:
            return p

        if f(a) * f(p) > 0:
            a = p
        else:
            b = p

        iteracion += 1

    print("Iteraciones agotadas")
    return
