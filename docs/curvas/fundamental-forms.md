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

