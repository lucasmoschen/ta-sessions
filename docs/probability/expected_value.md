# Esperança matemática

Seja $X$ uma variável aleatória discreta com função de distribuição $p(x_i)$.
A esperança de $X$ ou **valor esperado** de $X$ é definida como 
$$
E[X] = \sum_{i} x_i p(x_i).
$$
quando a série é absolutamente convergente.

Para uma variável aleatória $X$ e com distribuição $F$.
A **esperança** de $X$ é definida por 
$$
E[X] = \int_{-\infty}^{\infty} x \, dF(x),
$$
quando a integral de [Riemann-Stieltjes](/ta-sessions/probability/expected_value/#apendice-integral-de-stieltjes) está bem definida.
Quando $E[X]$ é finita, dizemos que $X$ é **integrável**.
Se $X$ tem densidade $f(x)$, então
$$
E[X] = \int x dF_X(x) = \int x f(x) \, dx.
$$

**Proposição:** $E[X] = \int_0^{\infty} (1-F(x)) \, dx - \int_{-\infty}^0 F(x) \, dx$.

Se $X$ assume somente valores inteiros não negativos, então
$$
E[X] = \sum_{n=0}^{\infty} P(X > n)= \sum_{n=1}^{\infty} P(X \ge n).
$$

## Propriedades da esperança

Seguem algumas propriedades relevantes sobre o valor esperado (sempre supondo que $X,Y$ são integráveis):

1. $P(X = c) = 1 \implies E[X] = c$.

2. $X \le Y \implies E[X] \le E[Y]$.

3. Linearidade: $E[aX + bY] = aE[X] + bE[Y]$

4. Desigualdade de Jensen: se $\varphi$ é função convexa, então $E[\varphi(X)] \ge \varphi(E[X])$. Se $\varphi$ for côncava, então $-\varphi$ é convexa e, portanto, $E[\varphi(X)] \le \varphi(E[X])$. De forma um pouco mais geral, basta que $\varphi$ seja convexa em uma região $I \subset \mathbb{R}$ tal que $P(X \in I) = 1$.

5. Desigualdade de Markov: se $X \ge 0$, para todo $\lambda > 0$, $P(X \ge \lambda) \le E[X]/\lambda$.

6. Desigualdade de Chebychev: seja $\mu = E[X]$. 
Assim, $P(|X-E[X]| \ge \lambda) \le Var(X)/\lambda^2$ para todo $\lambda > 0$.

7. Se $Z \ge 0$ e $E[Z] = 0$, então $P(Z=0)=1$.

### Integrabilidade

Podemos derivar algumas condições de integrabilidade a partir dessas propriedades.

1. Se $X$ é dominada por uma variável aleatória integrável $Y$, isto é, $|X| \le Y$, então $X$ é integrável.

2. $\sum_{n=1}^{\infty} P(|X| \ge n) \le E|X| \le 1 + \sum_{n=1}^{\infty} P(|X| \ge n)$ e, portanto $X$ é integrável se, e só se, $\sum_{n=1}^{\infty} P(|X| \ge n) < +\infty$.

## Esperanças de funções de variáveis aleatórias

Seja $X$ uma variável aleatória, $\varphi$ uma função mensurável e $Y = \varphi(X)$.
Então 
$$
E[Y] := \int y dF_{\varphi(X)}(y) = \int_0^{\infty} 1 - F_{\varphi(X)}(y) \, dy - \int_{-\infty}^0 F_{\varphi(X)}(y) \, dy.
$$
Para isso, precisamos encontrar a distribuição de $Y$, isto é, $P(\varphi(X) \le y)$ para cada $y$.

A lei do estatístico inconsciente (*Law of the unconscious statistician*, LOTUS) é um importante teorema para calcular o valor esperado de $Y$. 
Muitos livros antigos de estatística se referiam a esse resultado como uma definição, e não como um teorema, então utilizavam um resultado de forma inconsciente.

O resultado diz que 
$$
E[Y] = \int \varphi(x) dF_X(x) 
$$
de forma que, se $X$ é variável contínua com densidade $f$, 
$$
E[Y] = \int \varphi(x) f(x) dx
$$
e se $X$ é discreta com função de massa $p$,
$$
E[Y] = \sum_{i} \varphi(x_i)p(x_i).
$$

## Momentos

Seja $X$ uma variável aleatória e $b \in \mathbb{R}$.
O valor $E[(X-b)^k]$ é o $k$-ésimo momento de $X$ em torno de $b$.
Quando $b=E[X]$, dizemos **momento central** de ordem $k$ de $X$ e quando $b=0$, dizemos **momento** de ordem $k$ de $X$.
A variância é o segundo momento central.

Um resultado interessante é que se $E|X|^t$ é finita para algum $t > 0$, então para todo $s \in (0,t)$, vale que $E|X|^s$.

### Propriedades da variância

1. $P(X = c) = 1 \implies Var(X) = 0$.

2. $Var(aX + b) = a^2Var(X)$ para todas as constantes $a$ e $b$.

## Esperanças de funções de vetores aleatórios

Se $X=(X_1,\dots,X_n)$ e $\varphi:\mathbb{R}^n \to \mathbb{R}$ é uma função mensurável.
Então
$$
E[\varphi(X)] = \int \cdots \int \varphi(x_1, \dots, x_n) \, dF_X(x_1,\dots,x_n).
$$
Nos casos discreto e contínuo, essa integral tem as simplificações usuais.

**Proposição:** Se $X_1,\dots,X_n$ são variáveis aleatórias independentes e integráveis, 
$$
E[X_1X_2\cdots X_n] = \prod_{i=1}^n E[X_i].
$$

**Observação:** $E[XY] = E[X]E[Y]$ não implica independência de $X$ e $Y$.
Se $(X, Y)$ tem distribuição normal bivariada, covariância zero **implica** independência. Mas são poucos os exemplos.

A **covariância** entre $X$ e $Y$ é 
$$
Cov(X,Y) = E[(X-EX)(Y-EY)] = E[XY] - E[X]E[Y].
$$
Se $Cov(X,Y) = 0$, então $X$ e $Y$ são **não correlacionadas**.

Temos que 
$$
Var(X_1 + \cdots + X_n) = \sum_{i=1}^n Var(X_i) + \sum_{i \neq j} Cov(X_i, X_j).
$$

A **correlação** de $X$ e $Y$ é 
$$
\rho_{X,Y} = \frac{Cov(X,Y)}{\sqrt{Var(X)}\sqrt{Var(Y)}}.
$$

Vale que 

1. $\rho(X,Y) \in [-1,1]$
2. $\rho(X,Y) = \pm 1 \iff P(Y=\pm aX+b)=1$ para algum $a > 0$ e $b \in \mathbb{R}$.
3. $\rho(X,Y) = \rho(aX + b, cX + d)$.

## Apêndice: integral de Stieltjes

Seja $\varphi$ uma função contínua com domínio em $[a,b]$ e $F$ uma função de distribuição.
A integral de **Riemann-Stieltjes** de $\varphi$ em $[a,b]$ relação a $F$ como o limite das somas de Riemann da forma
$$
\sum_{i=1}^n  \varphi(y_i) [F(x_{i+1}) - F(x_i)],
$$
em que $a < x_i < x_{i+1} < b$ para todo $i=1,\dots,n$ e $y_i \in [x_i, x_{i+1}]$.
O limite é tomado quando $\max_{i=1,\dots,n} |x_{i+1}-x_i| = 0$.
Se o limite existe, denotamos ele por 
$$
\int_a^b \varphi(x) dF(x).
$$

Em geral, essa definição de integral tem alguns problemas que aparecem para casos simples.
O exemplo clássico é tomar
$$
F_0(x) = I_{\ge 0}(x)
$$
e procurar $\int_{-1}^1 F_0(x) dF_0(x)$, que não existe.
Por isso, em medida, é mais interessante usar a **integral de Lebesgue-Stieltjes**.

Essa integral não é introduzida aqui, mas vale para funções $\varphi$ mensuráveis.
Quando o integrando é uma função contínua, a integral de Lebesgue-Stieltjes torna-se a de Riemann.
Algumas propriedades são

**(1)** $\int_a^b dF(x) = F(b) - F(a)$.

**(2)** A integral é linear no integrando e no integrador, isto é, vale a linearidade para $f(x) = \alpha g(x) + \beta h(x)$ e para a distribuição $F(x) = \alpha G(x) + \beta H(x)$.

**(3)** Vale que $\int_a^c \varphi dF = \int_a^b \varphi dF + \int_b^c \varphi dF$ para $a < b < c$.

**(4)** Quando $F$ é distribuição discreta, se $P(X=x_i) = p_i$, então $\int \varphi dF = \sum_{i} \varphi(x_i) p_i$.

**(5)** Quando $F$ é distribuição contínua com densidade $f$, então $\int \varphi dF = \int \varphi(x) f(x) \, dx$.

