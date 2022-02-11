# Decomposição LU

Fatorização de uma matriz $A$ como um produto $P\cdot A = L\cdot U$, onde a primeira matrix é triangular inferior (lower), enquanto a segunda é triangular superior (upper). A matriz $P$ é uma matriz de permutação que garante a existência dessa fatorização. 


```python
import scipy.linalg
```


```python
A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
print(A)
```

    [[ 7  3 -1  2]
     [ 3  8  1 -4]
     [-1  1  4 -1]
     [ 2 -4 -1  6]]



```python
P, L, U = scipy.linalg.lu(A)
print(P), print(L), print(U)
```

    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]]
    [[ 1.          0.          0.          0.        ]
     [ 0.42857143  1.          0.          0.        ]
     [-0.14285714  0.21276596  1.          0.        ]
     [ 0.28571429 -0.72340426  0.08982036  1.        ]]
    [[ 7.          3.         -1.          2.        ]
     [ 0.          6.71428571  1.42857143 -4.85714286]
     [ 0.          0.          3.55319149  0.31914894]
     [ 0.          0.          0.          1.88622754]]





    (None, None, None)


