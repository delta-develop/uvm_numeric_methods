# Método de Jacobi
from codigo.ayudas.utilidades import actividad_4
from codigo.metodos_numericos.gauss_seidel import GaussSeidel
from codigo.metodos_numericos.jacobi import Jacobi


"""
    Entradas:
    A -- matriz
    b -- vector
    x0 -- aproximación inicial
    TOL -- error tolerable
    MAX -- número máximo de iteraciones

"""

A_1 = [
    [10, -1, 2],
    [-1, 11, -1],
    [2, -1, 10],
]
b_1 = [6, 25, -11]

A_2 = [
    [2, 10, -8],
    [3, 8, 13],
    [5, 2, -3],
]
b_2 = [1, 4, 7]


x0 = [0, 0, 0]

MAX = 1000

TOL = 1e-10
actividad_4(Jacobi, A_1, b_1, x0, TOL, MAX)
x0 = [0, 0, 0]  # Reiniciamos el vector
TOL = 1e-4
actividad_4(Jacobi, A_2, b_2, x0, TOL, MAX)
x0 = [0, 0, 0]  # Reiniciamos el vector

TOL = 1e-10
actividad_4(GaussSeidel, A_1, b_1, x0, TOL, MAX)
x0 = [0, 0, 0]  # Reiniciamos el vector
TOL = 1e-4
actividad_4(GaussSeidel, A_2, b_2, x0, TOL, MAX)
