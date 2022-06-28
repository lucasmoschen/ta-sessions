# Revisão de Probabilidade

Nessa seção, vamos introduzir alguns conceitos chave de probabilidade e medida para a compreensão do curso de estatística.

## Medida

Uma medida atribui um valor não negativo a subconjuntos $A \subseteq \mathcal{X}$, com certas propriedades que gostaríamos de ter. Por exemplo, se $\mathcal{X}$ for um conjunto enumerável, como os números naturais, poderíamos definir uma medida para $A$ como 
$$
\mu(A) = |A| = \text{número de elementos de } A,
$$
conhecida como **medida de contagem**.
No caso em que $\mathcal{X} = \mathbb{R}^n$ para algum $n$, podemos definir a noção de volume de $A$ com 
$$
\mu(A) = \int_{\mathbb{R}^n} I\{\boldsymbol{x} \in A\} \, d\boldsymbol{x},
$$
conhecida como **medida de Lebesgue**. Para tornar esse conceito mais rigoroso, definimos uma **$\sigma$-algebra** como 

> Uma coleção de subconjuntos $\mathcal{A}$ de $\mathcal{X}$, isto é, $\mathcal{A} \subseteq \mathcal{P}\mathcal{X}$ (conjunto das partes de $\mathcal{X}$ é uma $\sigma$-álgebra se: 

**i)** $\emptyset \in \mathcal{A}$.

**ii)** Se $A \in \mathcal{A}$, então $A^c \in \mathcal{A}$.

**iii)** Se $A_1, A_2, \dots \in \mathcal{A}$, então $\cup_{i=1}^{\infty} A_i \in \mathcal{A}$.

> Uma **medida**, portanto, é uma função $\mu : \mathcal{A} \to \mathbb{R}_{+}$ que satisfaz a propriedade de que se a sequência $A_1, A_2, \dots$ é disjunta dois a dois, então 
$$
\mu\left(\cup_{i=1}^n A_i\right) = \sum_{i=1}^n \mu(A_i).
$$

Podemos definir algumas características de interesse para medidas:

- $\mu$ é medida **finita** se $\mu(\mathcal{X}) < +\infty$.
- $\mu$ é medida **$\sigma$-finita** se existe uma $A_1, A_2, \dots \in \mathcal{A}$ com $\mu(A_i) < +\infty$ tal que $\mathcal{X} = \cup_{i=1}^n A_i$.
- $\mu$ é medida **de probabilidade** se $\mu(\mathcal{X}) = 1$.

Chamamos o par $(\mathcal{X}, \mathcal{A})$ de **espaço mensurável** e a tripla $(\mathcal{X}, \mathcal{A}, \mu)$ de **espaço medida**. No caso em que $\mu$ é medida de probabilidade, temos um **espaço de probabilidade**.

Se $\mu(N)=0$, dizemos que $N$ tem medida nula. Se alguma propriedade $\tau$ vale **quase sempre**, queremos dizer que o conjunto em que $\tau$ não vale tem medida nula.

*Observação: Os axiomas da probabilidade ou de Kolmogorov são os seguintes três: (I) $P(A) \ge 0$ para todo evento $A$, (II) $P(\mathcal{X}) = 1$ e (III) $P(\cup_{i=1}^n A_i) = \sum_{i=1}^n P(A_i)$ para uma sequência disjunta. 
O terceiro axioma é chamado de **aditividade contável**. 
Alguns estatísticos, como deFinetti, acreditam que esse axioma é muito forte e auto-evidente.
Para isso, sugerem a **aditividade finita** $P(A \cup B) = P(A) + P(B)$ para $A \cap B = \emptyset$.
Essa alteração, todavia, gera complicações que não, necessariamente, melhoram o entendimento dos conceitos.*

## Integração

> Uma função $f$ com valores reais e definida em $\mathcal{X}$ é **mensurável** se o conjunto
$$
f^{-1}(B) = \{x \in \mathcal{X} : f(x) \in B\}
$$
pertence a $\mathcal{A}$ para todo $B$ [conjunto de Borel](https://en.wikipedia.org/wiki/Borel_set). Podemos tomar $B$ da forma $(-\infty, b)$, por exemplo. Podemos mostrar que funções contínuas ou contínuas por partes são mensuráveis.

Podemos então, definir propriedades básicas da integral de Lebesgue. Denote $1_A(x) = I(x \in A)$. Assim:

**(1)** $\int 1_A \, d\mu = \mu(A)$.

**(2)** Se $f$ e $g$ são funções mensuráveis não negativas e $a,b > 0$: 
$$
\int (af + bg) \, d\mu = a\int f \, d\mu + b\int g \, d\mu
$$

**(3)** Se $0 \le f_1 \le f_2 \le \dots$ e $f(x) = \lim_{n\to\infty} f_n(x)$, então
$$
\int f \, d\mu = \lim_{n\to \infty} \int f_n \, d\mu,
$$
e essa propriedade é o [**Teorema da Convergência Monótona**](https://en.wikipedia.org/wiki/Monotone_convergence_theorem). 

Uma **função simples** é uma função constante por partes que assume um valor finito de valores $a_1, \dots a_n$. Podemos escrever uma função simples como 
$$
s(x) = \sum_{i=1}^n a_i 1_{A_i}(x),
$$
para alguns $A_1, \dots, A_n$ disjuntos, e obter que 
$$
\int s \, d\mu = \sum_{i=1}^n a_i \mu(A_i).
$$
Além disso, um teorema bem interessante mostra que se $f$ é não negativa e mensurável, então existe uma sequência de funções simples $f_1 \le f_2 \le \dots \le f$ com $f = \lim f_n$. Isso mostra que qualquer função não negativa mensurável pode ser integrada. 

Por fim, basta ver que $f(x) = f^{+}(x) - f^{-}(x) = \max\{0, f(x)\} - (-\min\{f(x), 0\})$ é a soma de duas funções não negativas, e portanto, pode ser integrada através de 
$$
\int f \, d\mu = \int f^+ \, d\mu - \int f^{-} \, d\mu.
$$
Dizemos que $f$ é **integrável** se 
$$
\int |f| \, d\mu < +\infty.
$$

Algumas consequências importantes: 

- Se $f = 0$ quase sempre, então $\int f \, d\mu = 0$

- Se $f \ge 0$ e $\int f \, d\mu = 0$, então $f = 0$ quase sempre. 

- Se $f = g$ quase sempre, então $\int f \, d\mu = \int g \, d\mu$ se uma das integrais existe.

- Se $\int 1_{(c,x)} f \, d\mu = 0$ para todo $x > c$, então $f(x) = 0$ quase sempre em $x > c$. 

- Se $f > g$ são integráveis, então $\int f\, d\mu > \int g \, d\mu$, a menos que $\mu$ seja identicamente nula.

## Eventos e variáveis aleatórias

Seja $(\mathcal{X}, \mathcal{A}, P)$ um espaço de probabilidade. Dizemos que $A \in \mathcal{A}$ é um **evento**. 
Todos os possíveis desfechos de um experimento dado pelo conjunto $\mathcal{X}$ formam o **espaço amostral**.
Uma **variável aleatória** é uma função mensurável $X : \mathcal{X} \to \mathbb{R}$. A **distribuição** de $X$ é $Q$, iso é, $X \sim Q$ quando 
$$
Q(B) = P(\{x \in \mathcal{X} | X(x) \in A\}) := P(X \in B),
$$
isto é, $Q$ é definida nos conjuntos de Borel de $\mathbb{R}$. A **função de distribuição acumulada (FDA)** (em inglês, CDF) de $X$ é a função
$$
F_X(x) = P(X \le x) = Q((-\infty, x]),
$$
para $x \in \mathbb{R}$.

**Caracterização da FDA:** A função $F$ é uma FDA se, e somente se, as seguintes condições valem:

1) $\lim_{x \to -\infty} F(x) = 0$ e $\lim_{x \to \infty} F(x) = 1$.

2) $F(x)$ é uma função monótona não decrescente de $x$.

3) $F(x)$ é contínua à direita, isto é, $\lim_{x \to x_0^+} F(x) = F(x_0)$.

Além do mais, se $P(X \in A) = P(Y \in A)$ para todo conjunto de Borel $A$, então $X$ e $Y$ são identicamente distribuídas.
Isso é equivalente a notar que $F_X(x) = F_Y(x)$ para todo valor de $x$.

## Densidades

Uma medida é absolutamente contínua com respeito a outra se ela dá volume $0$ para as regiões que a outra também dá, isto é:

> Sejam $P$ e $\mu$ medidas definidas em $(\mathcal{X}, \mathcal{A})$. Dizemos que $P$ é absolutamente contínua com respeito a $\mu$ se $P(A) = 0$ sempre que $\mu(A) = 0$. Nesse caso, escrevemos que $P \ll \mu$. Também dizemos que $\mu$ domina $P$.

**Teorema de Radon-Nikodym:** Se uma medida $P$ finita é absolutamente contínua com respeito a uma medida $\mu$ $\sigma$-finita, então existe uma função mensurável $f$ tal que 
$$
P(A) = \int_A f \, d\mu := \int f1_A \, d\mu.
$$
Chamamos $f$ de derivada Radon-Nikodym de $P$ com respeito a $\mu$, ou a densidade de $P$ com respeito a $\mu$ e escrevemos 
$$
f = \frac{dP}{d\mu}.
$$
Vejam que de fato isso generaliza a noção de derivada, pois pelo Teorema fundamental do Cálculo, 
$$
F(x) = \int_a^x f(t) \, dt \implies f = \frac{d F}{d x},
$$
em que nesse caso estamos tomando a medida de Lebesgue na reta. Concluímos também que a densidade de $P$ é determinada a menos de um conjunto de medida nula.

## Esperança 

Se $X$ é uma variável aleatória definida em $(\mathcal{X}, \mathcal{A}, P)$, o **valor esperado** de $X$ é definido como
$$
\mathbb{E}[X] = \int X \, dP.
$$
Se $X \sim P_X$, podemos mostrar que 
$$
\mathbb{E}[X] = \int x dP_X(x).
$$
Além do mais, se $Y = f(X)$, então
$$
\mathbb{E}[Y] = \int f \, dP_X.
$$
Se $P_X$ tem densidade $p$ com respeito a $\mu$, então
$$
\int f \, dP_X = \int fp\, d\mu.
$$
Finalmente, definimos $\operatorname{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]$, $\operatorname{Cov}(X,Y) = \mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]$ e $\operatorname{Cor}(X,Y) = \operatorname{Cov}(X,Y)\big/\sqrt{\operatorname{Var}(X) \operatorname{Var}(Y)}$.

## Vetores Aleatórios

Seja agora uma função $X : \mathcal{X} \to \mathbb{R}^n$ mensurável (no sentido dos conjuntos de Borel em $\mathbb{R}^n$). Se $X \sim P_X$ e $P_X$ é absolutamente contínua com respeito a medida de Lebesgue em $\mathbb{R}^n$ com densidade $p$, temos que 
$$
P_X(B) = \int_{B} p(x) \, dx.
$$
A esperança de $X$ é 
$$
\mathbb{E}[X] = \begin{pmatrix}
    \mathbb{E}[X_1] \\ 
    \vdots \\
    \mathbb{E}[X_n]
\end{pmatrix}.
$$
E se $T : \mathbb{R}^n \to \mathbb{R}$ é mensurável, então $T(X)$ é variável aleatória com 
$$
\mathbb{E}[T(X)] = \int T \, dP_X.
$$

## Medida produto

Sejam $(\mathcal{X}, \mathcal{A}, \mu)$ e $(\mathcal{Y}, \mathcal{B}, \nu)$ espaços de medida. Então existe uma única medida $\mu \times \nu$ chamada de **medida produto** em $(\mathcal{X} \times \mathcal{Y}, \sigma(\mathcal{A} \times \mathcal{B}))$ tal que 
$$
(\mu \times \nu)(A \times B) = \mu(A)\nu(B),
$$
para $A \in \mathcal{A}$ e $B \in \mathcal{B}$. 
Denotamos $\sigma(C)$ como a menor $\sigma$-álgebra que contém $C$.

Com respeito a integração, obtemos o seguinte teorema 

**Teorema de Fubini:** Se $f \ge 0$, então 
$$
\int f \, d(\mu \times \nu) = \int\left[\int f(x,y) \, d\nu(y)\right] \, d\mu(x) =  \int\left[\int f(x,y) \, d\mu(x)\right] \, d\nu(y).
$$
Além do mais, se $f \ge 0$ não é satisfeito, mas $f$ é integrável com respeito a $\mu \times \nu$, a relação ainda é válida.

## Independência

A partir da definição de medida produto, podemos falar do conceito de independência de duas variáveis aleatórias. Sejam dois vetores aleatórios $X(\cdot) \subseteq \mathbb{R}^n$ e $Y(\cdot) \subseteq \mathbb{R}^m$. Dizemos que eles são **independentes** se
$$
P(X \in A, Y \in B) = P(X \in A)P(Y \in B),
$$
para todos os conjuntos de Borel $A$ e $B$.

Seja $Z = (X,Y)$ em $\mathbb{R}^{n+m}$. Temos que $Z \in A \times B$ se, e só se, $X \in A$ e $Y \in B$. Nesse caso, 
$$
P_Z(A \times B) = P_X(A)P_Y(B) \implies P_Z = P_A \times P_Y.
$$
A densidade de $Z$ também é dada pelo produto das densidades de $X$ e $Y$ pelo Teorema de Fubini.

Finalmente, temos o resultado de que se $X_1, \dots, X_n$ são vetores aleatórios independentes e se $f_1, \dots, f_n$ são funções mensuráveis, então $f_1(X_1), \dots, f_n(X_n)$ são independentes.

### Densidades conjunta e marginais

A **densidade conjunta** de $X$ e $Y$ denotada por $p_Z$ satisfaz
$$
P(Z \in B) = \int \int 1_B(x,y)p_Z(x,y) \, d\mu(x) \, d\nu(y).
$$
A **densidade marginal** de $X$ ($Y$) pode ser obtida *integrando* $Y$ ($X$), e assim:
$$
p_X(x) = \int p_X(x,y) \, d\nu(y),
$$
com respeito a $\mu$.

## Cálculo de probabilidades

A partir dos Axiomas da Probabilidade, podemos obter alguns resultados importantes:

1) $P(\emptyset) = 0$ 

2) $P(A^c) = 1 - P(A)$

3) $P(\cup_{i=1}^{\infty} A_i) \le \sum_{i=1}^{\infty} P(A_i)$

## Condicionando 

Considere $X$ e $Y$ duas variáveis discretas definidas em $\mathcal{X}$ e $\mathcal{Y}$, respectivamente. 
Definimos a **probabilidade condicional** de $X = x_i$ dado $Y = y_j$ como 
$$
P(X=x_i | Y=y_j) = \frac{P(X=x_i, Y=y_j)}{P(Y=y_j)} := p_{i|j}.
$$
É fácil verificar que $P(\cdot | Y=y_j)$ define uma medida de probabilidade em $\mathcal{X}$. 
A média condicional de uma função $f$ de $X$ é dada por 
$$
\mathbb{E}[f(X) | Y=y_j] = \sum_{i=1}^{\infty} f(x_i) p_{i|j}.
$$

De forma geral, se $P(B) > 0$, escrevemos $P(A|B) = P(A\cap B)/P(B)$ para eventos $A$ e $B$. 
Mas o que fazer quando $P(B) = 0$? 
Em especial, isso ocorre quando falamos de variáveis aleatórias contínuas, já que $P(X=1) = 0$, por exemplo.

**Probabilidade condicional:** Dadas variáveis aleatórias $X$ e $Y$ com $\mathbb{E}|Y| < +\infty$ e um evento $A$, dizemos que $P(A|X)$ é probabilidade condicional de $A$ dado $X$ se é uma variável aleatória $\sigma(X)$-mensurável ($\sigma(X)$ é a menor $\sigma$-álgebra em $X$ é mensurável) e, para todos os Boreis $S \subseteq \mathbb{R}$, temos 
$$
\mathbb{E}[P(A|X)1_{S}(X)] = P(A \cap \{X \in S\}).
$$
De forma similar, introduzimos o conceito de $\mathbb{E}[Y|X]$, substituindo acima probabilidades por esperanças:
$$
\mathbb{E}[\mathbb{E}[Y|X]1_{S}(X)] = \mathbb{E}[Y1_S(X)].
$$
Como consequência, probabilidades e esperanças condicionais são definidas a menos de um conjunto de medida nula.

**Distribuição condicional:** Uma função $Q$ é distribuição condicional de $Y$ dado $X=x$ se 

1) $Q_x(\cdot)$ é uma medida de probabilidade para todo $x$;

2) $Q_x(B)$ é função mensurável de $x$ para todo Borel $B$;

3) $P(X \in A, Y \in B) = \int_A Q_x(B) \, dP_X(x)$.

Escrevemos então que $Y|X=x \sim Q_x$.

**Teorema (densidade condicional):** Suponha que $X$ e $Y$ sejam vetores aleatórios com densidade conjunta $p_Z$ com respeito a $\mu \times \nu$. Seja $E = \{x : p_X(x) > 0\}. Para $x \in E$, defina 
$$
p_{Y|X}(y|x) = \frac{p_Z(x,y)}{p_X(x)},
$$
e seja $Q_x$ a medida de probabilidade com densidade $P_{Y|X}(\cdot|x)$ com respeito a $\nu$.
Se $x \not \in E$, então defina $p_{Y|X}(y|x) = p_0(y)$ em que $p_0$ é densidade de uma distribuição de probabilidade $P_0$ arbitrária e seja $Q_x = P_0$. 
Então $Q$ é distribuição condicional de $Y$ dado $X=x$. 