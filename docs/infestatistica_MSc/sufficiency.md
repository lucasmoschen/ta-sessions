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

Seja $f(\boldsymbol{x}|\theta)$ a densidade de uma distribuição de $\boldsymbol{X} = (X_1, \dots, X_n)$ (com respeito a uma medida $\nu$ $\sigma$-finita, como a medida de Lebesgue em $\mathbb{R}^n$). Então $T(\boldsymbol{X})$ é estatística suficiente para $\theta$ se, e somente se, existem funções $m_1$ e $m_2$ tal que 
$$
f(\boldsymbol{x}|\theta) = m_1(\boldsymbol{x})m_2(T(\boldsymbol{x}) , \theta), \forall \theta \in \Theta.
$$

O lema 2.24 demonstrado no livro de Schervish determina que sob as hipóteses do teorema de Fisher-Neyman e assumindo que $T$ é suficiente, obtemos que existe uma medida em $(\mathcal{T}, \mathcal{C})$ que domina a distribuição de probabilidade de $T$ e define a densidade de $T=t$ sob o parâmetro $\theta$ como $m_2(t,\theta)$.

## Estatística suficiente mínima e completa

A estatística de ordem é uma estatística que pouco reduz a informação do dado. 
De fato, só retira a questão da ordenação. 
Todavia, algumas vezes uma estatística mais simples também é suficiente e, por isso, faz sentido definir quando ela é mínima.

> Uma estatística suficiente $T$ é dita **suficiente mínima** se para toda estatística $U$, existe uma função mensurável $g$ tal que $T = g(U)$ para todo $\theta$.

**Teorema (Lehmann-Scheffé):** Seja $f(x|\theta)$ a densidade e $T$ uma função mensurável tal que $T(x) = T(y) \iff y \in D(x)$, com
$$
D(x) = \{y \in \mathcal{X} : f(y|\theta) = f(x|\theta)h(x,y), \forall \theta \text{ e alguma função } h(x,y) \}.
$$

---
``📝`` **Exemplo**
}
Seja $X_1, \dots, X_n \overset{iid}{\sim} \operatorname{Bernoulli}(\theta)$. Temos que 
$$
f(x_1,\dots,x_n|\theta) = \theta^{S_x}(1-\theta)^{n-S_x},
$$
em que $S_x = \sum_{i=1}^n x_i$. 
Assim
$$
\frac{f(x_1,\dots,x_n|\theta)}{f(y_1,\dots,y_n|\theta)} = \left(\frac{\theta}{1-\theta}\right)^{S_x-S_y},
$$
que independe de $\theta$ se, e somente se, $S_x = S_y$. 
Isso mostra que $T(x) = S_x$ é estatística suficiente mínima.

---

---
``📝`` **Exemplo - Família Exponencial**

Considere uma distribuição com densidade 
$$
p_{\theta}(x) = \exp\{\eta(\theta)\cdot T(x) - B(\theta)\}h(x)
$$
com respeito a medida de Lebesgue. 
Pelo Teorema da Fatorização $T(x)$ é estatística suficiente.
Assim
$$
\log\left(\frac{p_{\theta}(y)}{p_{\theta}(x)}\right) = \eta(\theta)\cdot (T(y) - T(x)) + \log(h(y)) - \log(h(x)).
$$
Logo $T$ é estatística suficiente mínima se, e somente se, o complemento ortogonal de $\eta(\theta)$ possui apenas o $0$.

---

> Uma estatística $T$ é dita **completa** se para toda função $g$ mensurável e $\theta \in \Theta$, $\mathbb{E}_{\theta}[g(T)] = 0$ implique $g(T) = 0$. Ela será **completa limitada** se adicionamos a condição de que $g$ é limitada.

**Teorema de Bahadur:** Se $U$ é uma estatística suficiente completa limitada e de dimensão finita, então ela é suficiente mínima.

Ideias da demonstração:

- Tome uma outra estatística $T$ e defina $V_i(U) = (1 + \exp\{U_i\})^{-1}$ para cada componente de $U$. Note que $V$ é limitada.
- Defina $H_i(t)$ como o valor esperado de $V_i$ dado que $T=t$ e $L_i(u)$ como o valor esperado de  $H_i(T)$ quando $U=u$, que não dependem de $\theta$, pois as estatísticas são suficientes.
- Veja que $\mathbb{E}_{\theta}[V_i(U) - L_i(U)] = 0$, o que implica que $\mathbb{P}(V_i = L_i) = 1$ pois $U$ é completa.
- Conclua usando a Lei da Variância Total que $U_i = V_i^{-1}(H_i(T))$.

Note que se $U$ é completa, então $U$ é completa limitada, o que nos dá um resultado mais claro: Uma estatística suficiente e completa é suficiente mínima.

## Ancilaridade

Na outra ponta, temos estatísticas que são independentes do parâmetro.

> Uma estatística $U$ é dita anciliar se a sua distribuição independe de $\theta$.

---
``📝`` **Exemplo - Caso normal**

Sejam $X_1, X_2 \overset{iid}{\sim} \operatorname{Normal}(\mu, 1)$ e defina $U = X_2 - X_1$. Soma de normais independentes faz com que 
$U \sim \operatorname{Normal}(0, 2)$ e $U$ é anciliar.

---

Se $T=(T_1, T_2)$ é estatística suficiente mínima e $T_2$ é anciliar, dizemos que $T_1$ é **suficiente condicionalmente** dado $T_2$.

Quando uma estatística é anciliar, não significa que ela não tem importância e, portanto, deveria ser ignorada. 
Significa que se ela fosse a única observação possível, não mudaríamos a informação sobre $\theta$. 
Podemos, todavia, alterar a informação sobre outras quantidades, todavia.

Uma estatística ancilar $U$ é **maximal** se toda outra estatística ancilar é função de $U$.

**Teorema de Basu:** se $T$ é uma estatística suficiente completa limitada e $U$ é anciliar, então $U$ e $T$ são independentes sob $P_{\theta}$ para qualquer $\theta$.