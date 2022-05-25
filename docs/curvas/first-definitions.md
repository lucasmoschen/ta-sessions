# Definições preliminares 

Quando pensamos em curvas, em geral, expressamos como uma equação, como, por exemplo, 

$$
x^2 + y^2 = 1 
$$
que é uma circunferência 

<img alt = "circle" src = "/ta-sessions/curvas/first-definitions_files/circle-curve.png" width = 200> 

ou a reta $y = ax + b$. Chamamos essas curvas de **curvas de nível**, aquelas que são do tipo $f(x,y) = c$ para alguma função $f:\mathbb{R}^2 \to \mathbb{R}$ continua. Isso se deve ao fato de que a curva é o conjunto de pontos no plano cuja quantidade $f(x,y)$ atinge o nível $c$. Todavia uma definição um tanto melhor é pensar em uma curva como um caminho traçado por um ponto se movimentando, conceito que é formalizado a seguir.

**Curva parametrizada:** Seja $I$ um intervalo. Uma curva parametrizada é uma aplicação contínua $\alpha: I \subset \mathbb{R} \to \mathbb{R}^n$, muitas vezes notada como $\alpha(t) = (\alpha_1(t), ..., \alpha_n(t))$ e $t$ é chamado de parâmetro. Algumas definições pedem intervalo aberto. Dizemos que ela é **diferenciável** quando a aplicação é diferenciável. Por fim dizemos que a curva é **regular** quando $\alpha '(t) \neq 0, \forall t \in I$.

**Observação:** Definições de curva podem variar em cada livro. Alguns livros pedem que a aplicação seja de classe $C^{\infty}$ ou suave, enquanto outras pedem apenas classe $C^2$ e assim por diante. De forma geral exigir apenas a continuidade é mais fraco e podemos pedir diferenciabilidade ou suavidade posteriormente. 

**Traço da curva:** Seja uma curma $\alpha:I \to \mathbb{R}^n$. Dizemos que o traço de $\alpha$ é a imagem da aplicação $\alpha$, denotada $\alpha(I)$. Algumas definições de curva são precisamente o que definimos de traço da curva. 


```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='arbitrary parametric curve')
ax.legend()

plt.show()
```

![png](first-definitions_files/first-definitions_2_0.png)


## Encontrando parametrizações

### Exemplo 1

Vamos encontrar uma parametrização para a *parábola*  $y = x^2$ na reta. Seja $\gamma(t) = (\gamma_1(t), \gamma_2(t))$. Pela relação, temos que $\gamma_2(t) = \gamma_1(t)^2, \forall t \in \mathbb{R}$. Uma solução trivial é colocar $\gamma_1(t) = t$. Nesse caso, $\gamma(t) = (t,t^2)$ é uma curva cujo traço é uma parábola. Observe que essa **não é a única parametrização**. Por exemplo $(\frac{t}{2}, \frac{t^2}{4})$ também é uma parametrização na reta. Isso levanta uma questão: temos duas parametrizações diferentes para a mesma curva. Como dizer que elas são iguais, em um certo sentido, já que suas imagens são iguais? 

### Exemplo 2 

Considere a curva [astroide](https://en.wikipedia.org/wiki/Astroid) dada pela pela equação $x^{2/3} + y^{2/3} = 1$. Uma maneira é propor a parametrização dada por $x(t) = t$ e $y(t) = (1 - t^{2/3})^{3/2}.$ Primeiro temos que observar que $t \in [-1,1]$ devido a raiz quadrada que tomamos na expressão - o valor dentro do parênteses não pode ser negativo. Em particular $y$ não pode ser negativo nessa parametrização. Isso não corresponde a imagem total da curva, pois $y^{2/3} + x^{2/3} = 1$ é simétrico em relação ao dois eixos. 

Poderíamos tentar adaptar essa parametrização, mas o mais conveniente é lembrar da identidade trigonométrica $cos^2(t) + sen^2(t) = 1$. Assim podemos escrever que $(cos(t)^3)^{2/3} + (sen(t)^3)^{2/3} = 1$. Como consequência $(cos^3(t), sen^3(t))$ é uma parametrização da astroide. Note que essa curva é contínua e definida em toda reta. 


```python
# Astroid
fig = plt.figure(figsize = (5,5))
ax = plt.subplot()
ax.grid(alpha=.5)

t = np.linspace(-np.pi, np.pi,100)
x = np.cos(t)**3
y = np.sin(t)**3

ax.plot(x, y, label='Astroid')
ax.axvline(x = 0, color = 'grey', alpha = .7)
ax.axhline(y = 0, color = 'grey', alpha = .7)
ax.legend()

plt.show()
```


![png](first-definitions_files/first-definitions_4_0.png)


## Vetor tangente

Em geral, quando estudamos curvas e superfícies, é comum encontrar o termo *suave* associado. A definição de função suave varia em cada contexto e pode ir desde uma função diferenciável com derivada contínua até função que tem derivada de qualquer ordem (sempre considerando o intervalo $I$ de definição). 

Lembre que se $\gamma(t) = (\gamma_1(t), ..., \gamma_n(t)$, a derivada de $\gamma$ é 
$$\dot{\gamma(t)} = (\dot{\gamma_1}(t), ..., \dot{\gamma_n}(t)).$$

**Vetor tangente:** Seja $\alpha$ uma curva parametrizada. Sua primeira derivada $\dot{\alpha}(t)$ é chamada de vetor tangente a cada tempo $t$. 

### Proposição 

Se o vetor tangente de uma curva parametrizada é constante, então o traço da curva é parte de uma reta. De fato se $\dot{\alpha}(t) = c$, onde $c$ é um vetor constante, pelo teorema fundamental do cálculo, 
$$
\alpha(t) = \int_{t_0}^t \dot{\alpha}(s)ds = (t - t_0)c = ct + d, d = - t_0 c, t_0 \in I
$$
Se $c \neq 0$, esta é a equação paramétrica de um segmento de reta (potencialmente infinito). Se $c = 0$, a imagem da curva é um único ponto. 

## Comprimento de arco 

Definimos o comprimento de arco de uma curva $\gamma$ começando no ponto $\gamma(t_0)$ como a função 
$$
s(t) = \int_{t_0}^t ||\dot{\gamma}(s)||ds
$$
Se escolhermos um ponto $\tilde{t}_0$ diferente, o resultado será diferente. 

Dizemos que a curva tem **velocidade unitária** (ou é parametrizada pelo comprimento de arco    ) se $||\dot{\gamma}(t)|| = 1$

## Reparametrização

Sejam $I$ e $J$ intervalos. Uma **mudança de parâmetro** é uma função $h: J \to I$ bijetiva contínua com inversa contínua. Em particular, uma função com essa propriedade é chamada de **homeomorfismo**. 

Sejam $\tilde{\gamma}:J \to \mathbb{R}^n$ e $\gamma: I \to \mathbb{R}^n$ dua curvas. Dizemos que $\tilde{\gamma}$ é reparametrização da curva $\gamma$ se existe uma mudança de parâmetro $h$ tal que 
$$
\tilde{\gamma} = \gamma \circ h 
$$
Essa notação significa que $\forall t \in J, \tilde{\gamma}(t) = \gamma(h(t))$. Observe que se $\tilde{\gamma}$ é reparametrização de $\gamma$, essa é reparametrização da primeira. 

**Observação:** Dependendo em como definimos curva, existem variações nessa definição. De forma geral, podemos dizer que duas curvas de classe $C^k$ são equivalentes, isto é, uma é reparametrização da outra, quando existe uma mapa bijetivo de classe  $C^k$ com inversa também de classe $C^k$ tal que a igualdade acima é válida em todo ponto. Para mais detalhes, consulte o [Wikipedia](https://en.wikipedia.org/wiki/Curve#Differential_geometry). 

Lembre que uma curva pode ter muitas parametrizações, mas nem todas são reparametrizações uma da outra, como no exemplo a baixo: 

**Exemplo:** Considere as seguintes parametrizações da circunferência: 
$$
\alpha(t) = (cos(t), sen(t)), t \in [0,2\pi]
$$
$$
\beta(t) = (cos(2t), sen(2t)), t \in [0,2\pi]
$$
A segunda parametrização "dá uma volta a mais na circunferência". Devemos nos perguntar se existe uma mudança de parâmetro $h$ entre esses intervalos que garanta 
$$
cos(2t) = cos(h(t))
$$
$$
sen(2t) = sen(h(t))
$$
Não conseguimos fazer isso e manter a bijetividade de $h$ entre os intervalos. Uma solução para esse problema seria considerar o domínio de $\beta$ o intervalor $[0,\pi]$. Nesse caso $h(t) = 2t$ é uma mudança de parâmetro entre as parametrizações. 

### Proposições importantes 

Tente demonstrar essas proposições:

1. Toda reparametrização de uma curva regular é regular. 
2. O comprimento de uma curva diferenciável regular não muda depois de uma reparametrização. 

### Teorema da reparametrização 

Uma curva parametrizada tem uma reparametrização com velocidade unitária se, e somente se, é regular. 

### Demonstração

Um rascunho da demonstração supondo a regularidade da curva. Seja $\alpha$ uma curve (diferenciável). Queremos encontrar $\beta : J \to \mathbb{R}^n$ tal que $\beta = \alpha \circ h$ para algum $h$ **difeomorfismo** (bijeito diferenciável com inversa diferenciável). Se existesse, ele deveria ter o seguinte comportamento, 
$$
||\beta '(t)|| = ||\alpha'(h(t))h'(t)|| = 1, 
$$
por hipótese. Dado $t_0 \in I, t \in I, $ 
$$
s(t) := \int_{t_0}^t ||\alpha '(\tau)||d\tau
$$
é uma função crescente e derivável, pois $\alpha$ é regular. Então ela possui uma função inversa $t: s(I) \to I$ também crescente e derivável, de forma que 
$$
t'(s) = \frac{1}{\frac{ds}{dt}(t(s))} = \frac{1}{s'(t(s))} = \frac{1}{||\alpha'(t(s))||}
$$
Então defina $\beta: s(I) \to \mathbb{R}^n$ de forma que $\beta(s) = \alpha(t(s))$. Então, 
$$
||\beta'(s)|| = ||\alpha'(t(s))t'(s)|| = 1
$$
Então a mudança de parâmetro que estávamos procurando era a inversa da função de comprimento de curva. 

## Curvas fechadas

### Curva T-periódica

Seja $T \in \mathbb{R}$. Dizemos que uma curva suave $\alpha : \mathbb{R} \to \mathbb{R}^n$ é T-periódica se 
$$
\alpha(t + T) = \alpha(t), t \in \mathbb{R}
$$
Se $\alpha$ é não constante, mas T-periódica, com $T \neq 0$, então ela é dita **fechada**. Dizemos que o período da curva fechada é o menor número positivo $T$ tal que $\alpha$ seja T-periódica. 

**Exemplo:** A elipse é um exemplo onde o perído é $2\pi$. 

### Auto-intersecção

Uma curva $\alpha$ tem uma auto-intersecção no ponto $p$ se existem $a \neq b$ tal que $\alpha(a) = \alpha(b) = p$ e se $\alpha$ é fechada com período $T$, então $a - b$ não é um inteiro múltiplo de $T$. 