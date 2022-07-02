# Método de Lagrange


def LagrangePol(datos):
    def f_Lagrange(k, x):
        """Implementación funciones L_k(x)"""
        out = 1
        for i, p in enumerate(datos):
            if i != k:
                out *= (x - p[0]) / (datos[k][0] - p[0])
        return out

    def P(x):

        """Implementación polinomio P(x)"""
        # polinomio P(x) = Pkf(xk)Lk(x)
        lag = 0
        for k, p in enumerate(datos):
            lag += p[1] * f_Lagrange(k, x)

        return lag

    return P
