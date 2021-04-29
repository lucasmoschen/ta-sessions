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

## Mapas suaves 

Queremos entender a noção de mapa suave entre duas superfícies suaves. Até
agora, definimos a suavidade entre conjuntos de $\mathbb{R}^n$. Suponha que as
superfícies $S_1$ e $S_2$ são cobertas pelos patches $\sigma_1 : U_1 \to
\mathbb{R}^3$ e $\sigma_2 : U_2 \to \mathbb{R}^3$, respectivamente. Dizemos
que $f$ é *suave* se $\sigma_2^{-1} \circ f \circ \sigma_1 : U_1 \to U_2$ é
suave. 

Além disso, se $f: S_1 \to S_2$ é um difeomorfismo e $\sigma_1$ é um patch
regular $S_1$, então $f \circ \sigma_1$ é um patch regular em $S_2$. 

## Tangentes

**Definição:** Um *vetor tangente* a uma superfície $S$ em um ponto $p \in
S$ é o vetor tangente em $p$ de uma curva em $S$ que passa por $p$. O *espaço
tangente* é o conjunto desses vetores e é denotado por $T_pS$.  

Seja uma curva $\alpha$ em $S$. que passa por $p$. Em uma vizinhança de $p$,
podemos dizer que $\alpha(t) = \sigma(u(t), v(t))$ tal que $\alpha(t_0) = p$.
Podemos provar que $u$ e $v$ são suaves. Essa curva tem uma tangente em $p$
denotada por $\alpha '(t_0)$. Mas note que, essa curva não é necessariamente a
única que passa por $p$. 

Essa definição é pouco tratável para enxergar o espaço tangente. Para
isso, o teorema a seguir propõe uma caracterização mais palatável: 

**Proposição:** Seja $\sigma : U \to \mathbb{R}^3$ um patch da superfície $S$
que passa pelo ponto $p$ em $(u_0, v_0)$. O espaço tangente a $S$ em $p$ é o
plano gerado pelos vetores $\sigma_u(u_0, v_0)$ e $\sigma_v(u_0, v_0)$ que
passa pela origem.  Observe que o plano tangente é independente da escolha do
patch. 

**Derivada de mapa suave:** Com a definição de mapa tangente, podemos definir
a derivada de um para $f: S_1 \to S_2$. A derivada de $f$ em $p \in S_1$ mede
a variação de $f(p) \in S_2$ quando $p$ se move em sua vizinhança. 

Assim, dizemos que a derivada $D_pf$ de $f$ em $p \in S$ é um mapa 
$$
D_pf : T_pS_1 \to T_{f(p)}S_2
$$
tal que, se $w \in T_pS_1$, existe uma curva $\alpha$ em $S_1$ tal que $w = \alpha
'(t_0)$. Então $\gamma = f \circ \alpha$ é uma curva em $S_2$ passando por
$f(p)$ em $t_0$ e, então $D_{f(p)}S_2 = \gamma '(t_0)$. 

## Normais e orientabilidade 