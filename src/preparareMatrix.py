from math import sin

import numpy as np


def preparareMatrix(N, a1, a2, a3):
    M = np.zeros((N, N))
    # a1
    M += np.eye(N) * a1
    # a2
    M += np.eye(N, k=1) * a2
    M += np.eye(N, k=-1) * a2
    # a3
    M += np.eye(N, k=2) * a3
    M += np.eye(N, k=-2) * a3
    b = np.zeros((N, 1))

    for i in range(N):
        b[i][0] = sin(i * (5 + 1))

    return M, b


if __name__ == "__main__":
    preparareMatrix(918, 13, -1, -1)
