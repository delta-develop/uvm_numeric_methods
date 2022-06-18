# Método de Gauss-Seidel.
from math import *
from pprint import pprint
import numpy as np

def distinf(x, y):
    return max([abs(x[i]-y[i]) for i in range(len(x))])

def GaussSeidel(A, b, x0, TOL, MAX):

    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    while k <= MAX:
            for i in range(n):
                if abs(A[i][i]) <= 1e-15:
                    print("Imposible iterar")
                    return None
                s1 = sum([A[i][j]*x[j] for j in range(i)])
                s2 = sum([A[i][j]*x0[j] for j in range(i+1, n)])
                x[i] = (b[i] - s1 - s2)/A[i][i]
                x[i] = np.round(x[i], 4)       
            pprint(x)
            if distinf(x, x0) < TOL:
                print(r"Solución encontrada")
                return x
            k += 1
            for i in range(n):
                x0[i] = x[i]
    print("Iteraciones agotadas")
    return None


"""
    Entradas:
    A -- matriz 
    b -- vector
    x0 -- aproximación inicial
    TOL -- error tolerable
    MAX -- número máximo de iteraciones

"""

A = [[4, 1, 2],[3, 5, 1], [1, 1, 3],]
b = [4, 7, 3]
x0 = [0, 0, 0]
TOL=1e-5
MAX=50

print("Matriz A:")
pprint(A)

print("Vector b:")
pprint(b)

print("aproximación inicial x0:")
pprint(x0)

print("Iteración de Gauss-Seidel: \n")
GaussSeidel(A, b, x0, TOL, MAX)