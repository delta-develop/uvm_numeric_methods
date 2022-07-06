# -*- coding: utf-8 -*-
# Método de lagrange

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

from codigo.metodos_numericos.lagrange import LagrangePol,LagrangeFx


"""
    Entradas:
    Datos -- lista de puntos (x,y) de velocidad del paracaidista
             ------------------------------------
             Tiempo (s)       Velocidad (cm/s)
             ------------------------------------
                1               800
                3              2310
                5              3090
                7              3940
               13              4755

   Estimación en t=10

"""
Datos = [(1, 800), (3, 2310), (5, 3090), (7, 3940), (13, 4755)]
t = 10

# Función
Pf = LagrangePol(Datos)

# Obtener valor
Pf_t10 = Pf(t)
print("\n\n El valor del polinomio de Lagrange en t = 10:")
print(" {0:.8f}".format(Pf_t10))

#Obtener polinomio
Px = LagrangeFx(Datos)
Px= Px();

print("\n\n Polinomio f(x):")
print("\n",Px)

# se agrega el nuevo valor para t=10 a Datos
Datos.append((t, Pf_t10))

# Puntos para la grafica
a = [val[0] for val in Datos]
b = [val[1] for val in Datos]

# Puntos para el polinoimio
n = 60
x_pol = np.linspace(min(a), max(a), n)
y_pol = [Pf(i) for i in x_pol]


# Grafica
plt.plot(a, b, "o", label="Puntos")
plt.plot(x_pol, y_pol, label="Polinomio")
plt.legend(loc="lower center")
plt.show()
