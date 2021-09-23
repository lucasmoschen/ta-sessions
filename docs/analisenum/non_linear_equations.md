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

## Regula-Falsi

## Iteração de Ponto Fixo

### Teorema do Ponto Fixo 

## Método de Newton-Raphson

Também chamado de método de Newton. 
