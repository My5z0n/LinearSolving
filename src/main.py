from src.GaussSeidl import GaussSeidl
from src.Jacobi import Jacobi
from src.LUFactor import LUFactor
from src.PrintTimes import PrintTimes
from src.preparareMatrix import preparareMatrix


def main():
    # Zad A
    preparareMatrix(918, 13, -1, -1)

    # Zad B
    print("Jacobi:")
    results = Jacobi(918, 13, -1, -1, )
    print("Time: {0:0.2f}s Iterations: {1}".format(results[0], results[1]))

    print("GaussSeidl:")
    results = GaussSeidl(918, 13, -1, -1)
    print("Time: {0:0.2f}s Iterations: {1}".format(results[0], results[1]))

    #Zad C
    print("Jacobi:")
    try:
        results = Jacobi(918, 3, -1, -1,debug=True)
        print("Time: {0:0.2f}s Iterations: {1}".format(results[0], results[1]))
    except Exception as e:
        print("Error during Jacobi method:")
        print(e)
    print("GaussSeidl:")
    try:
        results = GaussSeidl(918, 3, -1, -1, debug=True)
        print("Time: {0:0.2f}s Iterations: {1}".format(results[0], results[1]))
    except Exception as e:
        print("Error during Jacobi method:")
        print(e)
    # Zad D
    print("LUFactor:")
    results = LUFactor(918, 3, -1, -1)
    print("Time: {0:0.2f}s Residuum: {1}".format(results[0], results[1]))

    # Zad E
    N = [100, 300, 500, 1000, 2000,3000]
    tG = []
    tJ = []
    tLU = []
    for i in range(len(N)):
        print(N[i])
        ret = Jacobi(N[i], 13, -1, -1, )
        tJ.append(ret[0])
        ret = GaussSeidl(N[i], 13, -1, -1, )
        tG.append(ret[0])
        ret = LUFactor(N[i], 13, -1, -1)
        tLU.append(ret[0])
    print("Jacobi:")
    print(tJ)
    print("Gauss:")
    print(tG)
    print("LU:")
    print(tLU)
    PrintTimes(tJ, tG, tLU, N)


if __name__ == "__main__":
    main()
