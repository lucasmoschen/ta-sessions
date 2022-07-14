# Funções de risco

Podemos ver a inferência estatística como a arte de aprender sobre uma quantidade desconhecida $\theta$ a partir de dados $X$, através de uma conexão definida a partir de um modelo probabilístico $X \sim P_{\theta}$. 
Para estudar a performance de estimadores de $g(\theta)$, conceito introduzido em [Estimação pontual](https://lucasmoschen.github.io/ta-sessions/infestatistica_MSc/estimation/point_estimation/), uma abordagem formalizada é a [Teoria da Decisão](https://lucasmoschen.github.io/ta-sessions/bayesian/decision-theory). 
Aqui introduziremos esses conceitos, mas uma visão mais geral sob a ótica de Inferência Bayesiana pode ser encontra [aqui](https://lucasmoschen.github.io/ta-sessions/bayesian/decision-theory).

> Seja $\mathcal{D}$ o espaço das decisões (por exemplo, uma estimativa é uma decisão) e $\Omega$ o espaço dos parâmetros. 
Uma função de perda é uma função $L : \Omega \times \mathcal{D} \to [0, +\infty]$ e avalia uma penalidade $L(\theta, d)$ em tomar a decisão $d$ com respeito a $\theta$. 
Quando $\mathcal{D} = h(\Omega)$, temos que $L(\theta, d)$ mede o erro em obter $h(\theta)$ por $d$.

Sendo $\phi(X)$ um estimador para $\theta$ (uma estatística que busca aproximá-lo), $L(\theta, \phi(X))$ é uma variável aleatória que pode ser grande, mesmo que $\delta$ seja um bom estimador. 
Com isso, definimos a **função de risco** $R$ como a perda média em usar $\phi(X)$ para estimar $\theta$
$$
R(\theta, \phi) = \mathbb{E}_{\theta}[L(\theta, \phi(X))], 
$$
isto é, tomando a esperança quando $X \sim P_{\theta}$.

---
``📝`` **Exemplo (caso binomial)**

Seja $X \sim Binomial(n, p)$ com $n$ conhecido. 
Um estimador para $p$ é $\phi(X) = X/n$.
Seja $L(\theta, d) = (\theta - d)^2$ a perda quadrática.
Assim, a função de risco para $\phi$ é 
$$
R(p, \phi) = \mathbb{E}_{p}[(p - X/n)^2] = Var_p(X/n) = \frac{np(1-p)}{n^2} = \frac{p(1-p)}{n}, p \in [0,1].
$$

---

A função de risco tem um problema clássico: é difícil comparar dois estimadores quaisquer, pois um pode ter risco menor em certas regiões e maior em outras.

---
``📝`` **Exemplos de riscos**

Para cada perda $L$, definimos um risco $R$. A seguir, temos alguns mais famosos.

- Perda quadrática ($L(\theta, d) = (\theta - d)^2$): mean squared error (erro médio quadrado) ou MSE.

- Perda absoluta ($L(\theta, d) = |\theta - d|$): mean absolute error (erro médio absoluto) ou MAE.

- Perda absoluta percentual ($L(\theta, d) = |\theta - d|/|\theta|$): mean absolute percentage error (erro médio absoluto percentual) ou MAPE.

- etc.

---
