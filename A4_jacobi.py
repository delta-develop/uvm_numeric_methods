# Método de Jacobi
from codigo.ayudas.utilidades import imprimir_matriz
from codigo.metodos_numericos.jacobi import Jacobi


"""
    Entradas:
    A -- matriz
    b -- vector
    x0 -- aproximación inicial
    TOL -- error tolerable
    MAX -- número máximo de iteraciones

"""

A = [
    [4, 1, 2],
    [3, 5, 1],
    [1, 1, 3],
]
b = [4, 7, 3]
x0 = [0, 0, 0]
TOL = 1e-4
MAX = 100

print("Matriz A:")
imprimir_matriz(A)
print("Vector b:")
imprimir_matriz(b)
print("aproximación inicial x0:")
imprimir_matriz(x0)
print("Iteración de Jacobi: \n")

Jacobi(A, b, x0, TOL, MAX)
