from math import sin

def make_zeros(N):
    M = []
    for i in range(N):
        M.append([])
        for j in range(N):
            M[i].append(0.0)
    return M


def add_a1(M, a1):
    for i in range(len(M)):
        for j in range(len(M)):
            if i == j:
                M[i][j] = a1
    return M


def add_a2(M, a2):
    for i in range(len(M)):
        for j in range(len(M)):
            if i + 1 == j or i - 1 == j:
                M[i][j] = a2
    return M


def add_a3(M, a3):
    for i in range(len(M)):
        for j in range(len(M)):
            if i + 2 == j or i - 2 == j:
                M[i][j] = a3
    return M


def preparareMatrix(N, a1, a2, a3):
    xDM = make_zeros(N)
    add_a1(xDM, a1)
    add_a2(xDM, a2)
    add_a3(xDM, a3)

    xDB = []
    xDB.append([])
    for i in range(N):
        xDB[0].append(sin((i + 1) * (5 + 1)))

    return xDM, xDB


if __name__ == "__main__":
    preparareMatrix(5, 13, -1, -1)
