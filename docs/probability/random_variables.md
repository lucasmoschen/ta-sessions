# Variáveis aleatórias

Formalmente, uma variável aleatória atribui um valor numérico a cada possível resultado de um experimento.
Em outras palavras, dado um espaço de probabilidade $(\Omega, \mathbb{A}, P)$, uma **variável aleatória** é uma função
\[
X : \Omega \to \mathbb{R}.
\]
Além disso, por questões técnicas, demandamos que $\{\omega \in Omega : X(\omega) \le x\} \in \mathbb{A}$ para todo $x \in \mathbb{R}$. 
Dizemos então que $X$ é **mensurável**.
Isso permite, por exemplo, que possamos calcular $F_X(x) = P(X \le x)$, o qual chamaremos de **função de distribuição acumulada** de $X$.

A função de distribuição acumulada tem as seguintes propriedades:

1. **Não decrescente:** $x \le y \implies F_X(x) \le F_X(y)$.
2. **Continuidade a direita:** se $x_n \to x$ e $x_n \ge x$ para todo $n$, temos que $F_X(x_n) \to F_X(x)$.
3. **Limites:** $F_X(-\infty) = 0$ e $F_X(\infty) = 1$.

Essas propriedades podem ser demonstradas a partir das propriedades da probabilidade.