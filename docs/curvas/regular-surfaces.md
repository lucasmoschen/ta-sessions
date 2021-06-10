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

**Definição:** O vetor normal unitário a $S$ no ponto $p$ é dado por 
$$
N_{\sigma} = \frac{\sigma_u \times \sigma_v}{||\sigma_u \times \sigma_v||}
$$
que é exatamente o vetor normal ao plano tangente. Note que esse vetor não é
independente da escolha do patch $\sigma : U \to \mathbb{R}^3$. Se
$\tilde{\sigma} : \tilde{U} \to \mathbb{R}^3$ é outro patch regular para $S$
em $p$, podemos demostrar que:

**Proposição:** Seja $\phi : \tilde{U} \to U$ um difeomorfismo. Então
$\tilde{\sigma} = \sigma \circ \phi : \tilde{U} \to \mathbb{R}^3$ é um mapa
regular. Além disso, 
$$
\tilde{\sigma}_{\tilde{u}} \times \tilde{\sigma}_{\tilde{v}} = \operatorname{det}(J(\phi)) \,
\tilde{\sigma}_u \times \tilde{\sigma}_v  
$$
em que $\operatorname{det}(J(\phi))$ é o determinante do Jacobiano da transformação $\phi$.
Portanto $N_{\tilde{\sigma}} = \operatorname{sign}(\operatorname{det}(J(\phi))) N_{\sigma}$.

**Orientabilidade:** Dizemos que $S$ é superfície orientável se existe um
atlas $A$ para $S$, de forma que, para quaisquer dois patches $\sigma_1$ e
$\sigma_2$ em $A$, se $\phi$ é o mapa de transição entre eles, então
$\operatorname{det}(J(\phi)) > 0$. 

### Abordagem alternativa 

A abordagem utilizada por [Ronaldo
Freire](https://www.sbm.org.br/wp-content/uploads/2016/06/Introdu%C3%A7%C3%A3o-a-Geometria-Diferencial_Ronaldo-Freire-Lima.pdf)
é um pouco diferente e será apresentada nessa subseção. 

**Definição (campos):** Seja uma superfície $\mathcal{S}$. Uma aplicação $f:
\mathcal{S} \to \mathbb{R}^3$ é chamada de campo. Ela será *unitária* quando $||f(p)||
= 1$ para todo ponto da superfície; *tangente* se sua imagem está contida no
espaço (plano) tangente; e *normal* se pertence ao complemento ortogonal do
espaço tangente, isto é, sua imagem é ortogonal ao plano tangente. 

Quando o campo é normal, unitário, e diferencial, denotamos por $N : \mathcal{S} \to
\mathbb{R}^3$. Note que sempre podemos definir essa função associando cada
ponto da superfície ao vetor normal à superfície que passe no ponto. 

**Superfície orientável:** Uma superfície regular é *orientável* quando
podemos definir um campo $N$ nessa superfície. Esse campo define a orientação
da superfície, quando existir. 

Uma superfície regular não orientável é a [*fita de Moebius*](https://www.youtube.com/watch?v=vLgCq4ikl78), uma faixa de
papel com uma das extremidades torcidas. 

**Atlas coerente:** Um atlas (família de parametrizações de uma superfície) é
*coerente* quando dadas duas parametrizações $\sigma_1$ e $\sigma_2$ do atlas,
o mapa de transição entre as parametrizações tem determinante positivo. Note
que essa é a definição que Pressley utiliza. Podemos provar (inclusive Freire
prova) que ambas são definições equivalentes.