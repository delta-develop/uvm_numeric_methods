from codigo.ayudas import imprimir


def regula(f, p0, p1, tolerancia, max_iteraciones, decimales=16):
    iteracion = 2

    print(f"\n Función: {f.__name__} \n")

    while iteracion <= max_iteraciones:

        q0 = f(p0)
        q1 = f(p1)
        p = p1 - (q1 * (p1 - p0)) / (q1 - q0)

        imprimir(iteracion, p, decimales)

        if abs(p - p1) < tolerancia:
            return p

        iteracion += 1

        q = f(p)

        if q * q1 < 0:
            p0 = p1
            q0 = q1

        p1 = p
        q1 = q

    print("Iteraciones agotadas")
    return
