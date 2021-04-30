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

## Segunda forma fundamental