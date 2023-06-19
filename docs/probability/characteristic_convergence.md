# Funções características

Seja $X$ uma variável aleatória. 
A **função característica** de $X$ é a função $\varphi : \mathbb{R} \to \mathbb{C}$ de forma que 
$$
\varphi_X(t) := E[e^{it X}] := E[\cos(tX)] + iE[\sin(tX)],
$$
usando como definição a relação de Euler $e^{ib} = \cos(b) + i\sin(b)$.

Essa função tem relevância no estudo de probabilidade e, em particular, no estudo de convergência de distribuições, dadas as suas propriedades:

**(1) Função limitada:** $|\varphi_X(t)| \le 1$ para todo $t \in \mathbb{R}$.

**(2)** $\varphi_X(0) = 1$.

**(3) Conjugado:** $\overline{\varphi_X(t)} = \varphi_X(-t)$, em que $\bar{x}$ é o complexo conjugado e $x$.

**(4) Uniformidade contínua:** para todo $\epsilon > 0$, existe $\delta > 0$ tal que $|t-s| < \delta \implies |\varphi_X(t) - \varphi_X(s)| < \epsilon$. 
Em outras palavras a escolha de $\delta$ para a continuidade de $\varphi$ não depende do ponto $t$ escolhido.

**(5) Soma de v.a.:** Se $X$ e $Y$ são independentes, então $\varphi_{X+Y}(t) = \varphi_X(t)\varphi_Y(t)$ para todo $t \in \mathbb{R}$.

**(6) Teorema da Unicidade** A função característica determina a função de distribuição de uma variável aleatória. 
Logo 
$$F_Y = F_X \iff \varphi_X = \varphi_Y.$$

**(7) Simetria:** A v.a. $X$ tem distribuição simétrica em torno do $0$ se, e somente se, $\varphi_X(t) \in \mathbb{R}$ para todo $t \in \mathbb{R}$.

**(8)** Se $Y = aX + b$, então $\varphi_Y(t) = e^{itb} \varphi_X(at)$.

**(9)** Se $E|X|^n$ é finito, então $\varphi_X$ é $n$ vezes diferenciável, com derivadas contínuas.
Em particular, $\varphi^{(k)}_X(0) = i^k E[X^k]$

## Função característica de um vetor aleatório

Para vetores aleatórios, a função característica é definida como 
$$
\varphi(t_1, \dots, t_n) = E\{\exp[i(t_1 X_1 + \cdots + t_n X_n)]\},
$$
que tem propriedades análogas a do caso unidimensional.

Uma propriedade interessante adicional é que marginalizar aqui é muito fácil.
$$
\varphi_{X,Y}(s,t) = \varphi_{X,Y,Z}(s,t,0), (s,t) \in \mathbb{R}^2.
$$

# Convergência em distribuição

Sejam $X, X_1, X_2, \dots$ variáveis aleatórias com funções de distribuição $F, F_1, F_2, \dots$, respectivamente.
Dizemos que $X_n$ **converge em distribuição** para $X$ se $F_n(x) \to F(x)$ para todo ponto $x$ em que $F$ é contínua.
Denotamos por $X_n \overset{D}{\to} X$.
Também dizemos que $F_{X_n}$ **converge fracamente** para $F$.

**Teorema de Helly-Bray:** Sejam $F, F_1, F_2, \dots$ funções de distribuição.
Se $F_n$ converge fracamente para $F$, então 
$$\int g(x) dF_n(x) \to \int g(x) dF(x)$$
para toda função $g:\mathbb{R} \to \mathbb{R}$ contínua e limitada.

Em particular, como $\sin(tx)$ e $\cos(tx)$ são funções limitadas para cada $t$ fixo, temos que
$$
\varphi_{X_n}(t) \to \varphi_X(t),
$$
usando o teorema acima. 
Isso ocorre porque $\varphi$ é um valor esperado e satisfaz as condições de Helly-Bray.

A recíproca pode ser escrita da seguinte forma:

**Teorema da continuidade de Paul Lévy:** Sejam $F_1, F_2, \dots,$ funções de distribuição e $\varphi_1, \varphi_2, \dots$ suas respectivas funções características, definidas como
$$
\varphi_n(t) = \int e^{itx} dF_n(x).
$$
Se $\varphi_n$ converge pontualmente para um limite $\varphi$ e se $\varphi$ é contínua em $t=0$, então **existe uma distribuição** $F$ tal que $F_n$ converge fracamente para $F$ e, **mais do que isso,** $\varphi$ é função característica de $F$.

Juntando ambos os teoremas acima, temos o famoso resultado 
$$
X_n \overset{D}{\to} X \iff \varphi_{X_n} \to \varphi_X.
$$
E além disso, a volta mostra que se $\varphi_n$ converge para algo contínuo em $0$, esse algo vai ser uma função característica.

Um resultado interessante que sai disso é que se $\varphi_{X_n}(t) \to e^{-t^2/2}$ para todo $t \in \mathbb{R}$, então $X_n$ converge em distribuição para uma variável aleatória normal com média $0$ e variância $1$, ou **normal padrão**.

**Teorema central do limite:** Sejam $X_1, X_2, \dots$ independentes e identicamente distribuídas com média $\mu$ e variância $\sigma^2 \in (0,\infty)$. 
Seja $S_n = X_1 + \cdots + X_n$.
Então
$$
\frac{S_n - n\mu}{\sigma \sqrt{n}} \overset{D}{\to} N(0,1).
$$

## Resultados adicionais

**Caso discreto:** Sejam $X_1, \dots, X_n, \dots$ e $X$ variáveis aleatórias discretas que tomam os valores inteiros não negativos.
Defina $p_n(k) = P(X_n = k)$.
Então $X_n \overset{D}{\to} X$ se, e somente se, $p_n(k) \to p(k)$ para todo $k= 0,1,\dots$

**Caso contínuo (Scheffé):** Sejam $X_1, \dots, X_n, \dots$ e $X$ v.a. contínuas com densidade $f_1,\dots,f_n, \dots$ e $f$.
Se $f_n(x) \to f(x)$ para quase todo ponto $x$ (medida de Lebesgue, isto é, não precisa ocorrer nos números racionais, por exemplo, mas não pode existir nenhum intervalo em que isso não ocorra em nenhum ponto), então $X_n \overset{D}{\to} X$.

**Implicações:**

**(1) Convergência quase certa implica convergência em probabilidade**, mas não o contrário necessariamente.

**(2) Convergência em probabilidade implica convergência em distribuição**, mas não vale a recíproca em geral.

**(3) Convergência em distribuição para variável constante implica convergência em probabilidade para essa constante**: assim $X_n \overset{D}{\to} c \iff X_n \overset{P}{\to} c$. 

## Teoremas de continuidade

**Continuidade:** Sejam $X_1, X_2, \dots$ e $X$ v.a. e $g$ uma função contínua definida nos reais.
Então $X_n \to X$ (quase certamente / em probabilidade / em distribuição) implica que $g(X_n) \to g(X)$ (quase certamente / em probabilidade / em distribuição).

**Slutsky:** $X_n \overset{D}{\to} X$ e $Y_n \overset{P}{\to} c$, em que $c$ e uma constate. 
Então

**(a)** $X_n + Y_n \overset{D}{\to} X + c$;

**(b)** $X_n - Y_n \overset{D}{\to} X - c$;

**(c)** $X_nY_n \overset{D}{\to} cX$;

**(d)** $X_n/Y_n \overset{D}{\to} X/c$ se $c \neq 0$ e $P(Y_n \neq 0) = 1$.

**Método Delta:** Se $\sqrt{n}(X_n - \mu) \overset{D}{\to} N(0,\sigma^2)$ e $g$ é uma função diferenciável em $\mu$, então 
$$\sqrt{n}(g(Y_n) - g(\mu)) \overset{D}{\to} N(0, \sigma^2 g'(\mu)^2).$$

