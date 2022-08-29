# Conjuntos completos ortonormais

Nessa parte, entraremos de forma mais profunda nos resultados de conjuntos completos ortonormais. 
Antes disso, vale a pena lembrar a definição: um conjunto é ortonormal quando todo vetor tem norma 1 e os vetores são ortogonais dois a dois.
Ele é completo quando ele não é contido por um conjunto ortonormal maior.
Uma forma de verificar a completude é verificando que todo vetor ortogonal ao conjunto deve ser nulo, isto é, não existe vetor não nulo e ortogonal ao conjunto ortonormal completo.

## Identidade de Parseval

**Teorema:** Seja $S$ um subconjunto denso do espaço com produto interno $X$.
Seja $A = \{x_{\alpha}\}_{\alpha \in \Lambda}$ um conjunto ortonormal.
Se para todo $y\in S$,
$$
\|y\| = \sum_{\lambda} |\langle y, x_{\alpha} \rangle|^2,
$$
então $A$ é completo.

---

Note que já temos esse resultado quando $S = X$.
Portanto, falta mostrar que se vale para todo $S \neq X$, então vale para o limite de pontos de $S$, que é exatamente $X$.

---

**Cardinalidade de conjuntos ortonormais completos:** Sejam $A$ e $B$ conjuntos completos ortonormais no espaço com produto interno $X$. 
Então, $A$ e $B$ tem a mesma cardinalidade.

**Estrutura de Espaços de Hilbert:** Um espaço com produto interno de dimensão $n$ é congruente a $\mathcal{C}^n$. Se $X$ tem dimensão infinita, mas é separável, então ele é congruente a $l^2$.

## Teorema da projeção para espaços de Hilbert

**Teorema:** Seja $M$ um subespaço fechado de $X$ (Hilbert) e tome $x \in X$. 
Denote $d = \inf_{y \in M} \|y-x\|$.
Existe $y \in M$ tal que $\|y-x\| = d$.

---
Ideia da prova:

- Considere $\{y_n\} \subseteq M$ tal que $\|y_n - x\| \to d$. A ideia é provar que essa sequência é Cauchy e, em particular, convergente.
Pelo subespaço ser fechado, o vetor limite pertence a ele e pela continuidade da norma, vale o resultado desejado.

- Note que pela lei do paralelogramo, 
$$
\|y_n - y_m\|^2 = 2\|y_n - x\|^2 + 2\|y_m - x\|^2 - 4\|(y_n + y_m)/2 - x\|^2 
$$
e que $\|(y_n + y_m)/2 - x\|^2 \ge d^2$, pois $(y_n + y_m)/2 \in M$. 
Por fim, basta aplicar o limite em $n$ e $m$.

---

**Teorema:** Seja $M$ subespaço fechado de $X$ (Hilbert) e $N$ subespaço próprio que contém $M$.
Então existe $w \in N$ tal que $w \perp M$.

---
Ideia da prova:

- Tome $x \in N-M$ e denote $d = d(x,M) = \|y-x\|$ para algum $y \in M$.
- Denote $w = y-x \in N$ e vamos provar que $w \perp M$.
- Para isso, note que $\|w + \alpha z\| = \|y+\alpha z - x\| \ge d = \|w\|$ para $z \in M$.
Observe que $\|w + \alpha z\| - \|w\| \ge 0$, mas com $\alpha = \beta\langle w, z \rangle$, existe $\beta$ que contradiz essa desigualdade. Daí só vale que $\langle w,z \rangle = 0$.

---

### Algumas propriedades de espaços de Hilbert

(1) Se $X$ é espaço com produto interno e $S$ um subconjunto, então $S^{\perp}$ é subespaço fechado.

(2) $S \cap S^{\perp} \subseteq \{0\}$.

(3) Vale que $S \subseteq S^{\perp\perp}$ e que $S_1 \subseteq S_2 \implies S_2^{\perp} \subseteq S_1^{\perp}$ para subconjuntos quaisquer.

(4) Se $X$ é espaço de Hilbert e $M$ é subespaço fechado, então $M = M^{\perp \perp}$.
Se $S$ for um subconjunto qualquer, $S^{\perp} = S^{\perp \perp \perp}$ e $S^{\perp \perp} = \overline{[S]}$.

**Teorema:** Sejam $M$ e $N$ subespaços fechados de $X$ (Hilbert) e suponha que $M \perp N$.
Então $M + N$ é subespaço fechado.

### Teorema da projeção

Se $M$ é subespaço fechado do espaço de Hilbert $X$, então $X = M \oplus M^{\perp}$.



