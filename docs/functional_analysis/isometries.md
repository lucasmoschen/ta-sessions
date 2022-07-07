# Isometrias e Homeomorfismos

Um conceito importante sobre espaços métricos é a ideia de **isometria**, isto é, funções que mantém propriedades relacionadas à métrica do espaço (iso = igual, metria = métrica).

Sejam $(X,d)$ e $(Y,d')$ dois espaços métricos e $f:X \to Y$ uma função bijetiva. Dizemos que $f$ é um **homeomorfismo** se $f$ e $f^{-1}$ são contínuas. Além do mais, se existe um homeomorfismo entre $X$ e $Y$, dizemos que $X$ e $Y$ são **homeomorfos**. 

Um homeomorfismo preserva conjuntos abertos e fechados, além de outras propriedades, como o conceito de ponto limite, isto é, se $x \in A'$, então $f(x) \in f(A)'$.

Se $f:X \to Y$ é bijetiva e para quaisquer $x,y \in X$, vale que 
$$
d(x,y) = d'(f(x), f(y)),
$$
então $f$ é dita **isometria**. Se existe uma isometria entre $X$ e $Y$, eles são ditos **isométricos**. 

Toda isometria é um homeomorfismo, pois se $d(x_n, x) \to 0$, então $d'(f(x_n), f(x)) \to 0$. Em contrapartida, se $d'(f(x_n), f(x)) \to 0$, é claro que $d(f^{-1}(f(x_n)), f^{-1}(f(x))) = d(x_n, x) \to 0$.

## Sequência de Cauchy

Considere a sequência $\{x_n\}$ no espaço métrico $(X,d)$. Ela é dita de **Cauchy** se para todo $\epsilon > 0$, existe $N \in \mathbb{N}$ tal que para todo $n, m> N$, vale que $d(x_n, x_m) < \epsilon$. Intuitivamente, a distância entre um elemento da sequência $x_m$ e seus subsequentes vai assintoticamente diminuindo. Observe que isso não garante convergência de forma geral, mas toda sequência convergente é de Cauchy, visto que 
$$
d(x_n, x_m) < d(x_n, x) + d(x, x_m), 
$$
quando $x$ é o limite dessa sequência.

Dizemos que um espaço é **completo** se toda sequência de Cauchy é convergente.

---
``📝`` **Completude dos números reais**

O espaço $X=\mathbb{R}^n$ com a métrica $d_2(x,y) = \sqrt{\sum_{i=1}^n (x_i-y_i)^2}$ é completo. Em particular, os reais formam um espaço completo com a distância dada pelo valor absoluto da diferença.

---

---
``📝`` **Métrica trivial**

Qualquer conjunto dotado da métrica trivial forma um espaço completo, pois a sequência só será de Cauchy se existir $N \in \mathbb{N}$ tal que $n > N \implies x_n = x_N$.

---

---
``📝`` **Os números racionais**

Considere $X= \mathbb{Q}$ e $d(x,y) = |x-y|$. É fácil ver que $(\mathbb{Q}, d)$ formam um espaço métrico não completo. Para isso, considere a sequência
$$
x_{n+1} = \frac{x_n}{2} + \frac{1}{x_n},
x_1 = 2,
$$
que está definida em $X$, pois soma e divisão são operações fechadas nos racionais. 
Note que 
$$
\frac{x_{n+1}}{x_n} = \frac{1}{2} + \frac{1}{x_n^2} \le 1 \iff x_n^2 \ge 2.
$$
Note que 
$$
0 \le (x_{n+1} - x_n)^2 = x_{n+1}^2 + x_n^2 - 2x_{n+1}x_n = x_{n+1}^2 + x_n^2 - x_{n}^2 -2 = x_{n+1}^2 - 2,
$$
o que implica que $x_n^2 \ge 1$ para todo $n$ e, $x_{n+1} \le x_n$ pela desigualdade inicial. Com isso, temos uma sequência decrescente limitada e, portanto, convergente em $\mathbb{R}$ e, portanto de Cauchy em $\mathbb{R}$ e, por consequência, de Cauchy em $X$. Seja $L$ o limite. Assim, 
$$
L = L/2 + 1/L \implies 2L^2 = L^2 +2 \implies L = \sqrt{2}.
$$
Como $L \not \in X$, então a sequência não converge em $X$ e $X$ não é completo.

---

**Proposição:** Duas sequências são **assintóticas** quando $d(x_n, y_n) \to 0 $.
Isso cria uma relação de equivalência no espaço das sequências.
Além do mais, se $\{x_n\}$ é Cauchy /converge para $x$, $\{y_n\}$ também será / converge.

## Completamento 

Seja $(X,d)$ um espaço métrico. O espaço métrico completo $(X^*, d^*)$ é um **completamento** de $(X,d)$ se $(X,d)$ é isométrico a um subespaço $(X_0, d^*)$ denso em $(X^*, d^*)$, isto é, que satisfaz, $\bar{X}_0 = X^*$. Nesse caso, todo ponto de $X^*$ é ponto de aderência de $X_0$, que é equivalente a $X$ no sentido de preservar a métrica.

**Teorema:** Todo espaço métrico $(X,d)$ tem um completamento $(X^*, d^*)$ e, além do mais, se $(X^{**}, d^{**})$ é um completamento de $(X,d)$, então $(X^*, d^*)$ é isométrico a $(X^{**}, d^{**})$.


---
``📝`` **Os números racionais (continuação)**

Vimos que $\{\mathbb{Q}, d\}$ é um espaço métrico não completo para $d(x,y) = |x,y|$.
Pelo Teorema acima, existe um espaço métrico $(\mathbb{Q}^*, d^*\}$ completo de forma que $\mathbb{Q}$ é isométrico a um subconjunto denso de $\mathbb{Q}^*$.
Além disso, sabemos que ele é único a menos de uma isometria.
Essa é uma forma de construir os números reais: o completamento dos números racionais. 
Para isso, basta definir um número real como a classe de equivalência das sequências de Cauchy nos racionais com a relação de duas sequências estarem na mesma classe se são assintóticas. 

Mais detalhes dessa construção, consulte o [Exercício 31 da lista](https://lucasmoschen.github.io/files/disciplines/functional-analysis/paper_sheet_metric_spaces.pdf).

---

**Proposição:** Seja $A \subseteq X$ em que $(X,d)$ seja um espaço métrico completo. 
Então $(A,d)$ é um espaço métrico com $(\bar{A}, d)$ sendo seu completamento.

---
``📝`` **Homeomorfismo, não isometria!**

Note que $\mathbb{R}$ é homeomorfo a $(0,1)$ através ta transformação $f(x) = \frac{1}{\pi}tan^{-1}(x) + 1/2$.
Todavia, um é completo, enquanto o outro não é.

---

### Teorema de Baire

> Seja $(X,d)$ um espaço métrico. 
Um subconjunto $S \subseteq X$ é dito **denso em lugar algum** se $S$ não é denso em nenhum subconjunto aberto não vazio $U \subseteq X$.

**Teorema:** Um espaço métrico completo não pode ser coberto por um número enumerável de conjuntos densos em lugar algum.

## Espaços Separáveis

Temos os seguintes tipos de espaços métricos, cada um "maior" do que o anterior.

- **Espaço métrico finito:** existe um número finito de distância para calcular entre os pontos do espaço.
- **Espaço métrico enumerável:** com um número infinito de pontos, um algoritmo pode calcular distâncias precisamente, mas isso pode tomar tempo.
- **Espaço métrico separável:** pontos podem ser aproximados por um de um número contável de pontos. Qualquer distância pode ser calculada de forma aproximada.
- **Espaço métrico não separável:** Pode não existir algoritmo para calcular distância entre pontos genéricos.

> Um espaço métrico $(X,d)$ é **separável** quando ele contém um subconjunto denso enumerável.

Espaços métricos enumeráveis são separáveis por definição. Temos que $\mathbb{R}$ é separável, pois $\mathbb{Q}$ é denso em $\mathbb{R}$.

**Proposição:** O produto de dois espaços separáveis é separável.