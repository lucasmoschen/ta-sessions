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

Existem algumas formas de verificar esse resultado usando alguns resultados da
literatura. De forma geral para métodos iterativos, podemos fazer:

(i) Mostrar que a matriz do método $T = -(D + L)^{-1}U$ tem o maior autovalor
em módulo é menor do que 1. Seja $x$ autovetor de $T$ cujo autovalor
correspondente é $\lambda$. Assim $-(D+L)^{-1}Ux = \lambda x \implies -Ux =
\lambda(D+ L)x$. De fato, teríamos que $||U||||x|| \ge |\lambda|||(D+L)x||$
para todo autovetor $x$, que pode ser considerado de norma 1. Assim, se
conseguíssemos mostrar que $||U||/||(D+L)x|| < 1$ para todo autovetor $x$,
teríamos que $\rho(T) < 1$. Se tomarmos a norma máximo, é fácil ver que $||U||
= 6$. Será que é fácil mostrar que $||(D+L)x|| > 6$? Eu acredito que não. Para
isso teríamos que encontrar o formato dos autovalores, pois, de forma geral,
se $x$ é um vetor qualquer, essa desigualdade não é observada. 

(ii) Mostrar que $||T|| = ||(D+L)^{-1}U|| < 1$ para alguma norma induzida.
Infelizmente, isso também não parece trivial de se fazer, mesmo sabendo que a
inversa de uma matriz triangular inferior é triangular inferior. 

(iii) A matriz $A$ é estritamente diagonalmente dominante: isso não é verdade para
essa matriz.

(iv) A matriz $A$ é irredutivelmente diagonalmente dominante: aqui precisamos
mostrar que ela é diagonalmente dominante (o que de fato é, pois a diagonal é
4, enquanto ou outros elementos da mesma linha são no máximo quatro valores
-1) e que pelo menos uma linha vale a desigualdade estrita, o que vale para a
primeira linha. Assim já provamos que vale a convergência de Gauss-Seidel.
Para verificar esse teorema, [esse
artigo](https://www.jstor.org/stable/2132758?seq=4#metadata_info_tab_contents)
pode ser um bom início. 

(v) A matriz $A$ é positiva definida. Provamos que se $0 < \omega < 2$, o
método SOR converge nesse caso. Como Gauss-Seidel é um casso particular
$\omega = 1$, basta verificar a positividade. Um bom material nesse sentido é
[esse
aqui](https://www.uio.no/studier/emner/matnat/ifi/nedlagte-emner/INF-MAT3350/h07/undervisningsmateriale/chap9slides.pdf).
Nesse caso, procurar os autovalores de $A$ (que têm um formato bem
conveniente) e mostrar que eles são positivos é uma boa. 

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
necessárias para que o erro na norma $\infty$ seja $\le 10^{-6}$. Comente
sobre os resultados obtidos.**

A implementação desse problema pode ser encontrado na [pasta do
repositório](https://github.com/lucasmoschen/ta-sessions/tree/master/Numerical_Analysis/lists/list2).

Vamos lembrar que a iteração do método SOR é dada por 
$$
x_i^{(k)} = (1 - \omega)x_{i}^{(k-1)} + \frac{\omega}{a_{ii}}\left[b_i -
\sum_{j-1}^{i-1} a_{ij}x_j^{(k)} - \sum_{j=i+1}^n a_{ij}x_{j}^{(k-1)} \right]
$$

Para essa matriz em particular, temos uma estrutura interessante. Observe que
para linha $i$ temos: 

- Um valor 4 na diagonal, isto é, $a_{ii} = 4$. 
- Um valor -1 à esquerda de 4 (exceto na primeira linha de cada $T$), isto é,
  $a_{i,i-1} = -1$ se $i \neq 1 \mod m$. 
- Um valor -1 à direita de 4 (exceto na última linha de cada $T$), isto é,
  $a_{i,i+1} = -1$ se $i \neq -1 \mod m$.
- Um valor -1 na identidade ao lado esquerdo de $T$, isto é,
  $a_{i,i-m} = -1$ se $i > m$. 
- Um valor -1 na identidade ao lado direito de $T$, isto é,
  $a_{i,i+m} = -1$ se $i + m \le m^2$. 

A iteração se reduz a 
$$
x_i^{(k)} = (1 - \omega)x_{i}^{(k-1)} + \frac{\omega}{4}\left[b_i +
x_{i-1}^{(k)} + x_{i-m}^{(k)} + x_{i+1}^{(k-1)} + x_{i+m}^{(k-1)} \right],
$$
com as restrições já citadas a cima. 

Além disso, $b$ também tem uma estrutura bem particular que pode ser também utilizada. Multiplicando pelo
vetor com só valores 1 faz com que somemos as linhas. O que fazemos então é
subtrair de 4 o número de condições verdadeiras: $i \neq 1 \mod m$, $i \neq -1
\mod m$, $i > m$, e $i \le m^2 - m$. 

Uma visualização interessante do processo que podemos ter é sobre o vetor $x$.
Ele é um vetor em $\mathbb{R}^{m^2}$. Porém podemos imagina-lo como uma matriz
$\mathbb{R}^{m \times m}$. Nesse caso se $j = mq + r$, dizemos que $x_j =
x_{q+1,r}$ a menos que $j = mq$. Nesse caso $x_j = x_{q,m}$. Com essa
estrutura, veja que $x_{i-m}$ fica na mesma coluna de $x_i$, mas uma linha
acima. Isso nos permite escrever 

$$
x_{i,j}^{(k)} = x_{i,j}^{(k-1)} + \frac{\omega}{4}\left[x_{i, j-1}^{(k)} +
x_{i-1,j}^{(k)} + x_{i,j+1}^{(k-1)} + x_{i+1,j}^{(k-1)} + b_{i,j} - 4x_{i,j}^{(k-1)}\right],
$$
e as condições se restringem a condições de borda (isto é, $1 \le i,j \le m$).
Do jeito que calculamos agora, não é possível paralelizar o cálculo. Para
fazer isso, uma estratégia é montar o [Grid
Red-Black](https://www.bu.edu/tech/support/research/training-consulting/online-tutorials/mpi/alliance/solvers/#:~:text=A%20Parallel%20SOR%20Red-black%20Scheme).

Esse problema é muito custoso quando $m$ cresce. Em particular, colocando
$x_0$ a uma distância de Normal(0, sd = 0.01), para fazer a seguinte figura,
levou 11s. Porém, para $m = 1000$, esse tempo já foi muito superior. 

![](exercise1.png)
 
## Outras questões da lista

[Métodos iterativos para sistemas de equações lineares](/files/disciplines/numerical-analysis/lista2.pdf)