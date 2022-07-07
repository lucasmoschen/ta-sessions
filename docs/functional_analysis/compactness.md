# Compacidade

> **Definição:** Uma **sequência de conjuntos encaixados** é uma sequência $\{F_n\}_{n\in\mathbb{N}}$ se $F_{n+1} \subseteq F_n$ para todo $n \in \mathbb{N}$.

Também definimos o diâmetro de um conjunto $A \subseteq X$ como $d(A) = \sup_{a,b \in A} d(a,b)$.

**Teorema:** Uma espaço métrico $(X,d)$ é completo se, e somente se, para toda sequência de conjuntos encaixados fechados e não vazios $\{F_n\}, n \ge 1$ com $d(F_n) \to 0$, vale que
$$
\cap_{n\in\mathbb{N}} F_n \neq \emptyset.
$$

> **Cobertura:** Seja $I$ um conjunto de índices. 
Dizemos que $\{G_{\alpha}\}_{\alpha \in I}$ é uma **cobertura** de $A$ se $A \subseteq \cup_{\alpha \in I} G_{\alpha}$.
Se $I$ é finito, chamamos de **cobertura finita**. 
Se $G_{\alpha}$ é aberto para todo $\alpha \in I$, chamamos de **cobertura aberta**.

## Conjuntos limitados 

Um subconjunto $A$ do espaço métrico $(X,d)$ é **limitado** se existe $M \in \mathbb{R}$ tal que $d(A) \le M$. 
A distância entre um ponto e um conjunto é dado por 
$$
d(x,B) = \inf_{y \in B} d(x,y)
$$
e a distância entre conjuntos é
$$
d(B,C) = \inf_{x \in B, y \in C} d(x,y).
$$

A união finita de conjuntos limitados é limitada. 
Outra relação é que um conjunto $B$ é limitado se existe uma bola que o contém.

## Conjuntos totalmente limitados

Um conjunto $B \subseteq X$ é **totalmente limitado** se pode ser coberto por um número finito de bolas de raio $\epsilon$, isto é,
$$
\forall \epsilon > 0, \text{ existem pontos } a_1, \dots, a_n \text{ tal que } B \subseteq \cup_{i=1}^n B_{\epsilon}(a_n).
$$

Temos que todo conjunto totalmente limitado é limitado. 

---
``📝`` **Exemplo**

Tome $A = [0,1]$ em $(\mathbb{R}, d)$. 
$A$ é totalmente limitado, pois, para todo $\epsilon > 0$, 
$$
A \subseteq \cup_{i=0}^n ((i-1)\epsilon, (i+1)\epsilon) = \cup_{i=0}^n B_{\epsilon}(i\epsilon),
$$
tomando $n \in \mathbb{N}$ de forma que $(n+1)\epsilon > 1$.

---

---
``📝`` **Nem todo conjunto limitado é totalmente limitado**

Considere a métrica trivial $d(x,y) = 1 \iff x \neq y$ e $X = \mathbb{N}$. 
O conjunto $A$ dos números pares é limitado, pois, 
$$
d(A) = \sup_{m,n \in A} d(m,n) = 1.
$$
Mas, para $\epsilon < 1$, $B_{\epsilon}(x) = \{x\}$ para todo $x \in \mathbb{N}$. 
Logo $A$ não pode ser totalmente limitado.

---

**Proposição:** Uma função uniformemente contínua mapeia conjuntos totalmente limitados em conjuntos totalmente limitados.

## Compacidade

> Um conjunto $A$ é **compacto** se para toda cobertura aberta, existe uma subcobertura finita.

Para mostrar que um conjunto não é compacto, basta selecionar uma cobertura aberta que não possua cobertura finita. 

---
``📝`` **Conjunto não compacto**

O conjunto $I = (0,1)$ não é compacto em $\mathbb{R}$. Tome a cobertura $\{I_n\}$ com $I_n = (1/n, 1)$. De fato, se $x \in (0,1)$, para $n > x^{-1}$ vale que $x \in (1/n, 1)$, o que mostra que $\{I_n\}$ é de fato uma cobertura aberta.
Observe que $I_{n} \subseteq I_{n+1}$. 
Com isso, $\cup_{i=1}^k I_{n_i} = (1/\max_{i=1,\dots,k} n_i, 1)$, que não pode cobrir $(0,1)$. 

---

**Teorema:** Seja $(X,d)$ um espaço métrico. Se $A$ é conjunto compacto, então $A$ é fechado e limitado.

---
Ideias da demonstração: 

**(1) $A$ é fechado:** tome $y \in A^c$ e mostra-se que existe $B$ aberto contendo $y$ com $A \cap B = \emptyset$, isto é, $y \not \in \bar{A}$. Isso mostra que $A = \bar{A}$.
Para definir $B$, para cada $x \in A$, sabemos que existe $\epsilon_x$ de forma que $B_{\epsilon_x}(x) \cap  B_{\epsilon_x}(y) = \emptyset$. Além disso, $\{B_{\epsilon_x}(x)\}$ define uma cobertura aberta de $A$ que possui subcobertura finita $\{B_{\epsilon_{x_i}}(x_i)\}_{i=1}^n$. Defina $B = \cap_{i=1}^n B_{\epsilon_{x_i}}(x_i)$.

**(2) $A$ é limitado:** Note que $A \subseteq \cup_{x \in A} B_1(x)$ e, portanto, existe subcobertura finita $\{B_1(x_i)\}_{i=1}^n$.
Defina $a = \max d(x_i, x_j)$. Se $A$ fosse ilimitado, existiriam $x,y \in A$ de forma que $d(x,y) > a + 2$. 
Porém, $x \in B_1(x_i)$ e $y \in B_1(x_j)$ para alguns $i, j$. 
Portanto, 
$$
a + 2 < d(x,y) \le d(x, x_i) + d(x_i, x_j) + d(x_j, y) < a + 2,
$$
um absurdo, que indica que $A$ é limitado.

---

**Proposição:** Funções contínuas mapeiam conjuntos compactos em compactos. Com isso, a imagem de conjuntos compactos tem mínimo e máximo.

---
``📝`` **Intervalo fechado e limitado**

O conjunto $A = [a,b]$ é compacto em $\mathbb{R}$.
Seja $\{A_i\}$ uma cobertura aberta de $A$. Suponha que não exista subcobertura finita. 
Portanto, $[a,(a+b)/2]$ ou $[(a+b)/2, b]$ não admite subcobertura finita: chame de $[a_1, b_1]$. 
Mesmo assim, $[a_1,(a_1+b_1)/2]$ ou $[(a_1+b_1)/2, b_1]$ não admite subcobertura finita: chame de $[a_2, b_2]$.
Assim, estamos definido um sequência de intervalos fechados encaixados $[a_n, b_n]$ com $d([a_n, b_n]) \to 0$.

As sequências $\{a_n\}$ e $\{b_n\}$ são sequências monótonas limitadas e, portanto convergentes, com $\lim a_n = \lim b_n = x$, pois $d(a_n, b_n) \to 0$. 
É claro que $x \in A$, pois $A$ é fechado. 
Nesse caso, $x \in A_i$ para algum $i$ e, por ser aberto, 
$x \in B_{r}(x) \subseteq A_i$.
Para $n$ suficientemente grande, $a_n, b_n \in B_r(x)$, o que implica que $[a_n, b_n] \subseteq B_r(x)$, o que contradiz o fato de ser uma sequência que não pode ser coberta de forma finita. 
Essa contradição mostra que existe subcobertura finita e, portanto, $[a,b]$ é fechado.

---

### Compacidade relativa e $\epsilon$-net

> Um conjunto é **relativamente compacto** se $\bar{A}$ é compacto. 

Um exemplo é $I=(0,1)$, que não é compacto, mas $[0,1]$ é. Também é fácil ver que um conjunto compacto é relativamente compacto, dado que é necessariamente fechado e $\bar{A} = A$.

> Um conjunto de pontos $N$ é uma $\epsilon$-net com respeito a um conjunto $A$ se, para todo $x \in A$, existe $y \in N$ tal que $d(x,y) < \epsilon$.

A ideia de uma $\epsilon$-net é que um conjunto de pontos estão $\epsilon$ próximos de qualquer ponto de $A$.

**Teorema:** Seja $A$ um subconjunto em um espaço métrico.
Se para toda sequência de pontos de $A$, existe uma subsequência convergente, então $A$ é totalmente limitado.

### Compacidade contável e sequencial

> Um conjunto $A$ é **compacto contável** se todo subconjunto infinito de $A$ tem um ponto limite em $A$.

**Teorema:** Compacidade implica compacidade contável.

---
A ideia da prova é mostrar que um conjunto não compacto contável, também não é compacto.
Para isso, deve existir $M = \{x_1, x_2, \dots\} \subseteq A$ infinito enumerável que não tenha pontos limites de $A$. 
Mas com isso, podemos fazer uma sequência de conjuntos abertos de forma que $E_n \cap M = \{x_n\}$. Se $x \in A / M$, então existe um aberto $E(x)$ com $E(x) \cap M = \emptyset$. A união dos conjuntos $E(x)$ para $x \in A / M$ não contém pontos de M. Além disso, todo ponto de $E_n$ só contém um ponto de $M$, mas
$$
A \subseteq \cup_{n\in\mathbb{N}} E_n \cup \cup_{x  \in A/M} E(x),
$$
mas é impossível existir subcobertura finita e, portanto, $A$ não é compacto, como queríamos verificar.

---

> Um conjunto $A$ é **compacto sequencialmente** se, para toda sequência em $A$, existe uma subsequência convergente com limite em $A$.

**Teorema:** Compacidade e compacidade sequencial são equivalentes em espaços métricos.

---
Que compacidade implica compacidade sequencial, prova-se que compacidade contável implica sequencial. 
Não é complicado, todavia, porque a partir de uma sequência em $A$, usamos que o conjunto desses pontos (quando infinito) tem ponto limite em $A$. Justamente, isso implica que existe subsequência convergente em $A$.

A volta é um pouco mais complicada e parte de uma cobertura aberta $\{G_{\alpha}\}$ e define-se 
$$\delta_0 = \inf\{\sup \{a : \exists \alpha; B_a(x) \subseteq G_{\alpha}\} | x \in A\},$$
que está bem definido, pois $G_{\alpha}$ é aberto e cobre $A$.
Toma-se uma sequência $\delta(x_n) \to \delta_0$ para se provar que $\delta_0 > 0$. 
Para isso, usamos o fato que a sequência $\{x_n\}$ tem subsequência convergente com limite em $A$, isto é, $x_{n_k} \to x_0 \in A$. Em particular, prova-se que $\delta_0 \ge \delta(x_0)/4 > 0$ com um pouco de álgebra.
Como toda sequência tem subsequência convergente, vale que o conjunto é totalmente limitado.
Daí para $\delta_0 > \epsilon > 0$, existe $\epsilon$-net finita com centros $y_1, \dots, y_n \in A$.
Isso implica que $B_{\epsilon}(y_i) \subseteq G_i$ e, portanto, $\{G_1, \dots, G_n\}$ formam uma subcobertura finita.

---

**Teorema:** Em um espaço métrico, compacidade relativa implica totalmente limitada. Se ele for completo, totalmente limitada implica compacidade relativa.


## Observações finais:

- Funções contínuas preservam compacidade;
- Funções uniformemente contínuas preservam totalmente limitados;
- Funções Lipschitz contínuas preservam limitados.
- Compacidade, compacidade contável e compacidade sequencial são conceitos equivalentes em espaços métricos.
- Se $A$ é compacto, então $A$ é fechado e totalmente limitado. Se o espaço métrico é completo, então $A$ ser fechado e totalmente limitado implica que $A$ é compacto.