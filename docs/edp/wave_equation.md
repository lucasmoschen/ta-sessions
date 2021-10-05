# Equação da Onda 

Estamos interessados em entender o comportamento da EDP 

$$u_{tt} - c^2u_{xx} = 0,$$

sujeita a condições iniciais e de fronteira. 

## Interpretação física 

Em uma dimensão (mais outra temporal), a equação da onda é um modelo simpleficado de uma corda vibrando e 
$u(x,t)$ representa o deslocamento de um ponto $x$ no tempo $t \ge 0$. Suponha que a massa da 
corda seja $\rho = \rho(x)$ e a elasticidade seja $k = k(x)$. Considere o pedaço da corda $[x, x + \Delta x]$. 
Então, a massa desse pedaço será $\rho(x) \Delta x$, sua velocidade é dada por $u_t(x,t)$ (a derivada do deslocamento 
com respeito ao tempo) e a sua energia cinética é $\Delta K = \rho (u_t)^2 \Delta x / 2$ (lembre que energia cinética 
é proporcional à massa e ao quadrado da velocidade). 

Portanto, a enegia cinética total será 
$$
K(t) = \frac{1}{2} \int_0^L \rho(x) (u_t(x,t))^2 \, dx.
$$
Pela [Lei de Hooke](https://en.wikipedia.org/wiki/Hooke%27s_law), a energia potencial da corda é $(k/2)y^2$ em que $y$ é o aumento da corda dado pelo comprimento de $u(x,t)$ na variável $x$. Esse [comprimento pode ser medido](https://en.wikipedia.org/wiki/Arc_length#Finding_arc_lengths_by_integrating) usando 
$$
\sqrt{1 + u_x^2}
$$
e, portanto, a energia potencial é 
$$
P(t) = \frac{1}{2}\int_0^L k(x)(1 + (u_x(x,t))^2) \, dx.
$$
A [ação da função](https://lucasmoschen.github.io/ta-sessions/edp/calculus_of_variations/#o-calculo-das-variacoes) $u$ é, portanto, 
$$
I(u) = \int_0^T K(t) - P(t) \, dt = \frac{1}{2} \int_0^T\int_0^L \rho(u_t)^2 - k(1 + u_x^2) \, dx \, dt.
$$

Se $u$ minimiza essa ação, pelo Teorema de Euler-Lagrange, derivando com respeito a $u_t$ e $u_x$, 
$$
-2\rho u_{tt} - 2(k_xu_x + ku_{xx})  = 0,
$$
que implica $\rho u_{tt} = -ku_{xx} - k_xu_x$, isto é, se a elasticidade for constante na corda, temos a equação da onda.

Note que a nossa construção supõe a velocidade inicial conhecida. Portanto, além da condição de fronteira usal, precisamos de uma condição adicional (o que era de se esperar, pois nas EDOs, esse comportamento também acontecia).

## Fórmula d'Alembert 

Considere o problema 
$$
\begin{cases}
    u_{tt} - u_{xx} = 0, \\
    u(x,0) = g(x), u_t(x,0) = h(x),
\end{cases}
$$
em que $g$ e $h$ são dadas. Note que 
$$
u_{tt} - u_{xx} = u_{tt} + u_{tx} - u_{xt} - u_{xx} = \left(\frac{\partial}{\partial t} + \frac{\partial}{\partial x}\right)(u_t - u_x) = \left(\frac{\partial}{\partial t} + \frac{\partial}{\partial x}\right)\left(\frac{\partial}{\partial t} - \frac{\partial}{\partial x}\right)u.
$$
Apesar de ser uma notação de funcional que pode ser complicada, ela é muito útil para definir 
$$
v(x,t) = \left(\frac{\partial}{\partial t} - \frac{\partial}{\partial x}\right)u, 
$$
e, então, 
$$
v_t + v_x = 0, (x \in \mathbb{R}, t > 0),
$$
que é a equação do transporte. Sabemos que a solução para esse problema é 
$$
v(x,t) = a(x - t), 
$$
em que $a(x) := v(x,0)$, e, portanto 
$$
u_t(x,t) - u_x(x,t) = a(x,t), 
$$
que também o problema do transporte não homogêneo. Esse problema [tem solução conhecida](https://www.youtube.com/watch?v=1emgOSiNocE): 
$$
u(x,t) = \int_0^t a(x + (t-s) - s) \, ds + b(x+t) = \frac{1}{2}\int_{x-t}^{x+t} a(y) \, dy + b(x,t).
$$
Além disso, em $t=0$, temos que $b(x,0) = g(x)$ e $a(x) = h(x) - g'(x)$. Portanto, 
$$
u(x,t) = \frac{1}{2} \int_{x-t}^{x+t} h(y) - g'(y) \,dy + g(x+t), 
$$
que implica 
$$
u(x,t) = \frac{1}{2}[g(x+t) - g(x-t)] + \frac{1}{2}\int_{x-t}^{x+t} h(y) \, dy.
$$

Esta é a fórmula de d'Alembert. Note que na solução, assumimos que $u$ é suficientemente suave (classe $C^2$). Essa condição é verificada se $g \in C^2(\mathbb{R})$ e $h \in C^1(\mathbb{R})$. 

Dizemos, então, que a solução $u$ tem a forma 
$$
u(x,t) = F(x+t) - G(x-t)
$$

*Observação: Esse desenvolvimento assume que a corda é infinita.*

## Extensões

Esse é um tópico muito rico que pode ter muitas variações. Aqui apresentarei duas extensões que podem ser mais estudadas nas referêncais do curso. 

### Médias esféricas e fórmulas de Poisson e Kirchhoff

Para dimensões espaciais $n \ge 2$, a solução é um pouco mais complexa. Para isso, é preciso resolver a equação de [Euler-Poisson-Darboux](https://en.wikipedia.org/wiki/Euler%E2%80%93Poisson%E2%80%93Darboux_equation) e reduzir o problema ao formato que se possa aplicar a fórmula de d'Alembert. Para o detalhamento desse processo, o livro do professor Lawrence Evans é bastante indicado. 

### Corda finita 

Nesse caso, temos restrições de contorno quando $x=0$ e $x=l$ (comprimento da corda): 

$$
\begin{cases}
u_{tt} = c^2u_{xx} \\
u(0,t) = u(l,t) = 0, \forall t \ge 0, \\
u(x,0) = f(x), x \in [0,l] \\ 
u_t(x,0) = g(x), x \in [0,l].
\end{cases}
$$

Podemos provar o seguinte teorema: 

**Teorema:** Seja $f \in C^2[0,l]$ e $g \in C^1[0,l]$ tais que $f, f''$ e $g$ se anulam em $x=0$ e $x=l$, então 
$$
u(x,t) = \frac{F(x+ct) - F(x-ct)}{2} + \frac{1}{2c} \int_{x-ct}^{x+ct} G(s) \, ds,
$$
em que $F$ e $G$ são extensões periódicas (período $2l$) e ímpares das funções $f$ e $g$, respecticamente, é a única solução do problema de corda infinita. 

#### O que é extensão periódica e ímpar? 

Dizemos que uma função $f: A \to B$ tem período $T$ se para todo $x \in A$, temos que $x+ T \in A$ e $f(x) = f(x+ T)$. A função será ímpar se $f(x) = -f(-x)$ para $x \le -l$ Assim, definimos a extensão periódica ímpar de $f$ como 
$$
F(x) = \begin{cases}
    -f(-x + 2kl ) &x \in [(2k-1)l, 2kl] \\
    f(x - 2kl) &x \in [2kl, (2k+1)l],\\
\end{cases}
$$
que é definida em intervalor fechados.

## Métodos de energia 

Esses métodos nos ajudam a estudar a unicidade da solução $u$ do problema. Considere novamente o problema 
$$
\begin{cases}
    u_{tt} - u_{xx} = 0, \\
    u(x,0) = g(x), u_t(x,0) = h(x),
\end{cases}
$$
Suponha que $u$ e $v$ sejam soluções para esse problema. Então $w = u - v$ é uma solução para 
$$
\begin{cases}
    u_{tt} - u_{xx} = 0, \\
    u(x,0) =0, u_t(x,0) = 0.
\end{cases}
$$
Defina a energia 
$$
E(t) := \frac{1}{2}\int_U w_t^2(x,t) + w_x(x,t)^2 \, dx, 0 \le t \le T. 
$$
Derivando com respeito a $t$ e supondo $U$ limitado com fronteira suave, temos que (Fórmula de Leibniz)
$$
\dot{E}(t) = \int_U w_tw_{tt} + w_xw_{tx} \, dx = \int_U w_t(w_{tt} - w_{xx}) = 0,
$$
em que a segunda igualdade vem de uma integração por partes combinada com o fato de na fronteira $w = 0$. Portanto $E(t) = E(0)$ para todo $T \ge t \ge 0$, que implica $E(t) = 0$. Em paricular, 
$$
w_t(x,t) = w_x(x,t) = 0, \forall x, t
$$
e, portanto $w \equiv 0$. 

## Sugestões 

- [CFL (1928)](https://web.stanford.edu/class/cme324/classics/courant-friedrichs-lewy.pdf)
- [Discretização da equação da onda](https://www.mtnmath.com/whatrh/node66.html)