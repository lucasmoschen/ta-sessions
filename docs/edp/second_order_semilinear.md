# Equações Semilineares de Segunda Ordem 

Esse é uma breve introdução ao tópico para indicar o estudo. Para mais detalhes, o livro da professora Valéria Iório é sugerido. Temos que uma EDP semilinear de segunda ordem com duas variáveis é da forma 
$$
a(x,y) u_{xx} + 2b(x,y)u_{xy} + c(x,y)u_{yy} = f(x,y,u,u_x,u_y),
$$
cuja parte principal é o lado esquerdo da equação. Suponha que as funções $a,b,c$ sejam contínuas e defina a função **discriminante**:
$$
\delta(x,y) = b^2(x,y) - a(x,y)c(x,y).
$$

O ponto $(x,y) \in \Omega$ é dito 

1. Parabólico se $\delta(x,y) = 0$
2. Hiperbólica se $\delta(x,y) > 0$
3. Elíptica se $\delta(x,y) < 0$

Se a condição (1), (2) ou (3) vale para todo o ponto em $\Omega$, então a EDP é dita parabólica, hiperbólica ou elíptica, respectivamente. 

**Propriedade importante:** O tipo da EDP é invariante sob mudanças de variáveis se o Jacobiano da transformação for não nulo em uma vizinhança de cada ponto. 

## Curvas características 

Para EDPs de segunda ordem, as curvas características são curvas planas ao longo das quais a EDP pode ser escrita em uma forma que contenha as derivadas de $u_x$ e $u_y$. Suponha que $a$ não se anula na região de interesse. Caso se anule, considere $c$ ou $b$, pois uma delas não se anula na região de interesse, se não a EDP seria de primeira ordem. Reescreva o problema como 

$$
\begin{cases}
p = u_x \\ q = u_y \\ a(x,y)p_x + 2b(x,y)p_y + c(x,y)q_y = f(x,y,u,p,q).
\end{cases}
$$

Quando $u$ é de classe $C^2$ como é nosso caso, $p_y = q_x$. Assim, para qualquer função $\lambda(x,y) \neq 0$ temos que 
$$
ap_x + 2bp_y + \lambda p_y - \lambda q_x + cq_y = 0.
$$
Defina $P(x) = p(x,y(x))$ e $Q(x) = q(x,y(x))$ e teremos (sim, regra da cadeia de novo) que 
$$
a\frac{dP}{dx} - \lambda\frac{dQ}{dx} = 0,
$$
em que 
$$
\frac{dy}{dx} = \frac{2b + \lambda}{a} = -\frac{c}{\lambda}.
$$
Assim, a função $\lambda$ deve satisfazer 
$$
\lambda^2 + 2b\lambda + ac = 0
$$

Agora se $-c/\lambda = \mu$, então 
$$
\left(\frac{c}{\mu}\right)^2 - 2\frac{bc}{\mu} + ac =0 \overset{\times \mu^2/c}{\implies} a\mu^2 - 2b\mu + c = 0,
$$
isto é, se $dy/dx = \mu(x,y)$, então $a\mu^2 - 2b\mu + c = 0$. Portanto, o sinal do discriminante $\delta = b^2 - ac$ introduzido acima determina se existem uma, duas, ou nenhuma solução $\mu$. 

- No caso parabólico, existe uma família de funções que satisfaz essa equação para $\mu$.
- No caso hiperbólico, duas famílias satisfazem. 
- No caso elíptico, não existem soluções para $\mu$. 

As curvas definidas por 
$$
\frac{dy}{dx} = \mu(x,y)
$$
são as **curvas características** da EDP.

**Exemplo:** Vamos encontrar as curvas características da equação da onda (que é hiperbólica)
$$
u_{tt} = c^2u_{xx}.
$$

Nesse caso $a, b, c$ são constantes com $a = 1, b = 0$ e $c = -c^2$. Assim, 
$$
\mu^2 -c^2 = 0 \implies \mu = \pm c.
$$
Obtemos que 
$$
\frac{dx}{dt} = \pm c \implies x = \pm ct + x_0.
$$
Logo as curvas são as famílias de retas $x + ct = k_1$ e $x - ct = k_2$, para $k_1, k_2$ constantes. 

A ideia para resolver esses problemas é, portanto, fazer a mudança de variáveis 
$$
\begin{cases}
    \xi = x + ct \\
    \eta = x - ct. 
\end{cases}
$$
e introduzir a função $v(\xi,\eta) = u(x(\xi,\eta),t(\xi,\eta))$. 
Outra forma de resolver a equação da onda é introduzida [aqui](https://lucasmoschen.github.io/ta-sessions/edp/wave_equation/).


