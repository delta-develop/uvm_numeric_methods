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
                return None
            s1 = sum([A[i][j] * x[j] for j in range(i)])
            s2 = sum([A[i][j] * x0[j] for j in range(i + 1, n)])
            x[i] = (b[i] - s1 - s2) / A[i][i]
            x[i] = round(x[i], 6)
        print(f"Iteración {k}: {x}")
        if distinf(x, x0) < TOL:
            print("Solución encontrada")
            return x
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return None
