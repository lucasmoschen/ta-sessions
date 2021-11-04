# Teoria de Fourier

Essa seção é apenas um pequeno resumo sobre o assunto de Fourier, que é uma
matéria bem densa e pode ficar matematicamente bem complicada. Para um
detalhamento mais acurado da teoria, o capítulo 2 do livro [Fourier Analysis and Partial 
Differential Equations](https://www.cambridge.org/core/books/fourier-analysis-and-partial-differential-equations/39312A08B4D4F25F65F39581D229285B)
dos autores Rafael Iorio e Valéria Iorio é uma boa referência. 

## Convoluções 

Dizemos que uma transformação $L$ é linear se $L(f + \lambda g) = L(f) +
\lambda L(g)$ para todas as funções $f,g$ em um espaço apropriado, como, por
exemplo, das contínuas e $\lambda \in \mathbb{R}$. Ela será invariante 
por translações quando $L(f(x-a)) = L(f(x) - a)$ para todo $x,a$ em
um espaço vetorial. Por exemplo, considere as funções $f: \mathbb{R} \to
\mathbb{R}$ que representam algum sinal, tipo o som. A figura abaixo 
mostra que uma transformação invariante por translação deve levar as 
curvas azul e vermelha no mesmo lugar.

![](fig1.png)

Toda transformação linear $L$ invariante por translação 
é dada por uma convolução 
$$L(f)(x) = (f * h)(x) := \int_{\mathbb{R}} f(u) h(x-u) \, du$$
em que $h = L\delta$ e $\delta$ é a [delta de Dirac](https://en.wikipedia.org/wiki/Dirac_delta_function), uma função 
generalizada estudada na Análise Funcional que é zero em todo
ponto diferente de zero e 
$$\int_{\mathbb{R}} \delta(x) \, dx = 1.$$ 
Essa propriedade advém do fato de que 
$$\int_{\mathbb{R}} f(x) \delta(x-u) \, du = f(x),$$
isto é, a convolução de $f$ por $\delta$ é exatamente $f$. 

Essa operação de convolução satisfaz as propriedades de 
comutatividade, associatividade, existência de elemento
identidade ($\delta$), além é claro dela ser fechada 
no espaço das funções por exemplo. É possível mostrar que
$$\frac{d(f * g)}{dx} = \frac{df}{dx} * g = f * \frac{dg}{dx},$$
o que permite dizer que a convolução de funções diferenciáveis 
é diferenciável. Podemos, portanto, definir um [grupo](https://en.wikipedia.org/wiki/Group_(mathematics)) em que
o espaço é das funções deriváveis e a operação é a convolução. 

Defina $L_h(f) = f * h$, isto é, $L_h$ é uma transformação
que faz a convolução de $f$ por $h$. [Nesse vídeo](https://www.youtube.com/watch?v=QmcoPYUfbJ8) 
temos uma intuição com a quantidade de fumaça $S(t)$ e 
a quantidade de fósforos $f(t)$ no tempo $t$. 

## Transformada de Fourier 

A função $e_w(x) = e^{2\pi w x i}$ é um autovetor do operador 
$L_h$ no espaço das funções para qualquer $h$ (sim, qualquer!).
Essa proposição é um bom exercício. Como dica, observe que o seu 
autovetor correspondente será 
$$\hat{h}(w) = \int_{\mathbb{R}} h(u) e^{-2\pi w u i} \, du$$
Chamamos essa função de **função de transferência**. (Note que 
muitos dos nomes aqui vem da teoria dos sinais). Temos então 
uma base formada pelos autovetores da transformação $L_h$. 
Considere uma função $f$ e decomponha na base formada por esses
autovetores. Assim:
$$f(x) = \int_{\mathbb{R}} \hat{f}(w)e_w(x) \, dw,$$
em que os coeficientes $\hat{f}(w)$ precisam ser determinados. A
extensão do somatório para integral pode ser levado apenas como intuição
até aqui. Assim, teremos que 
$$L_h(f) = \int_{\mathbb{R}} \hat{f}(w)L(e_w) \, dw = \int_{\mathbb{R}}
\hat{h}(w)\hat{f}(w)e_w \, dw.$$

No espaço de funções, definimos o produto interno da seguinte forma: 
$$\langle f, g \rangle = \int_{\mathbb{R}} f(x)\overline{g(x)} \, dx.$$ 

Lembre que os coeficientes de uma decomposição têm relação com o coeficiente
interno quando a base é ortogonal. Vamos ver que esse é o caso! E então,
teremos que 
$$\hat{f}(w) = \langle f, e_w \rangle = \int_{\mathbb{R}} f(u)e^{-2\pi w u i}
\, du.$$

Para ver que a base de funções é de fato ortogonal, precisamos do resultado
$\langle e_{w_1}, e_{w_2} \rangle = \delta(w_1 - w_2)$ que não vai ser
demonstrado aqui. 

Definimos a **Transformada de Fourier** de uma função $f(t)$ por 
$$\hat{f}(w) = \int_{\mathbb{R}} f(u)e^{-2\pi w u i} \, du, $$
sempre que essa integral é definida. Resumindo, a Transformada de Fourier é a
função que para cada $w$ determina o coeficiente correspondente ao autovetor
$e_w$ da operação de convolução. 

A **Inversa da Transformada de Fourier** é dada por 
$$f(x) = \int_{\mathbb{R}} \hat{f}(w) e^{2\pi w x i} \, dw :=
\check{f}(x).$$

Uma propriedade resultante interessante é que $\check{g}(w) =
\widehat{g(-w)}$. Em Teoria dos Sinais, $\hat{f}(w)$ mede o quanto uma frequência 
$w$ está presente no sinal $f(x)$. Isso acontece, porque o sinal $e_w(x) =
e^{2\pi w x i} = \cos(2\pi w x) + i\sin(2\pi w x)$ é o sinal "puro" da
frequência $w$ e $\hat{f}(w)$ é o peso correspondente.  Por isso, dizemos que
$f(x)$ está definida no domínio do tempo ou espaço enquanto $\hat{f}(w)$ está
no domínio da frequência. 

**Propriedades:** Valem as seguintes propriedades.

$$ \hat{\delta} = 1 \\ \widehat{f * h} = \hat{f}\cdot \hat{h} \\ 
g(x) = f(x-a) \implies \hat{g}(w) = \hat{f}(w)e^{-2\pi w a i}
\\
g(x) = f(ax) \implies \hat{g}(w) =a^{-1}\hat{f}(w/a) \\
g(x) = f'(x) \implies \hat{g}(w) = \widehat{(\delta')}\cdot \hat{f} = 2\pi w
\hat{f}(w) i \\
\int_{\mathbb{R}} |f(u)|^2 \, du = \int_{\mathbb{R}} |\hat{f}(w)|^2 \, dw$$

## Transformada de Fourier em Espaço Discreto 

Agora considere $f(x)$ com $x \in \mathbb{Z}$, por exemplo. Nesse caso, a
função de dirac tem a diferença de $\delta(0) = 1$, enquanto $0$ no resto 
dos inteiros. Vale também que 
$$\sum_{i=-\infty}^{+\infty} f(i)\delta(i) = f(0)$$
e
$$f(n) = \sum_{i=-\infty}^{+\infty} f(i)\delta(n-i).$$

A convolução discreta também tem uma definição similar 
$$Lf(n) = (f * h)(n) := \sum_{i=-\infty}^{+\infty} f(i)h(n-i).$$

As propriedades de convoluções contínuas, mas a derivada é 
substituída por $\Delta(f * g) = \Delta(f) * g = f * \Delta(g)$ para
$\Delta(f)(n) = f(n+1) - f(n)$. 

Os autovetores da convolução são da forma $e_w(n) = e^{2\pi w n i}$ com
autovalores 
$$\hat{h}(w) = \sum_{i=-\infty}^{+\infty} h(i)e^{-2\pi w a i}.$$

E, por fim, a transformada de Fourier de Tempo Discreto é 
$$\hat{f}(w) =  \sum_{i=-\infty}^{+\infty} f(i) e^{-2\pi w a i},$$
sempre que o somatório for válido. A inversa será
$$f(n) = \int_0^1 \hat{f}(w) e^{2\pi w n i}.$$

Note que $\hat{f}(w)$ é periódica com período 1. 

## Transformada de Fourier em Espaço Finito 

Agora os transformadores $L$ são do tipo $L:\mathbb{C}^N \to \mathbb{C}^N$ e
portanto possuem representação matricial. Em particular, vamos estar
interessados quando 
$$L(a_0, a_1, \dots a_{N-1}) = (b_0, \dots, b_{N-1}) \implies L(a_{N-1}, a_0,
\dots a_{N-2}) = (b_{N-1}, b_0, \dots, b_{N-2}),$$
que é semelhante à invariância por translação. Seja $\{\delta_0, \dots,
\delta_{N-1}\}$ a base canônica de $\mathbb{R}^N$, em que $(\delta_i)_i = 1$ e
$(\delta_i)_j = 0, j \neq i$. Nessa base, teremos que 
$$L = \begin{bmatrix} h_0 & h_{N-1} & \cdots & h_1 \\ 
 h_1 & h_{0} & \cdots & h_2 \\
 h_2 & h_{1} & \cdots & h_3 \\
 \vdots & \vdots & \ddots & \vdots \\
 h_{N-1} & h_{N-2} & \cdots & h_0 \\
\end{bmatrix},$$
em que $L\delta_0 = (h_0, h_1, h_2, \dots, h_N)$. Toda transformação dessa
maneira é dada por uma convolução circular
$$(Lf)_j = (f *_c h ) := \sum_{k=0}^j f_k h_{j-k} + \sum_{k=j+1}^{N-1} f_k
h_{N+j-k} = \sum_{k=0}^{N-1} f_k h_{j-k \mod N}$$
em que $h = L\delta_0$. 

O operador $L_h$ dado por $L_h f = f *_c h$. Essa matriz tem os autovalores e
autovetores conhecidos: se $\alpha$ é uma raiz $N$-ésima da unidade, então 
$e = (1, \alpha, \dots, \alpha^{N-1})$ é um autovetor de $L_h$ cujo autovalor
é dado por 
$$\lambda = \sum_{k=0}^{N-1} h_k e^{-\frac{2\pi k}{N} wi}.$$

Para obter uma base ortonormal, basta fazer $e_w = N^{-1/2}e$. A
**Transformada de Fourier Finita** de um vetor $f = (f_0, \dots, f_{N-1})$ é
dada por 
$$\hat{f}_w = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} f_k e^{-\frac{2\pi w}{N}
ki}.$$ 

Um comentário importante é que na literatura, essa transformação é chamada de 
**Transformada de Fourier Discreta (DFT)** e em alguns textos o coeficiente
$1/\sqrt{N}$ é substituído por $1/N$ ou $1$. A **Inversa** dessa transformação
é 
$$f = \sum_{w=0}^{N-1} \hat{f}_w e_w.$$

## Resolvendo uma EDP com Fourier 

Vamos lembrar que se $g(x) = f'(x)$ para uma função diferenciável $g$, então a
transformada de Fourier de $g$ é 
$$\hat{g}(w) = 2\pi w i \hat{f}(w).$$
Isso é "uma mão na roda", porque quando aplicamos a transformada na derivada
de uma função, estamos voltando para a transformada da própria função
multiplicada por uma função linear em $w$. Isso acontece quando a função é
definida na reta. Para funções definidas apenas em um intervalo, é importante 
observar [o seguinte trecho do site do Wikipedia](https://en.wikipedia.org/wiki/Fourier_transform#:~:text=More%20precisely%2C%20suppose%20T%20is%20large%20enough%20that%20the%20interval).
Nesse caso, é muito comum também encontrar a fórmula 
$$\hat{g}(w) = w i \hat{f}(w)$$
para funções definidas em $[-\pi, \pi]$. São algumas complicações
relacionadas à própria derivação do método. Vamos aplicar esse método na
equação de difusão 
$$\frac{\partial^2 u(x,t)}{\partial x^2} = c\frac{\partial u(x,t)}{\partial
t}.$$

O primeiro passo é aplicar a transformação de Fourier em ambos os lados da
equação. Na prática, o que se faz é multiplicar por $e^{-i w x}$ (ou $e^{-2\pi
i w x}$, mas lembre que é questão de parametrização) e integrar de $x = -\infty$ a
$x = +\infty$. Se a função for definida em $[-\pi, \pi]$, você integra nesse
intervalo, respectivamente. Nesse caso, observe que 
$$\widehat{u_{xx}}(w,t) = ik \widehat{u_x} = -w^2\hat{u}(w, t).$$
Com algumas hipóteses de regularidade, pela Regra de Leibniz,
$$\int_{-\infty}^{+\infty} u_t(x,t)e^{-i w x} \, dx =
\frac{d}{dt}\int_{-\infty}^{+\infty} u(x,t)e^{-i w x} \, dx$$
Dessa forma 
$$\widehat{u_t}(w,t) = \frac{\partial \hat{u}}{\partial t}(w,t).$$

Isso faz com que tenhamos o sistema 
$$-w^2\hat{u}(w,t) = c\hat{u}_t(w,t)$$
que é uma EDO com solução 
$$\hat{u}(w,t) = \hat{u}(w,0)e^{-w^2 t/c}.$$
Agora, basta aplicar a transformada inversa 
$$u(x,t) = \int_{-\infty}^{\infty} \hat{u}(w,t)e^{iw x} \, dw.$$

Você deve ter observado que nessa parametrização (sem o $2\pi$ no expoente),
eu deveria dividir cada integral por $2\pi$ para corretamente aplicar a
Transformada de Fourier. Acontece que elas vão se anular por esse motivo. Para
obter $\hat{u}(w,0)$ basta aplicar a transformada de Fourier em $u(x,0)$, que
é usualmente dado. 


## Adicionais 

- [Mas o que é a Transformada de Fourier? Uma introdução visual. 3B1B](https://www.youtube.com/watch?v=spUNpyF58BY)
- [Least deep and most incomplete explanation for Fourier Transform](http://dmorris.net/projects/tutorials/fourier_tutorial.pdf)
- [Implementando Fast Fourier Transform em Python](https://towardsdatascience.com/fast-fourier-transform-937926e591cb)