# Teoria da Decisão

Em geral, a estatística se preocupa em propor uma decisão frente a um problema apresentado. 
Nesse caso, a avaliação deve estar clara, como, por exemplo, com a descrição do procedimento e suas consequências. 
A Teoria da Decisão entra para axiomatizar a estrutura de avaliar um estimador para algum parâmetro. 
O critério para avaliar uma tomada de decisão é usualmente através de uma **função de perda**. 
Alguns estatísticos discordam de usá-la, justamente porque defini-la para um problema pode levar a resultados inesperados. 

Seja $\mathcal{D}$ o espaço das decisões (por exemplo, uma estimativa é uma decisão) e $\Omega$ o espaço dos parâmetros.
Uma função de perda é uma função $L : \Omega \times \mathcal{D} \to [0, +\infty]$ e avalia uma penalidade $L(\theta, d)$ em tomar a decisão $d$ com respeito a $\theta$. 
Quando $\mathcal{D} = h(\Omega)$, temos que $L(\theta, d)$ mede o erro em obter $h(\theta)$ por $d$.
Escolher uma função de perda de maneira a considerar o problema em questão não é uma tarefa fácil. 
A complexidade envolvida em defini-la a partir de conceitos subjetivos leva ao uso de perdas matematicamente tratáveis, como a perda quadrática ou absoluta, por exemplo.

Então, em uma inferência bayesiana, do ponto de vista da Teoria da Decisão, os três fatores principais são: a família paramétrica de distribuições das observações, a distribuição a priori dos parâmetros, e a função de perda associada às decisões. Inclusive a subjetividade em definir a função de perda e a priori não pode ser separada, conforme destacado por [Lindley (1985)](https://www.wiley.com/en-us/Making+Decisions%2C+2nd+Edition-p-9780471908081). 

---
``📝`` **Exemplo (Função de perda)**

Considere o problema de estimar a $\mathbb{E}[x] = \theta$, em que $x \sim Normal(\theta, \sigma^2)$, em que $\sigma^2$ é conhecido.
Nesse caso, $\mathcal{D} = \Omega = \mathbb{R}$. 
Uma ideia é usar a perda da forma 
$$L\left(\frac{\delta - \theta}{\sigma}\right), \delta \in \mathcal{D}, \theta \in \Omega,$$
em que o mínimo de $L$ é em 0. Além disso, a divisão pelo desvio padrão reduz o viés de variância grande, principalmente quando a dimensão de $\theta$ aumenta. 
Usualmente $L(t) = t^2$ é a perda escolhida.

---

## Função utilidade

Utilidade é definida como o oposto de perda e é utilizada quando se pretende ordenar consequências de decisões. 
Ou seja, a utilidade sumariza os possíveis resultados de uma decisão, como, por exemplo, o lucro da empresa.
Seja $\mathcal{R}$ o espaço das recompensas, que assumimos possuir uma ordenação total $\le$ de forma que para todo $r_1, r_2 \in R$, tem-se que $r_1 \le r_2$ ou $r_2 \le r_1$ e $r_1 \le r_2$ com $r_2 \le r_3$ implica $r_1 \le r_3$. 
A primeira propriedade permite comparar qualquer duas recompensas, enquanto a segunda é a transitividade e fixa uma noção que esperaríamos de recompensas.

Agora, vamos estender essa noção de ordem para $\mathcal{P}$, o espaço das distribuições de probabilidade em $\mathcal{R}$.
Assumimos que $\le$ está disponível em $\mathcal{P}$ e que satisfaz 

(H1) ordem total;

(H2) transitividade.

No caso, de certa forma, $\mathcal{R} \subseteq \mathcal{P}$ através das distribuições de Dirac com massa em um ponto $r \in \mathcal{R}$ específico.

Queremos construir uma função $U$ em $\mathcal{R}$ que chamaremos de **função de utilidade** através da relação $\le$. 
Através da seguinte axiomatização, conseguimos assegurar tal existência.
Observe que se a relação 
$$\mathbb{E}^{P_1}[U(r)] \le \mathbb{E}^{P_2}[U(r)]$$
for equivalente a $P_1 \le P_2$, então conseguimos determinar a existência dessa relação em $\mathcal{P}$, o que dá uma espécie de recíproca do que queremos encontrar.

Considere o conjunto das distribuições definidas em um suporte limitado $\mathcal{P}_{B}$. 
Uma mistura é definida como $P = \alpha P_1 + (1-\alpha)P_2$, em que $\alpha \in (0,1)$. 
Assumimos que

(H3) Se $P_1 \le P_2$, temos que $\forall P \in \mathcal{P}$, $\alpha P_1 + (1-\alpha) P \le \alpha P_2 + (1-\alpha) P$.

(H4) Se $P_1 \le P_2 \le P_3$, então existem $\alpha, \beta \in (0,1)$ de forma que, 
$$\alpha P_1 + (1-\alpha) P_3 \le P_2 \le \beta P_1 + (1-\beta)P_3.$$ 

Note que H4 implica que se $r_1 \le r \le r_2$ com $r_1 < r_2$, então existe um único $\alpha \in [0,1]$ de forma que $r = \alpha r_1 + (1-\alpha)r_2$. Para demonstrar esse resultado, basta supor a não existência e usar um argumento de supremo e ínfimo associado à hipótese de (H4). 
Com esse resultado, dados $r_1 < r_2$, defina $U$ da seguinte forma:
$$
\begin{cases}
    U(r) = v, &\text{se } r_1 \le r \le r_2 \text{ e } r = vr_2 + (1-v)r_1 \\
    U(r) = -\frac{v}{1-v}, &\text{se } r \le r_1 \text{ e } r_1 = vr_2 + (1-v)r \\
    U(r) = \frac{1}{v}, &\text{se } r_2 \le r \text{ e } r_2 = vr + (1-v)r_1.
\end{cases}
$$

Com essa definição, temos que $U(r_1) = 1$ e $U(r_2) = 0$. 
Além do mais, $U$ preserva relação de ordem e se $r = \alpha r_1 + (1-\alpha)r_2$, então teremos que $U(r) = \alpha U(r_1) + (1-\alpha) U(r_2)$.

Agora, precisamos extender a definição de $U$ para $\mathcal{P}_{B}$, o que existe uma hipótese adicional. 
Defina 
$$
\alpha(r) = \frac{U(r) - U(r_1)}{U(r_2) - U(r_1)}, \beta = \int_{[r_1, r_2]} \alpha(r) dP(r),
$$
em que $P([r_1, r_2]) = 1$. 
Note que $\alpha$ é obtido a partir das relações do parágrafo anterior, isto é, sabemos que para cada $r$, existe $\alpha(r)$, de forma que $r = \alpha(r) r_1 + (1-\alpha(r))r_2$ e obtemos $\alpha$ através da fórmula $U(r) = \alpha(r) U(r_1) + (1-\alpha(r)) U(r_2)$.
Além disso $\beta$ indica a probabilidade de selecionarmos $r_1$ quando escolhemos uma loteria $r = \alpha(r) r_1 + (1-\alpha(r))r_2$ segundo a distribuição de probabilidade $P$.
Assumimos que 

(H5) P = \beta \delta_{r_2} + (1-\beta) \delta_{r_1}

Com isso, é possível definir a função de utilidade em $\mathcal{P}_B$. 
Dos resultados que se seguem, considere o seguinte teorema:

> **Teorema:** Sejam $P_1, P_2 \in \mathcal{P}_B$. Então $P_1 \le P_2$ se, e somente se, $\mathbb{E}^{P_1}[U(r)] \le \mathbb{E}^{P_2}[U(r)]$. Além do mais, se outra função de utilidade $U^*$ satisfaz a relação de equivalência, então existem constantes $a > 0$ e $b$ de forma que $U^*(\cdot) = a U(\cdot) + b$.

Com duas hipóteses adicionais, podemos extender esse resultado para $\mathcal{P}_E$ que é o conjunto das distribuições $P$ que tem $\mathbb{E}^P[U(r)]$ finita.

Algumas críticas ao formalismo incluem: é impossível que um indivíduo consiga comparar quaisquer duas recompensas. 
Além do mais, a transitividade é algo forte demais. Às vezes, resultados da vida real levam à não transitividade.
A extensão de $\mathcal{R}$ para $\mathcal{P}$ também é bastante problematizada, mas explica um pouco da relação da priori com a escolha da função de perda, no sentido bayesiano.

Um exemplo interessante é o [paradoxo de Saint Petersburg](https://en.wikipedia.org/wiki/St._Petersburg_paradox) que argumenta que o valor esperado do prêmio é infinito, mas a quantidade que os jogadores recebem é em geral baixa. 
Uma solução possível para esse paradoxo é mudar a função de utilidade para uma limitada.

### Relação entre utilidade e perda

A Teoria da Decisão assume que cada ação $d \in \mathcal{D}$ pode ser avaliada e leva a uma recompensa $r$ com utilidade $U(r)$.
Seja $U(\theta, d) = \mathbb{E}_{\theta, d}[U(r)]$. 
Temos que $U$ mede uma proximidade entre $d$ e $h(\theta)$.
Após definir a função de utilidade, fazemos $L(\theta, d) = -U(\theta, d) \ge 0$ como a função de perda. 
Note que essa desigualdade implica que $U$ é limitada superiormente por $0$. 

É claro que $\min_d L(\theta, d)$, quando $\theta$ é desconhecido, é praticamente impossível, pois deveríamos ter um resultado uniforme em $\Omega$. Por isso, os **frequentistas** usam a noção de **perda média** ou **risco frequentista**:
$$
R(\theta, \delta) = \mathbb{E}_{\theta}[L(\theta, \delta(x))] = \int_{\mathcal{X}} L(\theta, delta(x)) f(x|\theta) \, dx,
$$
em que $\delta(x)$ é a decisão baseada em $x$ quando $x \sim f(x|\theta)$.
Chamamos $\delta$ de **estimador**, enquanto $\delta(x)$ de estimativa. 
No cenário frequentista, estimadores são comparados segundo a performance a longo-prazo, para todos os valores de $\theta$.

Note que $R(\theta, \delta)$ é uma perda média ponderada sobre a distribuição de  $x$. 
Logo, o dado observado não é considerado nesse caso, o que é uma crítica ao método.
Além disso, existe uma controvérsia sobre a ideia de repetir experimentos, conceito importante para o frequentismo. 
Por fim, para cada $\delta$, temos que $R(\cdot, \delta)$ é uma função e, portanto, não induz uma ordem total no conjunto de procedimentos.

No procedimento bayesiano, já integramos sobre o espaço de $\Omega$ dos parâmetros. 
Assim, usamos a **perda esperada a posteriori**:
$$
\varrho(\pi, d \mid x) = \mathbb{E}^{\pi}[L(\theta, d)| x] = \int_{\Omega} L(\theta, d) \pi(\theta \mid x) \, d \theta, 
$$
em que $\pi(\theta \mid x) \propto f(x \mid \theta)\pi(\theta)$. 
O **erro integrado** é definido como 
$$
r(\pi, \delta) = \mathbb{E}^{\pi}[R(\theta, \delta)] = \int_{\Omega} \int_{\mathcal{X}} L(\theta, \delta(x)) f(x|\theta) \, dx \, \pi(\theta) \, d\theta = \int_{\mathcal{X}} \varrho(\pi, \delta(x) | x) m(x) \, dx,
$$
em que a última relação é uma aplicação do Teorema de Fubini dado que $L \ge 0$.
Além do mais, para minimizar $r(\pi, \delta)$, para cada $x$, podemos tomar $d = \delta(x)$ que minimiza $\varrho(\pi, d | x)$, pela última igualdade da expressão acima.

> **Estimador de Bayes:** Seja uma priori $\pi$ e uma perda $L$. 
O estimador de Bayes é $\delta^{\pi}$ que minimiza $r(\pi, \delta)$. 
Em particular, para cada $x$, temos que $\delta^{\pi}(x) = \arg \min_d \varrho(\pi, d | x)$. 
O risco bayesiano é o valor $r(\pi) = r(\pi, \delta^{\pi})$.

Note que para perdas estritamente convexas, o estimador de Bayes é único.

## Maximalidade e admissibilidade

Considere $\mathcal{D}^*$ o espaço das distribuições de probabilidade em $\mathcal{D}$. 
Um **estimador aleatorizado** $\delta^*$ significa tomar uma decisão de acordo com a densidade de probabilidade $\delta^*(x, \cdot)$. 
A perda é definida como 
$$
L(\theta, \delta^*(x)) = \int_{\mathcal{D}} L(\theta, a) \delta^*(x, a) \, da.
$$
Usar esse estimador não é usual porque ele adiciona ruído em um fenômeno para tomar uma decisão sob incerteza.
Além do mais, ele não obedece o Princípio da Verossimilhança, dado que para o mesmo valor de $x$, podem existir vários valores estimados.

---
``📝`` **Exemplo (Estimador randomizado)**

Podemos definir um estimador randomizado segundo
$$
\delta^*(x_1, x_2)(t) = \begin{cases}
    1_{2t = x_1 + x_2} &\text{se } x_1 \neq x_2  \\
    [1_{t = x_1 - 1} + 1_{t = x_1 + 1}]/2 &\text{se } x_1 = x_2,
\end{cases}
$$
em que $1_{v}$ é a massa de Dirac em $v$. 

---

Para toda priori $\pi$, o risco de Bayes é o mesmo no conjunto dos estimadores randomizados e não randomizados, isto é, 
$$
\inf_{\delta \in \mathcal{D}} r(\pi, \delta) = \inf_{\delta^* \in \mathcal{D}^*} r(\pi, \delta^*) = r(\pi).
$$
Como um procedimento randomizado é a média de riscos de estimadores não randomizados, ele não pode melhorá-los.

### Maximalidade

> **Risco minimax**: $\bar{R} = \inf_{\delta \in \mathcal{D}^*} \sup_{\theta} R(\theta, \delta) = \inf_{\delta \in \mathcal{D}^*} \sup_{\theta} \mathbb{E}_{\theta}[L(\theta, \delta(x))]$. 
Um estimador minimax é um estimador $\delta_0$ que satisfaz $\sup_{\theta} R(\theta, \delta_0) = \bar{R}$. 

Note que esse estimador, toma o pior caso para $\theta$ e então minimiza para os procedimentos desse pior caso. 
Esse método enxerga a natureza como um agente inimigo que tende a escolher o pior caso.

O estimador minimax nem sempre existe. 
Para isso, condições suficientes precisam ser estudadas.
Se $\Omega$ é finito e $L$ é contínua, então existe uma estratégia minimax.
Outra proposta é verificar que o conjunto das funções de risco em $\mathcal{D}$ é compacto em um espaço maior em que $\mathcal{D}$ está inserido e que a perda é constante.

**Teorema:** Se $\mathcal{D} \subseteq \mathbb{R}^k$ é um conjunto convexo compacto e $L(\theta, d)$ é contínua e convexa como função de $d$ para $\theta$ fixado, então existe um estimador minimax não randomizado. 
O estimador será não randomizado pela [desigualdade de Jensen](https://en.wikipedia.org/wiki/Jensen%27s_inequality). 
Esse resultado é um caso particular do *Teorema Rao-Blackwell*.

O *risco de Bayes* é sempre menor do que o *risco minimax*, o que é expresso matematicamente por 
$$
\underbar{R} = \sup_{\pi} r(\pi) = \sup_{\pi} \inf_{\delta \in \mathcal{D}} r(\pi, \delta) \le \bar{R} = \inf_{d \in \mathcal{D}^*} \sup_{\theta} R(\theta, \delta).
$$
A **distribuição menos favorável** é $\pi^*$ tal que $r(\pi^*) = \underbar{R}$. 
O problema de estimação tem um *valor* quando $\underbar{R} = \bar{R}$.

Um resultado interessante é que se $\delta$ é estimador de Bayes com respeito a $\pi$ e $R(\theta, \delta) \le r(\pi)$ para todo $\theta \in \Omega$, então $\delta$ é estimador minimax e $\pi$ é a distribuição menos favorável.

> **Teorema:** Considere um problema estatístico que possua um valor, uma distribuição menos favorável $\pi_0$ e um estimador minimax $\delta^{\pi_0}$. 
Então se $\Omega \subseteq \mathbb{R}$ é compacto e $R(\theta, \delta^{\pi_0})$ é função analítica de $\theta$, então $\pi_0$ tem suporte finito ou $R(\theta, \delta^{\pi_0})$ é constante.

Esse teorema mostra que o minimax não é um bom estimador do ponto de vista bayesiano, dado que (1) ele pode ser randomizado ou (2) ele pode levar a prioris não realísticas com suporte finito.

### Admissibilidade

> **Admissibilidade:** Um estimador $\delta_0$ é inadmissível se existe um estimador $\delta_1$ que domina $\delta_0$, isto é, $R(\theta, \delta_0) \ge R(\theta, \delta_1)$ para todo $\theta \in \Omega$, e pelo menos para um valor $\theta_0$, vale a desigualdade estrita. 
Caso contrário, o estimador é admissível.

Construir um estimador apenas considerando a admissibilidade não é uma boa estratégia, afinal $\delta(x) = \theta_0 \in \Omega$ é um estimador que tem valor exato para $\theta = \theta_0$.
Logo, faz sentido considerar maximalidade simultaneamente. 
O interessante é que se existe um único estimador minimax, então ele é admissível. 
A recíproca é falsa em geral, mas se $\delta_0$ é admissível com risco constante, então ele é o único estimador minimax.

A relação de admissibilidade com estimadores de Bayes é bem estrita: 

(1) Se a priori $\pi$ é estritamente positiva em $\Omega$, com risco de Bayes finito, e a função de risco é contínua em $\theta$ para todo $\delta$, então o estimador de Bayes $\delta^{\pi}$ é admissível.

(2) Se o estimador de Bayes $\delta^{\pi}$ é único, então ele é admissível.

## Perdas clássicas

Essas perdas são tratáveis matematicamente e bem documentadas, mesmo que não representem perfeitamente o problema em questão. 

### Perda quadrática

É definida como $L(\theta, d) = (\theta - d)^2$. 
Provavelmente a perda mais utilizada.
Penalizada fortemente desvios altos.
Mas, como a perda é convexa e vale a desigualdade de Jensen mencionada mais acima, o que exclui estimadores randomizados.
O interessante é que, sob essa perda, o estimador de Bayes é a média a posteriori, um dos valores que pensaríamos naturalmente, mesmo sem adicionar a carga da teoria da decisão.

**Proposição:** O estimador de Bayes $\delta^{\pi}$ associado com a perda quadrática $L$ é a esperança a posteriori $\delta^{\pi}(x) = \mathbb{E}^{\pi}[\theta | x]$. 
O resultado imediato ocorre quando $L(\theta, \delta) = w(\theta)(\theta - \delta)^2$, como uma ponderação. 
Nesse caso, o estimador de Bayes é 
$$\delta^{\pi}(x) = \frac{\mathbb{E}^{\pi}[w(\theta) \theta | x]}{\mathbb{E}^{\pi}[w(\theta)| x]}.$$

### Perda absoluta

Uma alternativa à perda quadrática é $L(\theta, d) = |\theta - d|$, que pode ser generalizada para 
$$
L_{k_1, k_2}(\theta, \delta) = \begin{cases}
k_2(\theta - d) &\text{se } \theta > d \\
k_1(d - \theta) &\text{c.c.}
\end{cases}
$$
A penalização para desvios maiores é menor, apesar de manter a convexidade.
é possível também propor uma perda como uma mistura dessas perdas. 
Em uma região próxima de zero, usamos a perda quadrática. Depois, usamos a perda absoluta.
Com essa perda, por exemplo, não existe estimador de Bayes em forma fechada.

O estimador de Bayes associado a $L_{k_1, k_2}(\theta, \delta)$ e a $\pi$ é um quartil $k_2/(k_1 + k_2)$ de $\pi(\theta | x)$. Em particular, quando $k_1 = k_2$, o estimador é a mediana a posteriori.

### Perda 0-1

Essa perda é mais utilizada no contexto de teste de hipóteses. Ela é definida como $L(\theta, \delta) = 1 - 1_{\theta = \delta}$.

---
``📝`` **Exemplo (Teste de hipóteses)**

Seja o teste de hipóteses $H_0 : \theta \in \Omega_0$ e $H_1 : \theta \in \Omega_1$. 
Então $\mathcal{D} = \{0, 1\}$ em que $0$ significa rejeitar $H_0$.
Logo queremos estimar a função $1_{\theta \in \Omega_0}$. 
O risco frequentista é 
$$
R(\theta, \delta) = \begin{cases}
    \Pr_{\theta}(\delta(x) = 0), &\text{se } \theta \in \Omega_0 \\
    \Pr_{\theta}(\delta(x) = 1), &\text{c.c.,}
\end{cases}
$$
que são os erros do tipo 1 e do tipo 2, respectivamente.

---

O estimador de Bayes é dado por 
$$
\delta^{\pi}(x) = \begin{cases}
    1 &\text{se }\Pr(\theta \in \Omega_0 | x) > \Pr(\theta \in \Omega_1 | x) \\
    0, &\text{c.c.}
\end{cases}
$$

### Perdas intrínsecas

Às vezes, estamos em uma situação não informativa sobre a parametrização natural e a escolha da função de perda.
O estimador de Bayes não é invariante por transformações biunívocas em geral.
Dessa forma, pode ser interessante obter perdas invariantes.
Nesse caso, comparar $f(\cdot | \delta)$ com $f(\cdot | \theta)$ pode ser interessante, isto é, definir 
$$
L(\theta, \delta) = d(f(\cdot | \theta), f(\cdot | \delta)).
$$
Duas distâncias usuais são: (1) entropia, Kullback–Leibler divergence, ou (2) Hellinger. Elas resultam nas seguintes perdas:

$$
(1) L_e(\theta, \delta) = \mathbb{E}_{\theta}\left[\log\left(\frac{f(x|\theta)}{f(x|\delta)}\right)\right].
$$

$$
(2) L_H(\theta, \delta) = \frac{1}{2}\mathbb{E}_{\theta}\left[\left(\sqrt{\frac{f(x|\delta)}{f(x|\theta)}} - 1\right)^2\right].
$$

## Links

- [Optimal Statistical Decisions, Morris DeGroot](https://onlinelibrary.wiley.com/doi/book/10.1002/0471729000): esse livro expande os resultados de teoria da decisão apresentados no livro do Robert.