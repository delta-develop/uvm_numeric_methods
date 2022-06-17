from codigo.ayudas import imprimir


def newton_raphson(f, fprima, p0, tolerancia, max_iteraciones, decimales=16):
    iteracion = 1

    print(f"\n Función: {f.__name__} \n")

    while iteracion <= max_iteraciones:
        p = p0 - f(p0) / fprima(p0)
        imprimir(iteracion, p, decimales)

        if abs(p - p0) < tolerancia:
            return p

        p0 = p

        iteracion += 1

    print("Iteraciones agotadas")
    return
