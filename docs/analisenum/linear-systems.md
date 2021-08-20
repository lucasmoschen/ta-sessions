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
converge para o ponto fixo $x^* = Cx* + D$ se, e somente se, $\rho(C) < 1$,
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


## Método de Gauss-Seidel