# Método Delta

O método Delta é uma importante forma de encontrar a distribuição assintótica de estatísticas de interesse. 
Em termos gerais, se uma estatística converge para uma distribuição normal, então uma função diferenciável também convergirá, com média e variâncias definidas através dessa função.
Por exemplo, sabemos que 
$$
\sqrt{n}\left(\bar{X}_n - \mu\right) \to N(0, \sigma^2),
$$
pelo Teorema Central do Limite, em que $\mu = \mathbb{E}[X_1]$, $\sigma^2 = \operatorname{Var}(X_1)$, $X_1, \dots, X_n$ é uma amostra aleatória e $\bar{X}_n$ é a média amostral.
O método delta diz que, para uma função $g$ diferenciável, 
$$
\sqrt{n}\left(g(\bar{X}_n) - g(\mu)\right) \to N(0, g'(\mu) \sigma^2),
$$
desde que $g'(\mu) \neq 0$.