#!usr/bin/env python 

# https://people.eecs.berkeley.edu/~demmel/cs267/lecture24/lecture24.html

import numpy as np 
from scipy import sparse
import time
from numba import jit, prange, njit
import matplotlib.pyplot as plt

from tqdm import tqdm

class PoissonMatrix: 

    def __init__(self, m, value = 4, b = None):
        """
        Class with the objective to solve Ax = b with a very specific format 
            ⌈ T  -I        		 n    ⌉
            |-I   T  -I				  |
            |    -I   T  -I			  |
            |						  |
        A = |		    dots		  |
            |		       dots       |
            |						  |
            |					 	-I|
            ⌊ 					-I   T⌋ 
        with I equal identity in R^(m x m) and T in R^(m x m) such that
            ⌈value -1        			  ⌉
            |-1   value  -1				  |
            |    -1   value  -1			  |
        T = |		    dots	     	  |
            |		       dots           |
            |					 	    -1|
            ⌊ 					 -1  value⌋ 
        If b is None it takes b = A[2,2,...,2,2].
        """
        self.v = value
        self.m = m
        if b is None: 
            self.b = self.calculate_b()
        else: 
            self.b = b

    def calculate_b(self, matrix_form = True): 
        """
        Calculate b according to b = A[2,2,...,2,2].
        Not ready for other values of T matrix. 
        """
        if matrix_form: 
            b = np.zeros(shape= (self.m, self.m))
            b[:,[0,-1]] += 2
            b[[0,-1],:] += 2
        else: 
            b = np.array([2 if (i % self.m == 1) or (i % self.m == self.m-1) else 0 
                        for i in range(self.m**2)])
            b[0:self.m] += 2
            b[-self.m:] += 2 
            
        return b

    def generate_A(self):
        """
        Create the A matrix sparsely. 
        """
        row = []
        col = []
        data = []
        for i in range(self.m**2):
            row.append(i)
            col.append(i)
            data.append(4)
            if i - 1 >= 0 and i % self.m != 0:
                row.append(i)
                col.append(i - 1)
                data.append(-1)
            if i + 1 < self.m**2 and i % self.m != (self.m - 1):
                row.append(i)
                col.append(i + 1)
                data.append(-1)
            if i - self.m >= 0:
                row.append(i)
                col.append(i - self.m)
                data.append(-1)
            if i + self.m < self.m**2:
                row.append(i)
                col.append(i + self.m)  
                data.append(-1)        
        A = sparse.csr_matrix((data, (row, col)), shape = (self.m**2, self.m**2))
        return A

@jit(nopython=True)
def sor_method(x0, m, b, target = 1e-6, omega = None):
    """
    Solves the system Ax = b through SOR method
    x(i,j)^(k+1) = x(i,j)^k +
                w * ( x(i-1,j)^(k+1) + x(i+1,j)^(k) + 
                        x(i,j-1)^(k+1) + x(i,j+1)^(k) + b(i,j) 
                        - 4*x(i,j)^(k))/4,
    where w is the omega parameter. 
    """
    if omega is None: 
        omega = 2/(1 + np.sin(np.pi/(m+1)))

    x = np.zeros((m+2, m+2))
    for i in range(1, m+1): 
        x[i, 1:m+1] = x0[m*(i-1):m*i] 

    iter = 0 

    error = [1]
    append = error.append

    while error[-1] > target and iter <= 1000*m: 
        
        error_iter = 0
        iter += 1
        for i in range(1, m+1): 
            for j in range(1, m+1): 
                x[i,j] += (omega/4)*(b[i-1,j-1] + x[i-1,j] + x[i,j-1] + x[i+1,j] + x[i,j+1] - 4*x[i,j])

                e = np.abs(x[i,j] - 2)
                if  e > error_iter: 
                    error_iter = e

        append(error_iter)

    return (iter, error, x)

def sor_red_black_method(x0, m, b, target = 1e-6, omega = None):
    """
    Solves the system Ax = b through SOR method considering the Red-Black
    structure, that is separetes the black and red points. 
    x(i,j)^(k+1) = x(i,j)^k +
                w * ( x(i-1,j)^(k+1) + x(i+1,j)^(k) + 
                        x(i,j-1)^(k+1) + x(i,j+1)^(k) + b(i,j) 
                        - 4*x(i,j)^(k))/4,
    where w is the omega parameter. 
    """
    if omega is None: 
        omega = 2/(1 + np.sin(np.pi/(m+1)))

    x = np.zeros((m+2, m+2))
    for i in range(1, m+1): 
        x[i, 1:m+1] = x0[m*(i-1):m*i] 

    iter = 0 

    error = [1]
    append = error.append

    while error[-1] > target and iter <= 1000*m: 
        
        error_iter = 0
        iter += 1

        # Each of these steps can be parallelized. Future work. 
        x, error_iter = separate_points(x, m, error_iter, red=0)
        x, error_iter = separate_points(x, m, error_iter, red=1)

        append(error_iter)

    return (iter, error, x) 

def separate_points(x, m, error_iter, red): 

    for i in range(1, m+1): 
        for j in prange(1, m+1):
            if i + j % 2 == red:  
                x[i,j] += (omega/4)*(b[i-1,j-1] + x[i-1,j] + x[i,j-1] + x[i+1,j] + x[i,j+1] - 4*x[i,j])
                e = np.abs(x[i,j] - 2)
                if  e > error_iter: 
                    error_iter = e
            else: 
                continue

    return x, error_iter

if __name__ == '__main__': 

    ms = [20, 50, 100, 150]
    omegas = [1, 1, 1/2]

    fig, ax = plt.subplots(2,2,figsize = (12,8))

    for n, m in tqdm(enumerate(ms), desc = 'sizes'): 

        experiment = PoissonMatrix(m)
        b = experiment.calculate_b(matrix_form=True)
        x0 = np.random.normal(2, 0.01, size = m**2)

        for omega in tqdm(omegas, desc = 'omegas', position = 1, leave = False): 
            t0 = time.time()
            iter, error, _ = sor_method(x0, m, b, omega = omega)
            if omega is None: 
                omega = 'ótimo'
            ax[n//2,n%2].plot(error, label = r"$\omega$ = {}".format(omega))

        ax[n//2,n%2].legend()
        ax[n//2,n%2].set_title("Comparison for m = {}".format(m))
        ax[n//2,n%2].set_xscale('log')
        ax[n//2,n%2].set_yscale('log')

    plt.show()