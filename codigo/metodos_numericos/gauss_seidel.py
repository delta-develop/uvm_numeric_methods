def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])


def GaussSeidel(A, b, x0, TOL, MAX):

    n = len(A)
    x = [0.0 for _ in range(n)]
    k = 1
    while k <= MAX:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("Imposible iterar")
                return
            s1 = sum([A[i][j] * x[j] for j in range(i)])
            s2 = sum([A[i][j] * x0[j] for j in range(i + 1, n)])
            x[i] = (b[i] - float(s1) - float(s2)) / float(A[i][i])
        # print(f"Iteración {k}: {x}")

        if distinf(x, x0) < TOL:
            print(f"Solución encontrada después de {k} iteraciones\n")
            return x
        k += 1

        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return
