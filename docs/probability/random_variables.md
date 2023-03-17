# Variáveis aleatórias

Formalmente, uma variável aleatória atribui um valor numérico a cada possível resultado de um experimento.
Em outras palavras, dado um espaço de probabilidade $(\Omega, \mathbb{A}, P)$, uma **variável aleatória** é uma função
\[
X : \Omega \to \mathbb{R}.
\]
Além disso, por questões técnicas, demandamos que $\{\omega \in Omega : X(\omega) \le x\} \in \mathbb{A}$ para todo $x \in \mathbb{R}$. 
Dizemos então que $X$ é **mensurável**.
Isso permite, por exemplo, que possamos calcular $F_X(x) = P(X \le x)$, o qual chamaremos de **função de distribuição acumulada** de $X$.