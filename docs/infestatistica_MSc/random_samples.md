# Amostras aleatórias

**Definição:** As variáveis aleatórias $X_1, \dots, X_n$ formam uma **amostra aleatória** de tamanho $n$ se elas são mutualmente independentes e a densidade marginal de cada uma é a mesma $f(x)$, isto é, elas são independentes e identicamente distribuídas (i.i.d.).

O conceito de amostra aleatória corresponde à realização de experimentos repetidos que se originam do mesmo processo gerador. 
Além disso, uma hipótese comum é de que os efeitos de um experimento não influenciam os seguintes. 
Em certas situações, isso não é verdadeiro, mas pode ser uma simplificação razoável, pois, nesse caso, a densidade conjunta das variáveis $X_1, \dots, X_n$ é dada por 
$$
f(x_1, \dots, x_n) = \prod_{i=1}^n f_i(x_i) = \prod_{i=1}^n f(x_i),
$$
dada a independência na primeira igualdade, e a mesma distribuição na segunda.

**Estatística:** Seja $X_1, \dots, X_n$ uma amostra aleatória e considere a função $T : \mathcal{X}^n \to \mathbb{R}^m$.
A variável aleatória $Y = T(X_1, \dots, X_n)$ é chamada de **estatística** e a distribuição de probabilidade de $Y$ é chamada de **distribuição amostral** de $Y$.

Alguns exemplos são a **média amostral**, a **variância amostral** e o **desvio padrão amostral**, denotados por, respectivamente,
$$
\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 \text{ e } S = \sqrt{S^2}.
$$

## Estatística de Ordem

A estatística de ordem de uma amostra aleatória $X_1, \dots, X_n$ são os valores aleatórios da amostra ordenados de forma ascendente e são denotados por $X_{(1)}, \dots, X_{(n)}$. 
Em particular, $X_{(1)} = \min_{1 \le i \le n} X_i$ e $X_{(n)} = \max_{1 \le i \le n} X_i$.
A **mediana amostral** é defina por
$$
M = \begin{cases}
    X_{(n+1)/2} &\text{se } n \text{ é ímpar} \\
    (X_{n/2}+X_{n/2+1})/2 &\text{se } n \text{ é par} 
\end{cases}
$$

**Teorema:** Seja $X_{(1)}, \dots, X_{(n)}$ uma estatística de ordem de uma amostra aleatória $X_1, \dots, X_n$ de uma população contínua com CDF (ou FDA) $F_X(x)$ e densidade $f_X(x)$. 
Então a densidade marginal de $X_{(j)}$ é dada por
$$
f_{X(j)}(x) = \frac{n!}{(j-1)!(n-j)!}f_X(x)[F_X(x)]^{j-1}[1-F_X(x)]^{n-j}.
$$
Além do mais, 
$$
f_{X_{(1)}, \dots, X_{(n)}}(x_1, \dots, x_n) = n!f(x_1)f(x_2)\cdots f(x_n), 
$$
quando $x_1 < x_2 < \dots < x_n$ e $0$ caso contrário.