import numpy as np
import matplotlib.pyplot as plt


#basis function
def N(i,j,t,x):

    if j == 0:
        if x < t[i+1] and x >= t[i] :
            N_t = 1
        else:
            N_t = 0

    else:
        N_t = ((x - t[i]) / (t[i+j] - t[i])) * N(i,j-1,t,x) + ((t[i+j+1] - x) / (t[i+j+1] - t[i+1])) * N(i+1,j-1,t,x)

    return N_t

def _plot():

    xx = np.linspace(0,5,500)
    y =[N(0,2,t,x) for x in xx]
    plt.plot(xx,y,'r',label='N0,2')

    y =[N(1,2,t,x) for x in xx]
    plt.plot(xx,y,'b',label='N1,2')

    y =[N(2,2,t,x) for x in xx]
    plt.plot(xx,y,'g',label='N2,2')



    plt.show()






def cox_de_boor(i,j,t):

    """
        Args:
        i : int
        j :
        t : list
    """

    N[i,j] = ((t - t[i]) / (t[i+j] - t[i])) * N[i+1,j-1]



    return



def bspline(x,y):



    return
