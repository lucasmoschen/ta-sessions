#!usr/bin/env python

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt 

f = lambda x: 1 / (1 + 25 * x * x)

def polynomial_interpolation(n, chebyshev = False):

    if chebyshev: 
        x = np.array([np.cos((2*k+1)*np.pi/(2*(n+1))) for k in range(n+1)])
    else: 
        x = np.linspace(-1,1,n+1)
    y = f(x)
    poly = lagrange(x,y)

    return poly, x, y

def chebyshev_polynomials(n): 
    return lambda x: np.cos(n * np.arccos(x))

if __name__ == '__main__': 

    t = np.linspace(-1,1,100)
    y = f(t)

    p1, x1, y1 = polynomial_interpolation(3)
    p2, x2, y2 = polynomial_interpolation(5)
    p3, x3, y3 = polynomial_interpolation(10)
    p4, x4, y4 = polynomial_interpolation(20)

    fig, ax = plt.subplots(2,2,figsize = (20,20), sharex = True)
    fig.suptitle(r'Interpolação polinomial da função $f(x) = (1 + 25x^2)^{-1}$')
    
    ax[0][0].scatter(x1, y1, color = 'red')
    ax[0][1].scatter(x2, y2, color = 'red')
    ax[1][0].scatter(x3, y3, color = 'red')
    ax[1][1].scatter(x4, y4, color = 'red')

    ax[0][0].plot(t, y, color = 'darkblue', label = 'f(x)')
    ax[0][1].plot(t, y, color = 'darkblue', label = 'f(x)')
    ax[1][0].plot(t, y, color = 'darkblue', label = 'f(x)')
    ax[1][1].plot(t, y, color = 'darkblue', label = 'f(x)')

    ax[0][0].plot(t, p1(t), color = 'black', label = 'p(x)', linestyle = '--')
    ax[0][1].plot(t, p2(t), color = 'black', label = 'p(x)', linestyle = '--')
    ax[1][0].plot(t, p3(t), color = 'black', label = 'p(x)', linestyle = '--')
    ax[1][1].plot(t, p4(t), color = 'black', label = 'p(x)', linestyle = '--')

    ax[1][0].set_xlabel('x')
    ax[1][1].set_xlabel('x')
    
    ax[0][0].set_title('n = 3')
    ax[0][1].set_title('n = 5')
    ax[1][0].set_title('n = 10')
    ax[1][1].set_title('n = 20')

    ax[0][0].legend()

    plt.show()

    t = np.linspace(-1,1,100)
    plt.plot(t, (chebyshev_polynomials(0))(t), label = 'n=0', 
             linestyle = '--')
    plt.plot(t, (chebyshev_polynomials(1))(t), label = 'n=1', 
             linestyle = '-.')
    plt.plot(t, (chebyshev_polynomials(2))(t), label = 'n=2', 
             linestyle = ':')
    plt.plot(t, (chebyshev_polynomials(3))(t), label = 'n=3', 
             linestyle = '-')
    plt.plot(t, (chebyshev_polynomials(4))(t), label = 'n=4')
    plt.legend()
    plt.show()


    t = np.linspace(-1,1,100)
    y = f(t)
    p, x1, y1 = polynomial_interpolation(20, chebyshev=True)

    plt.title('Interpolando com Zeros de Chebyshev (n = 20)')
    plt.scatter(x1,y1)
    plt.plot(t,y)
    plt.plot(t,p(t))
    plt.show()