# Método de Gauss-Seidel.
from codigo.ayudas.utilidades import imprimir_matriz
from codigo.metodos_numericos.gauss_seidel import GaussSeidel

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
TOL = 1e-5
MAX = 50

print("Matriz A:")
imprimir_matriz(A)

print("Vector b:")
print(b)

print("aproximación inicial x0:")
print(x0)

print("\n Iteración de Gauss-Seidel: \n")
GaussSeidel(A, b, x0, TOL, MAX)
