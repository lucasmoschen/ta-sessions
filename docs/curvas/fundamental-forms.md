# Formas fundamentais 

## Primeira forma fundamental 

A primeira preocupação que podemos ter em uma superfície é medir a distância
entre dois pontos (o ser humano sempre fez isso de diversas formas no planeta
terra). Para isso, introduzimos o conceito da *primeira forma fundamental*. 

**Definição:** Seja $p$ um ponto na superfície de $S$. A primeira forma
fundamental de $S$ em $p$ associa $v, w \in T_pS$ ao escalar 
$$
\langle v, w \rangle_{p,S} = v \cdot w
$$
Seja $v \in T_pS$. Então, podemos representar $w$ como uma combinação linear
dos vetores $\sigma_u$ e $\sigma_v$: $w = \lambda \sigma_u + \mu \sigma_v$.
Assim
$$
\langle w, w \rangle = \lambda^2\langle \sigma_u, \sigma_u \rangle +
2\lambda\mu\langle \sigma_u, \sigma_v \rangle + \mu^2\langle \sigma_v,
\sigma_v \rangle
$$
Definimos $E = ||\sigma_u||^2, F = \sigma_u \cdot \sigma_v, G =
||\sigma_v||^2$ e assim, exprimimos a forma fundamental como 
$$
Edu^2 + 2Fdudv + Gdv^2
$$
em que $du = \lambda$ e $dv = \mu$. 

Se $\gamma(t) = \sigma(u(t), v(t))$, podemos calcular o comprimento de arco
utilizando que $\dot{\gamma} = \dot{u}\sigma_u + \dot{v}\sigma_v$ e, então, 
$$
||\dot{\gamma}||^2 = E\dot{u}^2 + 2F\dot{u}\dot{v} + G\dot{v}^2
$$
Portanto 
$$
L(\gamma) = \int (E\dot{u}^2 + 2F\dot{u}\dot{v} + G\dot{v}^2)^{1/2} dt
$$

### Isometrias em superfícies 

Se $\mathcal{S}_1$ e $\mathcal{S}_2$ são superfícies, dizemos que eles são
*localmente isométricos* se qualquer curva de $\mathcal{S}_1$ pode ser levada
por um mapa suave para uma curva em $\mathcal{S}_2$ de mesmo comprimento, isto
é, toda curva pode ser levada de uma superfície para outra, mantendo
comprimento. O mapa que realiza essa função é uma *isometria local*. 

Seja o mapa $D_pf : T_p\mathcal{S}_1 \to T_{f(p)}\mathcal{S}_2$ a derivada da
função suave $f$ entre as superfícies. Podemos provar que $f$ será uma
isometria local se, e somente se, $D_p\mathcal{S}_1$ é uma isometria (isto é,
preserva distâncias) para todo ponto $p \in \mathcal{S}_1$. Lembrando que por
isometria, queremos dizer que 
$$
\langle v, v \rangle_p = \langle D_p f(v), D_p f(v) \rangle_{f(p)}.
$$
Se $f$ for uma isometria local, ele será um difeomorfismo local dada a
invertibilidade de sua derivada $D_pf$. 

Um corolário interessante é que para todo mapa $\sigma_1$ de $\mathcal{S}_1$,
os patches $\sigma_1$ de $\mathcal{S}_1$, e $f \circ \sigma_1$ de
$\mathcal{S}_2$ tem a mesma forma fundamental. 

## Segunda forma fundamental

Seja $p=\sigma(u,v)$ um ponto em uma superfície. A medida que nos afastamos de
$(u,v)$, a superfície se distancia do plano tangente segundo a distância
(aproximada) 
$$
(\sigma(u + \Delta u, v + \Delta v) - \sigma(u,v))\cdot N.
$$
Pelo teorema de Taylor, essa distância vale 
$$
(\sigma_u\Delta u + \sigma_v\Delta v + \frac{1}{2}(\sigma_{uu}(\Delta u)^2 +
2\sigma_{uv}\Delta u\Delta v + \sigma_{vv}(\Delta v)^2) + R(\Delta u, \Delta
v))\cdot N
$$
onde esse esse resto sobre $(\Delta u)^2 + (\Delta v)^2$ tende a 0. Como $N$ é
perpendicular a $\sigma_u, \sigma_v$, o resto da expressão é escrita como 
$$
\frac{1}{2}(e(\Delta u)^2 + 2f\Delta u\Delta v + g(\Delta v)^2) + R(\Delta u,
\Delta v),
$$
em que 
$$
e = \sigma_{uu}\cdot N, f = \sigma_{uv}\cdot N, f = \sigma_{vv}\cdot N.
$$
A expressão acima é a *segunda forma fundamental* e está associada ao
curvamento da superfície em relação ao plano tangente. 

## Mapa de Gauss e de Weingarten 

**Mapa de Gauss:** O mapa $\mathcal{G} : \mathcal{S} \to \mathcal{S}^2$ que
associa cada ponto da superfície $p \in \mathcal{S}$, o ponto $N_p \in
\mathcal{S}^2$ que é o vetor normal unitário de $\mathcal{S}$ em $p$. 

Medimos a variação de $N$ ao longo de $\mathcal{S}$ pela derivada 
$$
D_p \mathcal{G} : T_p\mathcal{S} \to T_{\mathcal{G}(p)}\mathcal{S}^2.
$$
Seja $q = \mathcal{G}(p)$. O plano tangente a esse ponto é perpendicular a $q$
e passa pela origem. Observe, no entanto, que esse plano, é perpendicular a
$N_p$, que é exatamente $T_p\mathcal{S}$. Portanto esse mapa pode ser escrito
como 
$$
D_p \mathcal{G} : T_p\mathcal{S} \to  T_p\mathcal{S}.
$$

**Mapa de Weingarten:** O *mapa de Weingarten* da superfície $\mathcal{S}$ no
ponto $p$ é definida como $\mathcal{W}_{p,S} = - D_p\mathcal{S}$. A segunda
forma fundamental pode ser equivalentemente escrita como 
$$
\langle \langle v, w \rangle \rangle_{p,S} := \langle \mathcal{W}_{p,S}(v), w
\rangle_{p,S}, v, w \in T_p\mathcal{S}. 
$$

Podemos provar essa relação, além de provar que o mapa de Weingarten é
[autoadjunto](https://en.wikipedia.org/wiki/Self-adjoint_operator\#Bounded_self-adjoint_operators).

**Curvatura normal e geodésica:** Seja uma curva $\gamma$ na superfície
$\mathcal{S}$. A segunda derivada de $\gamma$ (relacionada com sua curvatura)
pode ser escrita como combinação linear 
$$
\ddot{\gamma} = \kappa_n N + \kappa_g(N\times\dot{\gamma}).
$$
Chamamos $\kappa_n$ de curvatura normal e $\kappa_g$ de geodésica. Em geral só
a magnitude desses valores é bem definida. Além disso 
$$
\kappa_n = L\dot{u}^2 + 2M\dot{u}\dot{v} + N\dot{v}^2
$$
