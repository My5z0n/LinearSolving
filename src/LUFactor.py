import copy


import time
import src.algorithms as al
from src.preparareMatrix import preparareMatrix, make_zeros, add_a1


def LUFactor(N, a1, a2, a3):
    tuple = preparareMatrix(N, a1, a2, a3)
    M = tuple[0]
    b = tuple[1]

    U = copy.deepcopy(M)
    L = make_zeros(N)
    add_a1(L, 1)

    start = time.time()

    m = N
    for k in range(m - 1):
        for j in range(k + 1, m):
            L[j][k] = U[j][k] / U[k][k]
            U[j][k:m] = al.sub(U[j][k:m], al.multiply(L[j][k], U[k][k:m]))

    # y2 = np.linalg.solve(L,b)
    y = []
    y.append([])
    for i in range(N):
        y[0].append(b[0][i])
    for i in range(1, N):
        for j in range(i, N):
            y[0][j] -= L[j][i - 1] * y[0][i - 1]



    # x = np.linalg.solve(U, y)
    x = []
    x.append([])
    for i in range(N):
        x[0].append(y[0][i])


    rr=reversed(range(1,N))
    for i in rr:
        x[0][i] /= U[i][i]
        for j in reversed(range(0, i)):
            x[0][j] -= U[j][i] * x[0][i]

    x[0][0]/=U[0][0]


    end = time.time()
    duration = end - start

    residuum = al.sub2(al.dot_product_matrix(M, x), b)
    err = al.norm(residuum)
    return duration, err


if __name__ == "__main__":
    LUFactor(4, 13, -1, -1)
