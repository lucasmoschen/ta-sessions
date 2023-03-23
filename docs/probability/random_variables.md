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