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

Definimos a **normal unitária com sinal** $n_s$ o vetor unitário que rotaciona o vetor tangente no sentido anti-horário em $\pi/2$. Em particular, $\ddot{\gamma}$ e $\dot{\gamma}$ são perpendiculares (pois a curva é parametrizada pelo comprimento de arco) e, portanto, é paralelo a $n_s$, assim
$$
\ddot{\gamma} = \kappa_s n_s
$$
Chamamos $\kappa_s$ de **curvatura com sinal**. Em particular, $\kappa = |\kappa_s|$.

### Função Ângulo 

Dada uma curva diferenciável $\gamma:I\to \mathcal{S}^1$, onde $\mathcal{S}^1$ é o círculo centrado na origem. Dizemos que $\theta : I \to \mathbb{R}$ é função ângulo de $\gamma$ quando 
$$
\gamma(s) = (\cos(\theta(s)), \sin(\theta(s)), \forall s \in I
$$

Observe que nessa definição, a imagem de $\gamma$ é um subconjunto de $\mathcal{S}^1$, como se fosse um arco. Por exemplo, 

$\gamma(s) = (\cos(2s), \sin(2s)) \implies \theta(s) = 2s$.

Considere o operador que rotaciona no sentido anti-horário em 90° um vetor. Podemos descrevê-lo em forma matricial como 

$$
J = \begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
$$

Defina o **determinante** entre dois vetores como 

$$
det(v,w) = \langle Jv , w \rangle
$$

que é o produto interno do vetor $v$ rotacionado e $w$.

#### Diferenciabilidade

Seja $\gamma : I \to \mathcal{S}^1$ uma curva diferenciável. Então $\gamma$ admite uma função ângulo $\theta$ diferenciável. Além disso, se $\theta '$ é função ângulo diferenciável de $\gamma$, ela difere de $\theta$ por uma constante. 

> Note que supondo a existência dessa função diferenciável, temos que, por aplicação da Regra da Cadeia, 
$$
\gamma '(s) = \theta '(s)(-\sin(\theta(s)), \cos(\theta(s))) = \theta '(s) J\gamma(s)
$$
Portanto, aplicando o produto interno em ambos os lados, observamos que 
$$
\theta '(s) = det(\gamma(s), \gamma '(s))
$$
Assim, a demonstração se dá defininido $\theta$ com essa derivada (Teorema Fundamental do Cálculo). 


Agora seja $\alpha$ uma curva regular, sem perda de generalidade, parametrizada pelo comprimento de arco. Seja $t(s) = \alpha '(s)$. Como $||t(s)|| = 1$, pela proposição anterior, existe uma função ângulo diferenciável $\theta$ de forma que definimos a curvatura de $\alpha$ como

$$
k(s) = \theta '(s) = det(t(s), t'(s)) = det(a'(s), a''(s))
$$

Observe que estamos rotacionando o vetor tangente, obtendo o que chamamos de vetor normal unitário e fazendo o produto interno com a aceleração da curva, o que coincide com a definição prévia! 

**Exemplo:** Considere a parametrização do círculo 
$$
\alpha(s) = p + r(\cos(s/r), \sin(s/r)), s \in \mathbb{R}
$$
Assim 
$$
\alpha'(s) = (-\sin(s/r), \cos(s/r))
$$

$$
\alpha''(s) = -\frac{1}{r}(\cos(s/r), \sin(s/r)) = \frac{1}{r}J\alpha '(s)
$$

$$
\kappa(s) = \langle J\alpha '(s), \alpha ''(s) \rangle = \frac{1}{r}
$$


## Movimento Rígido

**Isometria:** Uma aplicação $F: \mathbb{R}^n \to \mathbb{R}^n$ que preserva distância, isto é, $||x - y|| = ||F(x) - F(y)||, \forall x, y \in \mathbb{R}^n$. Diremos uma **movimento rígido** é uma isometria (a rigidez em mudar distâncias).

**Translação:** Uma aplicação $F: \mathbb{R}^n \to \mathbb{R}^n$  do tipo $v \mapsto F(v) := v + a$, para algum $a \in \mathbb{R}^n$ fixo. 

**Transformação Ortogonal:** Uma transformação **linear** que presetva o produto interno, isto é, $\langle u, v \rangle = \langle T(u), T(v) \rangle$. A matriz associada a essa transformação é ortogonal. 

Dizemos que o movimento é **direto** se $det(P) = 1$ e oposto ou inverso quando $det(P) = -1$. 

### Teorema 

Seja $P_{n\times n}$ uma matriz ortogonal e $a \in \mathbb{R}^n$. Então $F: \mathbb{R}^n \to \mathbb{R}^n$ definido como $F(v) = Pv + a$ é uma isometria. Reciprocamente, toda isometria pode ser escrito nessa forma.  Esse teorema permite uma caracterização simples de um movimento rígido.

### Invariância da curvatura

Sejam $\Phi = A + p_0$ um movimento rígido direto de $R^2$ e $\alpha : I \to \mathbb{R}^2$ uma curva regular parametrizada por comprimento de arco. Então, $\beta = \Phi \circ \alpha : I \to \mathbb{R}^2$ é uma curva regular de $\mathbb{R}^2$, parametrizada por comprimento de arco, cuja função curvatura coincide com a de $\alpha$, isto é, $\kappa_{\alpha}(s) = \kappa_{\beta}(s) \forall s \in I$.

> Observe que derivar $\beta ' = \Phi'(\alpha) = A\alpha '$ o que garante que $\beta$ é parametrizada pelo comprimento de arco e que $\beta '' = A\alpha ''$. Portanto, como $det(A) = 1$, vale que as curvaturas são as mesmas. 


## Equações de Frenet 

Página 21 (Ronaldo)


## Teorema Fundamental das Curvas no Plano

Páginas 39-40 (Pressley)
Páginas 22-23 (Ronaldo)
