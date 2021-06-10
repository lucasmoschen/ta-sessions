# Curvaturas de Superfícies

## Curvaturas Gaussiana e média

**Definição:** Seja $\mathcal{W}$ o mapa de Weingarten de uma superfície
orientada $\mathcal{S}$ e $p \in \mathcal{S}$. A curvatura Gaussiana $K$ e a
curvatura média $H$ de $\mathcal{S}$ em $p$ são 
$$
K = \det(\mathcal{W}), \; \; H = \frac{1}{2}\operatorname{traço}(\mathcal{W}).
$$
Defina, considerando a primeira e segunda formas fundamentais, 
$$
\mathcal{F}_I = \begin{pmatrix}
    E & F \\ F & G   
\end{pmatrix}, \; \; \mathcal{F}_{II} = \begin{pmatrix}
    e & f \\ f & g   
\end{pmatrix}.  
$$

**Proposição:** Seja $\sigma$ uma parametrização da superfície orientada
$\mathcal{S}$. Então a matriz do mapa de Weingarten com respeito a base
$\{\sigma_u, \sigma_v\}$ de $T_pS$ é $\mathcal{F}_I^{-1}\mathcal{F}_{II}$. 

**Corolário:** 
$$
H = \frac{eG - 2fF + gE}{2(EF - F^2)}, \; \; K = \frac{eg - f^2}{EG - F^2}
$$

## Curvaturas principais

Seja $p \in \mathcal{S}$. Existem $\kappa_1, \kappa_2$ e uma base $\{u,
v\}$ do plano tangente $T_p\mathcal{S}$ tal que 
$$
\mathcal{W}(u) = \kappa_1u, \; \; \mathcal{W}(v) = \kappa_2v, 
$$
em outras palavras, o mapa de Weingarten possui autovalores e autovetores. As
*curvaturas principais* de $\mathcal{S}$ são os autovalores do mapa, e $u, v$
são os *vetores principais* correspondentes. 

**Pontos umbílicos (ou umbilicais):** Pontos em que $\kappa_1 = \kappa_2$. Em
particular, $p$ é umbílico se, e somente se, o mapa de Weinngarten é um mapa
identidade multiplicado por um escalar. N

**Proposição:** As curvaturas principais em um ponto da superfície são os
valores máximo e mínimo da curvatura normal de todas as curvas da superfície
que passam pelo ponto. 

A demonstração dessa proposição utiliza o Teorema de Euler que afirma que 
$$
\kappa_n = \kappa_1 \cos^2(\theta) + \kappa_2 \sin^2(\theta),
$$
onde $\theta$ é o ângulo orientado $\hat{u\dot{\gamma}}$.

**Proposição:** Seja $\mathcal{S}$ uma superfície conectada em que todo ponto
é umbílico. Então $\mathcal{S}$ é um conjunto aberto da esfera ou do plano. 