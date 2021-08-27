# Métodos iterativos para resolver sistemas lineares 

Suponha que queremos resolver um problema do tipo $Ax = b$, em que $A$ é uma
matriz real $n \times n$ e $b$ é um vetor em $\mathbb{R}^n$. Matematicamente,
se estamos interessados em encontrar $x$, podemos apenas calcular a inversa de
$A$, caso exista. Se sim $x = A^{-1}b$. Apesar de ser fácil de calcular, esse
procedimento precisa fazer $O(n^3)$ operações, o que pode ser muito custoso
quando $n$ aumenta.  Nesse caso, precisamos de alternativas mais palatáveis
para resolver esse problema, principalmente para $n$ grande. Utilizamos
métodos iterativos para ajudar!

De forma geral, vamos querer reescrever o problema da forma: 
$$
x = Cx + D, 
$$
em que são matrizes. Se conseguirmos expressar $Ax = b$ dessa forma, estaremos
interessados nos pontos fixos do operador $L(x) = Cx + D$. 

**Teorema:** O processo iterativo $x^{k+1} = Cx^k + D$ satisfaz o seguinte:
Para todo valor inicial $x^0$, a sequência $\{x^k\}_{k \in \mathbb{N}}$
converge para o ponto fixo $x^* = Cx^* + D$ se, e somente se, $\rho(C) < 1$,
em que $\rho(C)$ é o raio espectral da matriz $C$, isto é, o maior autovalor
em módulo. 

Uma demonstração desse resultado pode ser encontrado no livro de Richard
L.Burden *Numerical Analysis* (página 457).

**Corolário:** Se $||C|| < 1$ para qualquer norma matricial induzida (induzida
por uma norma vetorial), então a
iteração anterior converge para o ponto fixo do operador $L$ para qualquer
chute inicial $x^0$. Esse resultado é uma consequência de $\rho(A) \le ||A||$
para todo norma natural $||\cdot||$. 

- Método de Jacobi
- Método de Gauss-Seidel
- Método Successive Over-Relaxation (SOR)
- Método Gradiente Conjugado

**Teorema:** Se $A$ é diagonalmente estritamente dominante, então para
qualquer escolha de $x^0$, os métodos de Jacobi e Gauss-Seidel convergem. 

## Método de Jacobi

Esse método é derivado resolvendo a $i$th equação de $Ax = b$ para $x_i$ (dado
que $a_{ii} \neq 0$)

$$
x_i = \sum_{j\neq i} \left(-\frac{a_{ij}x_j}{a_{ii}}\right) +
\frac{b_i}{a_{ii}}, ~~~ \text{ for } i = 1, 2, \dots, n.
$$

Assim, geramos iterativamente, 

$$
x_i^{(k)} = \frac{1}{a_{ii}} \left[ \sum_{j\neq i} \left(-a_{ij} x_j^{(k-1)}\right) + b_i\right]
$$

Vamos escrever em formato matricial. Observe que 


$$
x^{(k)} = \begin{bmatrix}
    0 & -a_{12}/a_{11} & -a_{13}/a_{11} & \dots & -a_{1n}/a_{11} \\
    -a_{21}/a_{22} & 0 & -a_{23}/a_{22} & \dots & -a_{2n}/a_{22} \\
    -a_{31}/a_{33} & -a_{32}/a_{33} & 0 & \dots & -a_{3n}/a_{33} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    -a_{n1}/a_{nn} & -a_{n2}/a_{nn} & -a_{n3}/a_{nn} & \dots & 0\\
\end{bmatrix}x^{(k-1)} + \begin{bmatrix}
    b_1/a_{11} \\ b_2/a_{22} \\ b_3/a_{33} \\ \vdots \\ b_n/a_{nn}
\end{bmatrix}
$$

e sendo $U$ e $L$ as matrizes triangulares superiores e inferiores, e $D$ a
matriz diagonal de $A$,

$$
x^{(k)} = -D^{-1}(L + U)x^{(k-1)} + D^{-1}b
$$

Assim, o procedimento Jacobi pode ser sumarizado da seguinte forma: 

- Sejam as entradas as matrizes $A$ e $b$ com uma aproximação inicial
  $x^{(0)}$. Defina uma tolerância para o critério de parada. 
- Realize a iteração até o critério de parada.
- Lembre de pré-calcular as matrizes $D^{-1}(L + U)$ e $D^{-1}b$. 

*Observação:* Na notação do livro, troca-se $L$ e $U$ por $-L$ e $-U$ para não
aparecer o sinal na expressão acima. 

**Acelerar a convergência:** Colocar $a_{ii}$ o máximo possível acelera a
convergência do método. 

## Método de Gauss-Seidel

Observe que quando iteramos o processo no método de Jacobi, fixamos
$x^{(k-1)}$ e fazemos a operação $x^{(k)}$. Por esse motivo, podemos utilizar
os valores já calculados $x_1^{(k)}, \dots, x_{i-1}^{(k)}$ para atualizar
o valor de $x_i^{(k)}$. Assim

$$
x_i^{(k)} = \frac{1}{a_{ii}} \left[ -\sum_{j=1}^{i-1} \left(a_{ij}
x_j^{(k)}\right) - \sum_{j=i+1}^{n} \left(a_{ij}
x_j^{(k-1)}\right) + b_i\right]
$$

Essa simples modificação gerou o método de Gauss-Seidel. Para obter essa
equação em formato matricial, precisamos de 

$$
\sum_{j=1}^{i} \left(a_{ij}
x_j^{(k)}\right) = - \sum_{j=i+1}^{n} \left(a_{ij}
x_j^{(k-1)}\right) + b_i
$$

Note que para cada linha $i$, estamos tomando todas as colunas $j \le i$ no
lado esquerdo. No lado direito é o contrário. Assim, 

$$
(D + L)x^{(k)} = Ux^{(k-1)} + b \implies x^{(k)} = -(D+L)^{-1}Ux^{(k-1)} + (D +
L)^{-1}b
$$

O processo iterativo é similar ao Método de Jordan. 

**Teorema (Stein-Rosenberg):** Se $a_{ij} \le 0$ para cada $i \neq j$ e
$a_{ii} > 0$, para cada $i=1,2,\dots,n$, então uma, e somente uma, das
afirmações vale: 

**(i)** $0 \le \rho(T_g) < \rho(T_j) < 1$;

**(ii)** $1 < \rho(T_j) < \rho(T_g)$;

**(iii)** $\rho(T_g) = \rho(T_j) = 0$;

**(iv)** $\rho(T_g) = \rho(T_j) = 1$, 

em que $T_j = -D^{-1}(L+U)$ e $T_g = -(D+L)^{-1}U$ são as matrizes dos métodos
de Jacobi e Gauss-Seidel. 

## Método Successive Over-Relaxation (SOR)