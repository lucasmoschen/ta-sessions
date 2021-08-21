#!urs/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def iterative_process(x0, x1, n):

    x = np.zeros(n)
    x[0] = x0
    x[1] = x1
    for i in range(2,n):
        x[i] = (22*x[i-1] - 3*x[i-2])/7

    return x

def direct_solution(x0, x1, n): 

    A = (7*x1 - x0)/20
    B = (21*x0 - 7*x1)/20

    x = np.array([A*3**i + B*7**(-i) for i in range(n)])

    return x

x0 = 1
x1 = 1/7
n = 40

x_ite = iterative_process(x0, x1, n)
x_dir = direct_solution(x0, x1, n)

plt.plot(range(n), x_ite, label = 'Iterative solution')
plt.plot(range(n), x_dir, label = 'Direct solution')
plt.title('Solution to the iterative process')
plt.legend()
plt.savefig('image_exercise5.png', bbox_inches = 'tight')
plt.show()