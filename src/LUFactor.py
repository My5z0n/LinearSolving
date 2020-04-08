import copy

import numpy as np
from numpy.linalg import norm
import time

from src.preparareMatrix import preparareMatrix


def LUFactor(N, a1, a2, a3):
    tuple = preparareMatrix(N, a1, a2, a3)
    M = tuple[0]
    b = tuple[1]



    U = copy.deepcopy(M)
    L = np.eye(N, N)

    start = time.time()

    m = N
    for k in range(m - 1):
        for j in range(k + 1, m):
            L[j][k] = U[j][k] / U[k][k]
            U[j][k:m] = U[j][k:m] - L[j][k] * U[k][k:m]


    #y = np.dot(U, x)
    y=np.linalg.solve(L,b)
    x=np.linalg.solve(U,y)
    end = time.time()
    duration = end - start

    err = norm(np.dot(M, x) - b)
    return duration,err





if __name__ == "__main__":
    LUFactor(4, 13, -1, -1)
