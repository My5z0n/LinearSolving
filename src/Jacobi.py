import numpy as np
from numpy.linalg import norm
import time

import  src.algorithms as al
from src.preparareMatrix import preparareMatrix


def Jacobi(N, a1, a2, a3, debug=False):
    tuple = preparareMatrix(N, a1, a2, a3)
    M = tuple[0]
    b = tuple[1]


    err = 1

    # numpy.linalg.solve
    xn1 = []
    xn1.append([])
    xn = []
    xn.append([])
    for i in range(N):
        xn1[0].append(1)
        xn[0].append(1)


    iters = 0

    start = time.time()

    while err > 1e-9:
        xn, xn1 = xn1, xn
        for m in range(N):
            s1= al.dot_product(M[m][:m],xn[0][:m])
            s2 = al.dot_product(M[m][ m + 1:], xn[0][m + 1:])
            xn1[0][m] = (b[0][m] - s1 - s2) / M[m][ m]

        residuum = al.sub2(al.dot_product_matrix(M, xn1) , b)
        err = al.norm(residuum)
        if debug and err > 1e14:
            raise Exception('Results of algorithm will be probably wrong. The result does not seem to coincide')

        iters += 1
    end = time.time()
    duration = end - start

    return duration, iters


if __name__ == "__main__":
    Jacobi(200, 13, -1, -1, debug=True)
