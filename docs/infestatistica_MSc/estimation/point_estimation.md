# Estimação pontual

Um **estimator pontual** de uma $g(\theta)$ é uma estatística que toma valores em $\operatorname{Imagem}(g)$.

## Estimador não enviesado

Mais formalmente:

> Sejam $\Omega$ espaço de parâmetros de uma família paramétrica de distribuições $P_{\theta}$ e $g : \Omega \to G$ uma função mensurável (contínua, por exemplo). 
Uma função $\phi : \mathcal{X} \to G' \supseteq G$ é **estimador** de $g(\theta)$, em que $\mathcal{X}$ é o espaço amostral.
Dizemos que $\phi$ é **não enviesado** se 
> $$
\mathbb{E}_{\theta}[\phi(X)] = g(\theta), \forall \theta \in \Omega.
> $$
> Além do mais, o viés de um estimador é dado por $b_{\phi}(\theta) = \mathbb{E}_{\theta}[\phi(X)] - g(\theta)$.

Um estimador é uma função das amostras, enquanto uma **estimativa** é uma avaliação dessa função em observações.

---
``📝`` **Exemplo (Normal)**

Seja $X_1 \dots, X_n \overset{iid}{\sim} Normal(\mu, \sigma^2)$, em que $\theta = (\mu, \sigma^2) \in \mathbb{R} \times \mathbb{R}_+$ é o parâmetro.
Suponha que estamos interessados em $g(\theta) = \mu$.
Um estimador para $\mu$ é $\phi(X_1, \dots, X_n) = X_1$ ou $\phi(X_1, \dots, X_n) = \min\{X_i\}$. 
Todavia, um estimador com melhores propriedades, que veremos ao decorrer do curso, é $\phi(X_1, \dots, X_n) = \bar{X}$. 
Note que 
$$
\mathbb{E}_{\mu}[\bar{X}] = \frac{1}{n}\sum_{i=1}^n \mathbb{E}_{\mu}[X_i] = \mu,
$$
o que mostra que $\bar{X}$ é não enviesado.

---

Aparentemente, um estimador ser não enviesado parece muito bom, não é? Mas nem sempre isso é suficiente ou possível. 
No exemplo a seguir, mostramos que não existe estimador não enviesado para a taxa da distribuição exponencial.

---
``📝`` **Exemplo (Exponencial)**

Seja $X \sim Exponencial(\lambda)$, em que $\lambda \in \R_+$ é o parâmetro. 
Seja $\phi(X)$ um estimador não enviesado para $\lambda$.
Então
$$
\mathbb{E}_{\lambda}[\phi(X)] = \lambda \int_0^{+\infty} \phi(x) \exp(-\lambda x) \, dx = \lambda, \forall \lambda \in \R_+. 
$$
Dividindo ambos os lados por $\lambda$ e diferenciando com respeito a $\lambda$, pela [Regra de Leibniz](https://en.wikipedia.org/wiki/Leibniz_integral_rule):
$$
- \int_0^{+\infty} x\phi(x) \exp(-\lambda x) \, dx = 0.
$$
Mas $x\exp(-\lambda x) > 0, \forall x > 0$. 
Se $\phi(x) > 0$ em um conjunto de medida positiva, pelo que estudamos em [Integração](https://lucasmoschen.github.io/ta-sessions/infestatistica_MSc/probability/#integracao), teríamos que a integral deveria ser positiva, o que é um absurdo. 
Com isso $\phi(x) = 0$ quase certamente e, portanto, não é um estimador não enviesado. 
Concluímos que não pode haver um estimador não enviesado para $\lambda$.

---

Um estimador ser não enviesado implique que, na prática, se fossem feitos infinitos experimentos e calculássemos o valor do estimador, o valor médio convergiria para o valor verdadeiro do parâmetro. 
Isso ocorre pela Lei dos Grandes Números.
Mas na prática, fazemos uma quantidade finita de experimentos e isso pode impactar nossos resultados. 
No próximo exemplo, vamos mostras que um estimador não enviesado e vamos visualizar sua distribuição.

---
``📝`` **Exemplo (Correlação normal multivariada)**

Seja $(X_1, Y_1), \dots, (X_n,Y_n) \sim Normal(\boldsymbol{\mu}, \Sigma)$, com média $\mu = (0,0)$ e matriz de correlação $\Sigma = [[1, \rho], [\rho, 1]]$. 
Assim o parâmetro de interesse é a correlação entre $X$ e $Y$ $\rho \in [-1,1]$.
Considere o estimador para $\rho$ para $n$ amostras sendo
$$
\phi(X_1, \dots, X_n) = \dfrac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^n (X_i - \bar{X})^2}\sqrt{\sum_{i=1}^n (Y_i - \bar{Y})^2}},
$$
conhecido como **correlação empírica** ou **correlação de Pearson**.
Apesar de famoso, esse estimador tem viés não nulo. 
Todavia, pode-se corrigi-lo para obtermos um estimador não enviesado [(Olkin and Pratt, 1958)](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-29/issue-1/Unbiased-Estimation-of-Certain-Correlation-Coefficients/10.1214/aoms/1177706717.full),
da forma
$$
\psi = G(\phi) = \phi F\left(\frac{1}{2}, \frac{1}{2}; (n-1)/2; 1 - \phi^2\right),
$$
que tem a propriedade de não ser enviesado, em que $F$ é a função hipergeométrica de Gauss.
Como $\phi$ e $\psi$ são funções mensuráveis das amostras, eles também têm uma distribuição amostral.
Uma maneira de visualizar essas distribuições é através de simulações de Monte Carlo.

1) Geramos $n$ amostras $(X_i, Y_i)$ da normal multivariada.
2) Calculamos $\phi$ e $\psi$. 
3) Repetimos esse processo $M$ vezes e temos amostras da distribuição de $\phi$ e $\psi$.

```python
# Parâmetros
rho = 0.1
n = 30
M = 100000
phi_samples = np.zeros(M)
psi_samples = np.zeros(M)
# Gerando os dados de acordo com a distribuição especificada
rng = np.random.RandomState(1001)
for i in range(M):
    Z = rng.multivariate_normal(mean=[0,0], cov=[[1,rho], [rho,1]], size=n)
    X = Z[:,0]
    Y = Z[:,1]
    # Calculando ~ correlação de Pearson
    phi_samples[i] = np.corrcoef(X,Y)[0,1]
    psi_samples[i] = phi_samples[i] * hyp2f1(1/2, 1/2, (n-1)/2, 1 - phi_samples[i]**2)

# Desenhando as distribuições
plt.hist(phi_samples, label=r'$\phi$', color='pink', bins=50)
plt.hist(psi_samples, label=r'$\psi$', color='blue', bins=50)
plt.legend()
plt.show()
```

![png](output_3_0.png)
    

Nesse caso, temos que o Erro Absoluto Percentual Médio do estimador $\psi$ é, aproximadamente,  
$$
\mathbb{E}_{\rho}\left[\bigg|\frac{\psi - \rho}{\rho}\bigg|\right] \approx 150\%.
$$
Ou seja, apesar de $\psi$ ser não enviesado e $\phi$ ter viés baixo, a variância dos estimadores é bem grande. 
Nesse caso, temos uma probabilidade alta de obter uma estimação 100% maior ou menor do que o valor verdadeiro de $\rho$.

Note que a diferença entre os estimadores é pequena, pois $n$ é razoavelmente grande e $\psi$ tem viés baixo.

---

### Erro quadrático

Seja $L(\theta, d) = (\theta - d)^2$ a perda quadrática.
A função de risco $R(\theta, \phi)$ para o estimador $\phi(X)$ é dada por 
$$
\begin{split}
R(\theta, \phi) &= \mathbb{E}_{\theta}[(\theta-\varphi(X))^2] \\
&= \mathbb{E}_{\theta}[(\theta-\mathbb{E}[\varphi(X)] + \mathbb{E}[\varphi(X)] - \varphi(X))^2] \\
&= (\theta-\mathbb{E}[\varphi(X)])^2 + 2(\theta-\mathbb{E}[\varphi(X)])(\mathbb{E}_{\theta}[\mathbb{E}[\varphi(X)] - \varphi(X))] + \mathbb{E}_{\theta}[(\mathbb{E}[\varphi(X)] - \varphi(X))^2] \\ 
&= b_{\phi}(\theta)^2 + 2(\theta-\mathbb{E}[\varphi(X)])(\mathbb{E}[\varphi(X)]-\mathbb{E}[\varphi(X)]) + \operatorname{Var}(\phi(X)) \\
&= b_{\phi}(\theta)^2 + \operatorname{Var}(\phi(X)).
\end{split}
$$
Portanto, para estimadores não enviesados, o risco é dado somente pela variância do estimador.

## Estimação não enviesada de menor variância

> Um estimador não enviesado $\phi$ é **uniformly minimum variance unbiased estimator (UMVUE)** (estimador não enviesada de variância uniformemente mínima) se $\phi$ tem variância finita e, para todo estimador não enviesado, $Var_{\theta} \phi(X) \le Var_{\theta} \psi(X), \forall \theta \in \Omega$.

Essa definição leva ao seguinte importante teorema:

**Teorema (Lehmann-Scheffé):** Se $T$ é uma estatística completa, então todos os estimadores não enviesados de $g(\theta)$, que são funções de $T$, mas não de $X$, são iguais quase certamente para todo $\theta$.
Além disso, se existe um estimador não enviesado que é função de uma estatística suficiente completa, então ele é UMVUE.

Cap 5.1.1 Schervish (298 - 301)
Cap 7.3.2 Casella (330 - 342)
Cap 5.1 Keenet (61 - 66)

## Limites inferiores para a variância

Cap 5.1.2 Schervish (301  307)
Cap 4.5 Keener (71 - 77)

## Estimador de Máxima Verossimilhança

Cap 5.1.3 Schervish (307 - 309)
Cap 7.2.2 Casella (315 - 324)

Obs.: incluir alguns pensamentos de cap 7.3.3 Cassella (342 - 348)
