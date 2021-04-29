# Superfícies

**Definição:** Dizemos que $S \subseteq \mathbb{R}^n$ é uma *superfície* se
para todo ponto $p \in S$, existe um conjunto aberto $U \subset \mathbb{R}^2$
e um conjunto aberto $W \subseteq \mathbb{R}^3$ contendo $p$ tal que $S \cap
W$ é homeomorfo a $U$.  O homeomorfismo $\sigma : U \to S \cap W$ é um
*patch* ou *parametrização*. A coleção desses homeomorfismos que cobrem $S$ é
chamada de *atlas*. 

Dizemos que $S \cap W$ é aberto em $S$ sempre que $W$ for aberto. 

Observe que para cada ponto da superfície, olhamos para uma vizinhança dele
(conjunto aberto que o contém) e essa vizinhança restrita à superfície deve
ser "parecida" com um subconjunto do plano. Quando caminhamos no planeta,
temos a sensação de caminharmos num plano justamente por esse conceito. 

Também observe que nosso atlas pode ser formado por uma quantidade infinita de
patches, mas, em geral, existe um número mínimo.

## Superfícies suaves

**Definição:** Um patch $\sigma : U \to \mathbb{R}^3$ é *regular* se é uma
função suave (diferenciável nas três componentes com derivadas parciais
contínuas de todas as ordens) e os vetores $\sigma_u =
\frac{\partial}{\partial u} \sigma$ e $\sigma_v =
\frac{\partial}{\partial v} \sigma$ são linearmente independentes para todo
$(u,v) \in U$. Isto é, basta exigir que $\sigma_u \times \sigma_v \neq 0$. 
Uma *superfície regular* é uma superfície tal que $p \in S$, existe um patch
regular cuja imagem contenha $p$. 

**Proposição:** Sejam $U$ e $V$ abertos de $\mathbb{R}^2$ e $\sigma : U \to
\mathbb{R}^3$ um patch regular. Seja $\phi : V \to U$ um difeomorfismo. Então 
$\tilde{\sigma} = \sigma \circ \phi : V \to \mathbb{R}^3$ é um patch regular.
Dizemos que $\sigma$ e $\tilde{\sigma}$ são reparametrizações um do outro e
$\phi$ um mapa reparametrização. 

Esse princípio permite que definhamos uma propriedade para superfícies
regulares desde que definhamos para qualquer patch regular de forma que será
inalterada para outra parametrização. 

## Tangentes

## Normais e orientabilidade 