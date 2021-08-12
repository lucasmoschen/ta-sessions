# Definições iniciais 

Uma *equação diferencial parcial* (EDP) ou *partial differential equation*
(PDE) é uma equação que envolve duas ou mais variáveis independentes e
derivadas parciais de uma função que depende dessas variáveis. De forma bem
geral, é uma equação com forma 
$$
F\left(x_1, \dots, x_n, u, \frac{\partial u}{\partial x_1}, \dots, \frac{\partial
u}{\partial x_n}, \dots, \frac{\partial^k u}{\partial x_{i_1} \dots \partial
x_{i_k}}, \dots, \frac{\partial^k u}{\partial x_n^k}\right) = 0,
$$
em que $u = u(x_1, ..., x_n)$ e na expressão aparece a $k$-ésima derivada de
$u$ com respeito a $k$ variáveis $x_{i_1}, \dots, x_{i_k}$. A função $u$ é em
geral desconhecida e assumidamente de classe $C^k$, isto é, $k$ vezes
continuamente diferenciável. 

Denotamos também, 
$$\nabla^2 u := \frac{\partial u}{\partial x_1^2} + \dots + \frac{\partial
u}{\partial x_n^2} = \Delta u,$$
o [operador de Laplace](https://en.wikipedia.org/wiki/Del#Laplacian).   

## Exemplos 

- [Equação da Onda](https://en.wikipedia.org/wiki/Wave_equation): 

$$
\Delta u = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2},
$$
em que $c$ mede a velocidade da propagação da onda. 

Nesse exemplo temos $n$ variáveis espaciais $x_1, \dots, x_n$ e uma variável
temporal $t$. Podemos definir 
$$
F\left(x_1, \dots, x_n, t, u, \frac{\partial^2 u}{\partial x_1^2}, \dots,
\frac{\partial^2 u}{\partial x_n^2}, \frac{\partial^2 u}{\partial t^2}\right) =
c^2\Delta u - u_{tt}
$$

- [Equação do calor](https://en.wikipedia.org/wiki/Heat_equation):

$$
\Delta u = \frac{1}{k}\frac{\partial u}{\partial t},
$$

- [Equação de Laplace](https://en.wikipedia.org/wiki/Laplace%27s_equation)

$$
\Delta u = 0 
$$

As soluções dessa equação são as [funções
harmônicas](https://en.wikipedia.org/wiki/Harmonic_function).

- [Equação de Schrödinger](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation)

$$
iu_t + \Delta u = 0
$$

é a função que governa a função de onda no sistema mecânico quântico. 

## Classificação de uma EDP

**Ordem:** Dada pela ordem parcial de maior ordem que ocorre na equação. Nos
exemplos anteriores, as equações tem ordem 2. 

**Linear:** Ela é dita linear se é de primeiro grau em $u$ e em todas suas
derivadas parciais. Caso contrário ela é dita **não linear**. 

Por exemplo, uma EDP linear de ordem 1 é dada pela expressão (veja as
diferentes expressões para [derivada parcial](https://en.wikipedia.org/wiki/Partial_derivative))
$$
\sum_{j=1}^n a_j(x) D_{x_j} u + b(x) u + c(x) = 0 
$$

**Homogênea:** Os termos das variáveis independentes são nulos, isto é, as
variáveis independentes não aparecem na expressão da função $F$. 

**Parte principal:** A parte da equação que contém as derivadas de maior
ordem. Se uma equação não linear possui parte principal linear, ela é dita
**semilinear**. 

### Exemplos 

- [Equação telegrafo](https://en.wikipedia.org/wiki/Telegrapher%27s_equations)

$$
u_{tt} + 2du_t - u_{xx} = 0, 
$$

é uma equação linear de ordem 2. 

- [Equação de beam](https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory)

$$
u_{tt} + u_{xxxx} = 0
$$

é uma equação linear de ordem 4

- Equação da onda (não linear)

$$
u_{tt} - \Delta u + f(u) = 0,
$$
em que $f$ é uma função não linear de $u$. Observe que a parte principal é
$u_{tt} - \Delta u$ que é linear e, portanto, a equação é semilinear. 

- Exemplo: Suponha que $u$ e $v$ são duas funções solução da equação
  (linear de ordem 1)
$$
\frac{\partial u}{\partial x} + xu = 0 
$$
Seja $z := \alpha u + \beta v$, em que $\alpha, \beta \in \mathbb{R}$.
Assim, 
$$
\frac{\partial z}{\partial x} + xz = \alpha\frac{\partial u}{\partial x} +
\beta\frac{\partial v}{\partial x} + \alpha x u + \beta x v =
\alpha\left(\frac{\partial u}{\partial x} + xu\right) +
\beta\left(\frac{\partial v}{\partial x} + xv\right) = 0,
$$
o que implica que $z$ também é solução. Essa propriedade não é exclusividade
do exemplo acima. Na verdade, vale para toda equação linear, isto é,
combinação linear de soluções é solução em problemas lineares.

## Princípio da Superposição

Considere uma EDP linear de ordem 2: 
$$
\sum_{i,j}^n a_{ij}(x)D_{x_i}D_{x_j} u(x) + \sum_{j=1}^n b_{j}(x)D_{x_j}u(x) +
c(x)u(x) + d(x) = 0.
$$
Podemos reescrever essa equação na forma 
$$
(Lu)(x) = \sum_{i,j}^n a_{ij}(x)D_{x_i}D_{x_j} u(x) + \sum_{j=1}^n b_{j}(x)D_{x_j}u(x) +
c(x)u(x)
$$
e $Lu = -d$. Dizemos que $L$ é um operador (no espaço de funções de classe
$C^k$ para o espaço de funções contínuas). no caso ele é linear de ordem 2.
Podemos generalizar para um de ordem $k$ qualquer.  

Seja $L$ um operador diferencial linear de ordem $k$ cujos coeficientes estão
definidos em $\mathbb{R}^n$. Suponha que $\{u_m\}_{m=1}^{+\infty}$ é um
conjunto de funções k vezes continuamente diferenciáveis satisfazendo 
$$
Lu = 0,
$$
e que $\{\alpha_m\}_{m=1}^{+\infty}$ é uma sequência tal que 
$$
u(x) = \sum_{m=1}^{+\infty} \alpha_m u_m(x)
$$
é convergente e $k$ vezes diferenciável termo a $t$. Então $u$ também é
solução. 

## Condições de Contorno e Iniciais 

Observe que para EDPs, estamos interessados em definir uma função em uma
região em um espaço de dimensão pelo menos 2. Por isso, não é mais suficiente
atribuir uma condição inicial ao problema, como se fazia aos problemas de EDO,
para determinar uma solução. Nesse caso, substituímos os extremos do intervalo
pelo fronteira do conjunto que queremos estudar. Nesse caso, o problema é dito
**problema de contorno**.

É comum fixar, por exemplo $u(x,0) = f(x)$ e $u(x,1) = g(x)$, em que a segunda
variável é o tempo. 
 