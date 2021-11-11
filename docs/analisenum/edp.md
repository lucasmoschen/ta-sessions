# Métodos numéricos para EDPs

Nessa seção, desenvolveremos métodos de aproximação numérica para Equações Diferenciais
Parciais. Para detalhes sobre os tipos de equações, consulte [esse link](https://lucasmoschen.github.io/ta-sessions/edp/second_order_semilinear/).

## Equações Parabólicas

A primeira equação é a do calor ou difusão, dada por 
$$\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2},$$ 
com condições 
$$u(x,0) = f(x), u(0,t) = a(t), \text{ e } u(1,t) = b(t).$$

## Equações Elípticas 

Considere a equação de Poisson 
$$\nabla^2 u(x,y) := u_{xx}(x,y) + u_{yy}(x,y) = f(x,y)$$
definida em um conjunto $U$ tal que $u(x,y) = g(x,y)$ em $(x,y)$ na fronteira
de $U$. Em geral, tomamos $U = \{(x,y) \mid a < x < b, c < y < d\}$.

O método consiste na aplicação do método das Diferenças Finitas em um grid de
duas dimensões. Seja $h = (b-a)/n$ e $k = (d-c)/m$ o tamanho do passo, em que 
$n$ e $m$ indicam a quantidade deles em cada direção. 

<img src="https://sites.me.ucsb.edu/~moehlis/APC591/tutorials/tutorial5/img31.png",
alt = "grid de pontos.">

> Métodos de diferenças finitas 
> Forward, backward e central difference. 
> Equação de difusão.