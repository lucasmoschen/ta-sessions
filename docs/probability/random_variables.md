# Variáveis aleatórias

Formalmente, uma variável aleatória atribui um valor numérico a cada possível resultado de um experimento.
Em outras palavras, dado um espaço de probabilidade $(\Omega, \mathbb{A}, P)$, uma **variável aleatória** é uma função
\[
X : \Omega \to \mathbb{R}.
\]
Além disso, por questões técnicas, demandamos que $\{\omega \in Omega : X(\omega) \le x\} \in \mathbb{A}$ para todo $x \in \mathbb{R}$. 
Dizemos então que $X$ é **mensurável**.
Isso permite, por exemplo, que possamos calcular $F_X(x) = P(X \le x)$, o qual chamaremos de **função de distribuição acumulada** (FDA) de $X$.

A função de distribuição acumulada tem as seguintes propriedades:

1. **Não decrescente:** $x \le y \implies F_X(x) \le F_X(y)$.
2. **Continuidade a direita:** se $x_n \to x$ e $x_n \ge x$ para todo $n$, temos que $F_X(x_n) \to F_X(x)$.
3. **Limites:** $F_X(-\infty) = 0$ e $F_X(\infty) = 1$.

Essas propriedades podem ser demonstradas a partir das propriedades da probabilidade. 
Uma questão que surge é: se uma função satisfaz as propriedades 1,2 e 3, então ela é a FDA de alguma variável aleatória.
A resposta é sim! 
Portanto, podemos definir como **função de distribuição** as funções que satisfazem essas propriedades.
Para uma demonstração, consulte o Teorema 1.2.2 [daqui](https://www.ime.usp.br/~manuelg/arquivos/Probability%3A%20Theory%20and%20Examples%20-%20Durrett.pdf).

## Tipos de variáveis aleatórias

A variável aleatória $X$ é dita **discreta** se toma um número enumerável de valores.
Ela é dita absolutamente contínua se existe uma função $f(x) \ge 0$ tal que 
$$
F_X(x) = \int_{-\infty}^x f(t) \, dt, \forall x \in \mathbb{R}.
$$
A função $f$ é chamada de densidade de $X$.
Em Teoria da Medida, essa definição perde um pouco do valor, porque a FDA da discreta também pode ser escrita como uma integral, só que na medida de contagem, enquanto a absolutamente contínua na medida de Lebesgue.
Note que ao ter uma função $f(x) \ge 0$ com 
$$
\int_{-\infty}^{\infty} f(x) \, dx = 1,
$$
podemos definir uma função de distribuição (que satisfaz as três propriedades acima) da seguinte forma:
$$
F(x) = \int_{-\infty}^x f(t) \, dt.
$$
Em geral, $X$ tem densidade se $F_X$ é contínua e derivável no interior de um número enumerável de intervalos fechados cuja união é a reta.
Nesse caso, a derivada é a densidade de $X$, isto é, $f(x) = F'_X(x)$.

## A distribuição de uma variável aleatória

**Proposição:** Se $X$ é uma variável aleatória em $(\Omega, \mathbb{A}, \mathbb{P})$, então o evento 
$$
[X \in B] := \{\omega \in \Omega\}
$$
é evento aleatório para todo boreliano $B$, isto é, $[X \in B] \in \mathbb{A}$ para todo $B$ boreliano.

A demonstração dessa proposição vem do fato de que um boreliano é um conjunto que pode ser escrito como uma união contável, intersecção contável ou complemento de intervalos abertos da reta.
Esses conjuntos podem ser escritos como conjuntos do tipo $[X \le x]$, que sabemos que são eventos por definição de variável aleatória.

Definindo $P_X(B) = \mathbb{P}(X \in B)$, então $P_X$ define uma probabilidade nos borelianos.
Chamamos $P_X$ de **distribuição** ou **lei** de $X$. 
Se $X$ é variável aleatória discreta, vale que 
$$
P_X(B) = \sum_{i,x_i \in B} \mathbb{P}(X=x_i) = \sum_{i,x_i \in B} p(x_i).
$$
Se $X$ é variável aleatória absolutamente contínua com densidade $f$, vale que 
$$
P_X(B) = \int_B f(x) \, dx.
$$

[Aqui podemos observar uma lista de distribuições de probabilidade](https://en.wikipedia.org/wiki/List_of_probability_distributions). 
A maioria é descrita pela densidade no caso contínuo e função de probabilidade no caso discreto.

## Vetores aleatórios

Um vetor $X = (X_1, \dots, X_n)$, cujas componentes são variáveis aleatórias definidas em $(\Omega, \mathbb{A}, \mathbb{P})$, é chamado de **vetor aleatório**.
A função de distribuição de $X$ é definida como 
$$
F_X(x) = F_X(x_1, \dots, x_n) = \mathbb{P}(X_1 \le x_1, \dots, X_n \le x_n),
$$
que é a distribuição conjunta das variáveis $X_1, \dots, X_n$.

A $\sigma$-álgebra de Borel em $\mathbb{R}^n$ é a menor $\sigma$-álgebra que contém todo retângulo aberto $n$-dimensional.

## Independência

Sejam $X_1, \dots, X_n$ variáveis aleatórias definidas em $(\Omega, \mathbb{A}, \mathbb{P})$. 
Elas são **independentes** (coletivamente) se
$$
\mathbb{P}(X_1 \in B_1, \dots, X_n \in B_n) = \prod_{i=1}^n \mathbb{P}(X_i \in B_i).
$$
Daí é imediado que se $X_1, \dots, X_n$ são independentes, então
$$
F_{X_1, \dots, X_n}(x_1, \dots, x_n) = \prod_{i=1}^n F_{X_i}(x_i), \forall x_1, \dots, x_n \in \mathbb{R}.
$$
