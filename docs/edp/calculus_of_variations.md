# Cálculo de Variações 

XXX: Importância 

## Equações características Hamilton-Jacobi 

A equação de Hamilton Jacobi é dada pela expressão 

$$
u_t + H(Du, x) = 0, 
$$

em que $H : \mathbb{R}^{2n} \to \mathbb{R}$ e $Du = (u_{x_1,}, \dots,
u_{x_n})$. Reescreva $p = Du$, $p_{n+1} = u_t$ e $q = (p,p_{n+1})$ (como se o tempo fosse a
dimensão $n+1$) e assim teremos $y = (x,t)$ nossa variável. Podemos reescrever
como o sistema 

$$
G(p, p_{n+1}, z, y) = p_{n+1} + H(p, x) = 0.
$$

Note que, em particular, $D_qG = (D_pG(p,x), 1)$ e $D_yG = (D_xH(p,x), 0)$ e
$D_zG = 0$. 

*Remark: Lembre que a notação $D_vG$ é o mesmo que dizer que você vai derivar
$G$ com respeito a cada componente de $v$. Se $v \in \mathbb{R}$, temos que
$D_vG = G'(v)$.*

Com isso, nós podemos montar as equações características (dadas pela curvas características
$\gamma(s)$ ), 

$$
\begin{cases}
    \dot{x}_1(s) = D_{p_1}G = H_{p_1}(p(s), \gamma(s)) \\
    \dot{x}_2(s) = D_{p_2}G = H_{p_2}(p(s), \gamma(s)) \\
    \dots \\
    \dot{x}_n(s) = D_{p_n}G = H_{p_n}(p(s), \gamma(s)) \\
    \dot{t}(s) = D_{p_{n+1}}G = 1 \implies t = s, \\
\end{cases}
$$

o que permite intercambiar os parâmetros $t$ e $s$. 

$$
\begin{cases}
    \dot{p}_1(t) = -D_{x_1}G - D_zG\cdot p_1 = -H_{x_1}(p(s), \gamma(s)) \\
    \dot{p}_2(t) = -D_{x_2}G - D_zG\cdot p_1  = -H_{x_2}(p(s), \gamma(s)) \\
    \dots \\
    \dot{p}_n(t) = -D_{x_n}G - D_zG\cdot p_1  = -H_{x_n}(p(s), \gamma(s)) \\
    \dot{p}_{n+1}(t) = -D_{t}G - D_zG\cdot p_1  = 0 \\
\end{cases}
$$

e, por fim 

$$
\begin{split}
    \dot{z} &= D_qG\cdot q = D_pH(p(t), \gamma(t))\cdot p(t) + p^{n+1}(t) \\
    &= D_pH(p(t), \gamma(t))\cdot p(t) - H(p(t), \gamma(s))
\end{split}
$$

Note portanto que podemos sumarizar essas equações em 

$$
\begin{cases}
    \dot{\gamma}(t) = D_pH(p(t),\gamma(t)) \\
    \dot{p}(t) = -D_{x}H(p(t), \gamma(t)) \\
    \dot{z}(t) = D_pH(p(t), \gamma(t)) - H(p(t), \gamma(t))
\end{cases}
$$

em que as primeiras duas equações são as **equações de Hamilton**.  A função
$H$ também é chamada de Hamiltoniano. 

## Aplicações 

XXX: TODO

## O cálculo das variações

Introduzimos o Lagrangiano 

$$
\begin{align*}
    L : \mathbb{R}^n \times \mathbb{R}^n &\to \mathbb{R} \\
    (v_1,\dots,v_n,x_1,\dots,x_n) &\mapsto L(v,x).
\end{align*}
$$

Além disso, definimos o funcional **ação** como 

$$
I[w(\cdot)] := \int_0^t L(\dot{w}(s), w(s))\, ds, 
$$

em que as funções $w$ são duas vezes continuamente diferenciáveis com $w(0) =
y$ e $w(t) = x$ fixados anteriormente. 

Um problema geral do cálculo das variações é encontrar uma função $x(\cdot)$
que minimiza $I[w(\cdot)]$ dentre todas as $w$. 

### Exemplo 

Qual a função $y = f(x)$ cuja curva (diferenciável) entre os pontos $(x_1, y_1)$ e $(x_2,
y_2)$ tem o comprimento. Dada uma função, sabemos que seu comprimento de arco
é 

$$
Comp[y] = \int_{x_1}^{x_2} \sqrt{1 + y'(x)^2} \, dx.
$$

Nesse caso, $L(f'(x), f(x)) = \sqrt{1 + f'(x)^2}$ e sabemos que sua solução é
o segmento de reta entre esses pontos. 

### Equações de Euler-Lagrange 

A solução ótima para o problema de cálculo das variações resolve o sistema de
equações Euler-Lagrange:

$$
-\frac{d}{ds}(D_v L(\dot{x}(s), x(s))) + D_xL(\dot{x}(s), x(s)) = 0, 0 \le s
\le t.
$$

Note que resolver as equações não nos dá as funções ótimas, da mesma forma que
derivada igual a zero não implica mínimo local. 

O interessante é que, dado uma Lagrangiano $L$, podemos introduzir o
**Hamiltoniano**

$$
H(p,x) := p\cdot v(p,x) - L(v(p,x), x),
$$

em que $v$ é definido como a função tal que $p = D_vL(v,x)$. 
Podemos demonstrar que a partir desse $H$, temos as equações de Hamilton, o
que permite uma conexão entre as duas teorias. 

### Aplicação ao exemplo

XXX: TODO 
