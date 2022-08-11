# Teorema de Hahn Banach

Queremos generalizar um pouco mais a ideia de norma para um **funcional convexo**.
Será fácil verificar que toda norma é um funcional convexo e, portanto, resultados para esses funcionais serão válidos para normas em geral.

> Um **funcional linear** é um mapa $f : X \to \mathbb{R}$ que é uma transformação linear.
> Um **funcional convexo** é um mapa 
> $$
> p : X \to \mathbb{R}
> $$
> que satisfaz 
> 
> **(I)** $p(x) \ge 0$ para todo $x \in X$; 
> 
> **(II)** $p(x+y) \le p(x) + p(y)$ para todo $x,y\in X$;
>
> **(II)** $p(\alpha x) = \alpha p(x)$ para todo $x \in X$, $\alpha \ge 0$.
> Se o item (I) não é satisfeito, chamamos $p$ de **funcional sublinear**.

**Lema:** Seja $M$ subespaço próprio de $X$ e $x_0 \in M^c$. 
Defina $N = [M \cup \{x_0\}]$, isto é, o menor subespaço que contém $M \cup \{x_0\}$.
Suponha que $f$ é um funcional linear em $M$, $p$ é um funcional sublinear em $X$ e $f(x) \le p(x)$ para todo $x \in M$.
Assim, **existe** um funcional linear $F$ em $N$ que estende $f$ e satisfaz $F(x) \le p(x)$ para todo $x \in N$.

Em resumo, ao incluir uma dimensão em nosso subespaço, conseguimos estender um funcional linear que ainda é limitado por um sublinear.

---
Ideia da prova:

1. Note que para $y_1, y_2 \in M$, tem-se que
$$
-p(-y_2 -x_0) - f(y_2) \le p(y_1+x_0) - f(y_1),
$$
o que implica que existe $c_0$ entre o supremo do lado esquerdo em $y_2$ e o ínfimo do lado direito em $y_1$.

2. Qualquer elemento de $N$ é unicamente escrito como 
$$
x = y + \alpha x_0.
$$
Assim, podemos definir 
$$
F(y +  \alpha x_0) = f(y) + \alpha c_0. 
$$

3. É claro que $F$ é linear e que $F$ estende $f$.
Falta verificar se $\alpha \neq 0$, então $F(x) \le p(x)$. 
Isso é verificável usando a desigualdade em (1).

A partir desse lema, podemos obter o seguinte famoso resultado.

---

**Teorema (Hahn-Banach):** Seja $M$ um subespaço de $X$, $p$ um sublinear e $f$ um funcional linear definido em $M$, tal que $f(x) \le p(x)$ para todo $x \in M$.
Assim, existe um funcional linear $F$ que estende $f$ em $X$ e satisfaz 
$$F(x) \le p(x)$$ 
para todo $x \in X$.

---
Ideia da prova:

1. Defina $S$ a classe de todos os funcionais lineares que estendem $x$ e que satisfazem $f(x) \le p(x)$ para $x$ no seu domínio $D_f$.
2. É claro que $S$ não é vazio, já que $f \in S$ para $D_f = M$.
3. Defina a seguinte ordem: $f_1 < f_2 \in S$ se $f_2$ estende $f_1$, que induz uma ordenação parcial em $S$. 
4. Precisamos provar que $S$ é indutivamente ordenado, isto é, todo subconjunto de $S$ totalmente ordenado tem um limite superior. 
A partir de um conjunto totalmente ordenado $\{f_{\alpha}\}$, basta considerarmos uma função cujo domínio seja $\cup_{\alpha} D_{f_{\alpha}}$.
Nesse caso, define-se que $f(x) = f_{\alpha}(x)$ quando $x \in D_{f_{\alpha}}$. Precisamos verificar que essa união é um subespaço e que $f$ é bem definida, mas isso é consequência do conjunto ser totalmente ordenado.
5. O Lema de Zorn implica a existência de um elemento maximal $F$ de $S$. 
6. Falta provar que $D_F = X$, mas isso é resultado do lema anterior, pois caso não fosse, poderíamos estender esse funcional, caindo em contradição.

---

## Funcionais lineares limitados

Em espaços normados, o conceito de continuidade para funcionais lineares é mais simples.
Se $f$ é um funcional linear contínuo em $x \in X$, então $f$ será contínuo em todo ponto do espaço.
Mais do que isso, continuidade e limitação de $f$ são equivalentes em espaços normados.

> Um funcional linear $f$ em um espaço normado é **limitado** se existe uma constante $k$ tal que $f(x) \le k\|x\|$ para todo $x \in X$.

**Teorema:** Seja $X$ um espaço normado e $f$ um funcional linear. Então $f$ é contínuo se, e só se, $f$ é limitado.

## Espaço conjugado

Em um espaço normado, se $f$ é um funcional linear limitado, defina 
$$
\|f\| = \sup_{x \neq 0} \frac{|f(x)|}{\|x\|} = \sup_{\|x\|=1} |f(x)|.
$$
O espaço de todos os funcionais limitados sobre $X$ com essa norma é chamado de **espaço conjugado** $\tilde{X}$.
Podemos demonstrar que $\tilde{X}$ é espaço de Banach.

**Teorema:** Se $X$ tem dimensão finita, todos os funcionais lineares são limitados (logo, contínuos), isto é, $\tilde{X}$ contém todos os funcionais lineares.

## Consequências do teorema de Hahn-Banach

## Teorema da Representação de Riesz
