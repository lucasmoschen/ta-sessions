# Métodos numéricos para EDPs

Nessa seção, desenvolveremos métodos de aproximação numérica para Equações Diferenciais
Parciais. Para detalhes sobre os tipos de equações, consulte [esse link](https://lucasmoschen.github.io/ta-sessions/edp/second_order_semilinear/).

## Equações Parabólicas

A primeira equação é a do calor ou difusão, dada por 
$$\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2},$$ 
com condições 
$$u(x,0) = f(x), u(0,t) = a(t), \text{ e } u(1,t) = b(t).$$

> Métodos de diferenças finitas 
> Forward, backward e central difference. 
> Equação de difusão.