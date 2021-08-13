# Aritmética do computador 

No computador, expressões como $(\sqrt{3})^2 = 3$ não são verdadeiras. Em
Python, 
```{python}
>>> (3**(1/2))**2
2.9999999999999996
```
Erros de cálculo realizados pela máquina são chamados de **erros de
arredondamento (round-off error)**. Isso acontece porque números reais são
representados de forma finita, e não cobrem todos os números reais de fato. 

## Números binários 

Em 1985, IEEE (Institute for Electrical and Electronic Engineers) [publicou um relatório](https://standards.ieee.org/standard/754-1985.html)
nomeado [*Binary Floating Point Arithmetic Standard 754–1985*](https://www.ias.ac.in/article/fulltext/reso/021/01/0011-0030) que estabelece
padrões para pontos flutuantes, algoritmos de arredondamento de operações
aritméticas e para lidar com exceções. 

A representação usual dos números reais é 64-bit (*double*). O primeiro bit é
o sinal do número. Depois vem a **característica** que é representa o expoente
(11-bit) e por fim a fração binária chamada de **mantissa** (52-bit). Os
números são armazenados na base 2. 

A representação ponto flutuante dos números é, portanto, 
$$
(-1)^s2^{c-1023}(1 + f), 
$$
em que $s$ é o sinal (0 para positivo e 1 para negativo), $c$ é o expoente
(tiramos o viés 1023 para assegurar que o intervalo de $c$ fique entre -1023 e
1024) e $f$ é a mantissa. 

- Exemplo: 

|s| c | f |
|-|-|-|
|0| 10000000011| 1011100100010000000000000000000000000000000000000000|

Nesse caso o sinal é 0, $c = 1\cdot 2^{10} + 0\cdot 2^9 + \dots + 1\cdot 2 + 1
= 1027$, e $f = 1\cdot 2^{-1} + 1\cdot 2^{-3} + \dots 1\cdot 2^{-12} =
0.722900390625$ e, portanto, 

$$
(-1)^s2^{c-1023}(1 + f) = 2^4(1 + 0.722900390625) = 27.56640625.
$$

O menor número positivo que pode ser representado é, portanto, 
$$
2^{0-1022}(1 + 0) \approx 10^{-307}
$$
e o maior 
$$
2^(2047 - 1023)(1 + (1  -2^{-52})) \approx 10^{309}
$$
Quando $s = c = f = 0$, representamos o 0. 

Note que quando um número tem representação infinita, ele deve ser, de alguma
forma, colocado em forma finita. Duas maneiras comuns de se fazer isso é
**chopping**, quando se simplesmente corta os dígitos a mais, ou
**arredondamento**. A representação de $x$ em ponto flutuante é denotada por
$fl(x)$. 

O infinito é representado quando todos os valores do expoente são 1. OS
valores de NaN (QNaN e SNaN) variam a mantissa e mantém os expoentes todos 1. 

*Um ponto interessante é a densidade dos números ponto flutuante. Quanto maior
fica o número, menor a densidade. Isso acontece porque o tamanho da mantissa é
fixo, então sempre vão existir $2^{52}$ números representados para cada
expoente. Assim o intervalo $[2^{k}, 2^{k+1})$ tem número fixo de números que
independe de $k$, apesar da distância crescer. Por esse motivo também,
$2^{-52}$ é o epsilon no sistema 64-bit.*

## Representação ponto flutuante

Vamos mostrar um exemplo de como transformar um número real $10.1$ em um ponto
flutuante. 

1. Separar parte inteira da parte decimal. 
2. Transformar a parte inteira e a parte fracionária em sua [representação
   binária](https://indepth.dev/posts/1019/the-simple-math-behind-decimal-binary-conversion-algorithms).
3. Deixar o número no formato $1.x_1x_2\dots \cdot 2^{\text{expoente}}$. 
4. Adicionar o viés 1023 ao expoente. 
5. Converter o expoente em binário. 
6. Casa 53: se for 1, soma-se a casa 52. 

Para conferir, você pode verificar a representação utilizando alguma linguagem
de programação. Por exemplo, em Python, 
```{python}
>>> import struct
>>> def binary(num): 
...     s = ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
...     return s[0] + ' ' + s[1:12] + ' ' + s[12:]
...
>>> binary(1/2)
'0 01111110000 00000000000000000000'
```

## Mensuração de erros

Seja $\bar{x}$ uma aproximação para $x$. Dizemos que
o **erro absoluto** é $|x - \bar{x}|$ e o **erro relativo** é $|x -
\bar{x}|/|x|$ quando $x \neq 0$. Dizemos que $\bar{x}$ aproxima $x$ em $t$
**dígitos significativos** se

$$
t = \max\left\{s \ge 0 \, \bigg| \, \frac{|x - \bar{x}|}{|x|} \le 5 \cdot 10^{-s} \right\}
$$