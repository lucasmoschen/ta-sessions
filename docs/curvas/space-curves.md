# Curvas no espaço

Vimos que as curvas no plano são essencialmente definidas por sua curvatura. Porém, isso não é verdade no espaço. Considere, por exemplo, a hélice circular 
$$
\alpha(t) = \left(\frac{1}{2}\cos(t), \frac{1}{2}\sin(t), \frac{1}{2}t\right)
$$
Ela está parametrizada pelo comprimento de arco. Então, se formos calcular a curvatura (usando a mesma noção de curvas planas), teremos que 
$$
\kappa_{\alpha}(t) = ||\alpha''(t)|| = 1
$$
Entretanto, a hélice não é uma circunferência de raio 1! Para isso, vamos precisar introduzir o conceito de **torção**. Veja também que não é possível definir uma função ângulo! Então, **curvatura com sinal** é um conceito vago no espaço. Assim, para lembrar, definimos curvatura para uma curva parametrizada pelo comprimento de arco no espaço como 

$$
\kappa_{\alpha}(t) = ||\alpha''(t)||
$$

Se a curva $\alpha$ é regular qualquer, seja $\beta = \alpha \circ h$ uma reparametrização pelo comprimento de arco. Definimos a curvatura de $\alpha$ como 
$$
\kappa_{\alpha}(t) = \kappa_{\beta}(h^{-1}(t))
$$
Em particular, teremos que 
$$
\kappa_{\alpha}(t) = \frac{||\alpha'(t) \times \alpha''(t)||}{||\alpha'(t)||^3}
$$

Dizemos que uma curva $\alpha$ é **2-regular** (ou regular de sgunda ordem) quando os vetores $\alpha'(t)$ e $\alpha''(t)$ são linearmente independentes para todo $t$. Se a curva for parametrizada pelo comprimento de arco, isso equivale a dizer que $\alpha'' \neq 0$ (verifique!). Se a curva for regular, isso é equivalente a provar que $\kappa_{\alpha}(t) > 0$ (verifique!). 

## Triedo de Frenet

Já vimos que não faz sentido rotacionar o vetor tangente. Por isso, definimos o vetor **normal principal** de uma curva $\alpha$ parametrizada pelo comprimento de arco como 
$$
N(s) = \frac{1}{\kappa_{\alpha}(s)}(\dot{T}(s))
$$
onde $T(s) = \alpha'(s)$. Veja que ambos os vetores são unitários e ortogonais (quando a curva é parametrizada pelo comprimento de arco, a primeira e segunda derivadas são ortogonais). Definimos, então o vetor **binormal** como 
$$
B(s) = T(s) \times N(s)
$$
De fato $B$ é ortogonal a $T$ e a $N$ e, além disso, 
$$
||B(s)|| = ||T(s)||||N(s)|| - 2\langle T(s), N(s) \rangle = 1
$$

Definimos, portanto, uma base ortonormal $\{T(s), N(s), B(s)\}$ para $\mathbb{R}^3$. 

## Torção

Observe que 
$$
\dot{B}(s) = \dot{T}(s) \times N(s) + T(s) \times \dot{N}(s)
$$

Como $\dot{T}(s) \parallel N(s)$m, então 

$$
\dot{B}(s) = T(s) \times \dot{N}(s)
$$

Como $B(s)$ é um vetor unitário, $B(s) \perp \dot{B}(s)$ (veja que isso acontece com qualquer função vetorial unitária). Além disso $\dot{B}(s) \perp T(s)$ pela equação acima. Pelo Triedro de Frenet, 

$$
\dot{B}(s) \perp N(s) \implies \dot{B}(s) = \tau(s)N(s)
$$

chamamos $\tau$ de torção. Alguns livros, $\tau$ tem o sinal oposto (mas isso é só questão de convenção e não trás problemas teóricos. Mais uma vez, se a curva $\alpha$ é uma curva regular, tomamos uma reparametrização pelo comprimento de arco $\beta = \alpha \circ h$ e 

$$
\tau_{\alpha}(s) = \tau_{\beta}(h^{-1}(s))
$$
Em especial 
$$
\tau = \frac{\langle \dot{\alpha} \times \ddot{\alpha}, \dddot{\alpha} \rangle}{||\dot{\alpha}\times\ddot{\alpha}||^2}
$$


## Equações de Frenet

Já sabemos que $\dot{T}(s) = \kappa_{\alpha}(s)N(s)$ e $\dot{B}(s) = \tau_{\alpha}(s)N(s)$. Agora, vamos calcular $\dot{N}(s)$. Sabemos que 

$$
B = T \times N \implies N = B \times T \implies \dot{N}(s) = \dot{B}(s) \times T(s) + B(s) \times \dot{T}(s)
$$

Portanto, 
$$
\dot{N}(s) = \tau_{\alpha} N(s) \times T(s) + \kappa_{\alpha} B(s) \times N(s) = -\tau_{\alpha} B(s) - \kappa_{\alpha} T(s)
$$

Chegamos então que, se $\alpha$ é uma curva parametrizada pelo comprimento de arco regular de ordem 2, então

$
\dot{T} = \kappa N
$

$
\dot{N} = - \kappa T - \tau B
$

$
\dot{B} = \tau N
$

Observe que se $x(s) = (T(s), N(s), B(s)) \in \mathbb{R}^9, \dot{x}(s) = Ax(s)$, onde 

$$
A = \begin{bmatrix}
0_{3\times 3}         & \kappa I_{3\times 3} & 0_{3\times 3}       \\
-\kappa I_{3\times 3} & 0_{3\times 3}        & -\tau I_{3\times 3} \\
0_{3\times 3}         & \tau I_{3\times 3}   & 0_{3\times 3}
\end{bmatrix}
$$

Para curvas regulares quaisquer, a definição se dá usando a inversa do comprimento de arco, como fizemos com a curvatura e a torção. 

## Planos 

**Plano Osculador:** Determinado pelos vetores tangente e normal. O vetor binormal é normal ao plano osculador e, portanto, podemos escrever sua equação como $(x - \alpha(s))\cdot B(s) = 0$. 

**Plano Normal:** Plano determinado pelos vetores normal e binormal. 

**Plano Retificante:** Plano determinando pelos vetores tangente e normal. 

Alguns simples desenhos podem ser vistos [nesse site](http://mathonline.wikidot.com/normal-rectifying-and-osculating-planes). 

## Consequências 

### Curva plana e torção nula

(p. 32 Ronaldo)

### Circunferência e curvatura constante 

(p. 59 Pressley)

## Teorema Fundamental da Teoria Local das Curvas Espaciais

(p. 60 Pressley)

Querem demonstração no site?
