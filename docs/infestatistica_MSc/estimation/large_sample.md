# Introdução a grandes amostras

Agora, vamos verificar algumas propriedades assintóticas, isto é, quando o número de amostras é muito grande, com $n \to \infty$.

## Conceitos de convergência

Uma lista de conceitos de convergência importantes. 
Em particular, o conceito de **consistência** é importante para estimadores, dado que gostaríamos que, com amostras suficientes, tivéssemos valores razoáveis para o parâmetro. 

1. **Determinística:** Seja $\{x_n\}_{n \in \mathbb{N}}$ uma sequência em um espaço normado e  $\{r_n\}_{n \in \mathbb{N}}$ uma sequência de reais.
Se para cada $c > 0$, existe $N$ suficientemente grande tal que $||x_n|| \le c|r_n|$ para $n \ge N$, dizemos que $x_n = o(x_n)$.
Se existe $c > 0$ tal que a desigualdade anterior valha para $n$ grande, então dizemos que $x_n = O(r_n)$.

2. **Estocástica:**  Seja $\{X_n\}_{n \in \mathbb{N}}$ uma sequência de variáveis aleatórias definidas em espaços normados e  $\{r_n\}_{n \in \mathbb{N}}$ uma sequência de reais.
Se para cada $c > 0$ e $\epsilon > 0$, existe $N$ tal que $P(||X_n|| \le c|r_n|) \ge 1 - \epsilon$ para $n \ge N$, dizemos que $X_n = o_P(x_n)$.
Se para cada $\epsilon >0$, existe $c > 0$ tal que a desigualdade anterior valha para $n$ grande, então dizemos que $X_n = O_P(r_n)$.

3. **Convergência em probabilidade:** Se $\{X_n\}_{n \in \mathbb{N}}$ e $X$ são quantidades aleatórias e, para todo $\epsilon >0$, vale que 
$$
\lim_{n \to \infty} Pr(||X_n - X|| > \epsilon) = 0,
$$
então dizemos que $X_n \overset{P}{\to} X$, isto é, $X_n$ converge em probabilidade para $X$.

Se $Y_n = f_n(X_n)$ para uma sequência de funções mensuráveis $f_n$ e $Y$ é uma outra quantidade aleatória, temos que $||Y_n - Y|| = o_P(1)$ se, e só se, $Y_n \overset{P}{\to} Y$.

4. **Consistência:** Sejam $g$ uma função mensurável e $P_{\theta}$ uma distribuição paramétrica definida em $\mathcal{X}$. 
A sequência de variáveis aleatórias $Y_n : \mathcal{X}^n \to G$ é consistente para $g(\theta)$ se $Y_n \overset{P}{\to} g(\theta)$ para todo $\theta \in \Omega$.
A ***lei dos grandes números** é um forte aliado, pois afirma que a média amostral converge em probabilidade para a média verdadeira.

5. **Convergência em distribuição:** Seja $\{X_n\}$ uma sequência de quantidades aleatórias e $X$ uma quantidade aleatória.
Se 
$$
\lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)],
$$
para toda função contínua limitada $f$, dizemos que $X_n$ converge em distribuição para $X$, isto é, $X_n \overset{D}{\to} X$.
Dizemos que a distribuição de $X$ é a **distribuição assintótica** de $X_n$.
Além do mais, dizemos que a distribuição de $X_n$ converge fracamente para a distribuição de $X$.

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

## Propriedades assintóticas MLE

- KN, Cap 8 e 9;
- SV, Cap 7.3.

- Cap 10.1.1 Cassela (467 - 470)
- Cap 8.1 Keener

### Distribuição assintótica de um estimador eficiente 

Assuma as hipóteses do teorema de Cramér-Rao. Seja $T$ um estimador eficiente para a sua média $m(\theta)$ e $m'(\theta) \neq 0$. Então: 

$$
\frac{[nI(\theta)]^{1/2}}{m'(\theta)}[T - m(\theta)] \overset{d}{\to} N(0,1)
$$

### Distribuição assintótica do MLE

Suponha que obtemos $\hat{\theta}_n$ resolvendo a equação $\lambda_n'(x|\theta) = 0$, isto é, maximizando a log-verossimilhança (MLE). E suponha que $\lambda_n''$ e $\lambda_n'''$ existem e satisfazem certas condições de regularidade. Então 

$$
[nI(\theta)]^{1/2}(\hat{\theta}_n - \theta) \overset{d}{\to} N(0,1)
$$

Como o MLE é não enviesado, então se ele for Eficiente, já sabemos que esse teorema é verdade pelo anterior. (se ele é não enviesado)

