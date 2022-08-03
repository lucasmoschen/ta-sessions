# Espaços normados

Um **espaço vetorial** $V$ sobre um corpo $F$ é um conjunto em que se define a soma $+ : V^2 \to V$ e o produto escalar $\cdot : F \times V \to V$, tal que a soma satisça as propriedades: *associatividade*, *comutatividade*, *existência de elemento zero* e *elemento inverso*, e o produto seja linear, isto é, $\lambda (x + y) = \lambda x + \lambda y$, $(\lambda + \mu) x = \lambda x + \mu x$ e $\lambda (\mu x) = (\lambda \mu) x$.

## Definição

Um **espaço normado** (linear) $X$ é um espaço vetorial sobre $F = \mathbb{R}$ ou $\mathbb{C}$ com uma função 
$$
\|\cdot\| : X \to \mathbb{R},
$$
tal que $\|x\| = 0 \iff x = 0$, $\|\lambda x\| = |\lambda|\|x\|$ e $\|x+y\| \le \|x\| + \|y\|$, para todo $x,y \in X$ e $\lambda \in F$.

---
``📝`` **Exemplos**

- O valor absoluto em $\mathbb{R}$ e $\mathbb{C}$ define uma norma.
- Os espaços $\mathbb{R}^n$ e $\mathbb{C}^n$ com a norma
$$
\|x\|_2 := \left(\sum_{i=1} |x_i|^p \right)^{1/p}
$$
para $p \ge 1$, definem espaços normados. 
Quando $p=2$, temos a norma Euclidiana.

- O espaço $l^1 = \{(a_n)_{n \in \mathbb{N}} : \sum |a_n| < +\infty\}$ com a métrica $\|(a_n)\| = \sum |a_n|$ define um espaço normado.
- O espaço das funções absolutamente integráveis em $A$, $L^1(A)$, com a norma 
$$
\|f\| = \int_A |f(x)| \, dx
$$
não forma um espaço normado, pois $\|f\| = 0$ não implica que $f = 0$. 
Mas temos que $f = 0$ **quase certamente** (isso demanda a necessidade de definir um espaço de medida, mas isso não será feito aqui). 
Com isso, o espaço de Lebesgue é definido pelas classes de equivalência de funções iguais quase certamente. 
Esse espaço é, de fato, espaço normado.

---

Note que um espaço normado é um espaço métrico com a métrica $d(x,y) = \|x-y\|$.
Logo, um espaço normado é completo se o espaço métrico induzido é completo.

> Um espaço normado completo é um **espaço de Banach**

Em contrapartida, nem todo espaço métrico define um espaço normado com a norma induzida.

---
``📝`` **Exemplo**

Considere um espaço vetorial $X$ e $d$ a métrica trivial. 
Assim, 
$$
d(\lambda x, 0) = 1.
$$
Mas se existe uma norma tal que $\|x-y\| = d(x,y)$, então teríamos que $d(\lambda x, 0) = \lambda d(x,0) = \lambda$.

---

Seja $X$ um espaço normado sobre o corpo $F$.

**Teorema:** Os mapas $(x,y) \mapsto x + y$, $(\alpha, x) \mapsto \alpha\cdot x$ e $x \mapsto \|x\|$ são contínuos. 

## Desigualdades de Hölder e Minkowski

O seguinte resultado é uma aplicação de resultados de integral.

**Lemma:** Sejam $a,b, \ge 0$ e $p, q > 1$ tal que $p^{-1} + q^{-1} = 1$.
Então $ab \le a^p/p + b^q/q$.

A ideia da demonstração é considerar as áreas 
$$
A_1 = \int_0^a x^{p-1} = \frac{a^p}{p} \text{ e } A_2 = \int_0^b y^{q-1} = \frac{b^q}{q},
$$
de forma que $y = x^{p-1} \implies x = y^{q-1}$ e, portanto, $ab \le A_1 + A_2$.

A partir dessa lema, chegamos no importante teorema de Hölder. 

**Teorema (Holder):** Seja $p,q > 1$ tal que $p^{-1} + q^{-1} = 1$. 
Então, vale que, se $x,y \in \mathbb{R} 
$$
\sum_{j=1}^n |x_i y_i| \le \left(\sum_{j=1}^n |x_j|^p\right)^{1/p}\left(\sum_{j=1}^n |y_j|^q\right)^{1/q}.
$$

Esse resultado pode ser estendido para o espaço das sequências definidas em $l^p \cap l^{q}$.
Além disso, o resultado se estende para o espaço das funções em $L^p \cap L^q$, 
$$
\int_a^b |f(x) g(x)| \, dx \le \left(\int_a^b |f(x)|^p \, dx\right)^{1/p}\left(\int_a^b |g(x)|^q\right)^{1/q} 
$$

Outra desigualdade importante é a de Minkowski, 

**Teorema (Minkowski):** Seja $p \ge 1$. 
Então, 
$$
\left(\sum_{j=1}^n |x_j + y_j|^p\right)^{1/p} \le \left(\sum_{j=1}^n |x_j|^p\right)^{1/p} + \left(\sum_{j=1}^n |y_j|^p\right)^{1/p},
$$
que também pode ser estendido para séries e funções.

## Completamento de um espaço normado

Seja $(X, \|\cdot\|)$ um espaço normado e $d(x,y) = \|x-y\|$ a métrica induzida.
Assim $(X,d)$ é um espaço métrico e existe um [completamento](https://lucasmoschen.github.io/ta-sessions/functional_analysis/isometries) $(X^*, d^*)$. 
Com uma definição apropriada, $X^*$ é um espaço normado (completo, claramente), com a propriedade de que $X$ é **isomorfo** e isométrico a um subjunto denso de $X^*$.
Além do mais, a norma de $X^*$ vai estender a norma de $X$.

*Observação: Uma função é uma **congruência** se é uma isometria e um isomorfismo.*

---
Ideia da prova:

1. Sejam $x^*, y^* \in X^*$ (classes de equivalência de sequências Cauchy). 
   Defina $x^* + y^* = \{x_n + y_n\}_{n\in\mathbb{N}}$, a sequência definida pela soma de suas respectivas representantes.
   É claro que soma de sequências de Cauchy é sequência de Cauchy e que se escolhessemos quaisquer outras representantes, teríamos sequências equivalentes. Além disso, é fácil ver também que $\{\alpha x_n\}$ é sequência de Cauchy se $\{x_n\}$ o for. Com isso, é fácil verificar que $X^*$ é um espaço vetorial.
2. Defina a norma $\|x^*\|_* = \lim \|x_n\|$. 
   Esse limite existe, pois $\{\|x_n\|\}$ é Cauchy e, portanto, convergente em $\mathbb{R}$. 
   Além disso, para qualquer outra sequência representante de $x^*$, o limite será o mesmo pela equivalência. 
   Após verificar que $\|\cdot\|_*$ é de fato uma norma, concluímos que $X^*$ é espaço normado.
3. Observe que $\|x^* - y^*\|_* = \lim \|x_n - y_n\| = \lim d(x_n, y_n ) = d^*(x^*, y^*)$, portanto, $d^*$ é a métrica induzida pela norma. Com essa métrica, sabemos que o espaço métrico $(X^*, d^*)$ é completo e, portanto, $X^*$ é espaço normado completo.
4. Seja $X_0$ o espaço das sequências constantes de $X^*$, que sabemos que é denso em $X^*$ e isométrico a $X$. 
   Falta verificar que o mapa $A : X \to X_0$ também é um isomorfismo, isto é, que ele é bijetivo, o que ele de fato é, e que ele preserva combinações lineares, o que é imediado.

Por (1)-(4), verificamos que $(X^*, \|\cdot\|_*)$ é um espaço métrico completo que contém um conjunto denso isométrico e isomorfo a $X$.

---

## Subespaços gerados e fechados

Seja $X$ um espaço vetorial linear. 
Um conjunto $S \subseteq X$ é um subespaço quando $S$ com as operações de $X$ forma um espaço vetorial.

> Sendo $S$ um subconjunto de $X$, o subespaço gerado por $S$, dito $[S]$, é a intersecção de todos os subespaços de $X$ que contém $S$. 
É fácil ver que a intersecção de subespaços é um subespaço e que $[S] \subseteq X$.
De forma equivalente $[S]$ é o conjunto de todas as combinações lineares de elementos de $S$.

Em espaços normados de dimensão finita, todos os subespaços são fechados.

**Teorema:** Se $M$ é subespaço de um espaço normado $X$, então $\bar{M}$ é subespaço também.

Para provar o teorema acima, é necessário verificar que qualquer combinação linear de elementos de $\bar{M}$ pertence a $\bar{M}$. 
Isso não é difícil de ver, pois se $x_n \to x$ e $y_n \to y$, então $\alpha x_n + \beta y_n \to \alpha x + \beta y$.

Para um conjunto $S$, definindo o menor subespaço fechado que contém $S$, dito $M$, como a interseccção desses subespaços, é fácil ver que $M = \bar{[S]}$, isto é, o fecho de $[S]$.  

## Normas equivalentes

> Seja $X$ um espaço vetorial sobre um corpo $F$ e sejam $\|\cdot\|_1$ e $\|\cdot\|_2$ normas em $X$.
Dizemos que $\|\cdot\|_1 \sim \|\cdot\|_2$, isto é, as normas são equivalente, se existem $a,b>0$ tal que
> $$
a\|x\|_1 \le \|x\|_2 \le b\|x\|_1, \forall x \in X,
> $$
> que forma uma relação de equivalência.

Com isso, sequência de Cauchy sobre uma norma, também será sobre qualquer outra norma equivalente.
Além disso, a classe de conjuntos abertos é a mesma para normas equivalentes.

### Todas as normas são equivalente em espaços finito-dimensionais

Como equivalência de normas é uma relação de equivalência, é suficiente mostrar que qualquer norma é equivalente a uma específica. 
Em particular, seja $x_1, \dots, x_n$ uma base de $X$ (espaço normado finito-dimensional). 
Para cada $x \in X$, defina 
$$
\|x\|_0 := \max_i |\alpha_i|, \text{ em que } x = \sum_{i=1}^n \alpha_i x_i,
$$
que é bem definida, pois a escrita de um vetor em um base é única.

---
Ideia da prova:

1. Seja $\|\cdot\|$ uma norma em $X$. Assim, $\|x\| = \|\sum_{i=1}^n \alpha_i x_i \| \le \sum_{i=1}^n |\alpha_i|\|x_i\| \le \|x\|_0 \sum_{i=1}^n \|x_i\| = b\|x\|_0$, com $b = \sum_{i=1}^n \|x_i\|$.
2. Para a outra igualdade, se prova por indução em $n = \operatorname{dim} X$. 
   Para $n=1$, isso é trivial, visto que $\|x\| \ge \|x\|_0 \|x_1\| = a\|x\|_0$.
3. Suponha que o teorema valha para espaços de dimensão menor ou igual a $n-1$, tome a base $\{x_1, \dots, x_n\}$ e defina $M = [\{x_1, \dots, x_{n-1}\}]$.
   Então $\|\cdot \| \sim \|\cdot\|_0$ em $M$. 
   Prova-se que $M$ é espaço completo e, portanto, fechado.
4. Considere o conjunto $x_n + M$, que é fechado e note que $0 \not \in x_n + M$.
   Como $(x_n + M)^c$ é aberto, existe uma bola aberta de centro $0$, tal que $B_{c_n}(0) \subseteq (x_n + M)^c$.
   Nesse caso, $\|x\| \ge c_n$ para todo $x \in x_n + M$.
5. Com isso, $\|x\| \ge |\alpha_n|c_n$ para todo $x \in X$, em que $\alpha_n$ é o coeficiente de $x_n$.
6. Note que os fatos acima valeriam também para qualquer $M_i = [\{x_j\}_{j=1}^n / x_i]$.
   Nesse caso, $\|x\| \ge |\alpha_i|c_i$ para todo $x \in X$.
   Em particular, $\|x\| \ge \min_i c_i \|x\|_0$, o que completa a prova.

---

Como consequência temos os seguintes fatos:

- Se $X$ é espaço normado finito-dimensional, então ele é completo.
- Se $X$ é espaço normado e $M$ subespaço finito-dimensional, então $M$ é fechado.

## Teorema de Riesz

Seja $M$ um subespaço fechado próprio de um espaço normado $X$ e $a \in (0,1)$.
Então existe um vetor $x_a \in X$ tal que $\|x_{a}\| = 1$ e $\|x - x_a\| \ge a$ para todo $x \in M$.

---
Ideia da prova:

1. Tome $x_1 \in X / M$ e defina $d = \inf_{x \in M} \|x-x_1\| > 0$, pois $M$ é fechado.
   Como $d/a > d$, existe $x_0 \in M$ tal que $\|x_0 - x_1\| < d/a$.
2. Defina 
   $$x_a = \frac{x_1 - x_0}{\|x_1 - x_0\|}.$$
   Veja que para todo $x \in M$, 
   $$
   \|x-x_a\| \ge \frac{d}{\|x_1 - x_0\|} \ge \frac{d}{d/a} = a,
   $$
   pois $(\|x_1 - x_0\|)x + x_0 \in M$ e $x - x_a \propto (\|x_1 - x_0\|)x + x_0 - x_1$.

---