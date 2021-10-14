# Integração Numérica

O objetivo da integração numérica é estimar 
$$I = \int_a^b f(x) \, dx,$$
principalmente quando não sabemos a antiderivada de $f$. Podemos extender para
problemas de dimensão maior, isto é, integrar 
$$I = \int_R f(x) \, dx,$$
em algum retângulo $R$ em dimensão $\mathbb{R}^n$. 

Chamamos de **quadratura numérica** o método básico de aproximação de $I$
através da soma $\sum_{i=0}^n a_i f(x_i)$. 

## Fórmula de Newton-Cotes

De forma geral, podemos
integrar o polinômio interpolador de Lagrange que aproxima para aproximar 
a integração da função aproximada pela função, isto é, 

$$\int_a^b f(x) \, dx = \int_a^b \sum_{i=0}^n f(x_i) L_i(x) + \int_a^b
\prod_{i=0}^n (x - x_i)\frac{f^{(n+1)}(\xi(x))}{(n+1)!} \, dx$$
em que $\{L_i(x)\}_{i=0}^n$ forma a base dos [polinômios de Lagrange](https://lucasmoschen.github.io/ta-sessions/analisenum/polynomial_interpolation/#polinomios-de-lagrange).

Nesse caso, uma possível aproximação para essa integral é 
$$ \int_a^b \sum_{i=0}^n f(x_i) L_i(x) \, dx = \sum_{i=0}^n a_if(x_i),$$
em que $a_i = \int_a^b L_i(x) \, dx$. O erro dessa estimação é dado por 
$$E(f) = \int_a^b
\prod_{i=0}^n (x - x_i)\frac{f^{(n+1)}(\xi(x))}{(n+1)!} \, dx.$$

A **fórmula de Newton-Cotes $(n+1)$-pontos fechada** usa os 
pontos interpoladores $x_i = x_0 + ih$ em que $h = (b-a)/n, x_0 = a$ e 
$x_n = b$. Ela é dita fechada por incluir os endpoints do intervalo. 
Apresentamos dois métodos com esse tipo de fórmula. Além do fechado, podemos tomar os pontos igualmente espaçados no interior 
do intervalo, isto é, $h = (b-a)/(n+2)$ e $x_i = x_0 + (i+1)h$ para $i = 0,
\dots, n$. Essas são ditas **fórmula de Newton-Cotes $(n+1)$-pontos aberta**.
Um exemplo conhecida é a regra do ponto médio que toma apenas um ponto 
$x_0 = (a + b)/2$. 

### Trapézio Simples

Nesse caso, definimos $x_0 = a, x_1 = b$ e $h=b-a$. Assim 
$$a_0 = \int_{x_0}^{x_1} \frac{(x - x_1)}{(x_0-x_1)} \quad \text{ e } a_1 =
\int_{x_0}^{x_1} \frac{(x - x_0)}{(x_1-x_0)}.$$

Vamos utilizar o [Teorema do Valor Médio Ponderado para Integrais](math.usm.edu/lambers/mat460/fall09/lecture3.pdf) 
(página 5) para estimar o erro. Nesse caso, ele é da seguinte forma: 
$$\begin{split}
  E(f) &= \int_{x_0}^{x_1} (x - x_0)(x - x_1)\frac{f^{(2)}(\xi(x))}{2!} \, dx
\\
&= \frac{f^{(2)}(\xi)}{2}\left[\frac{x^3}{3} - 
\frac{(x_0 + x_1)}{2}x^2 + x_0x_1x\right]_{x_0}^{x_1} \\
&= -\frac{h^3}{6}f^{(2)}(\xi),  
\end{split}$$
para algum $\xi \in (a,b)$.

A regra do trapézio se resume, então, a 
$$\int_a^b f(x) \, dx = \frac{h}{2}[f(a) + f(b)] - \frac{h^3}{12}f''(\xi).$$

### Fórmula de Simpson Simples

Para a fórmula de Simpson, fazemos $x_0 = a, x_2 = b$ e $x_1 = a + h$, 
para $h = (b-a)/2$, isto é, adicionamos mais um ponto para a aproximação 
polinomial. Nesse caso, 

$$a_0 = \int_{x_0}^{x_2} \frac{(x - x_1)(x - x_2)}{(x_0-x_1)(x_0 - x_2)}, a_1 =
 \int_{x_0}^{x_2} \frac{(x - x_0)(x - x_2)}{(x_1-x_0)(x_1 - x_2)} \text{ e }a_2 =
 \int_{x_0}^{x_2} \frac{(x - x_0)(x - x_1)}{(x_2-x_0)(x_2 - x_1)}.$$

Com essa derivação, vamos obter um erro $O(h^4)$ com um 
termo relacionado a $f^{(3)}$. Podemos reduzir esse erro com 
esses mesmos pontos usando uma abordagem levemente diferente.
É usada a expansão de Taylor em $x_1$ até ordem e um pouco de
simetria $x_2 - x_1 = x_1 - x_0$ para verificar que 
$$\int_{x_0}^{x_2} f(x) \, dx = 2hf(x_1) + \frac{h^3}{3}f''(x_1) + \frac{f^{(4)}(\xi')}{60}h^5.$$

Além disso, é usada a seguinte aproximação para $f''(x_1)$: 

$$f''(x_1) = \frac{1}{h^2}[f(x_0) - 2f(x_1) + f(x_2)] -
\frac{h^2}{12}f^{(4)}(\xi'')$$

a fim de obter a fórmula de Simpson 

$$\int_{a}^{b} f(x) \, dx = \frac{h}{3}[f(a) + 4f(a/2+b/2) + f(b)] -
\frac{h^5}{90}f^{(4)}(\xi).$$

### Precisão 

O **grau de precisão** da fórmula de quadratura é o maior inteiro 
positivo $n$ tal que a fórmula seja exata para $x^k$ para cada
$k = 0,\dots,n$. Para os exemplos desenvolvidos acima, basta olhar 
qual o maior inteiro $n$ tal que $f^{(2)} \equiv 0$ no caso 
do trapézio e $f^{(4)} = 0$ no caso de Simpson. 

### Fórmulas compostas 

É claro que as fórmulas deduzidas acima ficam bem ruins quando $b - a$ é
grande. Para isso, a ideia é subdividir o intervalo $[a,b]$ em $a = x_0 <
\dots < x_n = b$ (de forma igualmente espaçada, em geral) e aplicar a
quadratura numérica a cada um deles. Essa abordagem tira proveito da seguinte
propriedade: 
$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx.$$

Para a regra de Simpson composta teremos que 
$$\int_a^b f(x) \, dx = \frac{h}{3}\left[f(a) + 2\sum_{j=1}^{n/2 - 1}
f(x_{2j}) + 4\sum_{j=1}^{n/2} f(x_{2j-1}) + f(b)\right] -
\frac{b-a}{180}h^4f^{(4)}(\xi),$$
para $\xi \in (a,b)$ e $h = (b-a)/n$. O erro, portanto, é $O(h^4)$.

A fórmula do trapézio é similar: 
$$\int_a^b f(x) \, dx = \frac{h}{2}\left[f(a) + 2\sum_{j=1}^{n - 1}
f(x_{j}) + f(b)\right] -
\frac{b-a}{12}h^2f^{(2)}(\xi).$$

## Quadratura de Gauss-Legendre

### Polinômios Ortogonais 

### Polinômios de Legendre 

#### Fórmula de Bonnet 