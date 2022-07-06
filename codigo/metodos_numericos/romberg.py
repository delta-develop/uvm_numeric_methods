import math
import numpy as np
from .trapecio import trapecio


def romberg(fx, a, b, tramos, error):
    I = np.zeros((10, 10))
    ea = 100
    tramos = 1
    i = 1
    I[1, 1] = trapecio(fx, a, b, tramos, False)

    print("Romberg")
    print("\nIteración \t integral")

    while ea > error:
        tramos = 2**i

        I[i + 1, 1] = trapecio(fx, a, b, tramos, False)

        for k in range(2, i + 2):
            j = 2 + i - k
            I[j, k] = (4 ** (k - 1) * I[j + 1, k - 1] - I[j, k - 1]) / (
                4 ** (k - 1) - 1
            )

        ea = abs((I[1, i + 1] - I[2, i]) / I[1, i + 1]) * 100
        et = abs((1.71828 - I[1, i + 1]) / 1.7182) * 100

        print("%f \t %f" % (i, I[1, i + 1]))
        i += 1

    print("\n")
