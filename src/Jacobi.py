import numpy as np
from numpy.linalg import norm
import time

from src.preparareMatrix import preparareMatrix


def Jacobi(N, a1, a2, a3,debug=False):
    tuple = preparareMatrix(N, a1, a2, a3)
    M = tuple[0]
    b = tuple[1]

    L = np.tril(M, -1)
    U = np.triu(M, 1)
    D = np.diag(np.diag(M))

    err = 1

    # numpy.linalg.solve
    xn1 = np.ones((N, 1))
    xn = np.ones((N, 1))

    iters = 0

    start = time.time()
    while err > 1e-9:
        xn = xn1
        one = np.linalg.solve(-1 * D, np.dot(L + U, xn))
        two = np.linalg.solve(D, b)
        xn1 = one + two
        residuum = np.dot(M, xn1) - b
        err = norm(residuum)
        if debug and err>1e14 :
            raise Exception('Results of algorithm will be probably wrong. The result does not seem to coincide')

        iters += 1
    end = time.time()
    duration = end - start

    return duration, iters


if __name__ == "__main__":
    Jacobi(4, 13, -1, -1,debug=True)
