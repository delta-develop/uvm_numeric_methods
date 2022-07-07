# -*- coding: utf-8 -*-
"""
Integración de Romberg

"""
import sympy
from sympy.abc import x
from codigo.metodos_numericos import (romberg,lagrange)

from codigo.ayudas.utilidades import graficacion

"""
    Entradas:
        Datos -- Profundidades de un rio H
                 ------------------------------------
                  x,m               H,m
                 ------------------------------------
                    0               0
                    2               1.9
                    4               2
                    6               2
                    8               2.4
                    10              2.6
                    12              2.25
                    14              1.12
                    16              0
    Salidas:
        F(x), Integración Romberg criterio de detención de 1%,0.5% y 1.5%

""" 

Datos = [(0, 0), (2, 1.9), (4, 2), (6, 2), (8, 2.4),
                 (10, 2.6), (12, 2.25), (14, 1.12), (16, 0)]

#Paso 1: Interpolación para obtener polinomio mediante métodos de Lagrange

Px = lagrange.LagrangeFx(Datos)
Px= Px();

print("\n\n Paso 1.- Interpolación f(x):  ")
print("\n\t",  Px)

def fx1(x):
    return sympy.lambdify(x, Px)

lagrange.LagrangePlot(Datos,100)

#Paso 2: Integración Romberg, criterio de detención de 1%
print("\n\n\t Paso 2.- Integración Romberg criterio de detención de 1%:")
romberg(fx1(x), 0, 16, 64, 0.01)

#Paso 3: Integración Romberg, criterio de detención de 0.5%
print("\t Paso 3.- Integración Romberg criterio de detención de 0.5%:")
romberg(fx1(x), 0, 16, 64, 0.005)

#Paso 4: Integración Romberg, criterio de detención de 1.5%
print("\t Paso 4.- Romberg criterio de detención de 1.5%:")
romberg(fx1(x), 0, 16, 64, 0.015)

#Paso 5: Gráfica de integración
graficacion(fx1(x), 0, 16, 64)



