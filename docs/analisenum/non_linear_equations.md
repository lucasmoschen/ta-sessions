# Solução de equações não lineares 

Considere uma população com crescimento proporcional ao seu tamanho a cada
tempo $t$ sujeita a migrações constantes, isto, se $x(t)$ é o tamanho da
população no tempo $t$,

$$
\dot{x}(t) = \lambda x(t) + \nu \implies x(t) = x(0)e^{\lambda t } +
\frac{\nu}{\lambda}(e^{\lambda t} - 1)
$$

Se sabemos $x(t), x(0)$ e $\nu$, ainda não conseguimos resolver para $\lambda$
esse sistema. 

**Obsevação:** Muitas vezes, simplificações em sistemas de equações ou
equações podem ajudar a resolver o problema analiticamente, que é sempre mais
preciso. Nem sempre só jogar um sistema num solver vai resolver o problema. 

De forma geral, queremos resolver $f(x) = 0$ para $f : [a,b] \to \mathbb{R}$,
em geral, precisamos que $f(a)$ e $f(b)$ tenham sinais diferentes e $f$ seja
pelo menos contínua, para garantir existência de solução através do Teorema do
Valor Intermediário. 

## Método da Bisseção 

Esse é um método bem simples que se embasa totalmente no Teorema do Valor
Intermediário. Seja $x^*$ a solução do problema, isto é, $f(x^*) = 0$. Tome $a_1 = a, b_1 = b, x_1 = \frac{a_1 + b_1}{2}$. A partir de
$x_1$, verificamos o sinal de $f(x_1)$. Assim

- $f(x_1) = 0$: Nesse caso a solução é $x^* = x_1$. 
- $f(x_1) < 0$: Nesse caso, se $f(a) < 0$ e $f(b) > 0$, deve haver uma solução
  no intervalo $[x_1, b]$. Por isso, definimos $a_2 = x_1$ e $b_2 = b$ e
  seguimos o procedimento. Se $f(a) > 0$ e $f(b) < 0$, deve haver uma solução
  em $[a, x_1]$ e, portanto, $fa_2 = a, b_2 = x_1$ e seguimos o procedimento. 
- $f(x_1) > 0$: Nesse caso, se $f(a) > 0$ e $f(b) < 0$, deve haver  uma solução
  no intervalo $[x_1, b]$. Por isso, definimos $a_2 = x_1$ e $b_2 = b$ e
  seguimos o procedimento. Se $f(a) < 0$ e $f(b) > 0$, deve haver uma solução
  em $[a, x_1]$ e, portanto, $fa_2 = a, b_2 = x_1$ e seguimos o procedimento. 

Assim, esse processo se resume a tomar o ponto médio do intervalo e ir
cortando pela metade o intervalo a cada iteração. Precisamos de um critério de
parada melhor do que $f(x_k) = 0$, pois estamos num âmbito contínuo. Como
cortamos o intervalo pela metade a cada iteração, é fácil ver que 

$$
|x_n - x^*| \le \frac{b-a}{2^n}, \forall n \ge 1.
$$

Nesse caso, uma condição de parada possível é $(b-a) \le 2^n \epsilon$, em que
$\epsilon$ é a minha tolerância a erro. 

Alguns comentários importantes: calcular 

$$
x_n = a_n + \frac{b_n - a_n}{2}
$$

é melhor numericamente do que $x_n = (a_n + b_n)/2$. Além disso, cuidado com a
condição $f(a_n)f(b_n) < 0$, pois pode haver problema de underflow na
multiplicação. 

## Regula-Falsi (Método da posição falsa)

Esse é outro método bem antigo, com as primeiras aparições nos registros
babilônicos. A ideia era encontrar $x$ tal que $ax + b = 0$. Essa ideia foi
trazida para resolver o problema de encontrar raízes de $f$. Nesse caso, dados
os pontos $(a, f(a)), (b, f(b))$, sabemos que existe $x^* \in (a,b)$ tal que
$f(x^*) = 0$ quando os sinais são trocados e $f$ é contínua. Traçando um
segmento entre esses pontos, em algum momento ele vai atingir o eixo $x$ e é
nesse ponto que teremos a iteração. A continuação do algoritmo é o mesmo do
método da Bisseção, isto é, o intervalo vai sendo reduzido, não mais
pelo ponto médio, mas pelo ponto de intersecção da reta que passa por
$(a,f(a))$ e $(b, f(b))$ e o eixo $x$. 

A iteração desse método é dada por 

$$
x_k = a - \frac{f(a_k)}{f(b_k) - f(a_k)}(b_k-a_k), 
$$

em que $a_k$ e $b_k$ são obtidos conforme o método da Bisseção.

Se $|f'(x)| \ge d > 0$ para todo $x \in [a,b]$, asseguramos que 

$$|x^* - x_k| \le |f(x_k)|/d.$$

## Iteração de Ponto Fixo

Se $f : \mathbb{R}^n \to \mathbb{R}$ é uma função, dizemos que $x$ é ponto
fixo de $f$ quando $f(x) = x$. Esse nome fica claro pois $f(f(\dots(f(x)))) =
x$. Note que se $g(x) = f(x) - x$, temos que $g(x) = 0 \equiv f(x) = x$, isto
é, encontrar pontos fixos de $f$ equivale a encontrar as raízes de $g$. 

### Teorema do Ponto Fixo 

Existem alguns teoremas de garantia de existência e unicidade de pontos fixos,
com diferentes hipóteses. [Aqui tem uma lista no
Wikipedia](https://en.wikipedia.org/wiki/Fixed-point_theorem#List_of_fixed-point_theorems).

**Teorema do Ponto Fixo de Brower**

Seja $f$ contínua em um conjunto convexo compacto $C$ com imagem $f(C)
\subseteq C$. Então $f$ possui ponto fixo. [Aqui uma
demonstração](https://www.math3ma.com/blog/brouwers-fixed-point-theorem-proof)
interessante com um pouquinho de topologia. No nosso caso, tomamos $C =
[a,b]$, o intervalo limitado e fechado na reta, isto é, se $f$ é contínua em $[a,b]$ e $f(x) \in [a,b]$ para todo $x \in [a,b]$, isto
é, $f([a,b]) \subseteq [a,b]$, então $f$ possui ponto fixo. 

**Teorema do Ponto Fixo de Banach**

Dizemos que uma função $f : X \to X$, em que $X$ é um espaço normado completo
é uma contração se existe $L \in [0,1)$ tal que 
$$||f(x) - f(y)|| \le r||x-y||.$$
Como exemplo, podemos tomar $X = [a,b]$. Se $X$ não for vazio e $f$ for uma
contração, então $f$ admite um **único** ponto fixo $x^*$. Além do mais, para
todo $x_0 \in X$, a sequência iniciada em $x_0$ que segue a iteração $x_k =
f(x_{k-1})$ converge para $x^*$ (o que permite desenvolver um método). 

Podemos demonstrar que $||x^* - x_n|| \le \dfrac{r^n}{1 -r}||x_1 - x_0||$.  A
prova pode ser [facilmente
encontrada](https://en.wikipedia.org/wiki/Banach_fixed-point_theorem#Proof). 

Como já afirmei, se conseguirmos assegurar que $f$ satisfaz as condições do
Teorema, então a sequência $x_0, x_1, x_2, \dots, x_n, \dots$ com $f(x_k) =
x_{k-1}$ converge para o ponto fixo $x^*$, que implica $g(x^*) = 0$.  

## Método de Newton-Raphson

Também chamado de método de Newton. Por Taylor, seja $f$ pelo menos duas vezes
derivável. Assim 

$$
f(x^*) = f(x) + (x^* - x)f'(x) + \frac{(x^*-x)^2}{2}f''(x) + o((x^*-x)^2),
$$
em que $o(x)$ é qualquer função tal que $\lim_{x\to 0} o(x)/x = 0$. O método
de Netwon assume que $(x^* - x)^2$ é suficientemente pequeno, isto é, $x$ está
suficientemente próximo de $x^*$. Assim, 

$$
0 \approx f(x) + f'(x)(x^* - x) \implies x^* \approx x - \frac{f(x)}{f'(x)}.
$$

Com essa ideia em mente, definimos a iteração

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}, 
$$

em que se $x_0$ é suficientemente próximo de $x^*$, então $\lim_{k \to
+\infty} x_k = x^*$. A ideia é que as aproximações são dadas através da
tangente, isto é, $x_{k+1}$  é o ponto da intersecção do eixo $x$ com a
tangente de $f$ no ponto $x_k$. 

**Teorema de convergência:** Seja $f$ duas vezes continuamente diferenciável
em $[a,b]$. Se $f'(x^*) \neq 0$, existe $\delta > 0$ tal que a sequência de
gerada pelo método de Newton converge para todo $x_0 \in [x^* - \delta, x^* +
\delta]$. 

A ideia dessa demonstração é introduzir a função 

$$
g(x) = x -\frac{f(x)}{f'(x)}
$$

Note que quando $f(x) =0$, teremos que $g(x) = x$, isto é, $x$ é ponto fixo de
$g$, isto é, a prova se resume a verificar as condições do Teorema do Ponto
Fixo de Banach para algum $\delta > 0$. A derivada de $g$ vai ser controlada
em um intervalo suficientemente pequeno.
 
**Condição suficiente para convergência:** Voltando a expansão de Taylor, 

$$
f(x^*) = f(x) + (x^* - x)f'(x) + \frac{(x^*-x)^2}{2}f''(z)
$$
para algum $z$ entre $x$ e $x^*$. Usando a iteração de Newton, isto é, $f(x_n)
= f'(x_n)(x_n - x_{n+1})$, obtemos que

$$
0 = f'(x_n)(x^* - x_{n+1}) +  \frac{(x^*-x_n)^2}{2}f''(z_n).
$$

Definindo $e_n = (x^* - x_n)$, temos que 

$$
e_{n+1} = \frac{e_n^2}{2f'(x_n)}f''(z_n).
$$

Assumindo que $f'(x), f''(x) \neq 0$ para $x \in [a,b]$, temos que para todo
$x_0$ tal que $f(x_0)f''(x_0) > 0$, o método converge, o que é um resultado de
convergência global. 

## Sugestões 

- [Aplicação método de Newton](/ta-sessions/analisenum/application_newton/non_linear_equations)
- [Comparação de métodos numéricos](http://www.iosrjen.org/Papers/vol4_issue4%20(part-1)/A04410107.pdf)
- [Convergência de métodos numéricos](http://compmath-journal.org/dnload/Robin-Kumar-and-Vipan-/CMJV06I06P0290.pdf).