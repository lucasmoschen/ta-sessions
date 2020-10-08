# Análise Bayesiana de amostras da distribuição Normal 

## Precisão da distribuição normal

Definimos $\tau := 1/\sigma^2$ como a precisão da distribuição normal.  

A função da densidade de probabilidade da distribuição normal $f(x|\mu,\tau)$ é, $-\infty < x < \infty$:  

$$
f(x|\mu,\tau) = \left(\frac{\tau}{2\pi}\right)^{1/2}\exp\left[-\frac{1}{2}\tau(x-\mu)^2\right]
$$

### Teorema 

Suponha que $X_1,...,X_n \overset{iid}{\sim}
N_2(\mu, \tau)$, desconhecidos. Suponha que 

$$
\mu|\tau \sim N_2(\mu_0, \lambda_0 \tau)
$$
$$
\tau \sim \text{Gamma}(\alpha_0, \beta_0)
$$

Então a distribuição conjunta de $\mu$ e $\tau$ a posteriori é dada por: 

$$
\mu|\tau, X_1,...,X_n \sim N_2(\mu_1, \lambda_1\tau)
$$
$$
\tau|X_1,...,X_n \sim \text{Gamma}(\alpha_1, \beta_1),
$$

onde 

|Parâmetro|Valor a posteriori do parâmetro|
|----||
|$\mu_1$|$\frac{\lambda_0 \mu_0 + n\bar{x}_n}{\lambda_0 + n}$|
|$\lambda_1$|$\lambda_0 + n$|
|$\alpha_1$|$\alpha_0 + n/2$|
|$\beta_1$|$\beta_0 + s_n^2/2 + \frac{n\lambda_0(\bar{x}_n - \mu_0)^2}{2(\lambda_0 + n)}$|

## Família Normal-Gamma

Sejam $\mu$ e $\tau$ variáveis aleatórias. Suponha que a distribuição condicional de $\mu$ dado $\tau$ é normal com média $\mu_0$ e precisão $\lambda_0 \tau$ e que a dstribuição marginal de $\tau$ seja gamma com parâmetros $\alpha_0, \beta_0$. Então, falamos que a distribuição conjunta de $\mu$ e $\tau$ é a distribuição **normal-gamma** com hiperparâmeteros $\mu_0, \lambda_0, \alpha_0$ e $\beta_0$.


```python
# Continua!
```
