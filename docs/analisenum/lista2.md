# Lista 2 - Análise Numérica

**Escola de Matemática Aplicada, Fundação Getulio Vargas**

**Professor:** Hugo A. de la Cruz Cancino

**Monitor:** Lucas Machado Moschen

**Data da entrega:** 12/09/2021

1. Considere a matriz diagonal por blocos $A \in \mathbb{R}^{m^2 \times m^2}$
$$
A = \begin{bmatrix}
    T & -I & 0 & 0 & \dots & 0 \\
    -I & T & -I & 0 & \dots & 0 \\
    0 & -I & T & -I & \dots & 0 \\
    &&\dots&\dots&& \\
    0 & \dots & 0 & 0 & -I & T 
    \end{bmatrix}
$$
onde $I  \in \mathbb{R}^{m\times m}$ é a matriz identidade $T \in \mathbb{R}^{m\times m}$  é dada por
$$
T = \begin{bmatrix}
    4 & -1 & 0 & 0 & \dots & 0 \\
    -1 & 4 & -1 & 0 & \dots & 0 \\
    0 & -1 & 4 & -1 & \dots & 0 \\
    &&\dots&\dots&& \\
    0 & \dots & 0 & 0 & -1 & 4 
    \end{bmatrix}
$$

**(a) O método de Gauss-Seidel aplicado ao sistema $Ax = b (b \in R^m)$ é
convergente $\forall m \in N$ ? Justifique bem sua resposta.**

**(b) Uma boa escolha do parâmetro $\omega$ no método SOR pode levar a uma convergência mais rápida, comparado
com Jacobi e Seidel. Em geral determinar o valor ótimo de $\omega$ não é um problema fácil, mas em alguns
casos em que a matriz do sistema tem uma estrutura específica é possível achar esse valor ótimo $\omega$ ótimo.
Por exemplo, para a matriz $A$ acima é conhecido que**

$$
\omega_{\mathrm{otimo}} = \frac{2}{1 + \sin\left(\frac{\pi}{m+1}\right)}.
$$

**Implemente o método SOR para resolver o sistema $Ax = b$; onde $b$ é um vetor tal que o sistema tem a
solução exata $x = (2, 2, \dots, 2)$. Compare a performance do método SOR usando 4 valores diferentes
do parâmetro $\omega$:**

**i) $\omega = \omega_{\mathrm{otimo}}$** 

**ii) $\omega = 1$ (o método de Seidel)** 

**iii) $\omega = 0.5$**

**iv) $\omega = 0$,**

**para 4 valores diferentes de $m$: $m = 50, 100, 1000, 5000$. Como critério de comparação use o número de iterações
necessárias para que o erro na norma $\infty$ seja $\le 10^{-6}$. Comente sobre os resultados obtidos.**