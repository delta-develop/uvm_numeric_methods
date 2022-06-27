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
    [10, -1, 2],
    [-1, 11, -1],
    [2, -1, 10],
]
b = [6, 25, -11]
x0 = [0, 0, 0]
TOL = 1e-10
MAX = 100

print("Matriz A:")
imprimir_matriz(A)

print("\nVector b:")
print(b)

print("\nAproximación inicial x0:")
print(x0)

print("\n Iteración de Gauss-Seidel: \n")
resultado = GaussSeidel(A, b, x0, TOL, MAX)
print(f"Solución: {resultado}")
