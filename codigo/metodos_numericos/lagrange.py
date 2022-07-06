# Método de Lagrange
import sympy as sym

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

# f(x)
def LagrangeFx(datos):
    
    X = sym.Symbol('x')
    
    def f_Lagrange_Expresion(k):
        num = 1
        den = 1
        for i, p in enumerate(datos):
            if i != k:
                num = num*(X-p[0])
                den = den*(datos[k][0] - p[0])
        expreT=num/den
        
        return expreT
    
    def F():
        
        polinomio = 0
        for k, p in enumerate(datos):
            polinomio= polinomio+p[1]*f_Lagrange_Expresion(k)
            
    
        return polinomio.expand()
    
    return F