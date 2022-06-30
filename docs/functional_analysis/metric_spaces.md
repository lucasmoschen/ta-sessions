# Espaços métricos

Queremos introduzir o conceito de distância entre pontos em um espaço. Com isso bem definido, a noção de limite, fundamental para a área da Análise (e talvez um dos pontos que mais a distancie da Álgebra), fica bem entendida, já que estamos dizendo que uma sequência de pontos se aproxima cada vez mais de um ponto do espaço.
A ideia de se aproximar se conecta naturalmente com a distância entre os pontos diminuir.

**Definição:** Seja $X$ um conjunto qualquer e $d : X \times X \to \mathbb{R}$ uma função que satisfaz, para quaisquer $x,y,z \in X$, as seguintes propriedades:

**(1)** $d(x,y) \ge 0$ e $d(x,y) = 0$ se, e somente se, $x=y$, isto é, a distância é sempre positiva, a menos quando a medidos de um ponto a ele mesmo, o que naturalmente queremos que seja zero;

**(2)** $d(x,y) = d(y,x)$, isto é, a distância entre dois pontos independe da ordem com que se inicia a medida;

**(3)** $d(x,y) \le d(x,z) + d(z,y)$, a desigualdade triangular.

Chamamos a função $d$ de **métrica** e o par $(X,d)$ de **espaço métrico**.

---
``📝`` **Exemplo (Métrica trivial)**

Considere $X$ um conjunto qualquer e defina para $x,y \in X$,
$$
d(x,y) = \begin{cases}
    1 &\text{se } x \neq y \\
    0 &\text{se } x=y.
\end{cases}
$$

É claro que as condições (1) e (2) são satisfeitas. A condição (3) também é trivial no caso em que $x = y$. Se $x \neq y$, note que $d(x,z) + d(z,y) \ge 1$, pois $d(x,z) = 1$ ou $d(y,z) = 1$, dado que $z$ não pode ser simultaneamente igual a $x$ e $y$.

---

---
``📝`` **Exemplo (Métrica - Norma 2)**

Seja $X = \mathbb{R}^n$ e considere $d$ para $x,y \in X$,
$$
d(x,y) = ||x-y||_2 := \sqrt{(x_1-y_1)^2 + \dots + (x_n+y_n)^2},
$$
conhecida como norma-2 no estudo de Álgebra Linear. Mais uma vez, as condições (1) e (2) são triviais. Já a condição (3) é um pouco mais complicada e pode ser demonstrada usando a desigualdade de Cauchy-Schwartz.

Outras métricas podem ser definidas nesse espaço como a norma 1 ou a norma infinito.

---

---
``📝`` **Exemplo (Métrica - Norma infinito para funções contínuas)**

Seja $X = C[a,b]$, o espaço das funções contínuas definidas no intervalo $[a,b]$ e considere $d$ para $f,g \in X$,
$$
d(f,g) = \max_{x \in [a,b]} |f(x) - g(x)|.
$$
O primeiro passo nessa métrica é demonstrar que ela está bem definida, isto é, será que a função $h(x) = |f(x) - g(x)|$ tem máximo no intervalo $[a,b]$? Sabemos que sim pelo [Teorema do valor extremo](https://en.wikipedia.org/wiki/Extreme_value_theorem). As condições (1) e (2) para que $d$ seja métrica são trivialmente satisfeitas. Já a terceira condição é consequência da desigualdade triangular da métrica 
$$
d(x,y) = |x-y|
$$
definida nos reais.
O que acontece com funções não contínuas? E se trocarmos o máximo pelo supremo?

---

---
``📝`` **Exemplo (Pseudo-métrica)**

Seja $X = C[a,b]$ e defina para $f,g \in X$,
$$
d(f,g) = |f(a) - g(a)|.
$$
É claro que $d$ satisfaz as condições (2) e (3) e que $d(f,g) \ge 0$. Todavia, $d(f,g) = 0$ não implica que $f = g$, só fazer $g \equiv f(a) < f(b)$ para verificar esse fato. Chamamos funções que satisfazem (2) e (3), mas não satisfazem essa parte da primeira propriedade de pseudo-métrica.

---

## Noções topológicas 

Seja $(X,d)$ um espaço métrico. Vamos definir alguns conceitos importantes de topologia segundo o ponto de vista de espaços métricos:

**Bola aberta:** Tome $x \in X$ e $r > 0$, então a bola aberta de centro $x$ e raio $r$ é o conjunto $B_r(x) = \{y \in X | d(x,y) < r\}$.

**Ponto interior:** Tome $A \subseteq X$. Dizemos que $x \in A$ é ponto interior de $A$ se para algum $r > 0$, $B_r(x) \subseteq A$. Definimos o **interior** de $A$ como o conjunto $\mathring{A} = \{x \in A | x \text{ é ponto interior}\}$.

**Conjunto aberto:** $A$ é conjunto aberto se $A = \mathring{A}$. 

Seja $\mathcal{O}$ a família de conjuntos abertos de $X$. Então $\mathcal{O}$ satisfaz:

**(i)** $\emptyset \in \mathcal{O}$ e $X \in \mathcal{O}$.

**(ii)** Se $O_{\alpha} \in \mathcal{O}$ para $\alpha \in \Alpha$ sendo um conjunto de índices arbitrário, então $\cup_{\alpha \in \Alpha} O_{\alpha} \in \mathcal{O}$. 

**(iii)** Se $O_1, \dots, O_n \in \mathcal{O}$ para $n \in \mathbb{N}$, então $\cap_{i=1}^n O_i \in \mathcal{O}$.

*Observação: Podemos definir uma Topologia partindo de (i)-(iii) como axiomas.*

*Observação 2: Se considerarmos o item (iii) com $n = \infty$, a propriedade não vale! Para isso, basta considerar $O_i = (-i^{-1}, i^{-1}) \subseteq \mathbb{R}$.*

**Ponto de aderência:** Um ponto $x$ é um ponto de aderência de um conjunto $A \subseteq X$ se para qualquer $r > 0$, $B_r(x) \cap A \neq \emptyset$. O conjunto desses pontos é chamado de **fecho** e é denotado por $\bar{A}$.

Em particular, a partir dessa definição, podemos concluir que (i) $A \subseteq \bar{A}$, (ii) se $A \subseteq B$, então $\bar{A} \subseteq \bar{B}$, e (iii) $\overline{A \cup B} = \bar{A} \cup \bar{B}$.

---
``📝`` **Exemplo (Espaço $L^2$ e funções contínuas)**

Seja $X = L^2(0,T)$, o espaço de funções Lebesgue mensuráveis definidas em $[0,T]$ que satisfaçam 
$$
\int_X |f(x)|^2 \, dx < +\infty
$$
com métrica para $f,g \in X$ definida por
$$
d(f,g) = \left(\int_X (f(x) - g(x))^2 \, dx\right)^{1/2}.
$$
Se $A = C[0,T]$ é o conjunto das funções contínuas em $[0,T]$, sabemos que $A \subset X$. Além disso, 
$\bar{A} = X$. Dizemos que $A$ é **denso** em $X$ (veja [esse link](https://math.stackexchange.com/questions/226049/continuous-functions-on-0-1-is-dense-in-lp0-1-for-1-leq-p-infty)).

---

**Ponto limite (acumulação):**  O ponto $x$ é ponto limite de $A \subseteq X$ se, e somente se, para todo $r > 0$, $B_r(x) \cap A$ contém infinitos pontos. 
O conjunto desses pontos é o **conjunto derivado** e é denotado por $A '$. Um ponto $x \in A$ que não é limite é chamado de **ponto isolado**.

**Convergência:** Seja $\{x_n\}_{n \in \mathbb{N}} \subseteq X$ uma sequência de pontos. Dizemos que $\{x_n\}$ converge para o ponto $x$ se para todo $r > 0$, existe $N(r)$ tal que $n > N(r)$ implica $x_n \in S_r(x)$. Nesse caso, denotamos por $x_n \to x$. Logo, a definição de convergência é equivalente a afirmar que $d(x,x_n) \to 0$ nos reais.

Uma consequência dessa definição é que $x \in \bar{A}$ se, e somente se, existe uma sequência $\{x_n\}$ tal que $x_n \in A$ para todo $n \in \mathbb{N}$ e $x_n \to x$.

**Conjunto fechado:** Dizemos que $A$ é fechado se $A$ contém todos os seus pontos limite, isto é, $A' \subseteq A$. De forma equivalente $A = \bar{A}$.

**Teorema (relação entre conjuntos abertos e fechados):**  $A$ é fechado se, e somente se, $A^c$ é aberto. 
Esse teorema permite usar as propriedades de abertos para fechados através da [lei de DeMorgan](https://en.wikipedia.org/wiki/De_Morgan%27s_laws).

>  *"How often have I said to you that when you have eliminated the impossible, whatever remains, however improbable, must be the truth?"* - Sherlock Holmes. (Quantas vezes eu falei para você que quando você eliminou o impossível, qualquer coisa que sobra, mesmo que improvável, deve ser verdadeiro? - tradução livre)

## Continuidade

Sejam $(X,d)$ e $(Y,d')$ dois espaços métricos e $f: X \to Y$ uma função. $f$ é dita **contínua** no ponto $x_0 \in X$ se para qualquer $\epsilon > 0$, existe $\delta > 0$ tal que 
$$
f(B_{\delta}(x_0)) \subseteq B_{\epsilon}(f(x_0)).
$$
A função é contínua em $X$ se for contínua em todos os pontos de $X$.

Intuitivamente, estamos dizendo que a função $f$ mapeia uma vizinhança de $x_0$ suficientemente pequena em uma vizinhança arbitrariamente pequena de $f(x_0)$, isto é, por mais pequena que seja a vizinhança tomada de $f(x_0)$, a função $f$ é tão "regular", que ela encontra uma vizinhança de $x_0$ para mapear na de $f(x_0)$. Por **vizinhança** de $x$, queremos dizer um conjunto aberto que contenha $x$. De forma equivalente, uma bola aberta de centro $x$.

**Teorema:** $f: X \to Y$ é contínua no ponto $x \in X$ se, e somente se, para todo sequência de pontos $\{x_n\}$ com $x_n \to x$, vale que $f(x_n) \to f(x)$.  

---

Um rascunho para a demonstração é o seguinte: 

- (Necessidade): Suponha $f$ contínua e tome $x_n \to x$. Nesse caso, para todo $\epsilon > 0$, existe $\delta$ tal que $f(B_{\delta}(x)) \subseteq B_{\epsilon}(f(x))$. Para $n$ suficientemente grande, teremos que $x_n \in B_{\delta}(x_0)$ e, portanto, $f(x_n) \in B_{\epsilon}(f(x))$. Como $\epsilon$ é arbitrariamente pequeno, $f(x_n) \to f(x)$.

- (Suficiência) Tome $\epsilon > 0$. Suponha que para todo $\delta_n = 1/n$, exista $y_n$ tal que 
$$
d(f(y_n), f(x)) \ge \epsilon,
$$
isto é, $y_n \in B_{\delta_n}(x)$, mas $f(y_n) \not \in B_{\epsilon}(f(x))$. 
Está claro que $y_n \to x$, mas $f(y_n) \not \to f(x)$, o que implica que $f$ não é contínua em $x$. Provamos pela contrapositiva.

---

Outra equivalência com continuidade é a seguinte:

**Teorema:** A função $f: X \to Y$ é contínua se, e somente se, para todo conjunto $F \subseteq Y$ fechado (aberto), $f^{-1}(F)$ é fechado (aberto) em $X$.