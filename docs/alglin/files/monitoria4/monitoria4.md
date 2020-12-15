# Monitoria 4

---

## Tópicos já estudados 

- Matrizes e suas propriedade
     - Notação
     - Operações com matrizes e suas propriedades
     - A transposta e suas propriedades: $(AB)^T = B^TA^T$
     - Simétrica e Antissimétrica: $(A + A^T)$ é simétrica e $(A - A^T)$ é antissimétrica, $\forall A$. 
     - A inversa, quando existe, e suas propriedades
     - Método para obtenção da inversa utilizando matrizes elementares
     - Matrizes em outros conjuntos, como $Z_5$. 
     - Matriz singular: matriz não invertível.
     - Decomposição LU
     
     
- Sistemas Lineares e sua representação matricial
     - Escalonamento: método de Gauss e método de Gauss-Jordan
     - A é equivalente a B se, e só se, existe uma sequência de operações elementares que transformam A em B.
     - Posto de uma matriz e grau de liberdade (Teorema do Posto)
     - Posto (rank em inglês) pode ser definido como a dimensão do espaço linha ou a dimensão do espaço coluna de uma matriz.
     - Sistema homogêneo: sempre existe solução (trivial)
     - $Posto(A) = Posto(A^T)$
     - Matrizes Elementares: representantes matriciais das três operações elementares, trocar linha, multiplicação por constante e somar a linha a um múltiplo de outra linha
     - Matriz Completa: $[A|b]$
     
     
- Espaços Vetorias e vetores
    - Combinação Linear de vetores
    - O produto escalar -> módulo 
    - Projeção: $\vec{z} = \frac{\vec{v}\cdot\vec{u}}{\vec{u}\cdot\vec{u}}\cdot u$
    - Desigualdade de Cauchy-Schwarz e cosseno: $\|u\|\|v\| \geq \|u\cdot v\|$ 
    - Conjuntos geradores: $S = \{v_1,v_2,...,v_k\} \subset\mathbb{R}^n$. O conjunto de todas as combinações dos elementos de S é $ger(S)$. 
    - Depenência: um conjunto é linearmente dependente se um vetor do conjunto pode ser escrito como combinação linear de outros. Independente, caso contrário. Lembrar que se $\alpha_1\vec{v_1} + \alpha_2\vec{v_2} + ... + \alpha_k\vec{v_k} = 0 \implies \alpha_1 = \alpha_2 = ... = \alpha_k = 0$, o conjuntos dos vetores é linearmente independente. 
    - Espaços vetorias dotam-se de: comutatividade e associatividade da soma, existência do nulo e da identidade, existência do simétrico, distribuitividade com real. 
    - Subespaços vetoriais: tem o vetor nulo e a soma e produto por real são fechados.
    - Subespaços associados a matrizes: 
        - Espaço linha: conjunto gerado por suas linhas: $lin(A) = ger(\{L_1,L_2,...,L_m\})$
        - Espaço coluna: conjunto gerado por suas colunas: $col(A) = ger(\{c_1,c_2,...,c_m\})$
    - Espaço anulado por uma matriz: Também chamado de núcleo, é o conjunto solução do sistema $Ax = 0$
    - Bases de um espaço vetorial: É um conjunto LIque gera um espaço vetorial --- Próxima monitoria


```python
import numpy as np
import scipy as sp
import scipy.linalg as splin
import sympy as sc
```

## Exercícios

### Exemplo 1.4: Espaços Vetorias

Seja $X$ um conjunto não vazio. O símbolo $\mathbb{F}(X;\mathbb{R})$ representa o conjunto das funções reais $f,g: X \to \mathbb{R} $. Defino a soma: $f + g$ como $(f + g)(x) = f(x) + g(x)$ e o produto $\alpha\cdot f$ como $(\alpha f)(x) = \alpha\cdot f(x)$

### Exercício 2.13: Combinação Linear

Mostre que a matriz $d = \begin{pmatrix} 4 & -4 \\ -6 & 16 \end{pmatrix}$ pode ser escrita como combinação linear das matrizes:
$$
a = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, b = \begin{pmatrix} -1 & 2 \\ 3 & -4\end{pmatrix},  
c =\begin{pmatrix} 1 & -2 \\ -3 & 4 \end{pmatrix}
$$

### Exemplo: Subespaços

Seja $P_4$ o espaço vetorial de todos os polinômios de grau 4 ou menos com coeficientes reais. A soma e o produto por real são definidos naturalmente. $S_5$ é um subespaço? 
$$S_5 = \{f(x) \in P_4 \| f(1)~ is~ a ~rational~ number\}$$

### Questão Teste 2: Operações com matrizes

A matriz $A = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. Questão: $\exists n \in \mathbb{N}$, tal que $A^n = A$? 

Obs.: Observe que $\frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$, e se eu tratar $\theta = \frac{\pi}{4}$, temos que $A$ é matriz de rotação. Logo, basta encontrar $n$ tal que $n\cdot\frac{\pi}{4} = k\cdot2\cdot\pi \to n = 8\cdot k \to n = 8$ é solução, logo $A^8 = I \to A^9 = A$

### Questão 2.37 

Dado $X \subset E$, seja $Y$ o conjunto obtido de $X$ substituindo um dos seus elementos $v$ por $v + \alpha u$, onde $u\in X$ e $\alpha \in \mathbb{R}$. Prove que X e Y geram o mesmo subespaço vetorial de $E$. Conclua, então que $\{v_1,...,v_k\} \subset E$ e $\{v_1, v_2 - v_1, ..., v_k - v_1\} \subset E$ geram o mesmo subespaço vetorial de $E$. 

Alguém percebe a implicação prática dessa questão? 

1. Lembre que $S(Y)$ é o subespaço gerado por Y. 
2. Uma ajuda para desenvolver essa questão é reconhecer que $X \subset S(Y) \implies S(X) \subset S(Y)$. Você consegue demonstrar? 

## Conjuntos Geradores 

$u_1 = (1,1,2,3)$

$u_2 = (2,-1,1,2)$

$\pi = ger(\{u_1, u_2\})$

$w = (-2,7,5,6) \in \pi$

Queremos saber se, $\exists ~\alpha, \beta$, tal que: 

$$\alpha \begin{pmatrix} 1 \\ 1 \\ 2 \\ 3 \end{pmatrix} + \beta 
\begin{pmatrix} 2 \\ -1 \\ 1 \\ 2 \end{pmatrix} = 
\begin{pmatrix} -2 \\ 7 \\ 5 \\ 6 \end{pmatrix}$$

## Teste 1 2018

### Exercício 1:

Escreva a seguinte matriz como a soma de uma matriz simétrica e uma antissimétrica:
$
A = \begin{pmatrix} 
4 & 6 & 3\\ -2 & 0 & 5 \\ 5 & -1 & 2 
\end{pmatrix}$

### Resolução

$$A = \frac{1}{2}((A + A^T) + (A - A^T))$$

Ora, mas $A + A^T$ e $A - A^T$ são simétrica e antissimétrica, respectivamente.

Logo:


```python
A = np.array([[4,6,3],[-2,0,5],[5,-1,2]])
A = sc.Matrix(A)
A_T = A.T
1/2*(A + A_T)
```




$$\left[\begin{matrix}4.0 & 2.0 & 4.0\\2.0 & 0 & 2.0\\4.0 & 2.0 & 2.0\end{matrix}\right]$$




```python
1/2*(A - A_T)
```




$$\left[\begin{matrix}0 & 4.0 & -1.0\\-4.0 & 0 & 3.0\\1.0 & -3.0 & 0\end{matrix}\right]$$



### Exercício 2:

Encontre a inversa da seguinte matriz e depois resolva $AX = B$:
$$
A = \begin{pmatrix} 
4 & 6 & 3\\ -2 & 0 & 5 \\ 5 & -1 & 2 
\end{pmatrix} \\
B = \begin{pmatrix} 
7 & 1 & 4\\ -5 & 2 & 4 \\ 9 & 3 & -1 
\end{pmatrix}
$$


### Resolução


```python
A = np.array([[4,6,3],[-2,0 , 5], [5, -1, 2]])
B = np.array([[7,1,4],[-5,2,5],[9,3,1]])
A_inv = np.linalg.inv(A)
X = np.matmul(A_inv,B)
sc.Matrix(A_inv)
```




$$\left[\begin{matrix}0.025 & -0.075 & 0.15\\0.145 & -0.035 & -0.13\\0.01 & 0.17 & 0.06\end{matrix}\right]$$




```python
sc.Matrix(X)
```




$$\left[\begin{matrix}1.9 & 0.325 & -0.125\\0.0199999999999999 & -0.315 & 0.275\\-0.24 & 0.53 & 0.95\end{matrix}\right]$$



### Exercício 3:

Resolva o sistema em $\mathbb{Z}_5$:

$$
\begin{pmatrix} 
4 & 1 & 3\\ 3 & 0 & 2 \\ 0 & 4 & 2 
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z 
\end{pmatrix} =
\begin{pmatrix}
1 \\ 2 \\ 4
\end{pmatrix}
$$

### Exercício 4:

Uma <b> rede </b> consiste em um número finito de <b> nós </b> conectados por <b> arestas </b>. Cada aresta é rotulada com um <b> fluxo </b>, que relaciona uma direção e uma quantidade. A regra fundamental é a <b> conservação de fluxo </b>, isto é, em cada nó, o fluxo de entrada é igual ao fluxo de saída. 

Considere a seguinte rede: 

<img src="rede.png">

Encontre os intervalos de $f_1, f_2, f_3, f_4$

### Exercício 5:

Faça a fatoração LU da matriz 

$$\begin{pmatrix} 1 & 2 & 4 \\ 3 & 8 & 14 \\ 2 & 6 & 13 \end{pmatrix}$$

### Resolução:


```python
A = sp.array([[1,2,4], [3,8,14], [2,6,13]])
P, L, U = sp.linalg.lu(A)
print("L:")
sc.Matrix(L)
```

    L:





$$\left[\begin{matrix}1.0 & 0.0 & 0.0\\0.666666666666667 & 1.0 &
0.0\\0.333333333333333 & -0.999999999999999 & 1.0\end{matrix}\right]$$


```python
print("U:")
sc.Matrix(U)
```

    U:

$$\left[\begin{matrix}3.0 & 8.0 & 14.0\\0.0 & 0.666666666666667 & 3.66666666666667\\0.0 & 0.0 & 3.0\end{matrix}\right]$$

### Curiosidades

1. O conjunto $H$ dos pontos $x = (x_1,...,x_n) \in \mathbb{R^n}$, tais que $a_1x_1 + ... + a_nx+n = b$ é uma <b> variedade afim </b>. Se $a_i$ não são todos nulos, $H$ é um hiperplano. 
2. Por que é necessário que $0 \in F$, sendo $F \subset E$ um subespaço? Essa condição pode ser alterada po outra? Sugestão: Demonstrar que essa condição pode ser alterada por $F \neq \emptyset$
3. Definição de segmento de reta: $[u,v] = \{(1 - t)\cdot u + t\cdot v ~; ~ 0 \leq t \leq 1\}$, sendo $u, v \in E$, espaço vetorial. 
