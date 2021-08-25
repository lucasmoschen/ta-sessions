# O Método das Características

Considere a Equação Diferencial Parcial (EDP) 
$$
F\left(x_1, \dots, x_n, u, \frac{\partial u}{\partial x_1}, \dots, \frac{\partial
u}{\partial x_n}\right) = F(x, u, \nabla u) = F(x, u, Du) = 0,
$$
definida em um conjunto $U$. Além disso, suponha que $u = g$ na fronteira
de $U$, em que $g$ é dada função suave. 

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
\sum_{j=1}^n F_{p_j} (Du, u, x)u_{x_j x_i} + F_z(Du, u, x)u_{x_i} +
F_{x_i}(Du, u, x) = 0.
$$