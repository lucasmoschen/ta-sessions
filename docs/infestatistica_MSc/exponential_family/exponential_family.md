# Família exponencial

Em aplicações, a modelagem de fenômenos naturais por variáveis aleatórias gera a necessidade de obter a distribuição da variável aleatória, o que faz parte do processo de modelagem. 
Como uma forma de simplificação, usamos famílias de distribuições com propriedades conhecidas.
A mais conhecida de todas é a **família exponencial**, que inclui as distribuições mais conhecidas de nossos corações: normal, binomial, Poisson, gamma, entre outras.

## Densidade

Seja $h$ uma função não negativa e $T_1, \dots, T_k : \mathbb{R}^n \to \mathbb{R}$ funções mensuráveis.
Para $\theta \in \mathbb{R}^k$, defina 
$$
A(\theta) = \log \int_{\mathbb{R}^n} \exp\left[\sum_{i=1}^k \theta_i T_i(x)\right] h(x) \, d\mu(x).
$$
Se $A(\theta) < +\infty$, vale que 
$$
p_{\theta}(x) = h(x)\exp\left[\sum_{i=1}^k \theta_i T_i(x) - A(\theta)\right], x \in \mathbb{R}^n
$$
integra 1. 
> A família de distribuições $\{p_{\theta} : \theta \in \Theta\}$, em que $\Theta = \{\theta : A(\theta) < +\infty\}$, é chamada de **família exponencial** com $k$ parâmetros na **forma canônica**.
O conjunto $\Theta$ é chamado de **espaço de parâmetros natural**.

---
``📝`` **Exemplo de construção**
Sejam $h(x) = 1$ se $x > 0$ e $0$ caso contrário e $T_1(x) = x$.
Então
$$
A(\theta) = \log \int_0^{\infty} e^{\theta x} \, dx = \log(-1/\theta)
$$
que é bem definido se $\theta < 0$.
Logo
$$
p_{\theta}(x) = \exp(\theta x - \log(-1/\theta)) 1(x>0)
$$
é a densidade com $\theta < 0$.

---

Para situações mais gerais, seja uma função $\eta : \Omega \to \Theta$. 
A família exponencial é, então, 
$$
p_{\theta}(x) = h(x)\exp\left[\sum_{i=1}^k \eta_i(\theta) T_i(x) - B(\theta)\right],
$$
em que $B(\theta) = A(\eta(\theta))$.

## Identidade para os momentos

Seja $p_{\theta}$ uma densidade da família exponencial com formulação canônica.
Seja $\Theta_f \subseteq \Theta$ tal que $\mathbb{E}_{\theta}[|f(X)|] < +\infty$.
Então, a função 
$$
g(\theta) = \mathbb{E}_{\theta}[f(X)] 
$$
é contínua e com derivadas parciais de todas as ordens para $\theta$ no interior de $\Theta_f$ (mais do que isso, ela é [analítica](https://en.wikipedia.org/wiki/Analytic_function)).

A partir dessa propriedade com $f=1$, podemos concluir que 
$$
\mathbb{E}_{\theta}[T_j(X)] = \frac{\partial A(\theta)}{\partial \theta_j}.
$$

Também podemos obter que 

$$
\operatorname{Cov}_{\theta}(T_i, T_j) = \frac{\partial^2}{\partial \theta_i \partial \theta_j} A(\theta).
$$

## Propriedades

**Proposição:** Se $X$ tem uma distribuição da família exponencial, então a **estatística suficiente natural** $T(X)$ também é.
Em particular, a densidade é 
$$p_{T,\theta}(t) = \exp\{\theta \cdot t - A(\theta)\}.$$

- Para ver que $T(X)$ é estatística suficiente, basta aplicar a fatorização de Fisher-Neyman.
- Essa fatorização também permite a derivação da densidade da distribuição de $T$, que a define como pertencente à família exponencial.

**Teorema:** O espaço de parâmetros natural $\Theta$ é convexo e $\exp\{A(\theta)\}$ é uma função convexa.

> Agora um Teorema importante!

**Teorema:** Se o espaço dos parâmetros natural $\Theta$ de uma família exponencial contém um conjunto aberto em $\mathbb{R}^k$, então $T(X)$ é uma estatística suficiente completa.

## Teorema de caracterização

Seja $X=(X_1, \dots, X_n)$ uma amostra aleatória com densidade $f(x|\theta)$.
Seja $T$ uma estatística suficiente de dimensão 1.
Seja 
$$
f(x|\theta) = \prod_{i=1}^n f(x_i|\theta) = m_1(x)m_2(t,\theta)
$$
e defina 
$$
K_{\theta}(t) = \frac{\partial}{\partial \theta} \log m_2(t, \theta).
$$
Assuma que 

1) $C = \{x : f(x|\theta) > 0\}$ não depende de $\theta$.
2) A verossimilhança é diferenciável com respeito a $\theta$.
3) A densidade é diferenciável com respeito a $x$.
4) Existe $\theta_0$ tal que $K_{\theta_0}(t)$ é invertível.

Então $X$ tem uma distribuição da família exponencial com um parâmetro natural de dimensão $1$.
