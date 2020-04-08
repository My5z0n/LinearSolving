import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def SinglePrint(name,time,nsizes):


    fig, ax = plt.subplots()
    ax.plot(nsizes,time)

    title='Graph of the algorithm work time dependence on the size of the N matrix (For '+name+').'
    ax.set(xlabel='Time (s)', ylabel='Matrix Size [N]',
           title=title)
    ax.grid()

    fig.savefig("test.png")
    plt.show()

def PrintTimes(tJ,tG,tLU,nsizes):
    SinglePrint('Jacobi',tJ,nsizes)
    SinglePrint('GaussSeidl', tG, nsizes)
    SinglePrint('LUFactor', tLU, nsizes)