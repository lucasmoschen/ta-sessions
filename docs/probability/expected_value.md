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

## Esperanças de funções de variáveis aleatórias

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

**(4)** Quando $F$ é distribuição discreta, se $P(X=x_i) = p_i$, então $\int \varphi dF = \sum_{i} \varphi(x_i) p_i.

**(5)** Quando $F$ é distribuição contínua com densidade $f$, então $\int \varphi dF = \int \varphi(x) f(x) \, dx$.

