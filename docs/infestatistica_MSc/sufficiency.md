# Estatística suficiente

Um estatístico usa a informação de uma amostra $X_1, \dots, X_n$ para fazer inferência sobre uma quantidade de interesse $\theta$.
De acordo com Fisher, em "On the Mathematical Foundations of Theoretical Statistics", "o objeto dos métodos estatísticos é a redução dos dados".
Como a quantidade de dados é incapaz de ser compreendida diretamente pelo cérebro, ela é reduzida por poucas quantidades que representam o todo, pelo menos a informação relevante para o problema. 
Nesse sentido, uma estatística é uma forma de representar esses dados, em geral diminuir sua dimensão (os próprios dados formam uma estatística, então isso não é uma condição necessária).
De forma precisa, a definição de **estatística** é:

> Seja $(\mathcal{T}, \mathcal{C})$ um espaço mensurável em que $\mathcal{C}$ contenha todos os conjuntos unitários formados pelo elementos de $\mathcal{T}$. Se $T : \mathcal{X} \to \mathcal{T}$ é mensurável, então $T$ é uma estatística.

Com isso, podemos definir uma **estatística suficiente** no sentido clássico (lembrando que temos uma contrapartida bayesiana baseada na posteriori).

> Seja $T: \mathcal{X} \to \mathcal{T}$ uma estatística e $\mathcal{P}$ uma família de distribuições parametrizada por $\theta$ e definida em $(\mathcal{X}, \mathcal{B})$ (espaço amostral com $\sigma$-álgebra $\mathcal{B}$). Suponha que existem $P_{\theta}(\cdot|T)$ e uma função $r : \mathcal{B} \times \mathcal{T} \to [0,1]$ tal que $r(\cdot, t)$ é uma medida de probabilidade em $(\mathcal{X}, \mathcal{B})$ para todo $t \in \mathcal{T}$, $r(A, \cdot)$ é mensurável para todo $A \in \mathcal{B}$ e, para todo $\theta \in \Theta$ e $B \in \mathcal{B}$,
> $$
P_{\theta}(B|T=t) = r(B,t)
> $$
> quase certamente. Então dizemos que $T$ é **estatística suficiente** para $\theta$.

Apesar dessa definição ser bastante complexa, a ideia é que a distribuição condicional de $X$ dado $T=t$ não depende de $\theta$, isto é, a informação trazida por $T=t$ sobre $\theta$ compreende toda a informação disponível de $X$.
Após observar $T(x) = t$, podemos amostrar de $r(\cdot, t)$ e teremos dados falsos que imitam os iniciais, pois a distribuição será a mesma.
Assim, se considerarmos dois experimentadores, um tendo a amostra inteira, e o outro tendo apenas uma estatística suficiente, ambos terão a mesma quantidade de informação sobre o parâmetro de interesse $\theta$.

Note que, pela lei da esperança total,
$$
P_{\theta}(X \in B) = \mathbb{E}_{\theta}[P_{\theta}(X \in B|T)] = \mathbb{E}_{\theta}[r(B, T)].
$$
Se tomarmos $Y \sim r(\cdot, t)$ quando $T=t$, teremos 
$$
P_{\theta}(Y \in B) = \mathbb{E}_{\theta}[P_{\theta}(Y \in B|T)] = \mathbb{E}_{\theta}[r(B, T)].
$$

**Proposição:** A estatística de ordem $(X_{(1)}, \dots, X_{(n)})$ é estatística suficiente.

## Fatorização de Fisher-Neyman

Seja $f(\boldsymbol{x}|\theta)$ a densidade de uma distribuição de $\boldsymbol{X} = (X_1, \dots, X_n)$ (com respeito a uma medida $\nu$ $\sigma$-finita, como a medida de Lebesgue em $\mathbb{R}^n$). Então $T(\boldsymbol{X})$ é estatística suficiente para $\theta$ se, e somente se, existem funções $m_1$ e m_2$ tal que 
$$
f(\boldsymbol{x}|\theta) = m_1(\boldsymbol{x})m_2(T(\boldsymbol{x}) , \theta), \forall \theta \in \Theta.
$$

O lema 2.24 demonstrado no livro de Schervish determina que sob as hipóteses do teorema de Fisher-Neyman e assumindo que $T$ é suficiente, obtemos que existe uma medida em $(\mathcal{T}, \mathcal{C})$ que domina a distribuição de probabilidade de $T$ e define a densidade de $T=t$ sob o parâmetro $\theta$ como $m_2(t,\theta)$.

## Estatística suficiente mínima

TODO

pg. 46 KN
pg. 305 CB
pg. 92 SH
