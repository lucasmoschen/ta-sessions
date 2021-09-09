# O Método das Características

Considere a Equação Diferencial Parcial (EDP) 
$$
F\left(\frac{\partial u}{\partial x_1}, \dots, u, \frac{\partial
u}{\partial x_n}, x_1, \dots, x_n\right) = F(x, u, \nabla u) = F(x, u, Du) = 0,
$$
definida em um conjunto $U$. Além disso, suponha que $u = g$ na fronteira
de $U$, em que $g$ é dada função suave. 

## Descrição do método

A ideia geral desse método é transformar a EDP em um sistema de EDOs, em que
temos uma teoria de resolução bem estabelecida. Nisso, vamos construir
curvas da superfície formada por $u$ e integrar nessas curvas. Seja $\gamma(s)
= (a_1(s), \dots, a_n(s))$ essa curva (definida em $U$). Assumindo que $u$ é duas vezes
continuamente diferenciável, defina 
$$
z(s) := u(\gamma(s)).
$$
Também defina $p(s) = \nabla u(\gamma(s)) = (u_{x_1}(\gamma(s)), \dots,
u_{x_n}(\gamma(s)))$. Temos que (Regra da Cadeia)
$$
\frac{d}{ds}p_i(s) = \sum_{j=1}^n u_{x_ix_j}(\gamma(s))\frac{d}{ds}a_j(s).
$$
Voltando à EDP $F(x, u, Du) = 0$, derivando com respeito a $x_i$, 
$$
\sum_{j=1}^n F_{u_j} (Du, u, x)u_{x_j x_i} + F_z(Du, u, x)u_{x_i} +
F_{x_i}(Du, u, x) = 0.
$$
Vamos usar essa expressão para remover as segundas derivadas de $u$ (que são
em geral complicadas de se encontrar) Para isso, definimos 
$$
\frac{d}{ds}a_i(s) = F_{p_i}(p(s), z(s), \gamma(s)), i = 1, \dots n, 
$$
isto é, estamos definindo uma curva a partir de sua função tangente. Assumindo
isso e avaliando a expressão em $\gamma(s)$, obtemos que $u_{x_i}(\gamma(s)) =
p_i(s)$, logo 
$$
\sum_{j=1}^n F_{p_j} (p(s), z(s), \gamma(s))u_{x_j x_i}(\gamma(s)) + F_z(p(s), z(s), \gamma(s))p_i(s) +
F_{x_i}(p(s), z(s), \gamma(s)) = 0.
$$
Usando a expressão de $\frac{d}{ds}p_i(s)$ dada mais acima, teremos que 
$$
\frac{d}{ds}p_i(s) = - F_{x_i}(p(s), z(s), \gamma(s)) - F_z(p(s), z(s),
\gamma(s))p_i(s), 
$$
o que nos dá uma EDO para a função $p(s) = \nabla u(\gamma(s))$. Além disso,
diferenciando $z$ obtemos 
$$
\frac{d}{ds}z(s) = \sum_{j=1}^n u_{x_j}(\gamma(s))\frac{d}{ds}a_j(s) =
\sum_{j=1}^n p_j(s)F_{p_j}(p(s), z(s), \gamma(s)). 
$$
Isso nos reduz a um sistema de EDOs: 
$$
\begin{cases}
    \dot{p}(s) = - D_x F(p(s), z(s), \gamma(s)) - D_z F(p(s), z(s),
    \gamma(s))p(s) \\
    \dot{z}(s) = D_p F(p(s), z(s), \gamma(s))\cdot p(s) \\
    \dot{\gamma}(s) = D_p(p(s), z(s), \gamma(s)),
\end{cases}
$$
em que $D$ é a derivada (no caso vetorial, mas você pode pensar indivíduo a
indíviduo usando as expressões derivadas acima). Além disso, ao longo da curva
$\gamma(s)$, 
$$
F(p(s), z(s), \gamma(s)) = 0, 
$$
pela própria definição da $F$. 

## F é linear

Considere $F(Du, u, x) = b(x)\cdot Du(x) + c(x)u(x) = 0$, isto é, o caso
linear. Ao longo das curvas características, $F(p,z,x) = b(x)\cdot p + c(x)z$.
Assim, 

$$
\begin{cases}
    \dot{p}(s) = - D_x F(p(s), z(s), \gamma(s)) - D_z F(p(s), z(s),
    \gamma(s))p(s) \\
    \dot{z}(s) = D_p F(p(s), z(s), \gamma(s))\cdot p(s) = b(\gamma(s))\cdot
    p(s) = -c(\gamma(s))z(s) \\
    \dot{\gamma}(s) = D_p(p(s), z(s), \gamma(s)) = b(\gamma(s)),
\end{cases}
$$
Com isso, mesmo sem saber $p$, ainda conseguimos derivar $z$, o que simplifica
bastante o problema. 

<img src="../example.png" alt="Exemplo de solução de EDP"
style="width:500px;height:600px;">

## Condições de fronteira 

Anteriormente, definimos um sistema de equações diferenciais para resolver
$u(x)$. Todavia, esse sistema admite infinitas soluções quando não
especificado uma condição inicial. Para isso, tome $x_0$ na fronteira de $U$,
onde sabemos que $u = g$. Em geral, assumimos que essa fronteira fica no plano
${x_n = 0}$ próximo de $x_0$. Como assim? 

- Suponha que estamos com $U \subseteq \mathbb{R}^2$ e que a solução seja dada
  pela função $u(x,t)$. Estamos dizendo que se $\gamma(0) = (x_0, 0)$, sendo
  $\gamma$ a curva característica. 
- Suponha que $U \subseteq \mathbb{R}^4$ e que a solução seja dada
  pela função $u(x_1, \dots, x_4)$. Estamos dizendo que se $\gamma(0) =
  (x^{1}_0, x^{2}_0, x^{3}_0, 0)$.
  
Quando temos uma variável temporal, em geral denotada po $t$, dizemos que ela
sempre começa em 0, uma forma de "padronizar". Sugiro o livro do Lawrence,
seção 3.2.3 para uma demonstração de que essa suposição faz sentido. Dado um
$x_0$, falta agora definir 

$$
p(0) = p_0, z(0) = z_0, \gamma(0) = (x_0,0). 
$$

Está claro que $z_0 = u(\gamma(0)) = u(x_0, 0) = g(x_0)$. Além disso, 

$$
u(x_1, \dots, x_{n-1}, 0) = g(x_1, \dots, x_{n-1})
$$

na vizinhança de $x_0$ e, portanto, podemos diferenciar para obter 

$$
u_{x_i}(x_0,0) = g_{x_i}(x_0), \text{ para } i = 1,\dots, n-1.
$$

Dessa fora, $(p_0)^i = g_{x_i}(x_0)$ para cada $i$. Para determinar $(p_0)^n$,
usamos a relação dada por $F$, isto é, 
$$
F(p_0, z_0, x_0) = 0,
$$
por definição. As relações de $z(0)$ e $p(0)$ são chamadas de *condições de
compatibilidade*. Note que pode não existir ou pode não ser único a solução de
$p_0$ através da equação $F = 0$. 

## Existência local de soluções

Dado $y = (y_1, \dots, y_{n-1}, 0)$, queremos resolver 

$$
\begin{cases}
    \dot{p}(s) = - D_x F(p(s), z(s), \gamma(s)) - D_z F(p(s), z(s),
    \gamma(s))p(s) \\
    \dot{z}(s) = D_p F(p(s), z(s), \gamma(s))\cdot p(s) = b(\gamma(s))\cdot
    p(s) = -c(\gamma(s))z(s) \\
    \dot{\gamma}(s) = D_p(p(s), z(s), \gamma(s)) = b(\gamma(s)),
\end{cases}
$$

com $\gamma(0) = y, p(0) = p_0, z(0) = z_0$, com as expressões de
compatibilidade derivadas acima. 

**Lema (Uma aplicação do Teorema da Função Inversa):** Assuma que
$F_{p_n}(p_0, z_0, x_0) \neq 0$. Então existe $I \ni 0 \subseteq \mathbb{R}$,
uma vizinhança $W$ de $x_0$ na fronteira de $U$ e uma vizinhança $V$ de $x_0$
em $\mathbb{R}^n$   tal que para cada $x \in V$, existe um único $s \in I, y
\in W$ tal que 
$$
x = \gamma(y,s) = \gamma(y_1, \dots, y_{n-1},s).
$$

Essa lema é uma consequência do Teorema da Função Inversa. Não se preocupe
tanto com a demonstração. Mas a ideia é que se provarmos que $\det
D\gamma(x_0, 0) \neq 0$, valerá a invertibilidade que estamos propondo, isto
é, um mapa $x \mapsto (y,s)$. 

Assim, seja $y = y(x)$ e $s = s(x)$ de forma que $x = \gamma(y,s)$ (que exite
pelo que o lema prova). Assim, obtemos o seguinte Teorema:

### Teorema da Existência Local 

A função $u(x) := z(y(x), s(x))$ é solução para a EDP 

$$
F(Du(x), u(x), x) = 0,
$$
em que $x \in V$ e $u(x) = g(x)$ para $x \in \partial U \cap V$, lembrando que
$\partial U$ é a fronteira de $U$. 

# Leis da Conservação 

Considere o problema da lei de conservação para a dimensão 1

$$
u_t + [f(u)]_x = 0, x \in \mathbb{R}, t > 0 \\
u(x,0) = \phi(x).
$$

Como nem sempre temos soluções diferenciáveis para $u$, temos que relaxar um
pouco nossa definição de solução, e para isso introduzimos as *soluções
fracas*. 

## Solução fraca (ou integral)

Lembre que um conjunto em $\mathbb{R}^n$ é *compacto* quando é fechado e
limitado. Uma função tem suporte compacto quando existe um compacto $\Lambda$
tal que para todo $x \in \mathbb{R}^n / \Lambda$ a função se anula. Definimos
uma solução fraca $u$ quando 

$$
\int_0^{+\infty}\int_{-\infty}^{+\infty} [uv_t + f(u)v_x] \, dx \, dt +
\int_{-\infty}^{+\infty} \phi(x) v(x,0) \, dx = 0,
$$

para todas as funções infinitamente diferenciáveis definidas em um conjunto
compacto $v$ (que chamamos de *função teste*). Assim, a suavidade é
transferida para a função $v$. De forma equivalente, 

$$
\int_0^{+\infty}\int_{-\infty}^{+\infty} v[u + f(u)_x] \, dx \, dt = 0,
$$

**Teorema:** Se $u$ é uma solução forte (no sentido de ser $k$ vezes
continuamente diferenciável), então $u$ será uma solução fraca. 

Como $v$ é um solução que é nula para um valor suficientemente grande e o
integrando é zero na solução, então a integral converge e, em particular, será
zero. Claro que precisamos primeiro mostrar a equivalência acima usando
Integral por partes. 

Agora suponha que $u$ é uma função não contínua em uma curva $x = \xi(t)$, mas
$u$ é suave em ambos os lados da curva (pensando em $\mathbb{R}^2$). Denotamos
$u^{+}(x,t)$ para o limite de $u$ quando se aproxima de $(x,t)$ pela direita e
$u^{-}(x,t)$ pela esquerda. Vamos mostrar que existe uma relação entre
$\xi(t)$, $u^{-}$, e $u^+$.

**Teorema:** Se $u$ é uma solução fraca com a descontinuidade mencionada
acima, então, 
$$
\frac{f(u^{-}) - f(u^{+})}{u^{-} - u^{+}} = \xi'(t)
$$
na curva de descontinuidade. Chamamos $\xi '(t)$ de *velocidade da curva de descontinuidade*. 
O denominador e o numerador são chamados de *saltos*. Essa condição é chamada
de **Condição de Salto Rankine-Hugoniot**. 

Nas imagens você confere um exemplo de quando $u$ não é contínua da Equação de
Berger. 

<img src="../example-2.png" alt="Exemplo de solução de EDP - Parte 2"
style="width:500px;height:600px;">
<img src="../example-3.png" alt="Exemplo de solução de EDP - Parte 3"
style="width:500px;height:600px;">
<img src="../example-4.png" alt="Exemplo de solução de EDP - Parte 4"
style="width:500px;height:600px;">