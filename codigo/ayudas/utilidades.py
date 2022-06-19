def imprimir(iteracion, p, decimales=16):
    print("Iteración:", "%03d" % iteracion, " raiz:", f"%.{decimales}f" % p)


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(fila)))
