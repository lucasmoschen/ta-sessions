# Distribuições e Esperanças condicionais

Vamos iniciar com o caso em que $X$ e $Y$ são discretas.
Considere um espaço de probabilidade $(\Omega, \mathcal{A}, P)$ e $A \in \mathcal{A}$ tal que $P(A) > 0$.
A **distribuição conditional de $X$ dado o evento $A$** é
$$
P(X \in B | A) = \frac{P(X \in B, A)}{P(A)},
$$
em que $B$ é um boreliano da reta real.
Podemos verificar que $P(X|A)$ define uma probabilidade, visto que satisfaz os três axiomas da probabilidade: probabilidade não negativa,  probabilidade de $X \in \R | A$ sendo $1$ e probabilidade da união sendo a soma das probabilidade individuais para sequências de disjuntos.

A **função de distribuição condicional de $X$ dado $A$** é 
$$
F_X(x|A) = P(X \le x|A).
$$
e a **esperança conditional** é
$$
E(X|A) = \int x dF_X(x|A).
$$

Agora suponha que $Y$ seja uma variável discreta em $(\Omega, \mathcal{A}, P)$ que assuma os valores $y_1, y_2, \dots$.
Então, podemos usar os conjuntos $A_n = \{Y = y_n\}$ para particionar $\Omega$.
Nesse caso, 
$$
P(X \in B | Y = y_n) = P(X \in B| A_n)
$$
é a **distribuição condicional de $X$ dado $Y=y_n$**.

Daí podemos calcular 
$$
E[X] = \sum_{n=1} ^{\infty} E[X|Y=y_n] P(Y=y_n).
$$
A **esperança condicional de $X$ dado $Y$** é $E[X|Y] = E[X|Y=y]$, que é uma função de $y$.
Em particular, $E[X|Y]$ é uma variável aleatória cujas realizações são $E[X|Y=y]$.
Portanto, 
$$
E[X] = E[E[X|Y]],
$$
usando que 
$$E[E[X|Y]] = \int E[X|Y=y] dF_Y(y) = E[X].$$

---
``📝`` **Processo de Poisson**

Considere um contador de partículas que conta segundo um processo de Poisson com parâmetro $\lambda > 0$.
O número de partículas contadas até o tempo $t > 0$ é $X_t \sim Poisson(\lambda t)$
Seja $T_1$ o tempo de chegada da primeira partícula e $T_n$ o tempo entre as chegadas das partículas $n-1$ e $n$.
Vimos que $T_1, T_2, \dots$ são independentes e identicamente distribuídos com parâmetro $\lambda$.

Uma pergunta natural é qual a distribuição de $T_1 | X_t = 1$? A resposta é uniforme $[0,t]$, isto é, se sabemos que chegou exatamente um indivíduo no período $[0,t]$, o tempo que ele chegou está uniformemente distribuído em $[0,t]$.
Note que $X_t = 1$ implica que $T_1 \le t$.
Dessa forma,
$$
P(T_1 \le s | X_t = 1) = \begin{cases}
 0, &s \le 0 \\
 1, &s > t
 \end{cases}.
$$
Se $0 < s < t$,
$$
\begin{split}
P(T_1 \le s | X_t = 1) &= \frac{P(T_1 \le s, X_t = 1)}{P(X_t = 1)} \\
&= \frac{P(X_s = 1, X_t - X_s = 0)}{P(X_t = 1)} \\
&= \frac{P(X_s = 1)P(X_t - X_s = 0)}{P(X_t = 1)} \\
&=\frac{\lambda s e^{-\lambda s} e^{-\lambda(t-s)}}{\lambda t e^{-\lambda t}} = \frac{s}{t}.
\end{split}
$$
em que a segunda igualdade vem do fato que $T_1 \le s$ e $X_t = 1$ implica $X_s = 1$ e, portanto, $X_t - X_s = 0$.
A segunda igualdade vem do fato que os intervalos disjuntos são independentes no processo de Poisson.
Finalmente, a terceira vem do fato que as variáveis têm distribuição de Poisson e $X_t - X_s$ tem a mesma distribuição de $X_{t-s} - X_0 = X_{t-s}$.
Portanto $T_1 | X_t = 1 \sim U[0,t]$.

Mais do que isso, podemos provar que 
$$
(T_1, T_1 + T_2, \dots, T_1 + \dots + T_n)
$$
tem distribuição uniforme no conjunto
$$
A_n = \{(x_1, \dots, x_n) \in \mathbb{R}^n : 0 \le x_1 \le x_2 \le \dots \le x_n \le t\}.
$$
Note que se $Y_1, \dots, Y_n$ são iid $U[0,t]$, a estatística de ordem $Y_{(1)}, \dots, Y_{(n)}$ tem distribuição uniforme em $A_n$.

Com isso em mente, podemos pensar que dado que $n$ partículas chegaram até o tempo $t$, isto é, $X_t = n$, a chegada das $n$ partículas é modelada por $n$ variáveis aleatórias iid $U[0,t]$ e, após ordenadas, temos os tempos de chegadas das partículas em ordem.

---

## Caso geral

Seja $I$ um intervalo de tamanho $\Delta y$ e que contenha o ponto $y$.
Assim, dizemos que 
$$
P(X \in B|Y=y) = \lim_{\Delta y \to 0} P(X \in B| Y \in I),
$$
se o limite existe. 
Se para alguma vizinhança de $y$, $P(Y \in I) = 0$, então definimos $P(X \in B | Y=y) = P(X \in B)$.
Essa definição de probabilidade condicional não é única.
Além dela, existem baseadas em Teoria da Medida que dão um rigor maior em demostrações teóricas.

Podemos provar também que a **distribuição condicional de $X$ dado $Y$** é a única que satisfaz
$$
F_{X,Y}(x,y) = \int_{-\infty}^y F_X(x|Y=t) dF_Y(t), (x,y) \in \mathbb{R}^2
$$
para quaisquer pares de variáveis aleatórias $X$ e $Y$ definidas em um mesmo espaço de probabilidade.

Suponha que $X$ e $Y$ tenham densidade $f(x,y)$.
Seja 
$$
f(x|y) = \frac{f(x,y)}{\int f(x,y) \, dy} = \frac{f(x,y)}{f_Y(y)}
$$
a **densidade da distribuição condicional**.
Se $f_Y(y) > 0$, então $f(x|y)$ define uma densidade.
Além disso, essa densidade satisfaz as relações que estabelecemos para probabilidade condicional.
Se $f_Y(y) = 0$, os valores para a densidade não são relevantes, pois tem probabilidade $0$.

Formalmente, definimos $P(X \in B|Y=y)$ como a **distribuição condicional para $X$ dado $Y$** se 

**(I)** $\forall y \in \mathbb{R}$, $P(X \in B | Y=y)$ define uma probabilidade nos borelianos da reta.

**(II)** Para todo boreliano $B$, $P(X \in B | Y=y)$ é função mensurável de $y$ e para todo $(x,y) \in \mathbb{R}^2$,
$$
\int_{-\infty}^y P(X \le x | Y=t) dF_Y(t) = P(X\le x, Y \le y)
$$

Pode-se **provar** que para duas variáveis aleatórias $X$ e $Y$ definidas no mesmo espaço de probabilidade, existe uma distribuição condicional para $X$ dado $Y$, e ela é única exceto em um conjunto de medida nula.

Apesar de 
$$
P(X \in B|Y=y) = \lim_{\Delta y \to 0} P(X \in B| Y \in I),
$$
ser uma verdade, esse limite acerta com probabilidade $1$, mas não em todo ponto. 
Para distribuições contínuas, podemos obter resultados inesperados.
Em geral, o que se faz é usar a densidade conjunta para variáveis contínuas ou avaliar no caso discreto. 
Se não conseguirmos proceder com esses casos, temos que chutar a distribuição condicional e verificar as condições da definição.

Uma proposição importante é a seguinte, também conhecido como **princípio da substituição**.

**Proposição:** Sejam $X$ e $Y$ variáveis aleatórias e $\phi(x,y)$ uma função mensurável.
Se a distribuição condicional de $X$ dado $Y$ é 
$$
P(X \in B | Y=y), B \in \mathcal{B}, y \in \mathbb{R},
$$
então
$$
P(\phi(X,Y) \in B|Y=y) = P(\phi(X,y) \in B | Y=y) = P( X \in \{x : \phi(x,y) \in B\}|Y=y).
$$

## Esperança condicional

Sejam $X$ e $Y$ variáveis aleatórias.
A esperança condicional de $X$ dado $Y=y$ é 
$$
E[X|Y=y] = \int x \, dF_X(x|Y=y).
$$
Se $X$ é integrável, então essa esperança existe e é finita quase certamente para valores de $y$.
A variável aleatória $E[X|Y]$, que é função de $Y$, é a **esperança condicional de $X$ dado $Y$**.

Lembrando que $E[X] = E[E[X|Y]]$.
Além disso, se $X_1 \le X_2$, vale que $E[X_1 | Y] \le E[X_2 \le Y]$.
A linearidade e a desigualdade de Jensen do valor esperado também é mantida.
Outros resultados que valem para valor esperado $E[\cdot]$ também valem para $E[\cdot | Y]$.