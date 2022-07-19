# Introdução a grandes amostras

Agora, vamos verificar algumas propriedades assintóticas, isto é, quando o número de amostras é muito grande, com $n \to \infty$.

## Conceitos de convergência

Uma lista de conceitos de convergência importantes. 
Em particular, o conceito de **consistência** é importante para estimadores, dado que gostaríamos que, com amostras suficientes, tivéssemos valores razoáveis para o parâmetro. 

1. **Determinística:** Seja $\{x_n\}_{n \in \mathbb{N}}$ uma sequência em um espaço normado e  $\{r_n\}_{n \in \mathbb{N}}$ uma sequência de reais.
Se para cada $c > 0$, existe $N$ suficientemente grande tal que $||x_n|| \le c|r_n|$ para $n \ge N$, dizemos que $x_n = o(x_n)$.
Se existe $c > 0$ tal que a desigualdade anterior valha para $n$ grande, então dizemos que $x_n = O(r_n)$.

2. **Estocástica:**  Seja $\{X_n\}_{n \in \mathbb{N}}$ uma sequência de variáveis aleatórias definidas em espaços normados e  $\{r_n\}_{n \in \mathbb{N}}$ uma sequência de reais.
Se para cada $c > 0$ e $\epsilon > 0$, existe $N$ tal que $\mathbb{P}(||X_n|| \le c|r_n|) \ge 1 - \epsilon$ para $n \ge N$, dizemos que $X_n = o_P(x_n)$.
Se para cada $\epsilon >0$, existe $c > 0$ tal que a desigualdade anterior valha para $n$ grande, então dizemos que $X_n = O_P(r_n)$.

3. **Convergência em probabilidade:** Se $\{X_n\}_{n \in \mathbb{N}}$ e $X$ são quantidades aleatórias e, para todo $\epsilon >0$, vale que 
$$
\lim_{n \to \infty} Pr(||X_n - X|| > \epsilon) = 0,
$$
então dizemos que $X_n \overset{P}{\to} X$, isto é, $X_n$ converge em probabilidade para $X$.

Se $Y_n = f_n(X_n)$ para uma sequência de funções mensuráveis $f_n$ e $Y$ é uma outra quantidade aleatória, temos que $||Y_n - Y|| = o_P(1)$ se, e só se, $Y_n \overset{P}{\to} Y$. 
Em particular, se $f$ é contínua em $c$ e $X_n \overset{P}{\to} c$, então $f(X_n) \overset{P}{\to} f(c)$.

4. **Consistência:** Sejam $g$ uma função mensurável e $P_{\theta}$ uma distribuição paramétrica definida em $\mathcal{X}$. 
A sequência de variáveis aleatórias $Y_n : \mathcal{X}^n \to G$ é consistente para $g(\theta)$ se $Y_n \overset{P}{\to} g(\theta)$ para todo $\theta \in \Omega$.
A **lei dos grandes números** é um forte aliado, pois afirma que a média amostral converge em probabilidade para a média verdadeira.

5. **Convergência em distribuição:** Seja $\{X_n\}$ uma sequência de quantidades aleatórias e $X$ uma quantidade aleatória.
Se 
$$
\lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)],
$$
para toda função contínua limitada $f$, dizemos que $X_n$ converge em distribuição para $X$, isto é, $X_n \overset{D}{\to} X$ ou $X_n \Rightarrow X$.
Dizemos que a distribuição de $X$ é a **distribuição assintótica** de $X_n$.
Além do mais, dizemos que a distribuição de $X_n$ converge fracamente para a distribuição de $X$.
Se $H_n(x)$ é a função de distribuição acumulada de $X_n$ e $H$ é a CDF de $X$, então $H_n(x) \to H(x)$  sempre que $H$ é contínua em $x$ se, e somente se, $X_n \overset{D}{\to} X$

**Teorema:** Se $Y_n \Rightarrow Y$, $A_n \overset{P}{\to} a$ e $B_n \overset{P}{\to} b$, então
$$
A_n + B_nY_n \Rightarrow a + bY.
$$

6. **Convergência quase certa:** Uma sequência $\{X_n\}$ converge quase certamente para $X$ se $\mathbb{P}(Y_n \to Y) = 1$.

## Consistência

O exemplo clássico de consistência é o seguinte:

---
``📝`` **Exemplo (Lei fraca dos grandes números)**

Seja $X_1, X_2, \dots$ uma sequência de variáveis aleatórias independentes cuja distribuição tem densidade $f(x|\theta)$.
Defina $g(\theta) = \mathbb{E}_{\theta}[X]$ e $\bar{X}_n = n^{-1}(X_1 + \dots + X_n)$.
Pela lei fraca dos grandes números, temos que $\{\bar{X}_n\}$ é uma sequência de estimadores consistente para $g(\theta)$.

---

**Teorema:** Seja $\{W_n\}$ uma sequência de estimadores para $\theta$ tal que, para todo $\theta \in \Omega$,

(i) $\lim_{n \to \infty} \operatorname{Var}_{\theta}(W_n) = 0$,

(ii) $\lim_{n \to \infty} \operatorname{Bias}_{\theta}(W_n) = 0$.

Então $W_n$ é sequência de estimadores consistente de $\theta$.
Esse resultado é consequência direto do fato de que 
$$
\mathbb{E}_{\theta}[(W_n - \theta)^2] = \operatorname{Var}_{\theta}(W_n) + \operatorname{Bias}_{\theta}(W_n)^2
$$
e da desigualdade de Chebyshev, 
$$
P_{\theta}(|W_n - \theta| \ge \epsilon) \le \frac{\mathbb{E}_{\theta}[(W_n - \theta)^2]}{\epsilon^2}.
$$

Além do mais, se fizemos $U_n = a_n W_n + b_n$, com $a_n \to 1$ e $b_n \to 0$, temos que $U_n$ também é consistente.

## Teorema Central do Limite

Seja $X_1, \dots, X_n$ variáveis aleatórias iid com média $\mu$ e variância $\sigma^2$. 
Então
$$
\sqrt{n}(\bar{X}_n - \mu) \Rightarrow N(0, \sigma^2). 
$$

## Propriedades assintóticas MLE

O seguinte Teorema afirma que sob o modelo $f(x|\theta_0)$, a probabilidade de que a função de verossimilhança seja estritamente maior em $\theta_0$ tende a $1$ quando $n \to \infty$. 
Nesse sentido, se $n$ é suficientemente grande, nossa probabilidade de que sob aquela amostra a verossimilhança seja maior do que qualquer outro ponto é próximo a 1. 

**Teorema:** Seja $f_n(x|\theta)$ a densidade de uma amostra aleatória $(X_1, \dots, X_n)$.
Então, para cada $\theta_0, \theta \in \Omega$ com $\theta \neq \theta_0$, vale que 
$$
\lim_{n \to \infty} P_{\theta_0}\left[f_n(x|\theta_0) > f_n(x|\theta)\right] = 1.
$$

Agora, vamos verificar que o MLE é um estimador consistente.

**Teorema:** Seja $f_n(x|\theta)$ a densidade de uma amostra aleatória $(X_1, \dots, X_n)$ e fixe $\theta_0 \in \Omega$. 
Para cada $M\subseteq \Omega$ e $x \in \mathcal{X}$, defina
$$
Z(M,x) = \inf_{\psi \in M} \log \frac{f(x|\theta_0)}{f(x|\psi)} = \log f(x|\theta_0) - \sup_{\psi \in \Omega} \log f(x|\psi).
$$
Assuma que para cada $\theta \neq \theta_0$, exista uma vizinhança $N_{\theta}$ tal que $\mathbb{E}_{\theta_0}[Z(N_{\theta}, X_i)] > 0$.
Se $\Omega$ não é compacto, assuma que exista um compacto $C \subseteq \Omega$ tal que $\theta_0 \in C$ e $\mathbb{E}_{\theta_0} Z(\omega / C, X_i) > 0$. 
Então
$$
\lim_{n \to \infty} \hat{\theta}_n = \theta_0,
$$
quase certamente.

A função $Z(M,x)$ é a diferença da log-verossimilhança em $\theta_0$ e o máximo que ela atinge em $M$. 
Estamos assumindo que em uma vizinhança de cada ponto $\theta \in \Omega$, a máxima verossimilhança nessa região é, em média, menor do que a verossimilhança em $\theta_0$.
Além disso, para conjuntos não compactos, fora desse compacto, queremos que em média a verossimilhança em $\theta_0$ seja maior.
A dificuldade de utilizar esse teorema é verificar todas essas condições.

Assumindo a continuidade da função de verossimilhança para todo $x$ e que $\mathbb{E}_{\theta_0}[Z(N_{\theta}, X_i)] > -\infty$, também temos que MLE é um estimador consistente.

### MLE para a família exponencial

Seja $\hat{\theta}_n$ MLE calculado a partir de $X_1, \dots, X_n$ cuja distribuição tem densidade 
$$
f(x|\theta) = h(x)\exp\{\theta\cdot x - A(\theta)\},
$$
isto é, pertence à família exponencial na forma canônica.
Se $\Omega$ é um subconjunto aberto de $\mathbb{R}^k$, então

- $\lim_{n\to\infty} \mathbb{P}_{\theta}(\hat{\theta}_n \text{ existir}) = 1$

- $\sqrt{n}(\hat{\theta}_n - \theta) \overset{D}{\to} N_k(0, I_{\mathcal{X}}(\theta))^{-1}$, em que $I_{\mathcal{X}}(\theta)$ é a matriz informação de Fisher.

- $\{\hat{\theta}_n\}$ é consistente para $\theta$.

### Normalidade assintótica para MLEs

Sob algumas hipóteses de regularidade, podemos concluir que 
$$
\sqrt{n}(\hat{\theta}_n - \theta_0) \overset{D}{\to} N(0, I_{\mathcal{X}}(\theta_0)^{-1}),
$$
em que $I_{\mathcal{X}}(\theta_0)$ é a informação de Fisher.
Hipóteses:

1. $\{\hat{\theta}_n\}$ é consistente para $\theta$.
2. $f(x|\theta)$ tem derivadas de segunda ordem contínuas com respeito a $\theta$ e vale o sinal de integração pode ser trocado com o de diferenciação.
3. Existe uma função $H_r(x,\theta)$ que para todo $\theta_0$ tem valor esperando nulo quanto $r \to 0$ e seja limite superior da diferença na segunda derivada em uma bola de raio $r$ de $\theta_0$.

Na prática, podemos usar $I_{\mathcal{X}}(\hat{\theta}_n)$, visto que $\theta_0$ é desconhecido.