# Estatísticas Suficientes

A ideia por traś da estatística é, como o nome diz, ser suficiente. Uma estatística é uma função das variáveis aleatórias, como, por exemplo, $T = r(X_1, ..., X_n)$.  Média amostral, variância amostral, valor máximo, são todos exemplos. Imagine que temos um problema como o seguinte: 

Vamos imaginar que um estatístico dá um trabalho para seu estagiário para organizar os dados de forma mais eficiente possível, enquanto ele pensa no modelo. O estagiário de forma muito ingênua cria uma lista em seu Jupyter Notebook e salva o notebook com os dados na sua lista. Depois ele salva num arquivo `.txt` e vai para casa tranquilo que o trabalho acabou mais cedo. 

Será que era necessário ter salvo todos os dados? O estatístico no dia seuinte diz que não! E manda o estagiário estudar novamente estatística. Ele disse para estudar **Estatística Suficientes**.

### Definição Unidimensional

Seja $X_1, ..., X_n$ uma amostra aleatória de distribuição indexada pelo parâmetro $\theta$. Suponha que para todo valor que $\theta$ assume e para todo valor que $T$ assume (vamos chamar de $t = r(x_1, ..., x_n)$, nesse caso já observamos o processo e calculamos $t$), a distribuição conjunta condicional de $X_1, ...., X_n$ dado $T=t$ e $\theta$, isto é, dado que você observou uma estatística (a média de temperaturas, por exemplo) depende apenas de $t$, mas não de $\theta$. 

Isso significa que a distribuição é constante para todos os valores de $\theta$. Chamaremos essa estatística $T$ de suficiente para $\theta$. 

---

**Obs.:** Para quem estudou funções mensuráveis, podemos definir estatística como função mensurável dos dados. 

___

Seja $(\mathbb{T}, \mathbb{C})$ um espaço mensurável tal que $\mathbb{C}$ contém todos os conjuntos unitários. Se $T : \mathbb{X} \to \mathbb{T}$ é mensuável, então é uma estatística. 

Seja $\mathbb{P}_0$ uma familia paramétrica de distribuições em $(\mathbb{X}, \mathbb{B})$. Seja $(\Omega, \tau)$ um espaço dos parâmetros e $\Theta: \mathbb{P}_0 \to \Omega$ um parâmetro. Seja $T$ uma estatística. Ela é suficiente para $\Theta$ se para toda priori $\mu_{\Theta}$, existem versões da posteriori $\mu_{\Theta|X}$ e $\mu_{\Theta|T}$ tal que $\forall B \in \tau, \mu_{\Theta|X}(B|x) = \mu_{\Theta|T}(B|T(x))$, quase certamente convergente para $[\mu_X]$ onde $\mu_X$ é distribuição marginal de $X$. 

---

## Critério de Fatorização

Teorema atribuído a Neyman-Fisher. 

$X_1,...X_n$ amostra aleatória com pdf ou pmf $f(x|\theta)$, onde $\theta$ é desconhecido. Uma estatística $T = r(X)$ para $\theta$ é suficiente se, e somente se, a distribuição conjunta $f_n(x|\theta)$ pode ser fatorada para todo valor $x \in \mathbb{R}^n$ da seguinte forma: 

$$f_n(x|\theta) = u(x)v[r(x), \theta]$$

Onde $u$ e $v$ são não negativas, $u$ não depende de $\theta$ e $v$ só depende dos dados através da estatística. Isto é, não adianta você encontrar qualquer função de $x$, tem que encontrar a estatística $T$ em $v$. 

### Estatísticas Conjuntas Suficientes

Suponha que para cada $\theta$, vetor, e cada valor das estatísticas $(T_1, ..., T_k) = (t_1, ..., t_k)$ a distribuição conjunta condicional dos dados dadas as estatísticas não depende de $\theta$. Veja que nesse caso, a diferença é que condiciono em $k$ estatísticas, $k \geq 1 $. 

### Critério de Fatorização

Sejam $r_1, ..., r_k$ funções de $n$ variáveis. A estatísticas $T_i = r_i(X)$ são estatísticas suficientes conjuntas para $\theta$ se, e somene se, a pdf conjunta $f_n(x|\theta)$ pode ser fatorado como 

$$f_n(x|\theta) = u(x)v[r_1(x), ..., r_k(x),\theta], $$

para todos os valores $x \in \mathbb{R}^n$ e $\theta \in \Omega$

**Obs.:** Podemos mostrar que qualquer função injetiva de uma estatística suficiente é uma estatística suficiente. 

## Estatística Suficiente Mínima

### Estatística de Ordem

Considere uma amostra aleatória e a ordene. Diremos que a nova amostra, ordenada, é uma estatística de ordem. Observe que ela funciona como uma matrix de "shifts" que opera trocando as linhas do vetor de lugar. Por isso ela é uma função. 

Essa estatística é sufciente conjunta para $\theta$. O interessante que podemos ver isso dado que o produtório não importa a ordem. 

### Estatística Suficiente Mínima 

É uma estatística $T$ suficiente e, além disso, é função de todas as outras estatísticas suficientes.

### MLE e Estatística Suficiente 

Seja $T$ uma estatística suficiente para $\theta$. Então o estimador de máxima verossimilhança $\hat{\theta}$ depende das observações somente através da estatística $T$. Além disso, se $\hat{\theta}$ é suficiente, então é mínimo.  

### Estatísticas Suficientes e Estimador de Bayes

$T = r(X)$ estatística suficiente para $\theta$. Então todo estimador de Bayes $\hat{\theta}$ depende nas observações $X_1, ..., X_n$ apenas através da estatística $T$. Além do mais, se for suficiente, será suficiente mínimo. 

## Definições Adicionais 

Considere uma amostra aleatória $X_1,...,X_n$

____

### Estatística Completa

Seja $t = T(X)$ estatística. Se 

$$E[g(T(X))|\theta] = 0, \forall \theta \implies P[g(T(X)) = 0] = 1,$$

então ela é dita completa.
____
____

### Estatística Ancillary

Suponha que queremos estimar $\theta$ e $f_n(x|\theta)$ seja a pdf conjunta. Seja $A(X)$ uma estatística. Se a sua distribuição **não** depende de $\theta$, então será uma estatística ancillary (auxiliar?) 

Por exemplo, se $X_1, X_2 \sim N(\mu, \sigma^2)$ e  $\mu$ é desconhecido, temos que $X_1 - X_2 \sim N(0, 2\sigma^2)$ é uma estatística auxiliar. 

____

# Melhorando um Estimador 

___

Suponha que temos uma amostra aleatória $X = (X_1, ..., X_n)$ cuja pdf é $f(x|\theta)$ e $\theta \in \Omega$ desconhecido, tal que queremos estimar $h(\theta)$ para alguma função $h$. Seja $Z = g(X_1, ..., X_n)$. 

$$
E_{\theta}(Z) = \int_{-\infty}^{\infty}...\int_{-\infty}^{\infty} g(x)f_n(x|\theta)dx_1, ..., dx_n
$$

Para cada estimado $\delta(X)$ e para todo valor de $\theta$, definimos o MSE (Erro Médio Quadrático)

$$
R(\theta, \delta) = E_{\theta}\{[\delta(X) - h(\theta)]^2\}
$$

Quando não atribuímos uma priori para $\theta$, então queremos encontrar um estimador para que o MSE seja pequeno para vários valores de $\theta$. 

Seja $T$ uma estatística suficiente conhecida. Definimos 

$$
\delta_0(T) = E_{\theta}\{\delta(X)|T\} \overset{1}{=} E\{\delta(X)|T\}
$$

___

(1) Agora, por que podemos chamar $\delta_0$ de estimador se depende de $\theta$? 

Como $T$ é uma estatística suficiente, a distribuição condicionada em $T$ e em $\theta$ da amostra $X_1, ..., X_n$ não depende de $\theta$!!! Em particular o valor esperado do estimador $\delta(T)$. Logo, como esse valor esperado não depende de $\theta$, podemos dizer sim que ele é um estimador. 

## Teorema Rao - Blackwell 

Teorema 7.9.1 do livro.

Seja $\delta(X)$ um estimador e $T$ uma estatística suficiente para $\theta$. O estimador $\delta_0(T)$ definido acima, para todo valor $\theta \in \Omega$ é:

$$
R(\theta, \delta_0) \leq R(\theta, \delta),
$$

isto é, é um estimador com menor erro quadrático médio (MSE). Em particular se $R(\theta, \delta) < \infty$, a desigualdade se torna estrita, a menos que $\delta(X)$ seja um afunção de $T$, isto é, se $\delta(X)$ não for função de $T$, então a desigualdade será estrita. Por desigualdade estrita entenda $<$.

**Obs.:** Chamamos o processo de melhorar um estimador com esse teorema de "Rao-Blackwelliation".

---

**Obs.2:** Podemos generalizar um pouco mais. Para isso, pesquise sobre [Conjuntos Convexos](https://en.wikipedia.org/wiki/Convex_set) e sobre [Funções Convexas](https://en.wikipedia.org/wiki/Convex_function). Em um conjunto convexo, se a nossa função de perda não for o MSE, mas for uma função convexa, o teorema também valerá. Uma suposição interessante que o Livro não impõe é que $E[||\delta(X)||) < \infty$.

---

## Inadmissibilidade

Suponha que $R(\theta, \delta)$ é MSE. O estimador $\delta$ é **inadimissível** se existe outro estimador $\delta_0$ tal que $R(\theta, \delta_0) \leq R(\theta, \delta)$ para todo valor de $\theta$ e existe a desigualdade estrita em, **pelo menos um** valor de $\theta$. Dizemos nesse caso que $\delta_0$ **domina** o estimador $\delta$. Um estimador $\delta_0$ é **admissível** se não existe outro estimador que o domine. 
