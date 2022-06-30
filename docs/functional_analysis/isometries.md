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
Como $L \not \in X$, então a sequência não converge em $X e $X$ não é completo.

---

## Completamento 

Seja $(X,d)$ um espaço métrico. O espaço métrico completo $(X^*, d^*)$ é um **completamento** de $(X,d)$ se $(X,d)$ é isométrico a um subespaço $(X_0, d^*)$ denso em $(X^*, d^*)$, isto é, que satisfaz, $\bar{X}_0 = X^*$. Nesse caso, todo ponto de $X^*$ é ponto de aderência de $X_0$, que é equivalente a $X$ no sentido de preservar a métrica.

**Teorema:** Todo espaço métrico $(X,d)$ tem um completamento $(X^*, d^*)$ e, além do mais, se $(X^{**}, d^{**})$ é um completamento de $(X,d)$, então $(X^*, d^*)$ é isométrico a $(X^{**}, d^{**})$.

