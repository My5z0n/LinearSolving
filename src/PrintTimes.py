
import matplotlib.pyplot as plt




def PrintTimes(tJ,tG,tLU,nsizes):
    fig, ax = plt.subplots()
    ax.plot(nsizes, tJ,label='Jacobi')
    ax.plot(nsizes, tG,label='Gauss')
    ax.plot(nsizes, tLU, label='LU')
    title = 'Time dependence on the size N'
    ax.set(ylabel='Time (s)', xlabel='Matrix Size [N]',
           title=title)
    ax.grid()
    plt.legend(shadow=True, fancybox=True)
    # fig.savefig("test.png")
    plt.show()