#!usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt

def bissection_method(function, interval, error): 

    a = interval[0]
    b = interval[1] 

    assert np.sign(function(a)) * np.sign(function(b)) < 0

    a_k, b_k = a, b

    number_iterations = int((np.log((b-a)/error)/np.log(2))) + 1
    x = np.zeros(number_iterations)

    for k in range(number_iterations): 

        x[k] = (a_k + b_k)/2
        if function(x[k]) == 0: 
            x = x[:k+1]
            break
        if np.sign(function(x[k])) * np.sign(function(a_k)) < 0:
            a_k, b_k = a_k, x[k]
        else: 
            a_k, b_k = x[k], b_k
    return x

def regula_falsi_method(function, interval, error, d, max_number_iterations): 
    """
    For this regula-falsi implementation, we suppose that it's known |f'(x)| >
    d for all x in the interval. 
    """

    a = interval[0]
    b = interval[1] 

    assert np.sign(function(a)) * np.sign(function(b)) < 0

    a_k, b_k = a, b
    x = []
    m = 0

    while m <= max_number_iterations:  

        f_a_k, f_b_k = function(a_k), function(b_k)
        x_k = (a_k * f_b_k - b_k * f_a_k)/(f_b_k - f_a_k) 
        if abs(function(x_k)) <= error * d: 
            x.append(x_k)
            break 
        elif np.sign(function(x_k)) * np.sign(function(a_k)) < 0:
            a_k, b_k = a_k, x_k
        else: 
            a_k, b_k = x_k, b_k
        x.append(x_k)

        m += 1
        
    return x

def newton_method(function, derivative, x0, error, max_number_iterations):

    xn = x0
    x = []
    for _ in range(0,max_number_iterations):
        fxn = function(xn)
        x.append(xn)
        if abs(fxn) < error:
            return x
        Dfxn = derivative(xn)
        assert Dfxn != 0
        
        xn = xn - fxn/Dfxn

    raise('INFO - Exceeded maximum iterations. No solution found.')

def fixed_point_method(function, x0, error, L):
    """
    This implementation needs the calculation of the Lipschitz constant L.
    """
    x1 = function(x0) 
    number_iterations = int((np.log(error) + np.log(1-L) - np.log(abs(x1 - x0))) / np.log(L)) + 1
    
    x = [x0,x1]
    
    for _ in range(number_iterations-1):
        x.append(function(x[-1]))

    return x

if __name__ == '__main__': 

    print('--------- Paper sheet 3 ----------')
    print('Do you want to see the plots?')
    while True: 
        ans = input('[y/n]')
        if ans == 'y':
            plot = True
            break
        elif ans == 'n':
            plot = False
            break

    print('INFO - Exercise 1')
    print('INFO - Bissection method: f(x) = (x)^(1/2) * sin(x) - x^3 + 2')

    interval = [1,2]
    error = 1/30 
    function = lambda x: np.sqrt(x) * np.sin(x) - x**3 + 2

    x = bissection_method(function, interval, error)
    print('INFO - The solution is: {}'.format(x[-1]))
    print('INFO - The number of iterations is: {}'.format(len(x)))

    if plot: 
        t = np.linspace(0,2,100)
        plt.plot(t, function(t), color = 'black')
        plt.scatter(x, np.zeros_like(x), color = 'red',  
                    alpha = np.linspace(0.1, 1, len(x)), s = 20)
        plt.title('Bissection method')
        plt.axhline(0, linestyle = '--', color = 'grey')
        plt.show()

    print('INFO - Exercise 4')
    print('INFO - Regula-falsi method: f(x) = x^3 + 2x^2 + 10x - 20')

    interval = [0,2]
    error = 1e-5
    d = 10
    function = lambda x: x**3 + 2*x**2 + 10*x - 20
    max_number_iterations = 1000

    x = regula_falsi_method(function, interval, error, d, max_number_iterations)
    print('INFO - The solution is: {}'.format(x[-1]))
    print('INFO - The number of iterations is: {}'.format(len(x)))

    if plot: 
        t = np.linspace(0,2,100)
        plt.plot(t, function(t), color = 'black')
        plt.scatter(x, np.zeros_like(x), color = 'red',  
                    alpha = np.linspace(0.1, 1, len(x)), s = 20)
        plt.title('Regula-falsi method')
        plt.axhline(0, linestyle = '--', color = 'grey')
        plt.show()

    print('INFO - Exercise 5')
    print('INFO - Newton method: f(x) = cos(x) - x^2')

    x0 = 1
    error = 1e-5
    function = lambda x: np.cos(x) - x**2
    derivative = lambda x: - np.sin(x) - 2*x
    max_number_iterations = 1000

    x = newton_method(function, derivative, x0, error, max_number_iterations)
    print('INFO - The solution is: {}'.format(x[-1]))
    print('INFO - The number of iterations is: {}'.format(len(x)))

    if plot: 
        t = np.linspace(-0.5,1.5,100)
        plt.plot(t, function(t), color = 'black')
        plt.scatter(x, np.zeros_like(x), color = 'red',  
                    alpha = np.linspace(0.1, 1, len(x)), s = 20)
        plt.title('Newton method')
        plt.axhline(0, linestyle = '--', color = 'grey')
        plt.show()

## I STOPPED HERE

    print('INFO - Exercise 6')
    print('INFO - Fixed point method: log(15 - log(x)) - x')

    x0 = 2
    error = 1e-5
    function = lambda x: np.log(15 - np.log(x))
    L = np.exp(-1)

    x = fixed_point_method(function, x0, error, L)
    print('INFO - The solution is: {}'.format(x[-1]))
    print('INFO - The number of iterations is: {}'.format(len(x)))

    if plot: 
        t = np.linspace(0.5,3,100)
        plt.plot(t, function(t) - t, color = 'black')
        plt.scatter(x, np.zeros_like(x), color = 'red',  
                    alpha = np.linspace(0.1, 1, len(x)), s = 20)
        plt.title('Fixed point method')
        plt.axhline(0, linestyle = '--', color = 'grey')
        plt.show()