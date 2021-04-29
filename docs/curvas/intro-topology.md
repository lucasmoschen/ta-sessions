# Introdução à topologia 

Topologia é uma área da matemática que estuda objetos geométricos com noções
de continuidade e convergência. Material na *internet* sobre esse tópico não
falta, mas eu gostaria de destacar o curso de [Introdução à Topologia
Geral](http://andrec.mat.unb.br/introducao_a_topologia/) da Universidade de
Brasília pelo professor André Caldas. Estudar topologia pode contribuir para a
compreensão de superfícies em um nível mais profundo, pois uma superfície em
$\mathbb{R}^3$ é um objeto que se parece com um plano na vizinhança de todo
ponto.  Mas esses conceitos só ficam precisos com o estudo de topologia. Aqui
faremos apenas um resumo de alguns conceitos sob a ótica do que chamamos de
*espaços métricos*. 

---

## Definições básicas

**Bola aberta:** A bola aberta de centro $x \in \mathbb{R}^n$ e raio $r > 0$ é
o conjunto $\mathcal{B}_r(x) = \{y \in \mathbb{R}^n : ||x-y|| < r\}$. Se
$n=1$, esses conjuntos são chamados de intervalos abertos e se $n=2$ de discos
abertos. 

**Bola fechada:** $\bar{\mathcal{B}}_r(x) = \{y \in \mathbb{R}^n : ||x-y|| \le
r\}$.

**Conjunto aberto:** Dizemos que o conjunto $U \subseteq \mathbb{R}^n$ é aberto
se $\forall x \in U, \exists \epsilon > 0$ tal que $\mathcal{B}_{\epsilon}(x)
\subseteq U$. 

**Conjunto fechado:** Dizemos que $F \subseteq \mathbb{R}^n$ é fechado se
$F^c$ é aberto. 

**Lema:** Toda bola aberta é um conjunto aberto. 

**Proposição:** A partir da definição de conjunto aberto, podemos demonstrar que:

**(i)** O conjunto vazio $\emptyset$ é aberto. 

**(ii)** A união de conjuntos abertos é um conjunto aberto.

**(iii)** A intersecção finita de de conjuntos abertos é aberta. 

Podemos definir uma topologia usando (i)-(iii).

**Ponto interior:** se $x \in A \subseteq \mathbb{R}^n$ é ponto interior de $A$
se existe $\epsilon > 0$ tal que $\mathcal{B}_{\epsilon}(x) \subseteq A$. 

---

**Vizinhança:** Dizemos que $U \subseteq \mathbb{R}^n$ é uma vizinhança do ponto
$x \in \mathbb{R}^n$ se existe $\epsilon > 0$ tal que
$\mathcal{B}_{\epsilon}(x) \subseteq U$. 

**Ponto de fronteira:** Se $x \in \mathbb{R}$ é ponto de fronteira de $A$ se
$\forall \epsilon > 0$, a bola $\mathcal{B}_{\epsilon}(x)$ contém pontos de
$A$ e pontos de $A^c$. O conjunto desses pontos é notado como $\partial A$. 

**Caracterização de conjuntos fechados:** Seja $F \subseteq \mathbb{R}^n$. Ele
é fechado se, e somente se, toda sequência de elementos de $F$ converge a um
elemento de $F$. 

## Convergência e continuidade

**Convergência:** Seja $\{x_n\}_{n \in \mathbb{N}} \subseteq \mathbb{R}^n$ uma
sequência de pontos. Dizemos que $x_n$ converge para um ponto $x^* \in
\mathbb{R}^n$, quando $\forall \epsilon > 0$, existir $N \in \mathbb{N}$ tal
que $n \ge N, d(x_n, x^*) < \epsilon$ e denotamos $x_n \to x^*$. 

**Ponto de aderência:** Seja $A \subseteq \mathbb{R}^n$. Dizemos que $a \in
\mathbb{R}^n$ é ponto aderente de $A$ se existe $\{x_n\} \subseteq A$ tal que
$x_n$ converge para $a$. 

**Continuidade:** Uma função $f : \mathbb{R}^n \to \mathbb{R}^m$ é contínua se
para todo conjunto aberto $V \subseteq \mathbb{R}^m$, a imagem inversa
$f^{-1}(V) = \{x \in \mathbb{R}^n | f(x) \in V\}$ é conjunto aberto. 

De forma equivalente, dizemos que $f$ é contínua em $a \in \mathbb{R}^n$
quando para todo sequência $\{x_n\} \subseteq \mathbb{R}^n$ convergente para
$a$, então $f(x_n)$ converge para $f(a)$ e $f$ é contínua quando é contínua
para todo ponto $a \in \mathbb{R}^n$. 

Agora, se $f: X \subseteq \mathbb{R}^n \to Y \subseteq \mathbb{R}^m$, dizemos 
que ela é contínua quando para todo $V \subseteq \mathbb{R}^m$, existe um
conjunto aberto $U \subseteq \mathbb{R}^n$ tal que $U \cap X = \{x \in U: f(x)
\in V\}$. 

**Homeomorfismo:** Se $f : X \to Y$ é contínua e bijetiva e se o mapa inverso
$f^{-1} : Y \to X$ também é contínuo, dizemos que $f$ é um homeomorfismo e $X$
e $Y$ são *homeomorfos*. 

**Difeomorfismo:** Sejam $X \subseteq \mathbb{R}^n$ e $Y \subseteq
\mathbb{R}^m$. Dizemos que $f : X \to Y$ é diferenciável quando para cada $a
\in X$, existe uma extensão um aberto $U \subseteq \mathbb{R}^n$ contendo $a$
tal que $F: U \to \mathbb{R}^m$ é diferenciável e $F|_{U \cap X} = f|_{U \cap
X}$. Se $f$ é um homeomorfismo diferenciável e $f^{-1}$ é diferenciável, então
$f$ é um difeomorfismo. Então $X$ e $Y$ são difeomorfos. 