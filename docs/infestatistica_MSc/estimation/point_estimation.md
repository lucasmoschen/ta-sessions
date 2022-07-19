# Estimação pontual

Um **estimator pontual** de uma $g(\theta)$ é uma estatística que toma valores em $\operatorname{Imagem}(g)$.
Mais formalmente:

> Sejam $\Omega$ espaço de parâmetros de uma família paramétrica de distribuições $P_{\theta}$ e $g : \Omega \to G$ uma função mensurável (contínua, por exemplo). 
Uma função $\phi : \mathcal{X} \to G' \supseteq G$ é **estimador** de $g(\theta)$, em que $\mathcal{X}$ é o espaço amostral.

Vamos explorar formas de comparar estimadores pontuais.

## Viés de um estimador

> Dizemos que $\phi$ é **não enviesado** se 
> $$
\mathbb{E}_{\theta}[\phi(X)] = g(\theta), \forall \theta \in \Omega.
> $$
> Além do mais, o viés de um estimador é dado por $b_{\phi}(\theta) = \mathbb{E}_{\theta}[\phi(X)] - g(\theta)$.
> Se existe um estimador não enviesado para $g(\theta)$, dizemos que $g$ é U-estimável.

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

Seja $X \sim Exponencial(\lambda)$, em que $\lambda \in \mathbb{R}_+$ é o parâmetro. 
Seja $\phi(X)$ um estimador não enviesado para $\lambda$.
Então
$$
\mathbb{E}_{\lambda}[\phi(X)] = \lambda \int_0^{+\infty} \phi(x) \exp(-\lambda x) \, dx = \lambda, \forall \lambda \in \mathbb{R}_+. 
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
A [função de risco](https://lucasmoschen.github.io/ta-sessions/infestatistica_MSc/risk_function/) $R(\theta, \phi)$ para o estimador $\phi(X)$ é dada por 
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

Note que quando queremos avaliar o melhor estimador, estamos lidando com uma classe bem grande para comparar. 
Por exemplo, o estimador $\hat{\theta} = 0$ para todo $\theta$ tem o menor MSE em $\theta = 0$, mas é um estimador horrível quando $\theta$ se afasta de zero.
Nesse, sentido uma forma de avaliar estimadores é restringindo a classe de interesse. 
Uma classe considerada razoável é a dos estimadores não enviesados.
Nesse caso, os MSEs serão iguais às variâncias dos estimadores.

> Um estimador não enviesado $\phi$ é **uniformly minimum variance unbiased estimator (UMVUE)** (estimador não enviesado de variância uniformemente mínima) se $\phi$ tem variância finita e, para todo estimador não enviesado, $Var_{\theta} \phi(X) \le \operatorname{Var}_{\theta} \psi(X), \forall \theta \in \Omega$.

Essa definição leva ao seguinte importante teorema:

**Teorema (Lehmann-Scheffé):** Se $T$ é uma estatística completa, então todos os estimadores não enviesados de $g(\theta)$, que são funções de $T$, mas não de $X$, são iguais quase certamente para todo $\theta$.
Além disso, se existe um estimador não enviesado que é função de uma estatística suficiente completa, então ele é UMVUE.

---
Ideia da prova: Sejam $\phi_1(T)$ e $\phi_2(T)$ estimadores não enviesados de $g(\theta)$. 
Então $\mathbb{E}_{\theta}[\phi_1(T) - \phi_2(T)] = 0$ para todo $\theta$.
Como $T$ é uma estatística completa, vale que $\phi_1(T) = \phi_2(T)$ quase certamente.
Agora suponha que $T$ é estatística suficiente completa e seja $\phi(T)$ um estimador não enviesado.
Tome um estimador não enviesado $\psi(X)$ e defina $\phi'(T) = \mathbb{E}[\psi(X)|T]$. Usando a perda quadrática, pelo [Teorema de Rao-Blackwell](https://lucasmoschen.github.io/ta-sessions/infestatistica_MSc/sufficiency/sufficiency/#teorema-de-rao-blackwell), $\operatorname{Var}_{\theta}(\phi ') = R(\theta, \phi ') \le R(\theta, \psi) = \operatorname{Var}_{\theta}(\psi)$ para todo $\theta$.
Portanto $\phi '$ é UMVUE. Além disso, como acabamos de provar, $\phi = \phi '$ quase certamente e, portanto, também é UMVUE.

---

Note que basta a existência de um estimador não enviesado $\delta$ e de uma estatística completa $T$ para que encontremos um estimador UMVUE usando Rao-Blackwell:
$$
\phi(T) = \mathbb{E}_{\theta}[\delta(X) | T].
$$

Considere o exemplo para o caso normal.

---
``📝`` **Exemplo (Distribuição normal - ela de novo)**

Seja $X_1, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$ e $\theta = (\mu, \sigma^2)$.
Então
$$
\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2
$$
são estatísticas suficientes e completas, além de serem estimadores não enviesados para $\mu$ e $\sigma^2$ respectivamente.
Pelo Teorema acima, qualquer função deles é um UMVUE pelo resultado acima, para $\mu$ e $\sigma^2$, respectivamente.
Todavia, é possível verificar que $S^2$ não minimiza o erro quadrado.

*Obs.: para mostrar a suficiência, o Teorema da Fatorização é suficiente. Já a completude vem do fato de que o espaço de parâmetros natural contém um conjunto aberto em $\mathbb{R}^2$*.

---

Quando não existem estatísticas completas, o seguinte resultado pode ser útil:

**Teorema:** Uma condição suficiente e necessária para que um estimador $\delta$ de $\mathbb{E}_{\theta} \delta(X)$ seja UMVUE é que para todo $U$ que satisfaça $\forall \theta, \mathbb{E}_{\theta}[U] = 0$, valha que $\operatorname{Cov}_{\theta}(\delta(X), U(X)) = 0$

---
``📝`` **Exemplo (Bernoulli)**

Seja $X_1, \dots, X_n \sim \overset{iid}{\sim} Bernoulli(\theta)$.
Temos que $T(X) = \sum_{i=1}^n X_i$ é uma estatística suficiente completa para $\theta$.
Além disso, sabemos que $T(X) \sim Binomial(n,\theta)$.
Em particular, $T$ é estatística completa, pois o espaço de parâmetros natural da distribuição binomial tem interior não vazio.
Considere $g(\theta) = \theta^2$. 
Um estimador não enviesado para $g$ é $\delta(X) = X_1 X_2$.
Nesse caso, o estimador UMVUE de $g$ é $\mathbb{E}[\delta(X)|T]$, isto é, 
$$
\phi(T) = \mathbb{E}_{\theta}[X_1X_2|T] = \mathbb{P}_{\theta}(X_1 = 1, X_2 = 1 | T = t).
$$
Podemos calcular essa probabilidade pela definição de probabilidade condicional, mas vamos fazer isso intuitivamente.
Temos $n$ espaços e $t$ bolinhas para preencher $t$ desses espaços. 

- Quantas formas eu tenho de posicionar as bolinhas? $n \choose t$. 

- Quantas dessas formas eu tenho interesse? Posiciono duas bolinhas nas primeiras posições (veja que preciso de $t \ge 2$) e tenho $n-2 \choose t-2$ formas de posicionar as outras bolinhas. Portanto:

$$
\mathbb{P}_{\theta}(X_1 = 1, X_2 = 1 | T = t) = \frac{(n-2)(n-3)\cdots(n-t+1)\cdot t(t-1)\cdots 1}{(t-2)(t-1)\cdots 1 \cdot n(n-1)\cdots(n-t+1)} = \frac{t(t-1)}{n(n-1)}.
$$

Portanto, o estimador $\phi(T) = T(T-1)/(n^2 - n)$ se $T \ge 2$ e $\phi(T) = 0$ se $T \le 1$ é UMVUE para $g(\theta) = \theta^2$.

---

## Método dos Momentos

O método de momentos é uma abordagem para derivar estimadores para os parâmetros do modelo a partir dos dados.
Ele é simples para ser definido, mas pode apresentar vários problemas como estimador.
Considere uma amostra aleatória $X = (X_1, \dots, X_n)$ com densidade $f_n(x|\theta)$, com $\theta \in \Omega \subseteq \mathbb{R}^k$.
Então, o estimador do método de momentos para $\theta$ é a solução do sistema 
$$
m_i = \mu_i(\theta), i=1,\dots,k,
$$
em que $m_i = \sum_{j=1}^n X_j^i$ é o $i$-ésimo momento empírico da amostra e $\mu_i(\theta) = \mathbb{E}_{\theta}[X^i]$, 
isto é, dada uma observação, estamos igualando momentos empíricos aos momentos da distribuição.

Um problema com o método de momentos é que ele nem sempre provê estimativas no espaço dos parâmetros. 
Isso pode acontecer se a variabilidade nos dados é muito grande.

## Estimador de Máxima Verossimilhança

Outro método para derivar estimadores é o de maximar a função de verossimilhança.

> Seja $X$ uma variável aleatória cuja distribuição tem densidade $f(x|\theta)$.
Se $X=x$ é observado, a função do parâmetro $L(\theta|x) = f(x|\theta)$ é a **função de verossimilhança**.
O **estimador de máxima verossimilhança (MLE)** de $\theta$ é o valor 
$$
\hat{\theta} = \operatorname{arg}\max_{\theta \in \Omega} f(x|\theta),
$$
isto é, é o valor do parâmetro em $\Omega$ que maximiza a função de verossimilhança.

---
``📝`` **Exemplo (Uniforme)**

Considere $X_1, \dots, X_n \overset{iid}{\sim} \operatorname{Unif}(0,\theta)$, cuja densidade é 
$$
f_n(x|\theta) = \frac{1}{\theta^n}I_{[0,\theta]}(\max_{i} x_i).
$$
Supondo observada a amostra, queremos encontrar $\theta \ge \max_i x_i$ (caso contrário, a densidade se anularia) que maximize $\theta^{-n}$. 
Isso acontece quando $\theta$ é mínimo. 
Nesse caso, $\hat{\theta} = \max_i x_i$.
Observe que se tivéssemos tomado intervalo aberto, ao invés de fechado, teríamos que $\theta > \max_i x_i$, mas não poderia ser igual de fato.
Nessa situação, não existe MLE, visto que para qualquer $\theta > \max_i x_i$, existe $\theta '$ tal que $\theta > \theta ' > \max_i x_i$.

---

Mesmo quando o MLE existe, não há garantias de que ele é único.
Porém, se ele existe, ele satisfaz a seguinte propriedade chamada de **invariância**

**Teorema:** Seja $g : \Omega \to G$ uma função mensurável.
Suponha que exista um espaço $U$ e uma função $h : \Omega \to G \times G'$ bijetiva tal que $h(\theta) = (g(\theta), g'(\theta))$ para alguma função $G$.
Se $\hat{\theta}$ é MLE de $\theta$, então $g(\hat{\theta})$ é MLE de $g(\theta)$.

Note que uma consequência direta é que transformações bijetivas levam MLEs em MLEs.

Note que $\hat{\theta}$ maximiza a verossimilhança se, e somente se, maximiza o logaritmo da verossimilhança. 
Com isso, temos uma abordagem mais simples para encontrar o MLE de distribuições da família exponencial, pois 
$$
\log L(\theta|x) = \log h(x) - A(\theta) + x\cdot \theta.
$$
Se o MLE $\hat{\theta}$ ocorre no interior do espaço de parâmetros natural, as derivadas parciais de $\log L(\theta)$ se anulam em $\theta = \hat{\theta}$.
Em particular, 
$$
x = \nabla A(\theta) = \mathbb{E}_{\theta}[X],
$$
como visto [aqui](https://lucasmoschen.github.io/ta-sessions/infestatistica_MSc/exponential_family/exponential_family/#identidade-para-os-momentos), o que implica que o MLE de $\theta$ é o valor tal que $x = \mathbb{E}_{\hat{\theta}}[X]$.

Portanto o procedimento padrão para encontrar o MLE é o seguinte:

1. Verificar se a verossimilhança tem alguma estrutura que facilite maximizar, como no caso da distribuição uniforme.

2. Tomar o logaritmo da verossimilhança e encontrar o ponto crítico derivando e igualando a zero para pontos no interior do espaço de parâmetros.

3. Verificar condições de suficiência para os pontos críticos. Por exemplo: segunda derivada negativa (ou Hessiana no caso de multivariada negativa definida). 

4. Verificar a fronteira se necessário.

5. Utilizar recursos numéricos.