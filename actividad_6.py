from codigo.metodos_numericos import Jacobi, GaussSeidel
from codigo.ayudas.utilidades import resolver_sistema_ecuaciones


cobre = [4, 3, 2]
zinc = [1, 3, 1]
vidrio = [2, 1, 3]

matriz_materiales = [cobre, zinc, vidrio]

materiales_disponibles = [960, 510, 610]

vector_inicial = [0, 0, 0]

tolerancia = 0.001
max_iteraciones = 1000

resolver_sistema_ecuaciones(
    metodo_numerico=Jacobi,
    A=matriz_materiales,
    b=materiales_disponibles,
    x0=vector_inicial,
    tolerancia=tolerancia,
    max=max_iteraciones,
)

vector_inicial = [0, 0, 0]

resolver_sistema_ecuaciones(
    metodo_numerico=GaussSeidel,
    A=matriz_materiales,
    b=materiales_disponibles,
    x0=vector_inicial,
    tolerancia=tolerancia,
    max=max_iteraciones,
)
