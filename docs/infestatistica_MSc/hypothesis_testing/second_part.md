# Teste de Hipóteses: Alguns testes

Agora que já definimos os principais conceitos de teste de hipótese, vamos discutir algun casos particulares:

1. Teste de Razão de Verossimilhança
2. Teste de Hipóteses Simples 
3. Karlin-Rubin
4. Hipótese Alternativa Bilateral
5. Teste T
6. Comparando médias de duas Normais
7. Comparando variâncias de duas Normais

## Teste de Razão de Verossimilhança

Se $L(\theta | x)$ é a verossimilhança de um modelo para $X_1, \dots, X_n$, considere a estatística
$$
\lambda(x) = \frac{\sup_{\theta \in \Theta_0} L(\theta|x)}{\sup_{\theta \in \Theta} L(\theta|x)},
$$
para o teste $H_0: \theta \in \Theta_0$ contra $H_1 : \theta \in \Theta_1 = \Theta - \Theta_0$.
A região de rejeição desse teste é do tipo 
$$
{x : \lambda(x) \le c},
$$
com $c$ dado de forma que $\Pr_{\theta \in \Theta_0}(\lambda(X) \le c) \le \alpha$.


## Teste de Hipótese Simples

Uma hipótese $H_i : \theta \in \Omega_i$ é dita **simples** se $\Omega_i$ contém um único parâmetro $\theta_i$.
Nesse caso, o espaço $\Omega$ é formada por duas distribuições concorrentes.
Isto é, vamos assumir que $X = (X_1, ..., X_n)$ vem de $f_0(x)$ ou $f_1(x)$. 
Assim $\Omega = \{\theta_0, \theta_1\}$ e $\theta = \theta_i$ se os dados tem distribuição $f_i(x), i = 0,1$. 

A função poder para um teste $\delta$ é denotada da seguinte forma:

$$
\alpha(\delta) = P(\text{Rejeitar} H_0|\theta = \theta_0) = P(\text{Erro I}) = \int \delta(x) f_0(x) \, dx,
$$
$$
\beta(\delta) = P(\text{Não rejeitar} H_0|\theta = \theta_1) = P(\text{Erro II}) = \int \delta(x) f_1(x) \, dx.
$$

**Teorema:** Seja $\delta^*$ o procedimento de teste que não rejeita $H_0$ se $af_0(x) > bf_1(x)$ e rejeita se $af_0(x) < bf_1(x)$. Então, para todo outro procedimento de teste $\delta$, 
$$
a\alpha(\delta^*) + b\beta(\delta^*) \le a\alpha(\delta) + b\beta(\delta) 
$$

Queremos escolher um teste que minimize essa combinação linear $a\alpha(\delta) + b\beta(\delta)$. Claro que seria ótimo ter esse erro zerado, mas sabemos que existe uma espécie de *trade off* entre esses erros. Esse teorema dá o teste necessário para que isso acontença. 

**Corolário:** Considere as hipóteses do teorema anterior, $a > 0$ e $b > 0$. Defina estatística de teste **razão de verossimilhança**:
$$
\Lambda(x) = \begin{cases}
              \frac{f_0(x)}{f_1(x)}, \text{ se } f_0(x) \le f_1(x) \\
              1, \text{ caso contrário }. 
\end{cases}
$$
Defina o procedimento de teste $\delta$: Rejeita $H_0$ se $\Lambda(x) > a/b$. Então o valor de $af_0(x) + bf_1(x)$ é mínimo.  

### Lema Neyman-Pearson

Suponha que $\delta '$ tem a seguinte forma, para algum $k > 0$: $H_0$ não é rejeitada se $f_1(x) < kf_0(x)$ e o é quando $f_1(x) > kf_0(x).$ Se $\delta$ é outro procedimento de teste tal que $\alpha(\delta) \le \alpha(\delta ')$, então $\beta(\delta) \ge \beta(\delta ').$

---
``📝`` **Exemplo inicial**

Considere a densidade
$$
p_{\theta}(x) = \theta e^{-\theta x} 1\{x > 0\}.
$$
Considere a Hipotese Nula $H_0 : \theta = 1$ e a Alternativa $H_1 : \theta = \theta_1 > 1$.
Rejeitamos a hipótese nula se
$$
\frac{p_{\theta_1}(x)}{p_1(x)} = \frac{\theta_1 e^{-\theta_1 x}}{e^{-x}} > k,
$$
em que $k$ é determinado de forma que
$$
\alpha = \Pr_0\left(\theta_1 e^{-(\theta_1-1) x} > k\right) =\Pr_0\left( x < -\frac{\log(k/\theta_1)}{\theta_1-1} \right) = 1 - \exp\left\{\frac{\log(k/\theta_1)}{\theta_1-1}\right\},
$$
para um $\alpha$ pre-especificado.
Pelo Lema de Neyman Pearson, qualquer outro procedimento com nível $\alpha$ reduz o poder do teste.

---

### Implementação 

Vamos fazer uma simples implementação de uso para esse tipo de problema. 

```python
import numpy as np 
from scipy.stats import bernoulli, binom
from scipy.optimize import brute
```

Nesse caso, vamos fazer uma simples simulação, onde um parâmetro de uma distribuição de Bernoulli pode ser $p = 0.4$ ou $p = 0.6$. Vamos gerar essa amostra, mas sem de fato conhecer $p$ verdadeiro.


```python
ro = np.random.RandomState(1000000) #random state 
p = ro.choice([0.4, 0.6])
```

Teremos uma amostra de tamanho $n$.


```python
n = 20
X = ro.binomial(1, p, size = n)
```

Vamos utilizar o Lema Neyman-Pearson. O objetivo é testar as seguintes hipóteses: 

$$
H_0: p = 0.4
$$
$$
H_1: p = 0.6
$$

Vamos fixar $\alpha_0 = 0.05$ o tamanho do teste. Temos que, se $y = \sum_{i=1}^n x_i \sim Binomial(n,p)$, 

$$
\frac{f_1(x)}{f_0(x)} = \frac{0.6^y0.4^{n-y}}{0.4^y0.6^{n-y}} = \left(\frac{3}{2}\right)^y\left(\frac{2}{3}\right)^{n-y} = \left(\frac{3}{2}\right)^{2y - n}
$$

Assim:

$$
\begin{split}
0.05 &= P(f_1(x) > kf_0(x)|p = 0.4) = P\left(\left(\frac{3}{2}\right)^{2y - n} > k\right) \\
&= P\left(2y - n > \frac{\log(k)}{\log(3/2)}\right)  \\
&= P\left(y > \frac{\log(k)}{2\log(3/2)} + \frac{n}{2}\right), y \sim Binomial(n,0.4)
\end{split}
$$

Isto é, preciso escolher $k$ que satisfaça essa relação. Vamos calcular $k$ numericamente utilizando um método de otimização por bruta força (são poucas as opções). Como não queremos que seja marior do que 0.05, precisamos colocar peso para que não seja. Veja que existem vários valores de $k$ que satisfazem isso. 

```python
alpha0 = 0.05 
Y = binom(n = n, p = 0.4)

func = lambda k, n: np.abs(0.95 - Y.cdf((1/2)*np.log(k)/np.log(3/2) + n/2)) + \
                    10*(0.95 > Y.cdf((1/2)*np.log(k)/np.log(3/2) + n/2))
```

```python
k = brute(func, ranges = (slice(1,20,1),), args = (n,))[0]
k
```
    6.0

Por esse motivo, vamos tomar $k=6$. Pela Lema de Neyman Pearson, esse teste é o que minimiza o Erro do Tipo II.  

Vamos ver se rejeitamos ou não a hipótese nula baseado nos dados obtidos. 


```python
f0 = lambda x: 0.4**(sum(x))*0.6**(len(x) - sum(x))
f1 = lambda x: 0.6**(sum(x))*0.4**(len(x) - sum(x))

if f1(X) > k*f0(X):
    print(r'Rejeitamos H0.')
else:
    print(r'Não rejeitamos H0.')
```

    Não rejeitamos H0.

Vamos ver quem é $p$, então. 

```python
print('O valor de p é .... ')
print(p)
```
    O valor de p é .... 
    0.4

Fizemos bem em não rejeitar a hipótese nula!

## Karlin-Rubin

O Teorema de Karlin-Rubin estende o Lema de Neyman-Pearson para hipóteses compostas.
Assim, considere $H_0 : \theta \le \theta_0$ contra $H_1 : \theta > \theta_0$. 
Se $T$ é uma estatística suficiente para $\theta$ e a familia de pdfs $\{g(t|\theta) : \theta \in \Theta\}$ de $T$ tem razão de verossimilhanças crescentes, então para todo $t_0$, o teste que rejeita $H_0$ se $T > t_0$ é UMP com nível $\alpha$, em que $\alpha = \Pr_{\theta_0}(T > t_0)$.

## Hipótese Alternativa Bilateral 

Seja $X = (X_1, ..., X_n)$ uma amostra aleatória de uma distribuição normal com média $\mu$ desconhecida e variância $\sigma^2$ conhecida e queremos testar a hipótese 
$$
H_0: \mu = \mu_0
$$
$$
H_1: \mu \neq \mu_0
$$

Como $\bar{X}_n$ é um estimador consistente de $\mu$, faz sentido rejeitar a hipótese nula quando a média amostral se afasta de $\mu_0$. Para isso, vamos escolher $c_1, c_2$ de forma que 

$$
\begin{split}
    P(\bar{X}_n \leq c_1|\mu = \mu_0) + P(\bar{X}_n \geq c_2|\mu = \mu_0) = \alpha_0 &\Rightarrow P\left(Z \leq \sqrt{n}\frac{c_1 - \mu_0}{\sigma}\right) + P\left(Z \geq \sqrt{n}\frac{c_2 - \mu_0}{\sigma}\right) = \alpha_0 \\
    &\Rightarrow \Phi\left(\sqrt{n}\frac{c_1 - \mu_0}{\sigma}\right) + 1 -  \Phi\left(\sqrt{n}\frac{c_2 - \mu_0}{\sigma}\right) = \alpha_0 \\
    &\Rightarrow \Phi\left(\sqrt{n}\frac{c_1 - \mu_0}{\sigma}\right) = \alpha_1 \text{ e } \Phi\left(\sqrt{n}\frac{c_2 - \mu_0}{\sigma}\right) = 1 - \alpha_2, \text{ com } \alpha_1 + \alpha_2 = \alpha_0 
\end{split}
$$

*Observação:* $\bar{X}_n \sim N(\mu, \sigma^2/n) \Rightarrow Z = \sqrt{n}\frac{\bar{X}_n - \mu}{\sigma} \sim N(0,1)$

*Observação 2:* No cálculo substituimos $\mu$ por $\mu_0$, porque estamos "condicionando" no conhecimento deles serem iguais. 

Isto é, queremos que o tamanho do teste seja $\alpha_0$, lembrando que o tamanho do teste é o supremo das probabilidades de se rejeitar a hipótese nula quando ela é verdadeira. 

## Teste t

Suponha que $(X_1,...,X_n)$ é uma amostra aleatória da distribuição $N(\mu,\sigma^2)$, com parâmetros desconhecidos e queremos testar a hipótese:
$$
H_0: \mu \le \mu_0 \implies \Omega_0 = \{(x,y) \in \mathbb{R}^2 | x \le \mu_0 \text{ e } y > 0\}
$$
$$
H_1: \mu > \mu_0 \implies \Omega_1 = \{(x,y) \in \mathbb{R}^2 | x > \mu_0 \text{ e } y > 0\}
$$

Sabemos que $U = n^{1/2}\frac{\bar{X}_n - \mu_0}{\sigma '}$ é uma boa estatística de teste e rejeitamos $H_0$ se $U \ge c$. Essa estatística é interessante porque quando $\mu = \mu_0, U \sim t(n-1)$. Por isso chamamos de testes t quando baseados na estatística $U$. Podemos também inverter os sinais de desigualdade e rejeitar $H_0$ quando $U \le c$. 

```python
from pandas import DataFrame
from scipy.stats import t
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

%matplotlib notebook
```

```python
mu0 = 10
# Vamos escolher mu e sigma de forma aleatória, mas não significa que é uma variável aleatória. 
n = 20
```

### Distibuição de U

Vamos gerar uma aproximação para a distribuição de $U$ para um determinado $\mu$. 

```python
U_values = {}
for i in range(6):
    mu = ro.normal(mu0, 1) if i < 5 else 10
    sigma = ro.exponential(mu0) 
    key = 'mu = {}, sigma = {}'.format(np.round(mu,2), np.round(sigma,2))
    U_values[key] = np.zeros(10000)
    for j in range(10000):
        X = ro.normal(mu, sigma, size = n)
        U = np.sqrt(n)*(np.mean(X) - mu0)/np.std(X, ddof = 1)
        U_values[key][j] = U
U_values = DataFrame(U_values)
```

```python
fig, ax = plt.subplots(figsize = (10,6))
sns.kdeplot(data = U_values, ax = ax)
ax.set_title('Distribuição aproximada de U')
plt.show()
```

![png](output_23_0_2.png)

**Teorema:** Seja $c$ o $1 - \alpha_0$ quartil da distribuição $t$ com $n-1$ graus de liberdade. Então, segundo o teste citado acima, a função poder tem as seguintes propriedades: 

1. $\pi(\mu, \sigma^2|\delta) = \alpha_0$, quando $\mu = \mu_0$.
2. $\pi(\mu, \sigma^2|\delta) < \alpha_0$, quando $\mu < \mu_0$.
3. $\pi(\mu, \sigma^2|\delta) > \alpha_0$, quando $\mu > \mu_0$.
4. $\pi(\mu, \sigma^2|\delta) \to 0$, quando $\mu \to -\infty$.
5. $\pi(\mu, \sigma^2|\delta) \to 1$, quando $\mu \to \infty$.

O teste também é não enviesado como consequência.

### P-valores para testes t

Seja $u$ a estatística $U$ quando observada. Seja $T_{n-1}(\cdot)$ a cdf da distribuição t com $n-1$ graus de liberdade. Então o p-valor para $H_0: \mu \leq \mu_0$ é $1 - T_{n-1}(u)$, enquanto o p-valor para $H_0: \mu \ge \mu_0$ é $T_{n-1}(u)$. 

### Distribuição t não central 

O objetivo é encontrar a distribuição de $U$ mesmo quando $\mu \neq \mu_0$. Seja $W$ e $Y$ variáveis aletórias independentes com distribuição $N(\psi, 1)$ e $\chi^2(m)$, respectivamente. Então 
$$
X = \frac{W}{\left(\frac{Y}{m}\right)^{1/2}}
$$
tem distribuição t não central com $m$ graus de liberdade e não centralidade $\psi$. Denotaremos $T_m(x|\psi)$ a cdf dessa distribuição.  

**Teorema: (Função Poder):** Seja $X_1, ..., X_n$ amostra aleatória de $N(\mu,\sigma^2)$. A distribuição de $U$ é t não central com $n-1$ graus de liberdade e parâmetro de não centralidade $\psi = n^{1/2}(\mu - \mu_0)/\sigma$ 
(*Observe que isso ocorre porque dividimos o numerador e o denominador por $\sigma$. Além disso, note que $X$ não é uma quantidade pivotal, dado que sua distribuição depende de parâmetros desconhecidos*)
Suponha que o procedimento $\delta$ rejeita $H_0: \mu \le \mu_0$ se $U \ge c$. Então a função poder é 
$$\pi(\mu,\sigma^2|\delta) = 1 - T_{n-1}(c,\psi)$$ 
Se $\delta '$ rejeita $H_0: \mu \ge \mu_0$ se $U \le c$. Então a função poder é 
$$\pi(\mu,\sigma^2|\delta) = T_{n-1}(c,\psi)$$


```python
from scipy.stats import nct #noncentral t distribution
from matplotlib import animation
from IPython.display import HTML
import warnings

warnings.filterwarnings('ignore')
```

```python
n = 10
mu0 = 5
sigma = 2
psi = lambda mu: np.sqrt(n)*(mu - mu0)/sigma
```

```python
X = nct(df = n-1, nc = psi(-20))
```

Vamos ver o que acontece quando variamos $\mu$. Nesse caso $-20 \leq \mu \geq 20$. 

```python
fig, ax = plt.subplots()

x = np.linspace(X.ppf(0.01), 
                X.ppf(0.99), 100)

line, = ax.plot(x, X.pdf(x), 'r-', lw=5, alpha=0.6)

ax.set_xlim((-60,60))
ax.set_ylim((0,0.3))
ax.set_title('t não central')

def animate(i,n):
    
    x = np.linspace(-60, 60, 100)
    line.set_data(x, nct.pdf(x, df = n-1, nc = psi(i-20)))
    
    return line,

HTML(animation.FuncAnimation(fig, animate, frames = 40,
                               interval = 100, fargs=(n,), repeat = False).to_html5_video())
```

<video width="432" height="288" controls autoplay>
  <source type="video/mp4" src="data:video/mp4;base64,AAAAIGZ0eXBNNFYgAAACAE00ViBpc29taXNvMmF2YzEAAAAIZnJlZQAAOF1tZGF0AAACrgYF//+q
3EXpvebZSLeWLNgg2SPu73gyNjQgLSBjb3JlIDE2MCByMzAxMSBjZGU5YTkzIC0gSC4yNjQvTVBF
Ry00IEFWQyBjb2RlYyAtIENvcHlsZWZ0IDIwMDMtMjAyMCAtIGh0dHA6Ly93d3cudmlkZW9sYW4u
b3JnL3gyNjQuaHRtbCAtIG9wdGlvbnM6IGNhYmFjPTEgcmVmPTMgZGVibG9jaz0xOjA6MCBhbmFs
eXNlPTB4MzoweDExMyBtZT1oZXggc3VibWU9NyBwc3k9MSBwc3lfcmQ9MS4wMDowLjAwIG1peGVk
X3JlZj0xIG1lX3JhbmdlPTE2IGNocm9tYV9tZT0xIHRyZWxsaXM9MSA4eDhkY3Q9MSBjcW09MCBk
ZWFkem9uZT0yMSwxMSBmYXN0X3Bza2lwPTEgY2hyb21hX3FwX29mZnNldD0tMiB0aHJlYWRzPTYg
bG9va2FoZWFkX3RocmVhZHM9MSBzbGljZWRfdGhyZWFkcz0wIG5yPTAgZGVjaW1hdGU9MSBpbnRl
cmxhY2VkPTAgYmx1cmF5X2NvbXBhdD0wIGNvbnN0cmFpbmVkX2ludHJhPTAgYmZyYW1lcz0zIGJf
cHlyYW1pZD0yIGJfYWRhcHQ9MSBiX2JpYXM9MCBkaXJlY3Q9MSB3ZWlnaHRiPTEgb3Blbl9nb3A9
MCB3ZWlnaHRwPTIga2V5aW50PTI1MCBrZXlpbnRfbWluPTEwIHNjZW5lY3V0PTQwIGludHJhX3Jl
ZnJlc2g9MCByY19sb29rYWhlYWQ9NDAgcmM9Y3JmIG1idHJlZT0xIGNyZj0yMy4wIHFjb21wPTAu
NjAgcXBtaW49MCBxcG1heD02OSBxcHN0ZXA9NCBpcF9yYXRpbz0xLjQwIGFxPTE6MS4wMACAAAAO
LWWIhAAQ//73gb8yy18iuslx+ed9LKzPPOQ8cl2JrrjQAAADAAzyh/DyFGoDL4wAuOMTZI/VtrrF
ouviByP/ph4AWHldEUIMBr6evR/AbNzAls/wpTXU5/dAN5BIJXIy35Y5jl75M5KIK8SAOet7gXWn
ckQw6/PUG6QTNpMCTdWvly9f7n/4noESTgImAFgkntBK+/Hp/OP29RXFKBLZygfPjMT0lf2mXKk8
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
AAAAHWRhdGEAAAABAAAAAExhdmY1OC40NS4xMDA=
">
  Your browser does not support the video tag.
</video>

![png](output_30_1.png)

### Alternativa Bilateral 

Tome agora a hipótese
$$
H_0: \mu = \mu_0
$$
$$
H_1: \mu \neq \mu_0
$$

Podemos usar a mesma estatística $U$, mas agora que temos dois lados, vamos fazer o seguinte processo (vou construir de forma intuitiva, no livro tem uma formalização): 

1. O procedimento de teste é do tipo: Rejeitamos $H_0$ se $U \le c_1$ ou $U \ge c_2$. Vamos considerar $c_1 = -c$ e $c_2 = c$, para simplificar.   

2. Seja $\alpha_0$ o tamanho do teste, isto é, a probabilidade de rejeitarmos a hipótese nula quando $\mu = \mu_0$. Quando $\mu = \mu_0$, $U$ tem distribuição t com $n-1$ graus de liberdade. Assim: 

$$
P(|U| \ge c|\mu = \mu_0) = \alpha_0 = P(U \le -c) + P(U \ge c) \overset{simetria}{=} 2P( U \ge c) = 2(1 - P(U \le c))
$$

```python
n = 20
alpha0 = 0.05 
c = t.ppf(df = n-1, q = 1 - alpha0/2)
```

```python
X = t(df = n-1)
x = np.arange(-5,5,0.1)
plt.plot(x, X.pdf(x))
plt.fill_between(x[(x < -c)], X.pdf(x[(x < -c)]), color = 'blue')
plt.fill_between(x[(x > c)], X.pdf(x[(x > c)]), color = 'blue')
plt.title('Distribuição de U e Região de Rejeição')
plt.show()
```

![png](output_33_0.png)

### Função Poder 

$$\pi(\mu,\sigma^2,|\delta) = T_{n-1}(-x|\psi) + 1 - T_{n-1}(c|\psi)$$

### P-valor

Seja $u$ o valor observado da variável $U$. Vamos lembrar que o p-valor é o menor tamanho $\alpha_0$ tal que se rejeita a hipótese com esse valor observado. Como só rejeitamos se:

$$
|u| \ge c = T_{n-1}^{-1}(1 - \alpha_0/2) \implies \alpha_0 \ge 2 - 2T_{n-1}(|u|)
$$

Logo o p-valor é $2 - 2T_{n-1}(|u|)$.

## Comparando médias de duas normais

Assumimos que $X = (X_1,...,X_m)$ é uma amostra da distribuição normal com média $\mu_1$ e variância $\sigma^2$, enquanto $Y = (Y_1, ..., Y_n)$ é normal com média $\mu_2$ e variância $\sigma^2$. Estamos interessados no teste 
$$
H_0: \mu_1 \le \mu_2
$$
$$
H_1: \mu_1 > \mu_2
$$
A função poder é dada por $\pi(\mu_1, \mu_2, \sigma^2|\delta)$. A discussão quando as normais tem diferentes normais será postergada. 

Defina 
$$
S_x = \sum_{i=1}^m (X_i - \bar{X}_m)^2
$$
$$
S_y = \sum_{i=1}^n (Y_i - \bar{Y}_n)^2
$$
$$
U = \frac{(m + n - 2)^{1/2}(\bar{X}_m - \bar{Y}_n)}{\left(\frac{1}{n} + \frac{1}{m}\right)^{1/2}(S_x^2 + S_y^2)^{1/2}}
$$

A distribuição: $U \sim t$ com $m + n - 2$ graus de liberdade, com parâmetro de não centralidade
$$
\psi= \frac{\mu_1 - \mu_2}{\sigma\left(\frac{1}{m} + \frac{1}{n}\right)^{1/2}}
$$

Note que se $\mu_1 = \mu_2$, $U$ é uma distribuição t padrão.

### Função Poder

Considere o procedimento de teste $\delta$ que rejeite $H_0$ se $U \ge T_{m+n-2}^{-1}(1 - \alpha_0)$. Assim:

1. $\pi(\mu_1, \mu_2, \sigma^2|\delta) = \alpha_0$, quando $\mu_1 = \mu_2$.
2. $\pi(\mu_1, \mu_2, \sigma^2|\delta) < \alpha_0$, quando $\mu_1 < \mu_2$.
3. $\pi(\mu_1, \mu_2, \sigma^2|\delta) > \alpha_0$, quando $\mu_1 > \mu_2$.
4. $\pi(\mu_1, \mu_2, \sigma^2|\delta) \to 0$, quando $\mu_1 - \mu_2 \to -\infty$.
5. $\pi(\mu_1, \mu_2, \sigma^2|\delta) \to 1$, quando $\mu_1 - \mu_2 \to \infty$.

Além do mais o teste é não enviesado. 

### P-valor

Depois de termos observado as amostras, seja $u$ a estatística observada de $U$. O p-valor da hipótese é $1 - T_{m+n-2}(u)$.

> Equivalentemente com o teste t do item 3, podemos expressar tudo com a hipótese bilateral e só altera o graude liberade quando comparado com o teste t anterior.  

### Variâncias diferentes

#### Razão entre as variâncias é conhecida

Suponha que se as variâncias de $X$ e $Y$ são $\sigma_1^2$ e $\sigma_2^2$ e que $\sigma^2_2 = k\sigma^2_1, k > 0$. Então podemos usar a estatística 

$$
U = \frac{(m + n - 2)^{1/2}(\bar{X}_m - \bar{Y}_n)}{\left(\frac{1}{n} + \frac{k}{m}\right)^{1/2}(S_x^2 + \frac{S_y^2}{k})^{1/2}}
$$

#### Problema de Behrens-Fisher

Quando os 4 parâmetros das normais são desconhecidos, tão pouco a razão de variâncias, nem a estatística de razão de verossimilhança tem distribuição conhecida. Algumas tentativas já foram feitas, como [Welch](https://en.wikipedia.org/wiki/Welch%27s_t-test) e [outros](https://en.wikipedia.org/wiki/Behrens%E2%80%93Fisher_problem#Other_approaches).

## Comparando variâncias de duas Normais

Assumimos que $X = (X_1,...,X_m)$ é uma amostra da distribuição normal com média $\mu_1$ e variância $\sigma^2$, enquanto $Y = (Y_1, ..., Y_n)$ é normal com média $\mu_2$ e variância $\sigma^2$. Estamos interessados no teste 
$$
H_0: \sigma_1^2 \le \sigma_2^2
$$
$$
H_1: \sigma_1^2 > \sigma_2^2
$$
A função poder é dada por $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta)$. COnsidere $S_x^2$ e $S_y^2$ definidos anteriormente. Então temos que $S_x^2/(m-1)$ é estimador para $\sigma_1^2$, enquanto $S_y^2/(n-1)$ é estimador para $\sigma_2^2$.

Defina 
$$
V = \frac{S_x^2/(m-1)}{S_y^2/(n-1)}
$$

Rejeitaremos $X_0$ se $V \ge c$, onde $c$ será escolhido para que esse teste tenha nível de significância $\alpha_0$. Esse teste é chamado de teste F, pois a distribuição de $(\sigma_1^2/\sigma_2^2)V$ é F com parâmetros $m-1$ e $n-1$. Em particular se $\sigma_1^2 = \sigma_2^2$, $V$ tem distribuição F. Onde a [distribuição F é descrita aqui](https://lucasmoschen.github.io/TA_sessions/infestatistica_BSc/SamplingDistribution/SamplingDistribution/#distribuicao-f). 

### Função Poder

Considere o procedimento de teste $\delta$ que rejeite $H_0$ se $V \ge F_{m-1,n-1}^{-1}(1 - \alpha_0)$. Assim:

1. $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta) = 1 - F_{m-1,n-1}(\frac{\sigma_2^2}{\sigma_1^2}c)$
2. $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta) = \alpha_0$, quando $\sigma_1^2 = \sigma^2_2$.
3. $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta) < \alpha_0$, quando $\sigma_1^2 < \sigma_2^2$.
4. $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta) > \alpha_0$, quando $\sigma^2_1 > \sigma_2^2$.
5. $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta) \to 0$, quando $\sigma_1^2/\sigma_2^2 \to 0$.
6. $\pi(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2|\delta) \to 1$, quando $\sigma_1^2/\sigma_2^2 \to \infty$.

Além do mais o teste é não enviesado. 

### P-valor

Depois de termos observado as amostras, seja $v$ a estatística observada de $V$. O p-valor da hipótese é $1 - F_{m-1,n-1}(v)$.