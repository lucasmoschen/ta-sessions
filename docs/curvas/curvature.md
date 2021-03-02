# Curvatura de uma curva

## Curvatura 

Seja $\gamma$ uma curva parametrizada pelo comprimeto de arco. Definimos **curvatura** como a função $\kappa(t) = ||\ddot{\gamma}(t)||$. Essa definição é consistente com o que esperávamos de uma reta (curvatura nula) e de um círculo (curvatura constante positiva). Porém se $\gamma$ é uma curva regular qualquer, podemos definir a sua curvatura como sendo a curvatura de sua reparametrização pelo comprimento de arco. Isto é, seja $\hat{\gamma}$ uma reparametrização pelo comprimento de arco de $\gamma$ com curvatura $\kappa$. Então a curvatura de $\gamma$ será $\kappa$. 

Uma questão que se levanta é: e se houver outra reparametrização de $\gamma$? Para isso, precisamos mostrar que a curvatura é invariante (não muda) segundo a reparametrização. Isso não é dificíl de ver pois as tangentes das reparametrização tem mesmo tamanho e, possivelmente, diferente sinal.

### Curvatura de uma curva regular

Seja $\gamma(t)$ uma curva em $\mathbb{R}^3$, então sua curvatura é dada pela expressão

$$
\kappa = \frac{||\ddot{\gamma} \times \dot{\gamma}||}{||\dot{\gamma}||^3}
$$

Observe que para curvas no plano essa expressão pode também ser utilizada, 
$$
\kappa = \frac{|\ddot{\gamma}_1\dot{\gamma}_2 - \ddot{\gamma}_2\dot{\gamma}_1|}{||\dot{\gamma}||^3}
$$

### Curvatura com sinal 

Definimos a **normal unitária com sinal** o vetor unitário que rotaciona o vetor tangente no sentido anti-horário em $\pi/2$. Em particular, $\ddot{\gamma}$ e $\dot{\gamma}$ são perpendiculares (pois a curva é parametrizada pelo comprimento de arco) e, portanto, 
$$
\ddot{\gamma} = \kappa_s \dot{\gamma}
$$
Chamamos $\kappa_s$ de **curvatura com sinal**. Em particular, $\kappa = |\kappa_s|$.

### Função Ângulo 

Dada uma curva diferenciável $\gamma:I\to \mathcal{S}^1$
