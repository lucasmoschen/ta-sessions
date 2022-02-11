# Monitorias 10 e 11

## Definições e Teoremas

**Lembrando:** Uma transformação linear
$T: \mathbb{R}^n \to \mathbb{R}^m$ fica inteiramente determinada por uma
matriz $A = [a_{ij}] \in M(m \times n)$. Os vetores coluna dessa matriz
são as imagens $A \cdot e_j$ dos vetores da base canônica. Definimos $A$
como matriz de transformação. Assim,
$A \cdot e_j = \sum_{i=1}^m a_{ij}e_i (j=1,...,n)$, onde
$e_i \in \mathbb{R}^m$.

**Simetrias:** Matrizes de tranformação referentes à simetria em
relação aos eixos x e y, e em relação à origem, respectivamente:
$$S_x = \left[
\begin{array}{cc}
1 & 0  \\
0 & -1
\end{array}
\right]
S_y = \left[
\begin{array}{cc}
-1 & 0  \\
0 & 1
\end{array}
\right]
S_o = \left[
\begin{array}{cc}
-1 & 0  \\
0 & -1
\end{array}
\right]$$

**Dilatações:** Basta multiplicar uma coluna que se quer dilatar por
$r$. Podemos chamar $r$ de coeficiente de dilatação.

**Rotação:** Para montar essa matriz, basta conhecer a transformação dos
vetores $(1,0)$ e $(0,1)$. 

$$R_{\theta} = \left[
\begin{array}{cc}
\cos \theta & - \sin \theta  \\
\sin \theta & \cos \theta
\end{array}
\right]
$$ 

A rotação tem algumas propriedades:

-   $R_{\theta}^{-1} = R_{-\theta}$

-   $R_{\alpha}R_{\beta} = R_{\alpha + \beta}$

-   $(R_{\theta})^n = R_{n\theta}$

**Projeções:** Podemos considerar a transformação que projeta os vetores
sobre a reta $y = ax$. 

$$P = \frac{1}{1+a^2} \left[
\begin{array}{cc}
1 & a  \\
a & a^2
\end{array}
\right]
$$ 

Se quisermos que a projeção sobre um eixo e paralelo a uma
reta, temos que 

$$P_p = \left[
\begin{array}{cc}
1 & -\frac{1}{a}  \\
0 & 0
\end{array}
\right]
$$

**Núcleo de $A$:** $N(A) = \{v \in E | Av = 0\}$. É o espaço anulado da
matriz $A$.

**Imagem de $A$:**
$Im(A) = \{Av | v \in E\} \implies \exists v \in E; Av = w \implies w \in Im(A) $.
Notemos que $posto(A) = dim~Im(A) = dim~col(A)$. Isto ocorre, pois
$w \in Im(A)$ é combinação linear das colunas da matriz $A$.

**Transformação Injetiva:** $A: E \to F$ é injetiva se
$\forall v, v', v \neq v' \implies Av \neq Av'$. Uma transformação é
injetiva se, e só se, transforma vetores LI em vetores LI. Para essa
demonstração, é necessário mostrar que uma transformação é injetiva se,
e só se, seu núcleo possui apenas o vetor nulo.

**Transformação Sobrejetiva:** Ocorre quando $Im(A) = F$, onde $F$ é o
espaço vetorial contradomínio.

**Teorema do Núcleo e da Imagem:** Como $dim~Im(A) = posto(A)$, podemos
usar no teorema do posto. Podemos alterar $n$ para $dim~E$, sendo $E$ o
domínio da transformação.

**Laplace:** Escolhe-se uma linha uma coluna e para cada elemento, calcula-se o seu cofator.
$A_{ij} = (-1)^{i+j}D_{ij}$.

### Propriedades Importantes: 

- $det(A) = det(A^{T})$;
- trocar duas linhas ou colunas inverte o sinal do determinante; 
- duas linhas proporcionais indica determinante 0;
- multiplicar uma linha por $\alpha$ implicará multiplicar o determinante pelo mesmo fator; 
- determinante do produto de matrizes é o produto dos determinantes; 
- o determinante de uma matriz com a operação de somar com múltiplo de outra linha é idêntico; 
- determinante da inversa é o inverso do determinante

## Lembretes para exercícios:

1.  Para calcular uma matriz de tranformação, precisamos apenas saber a
    transformação linear de uma base do domínio. Com essa transformação,
    precisamos obter a transformação da base canônica, para que a matriz
    seja constrída nessa base. Essa matriz de tranformação também pode
    ser obtida por $T = AP^{-1}$, onde $P$ tem como colunas os vetores
    da base, e $A$ os vetores da base após a transformação.

2.  Para mostrar injetividade, podemos usar a contrapositiva da
    definição.

3.  Você sabe encontrar uma base para o núcleo e uma base para a imagem
    de uma transformação? A base da imagem é basicamente a base para o
    espaço coluna (consegue enxergar o porquê? Tente representar um
    vetor da imagem como combinação linear das colunas. E a base para o
    núcleo?

## Exercícios: 

1. **Reflexão em torno de uma reta:** Seja
    $S: \mathbb{R}^2 \to \mathbb{R}^2$ a transformação que reflete um
    veotr em torno da reta $y = ax$. Assim, a reta é a bissetriz do
    ângulo entre $v$ e $Sv$ e é perpendicular à reta que liga $v$ a
    $Sv$.
   - **Solução:** Seja $P$ a matriz de projeção. Projetamos
    ortogonalmente $v$ sobre a reta $y = ax$. Assim, teremos que
    $v + Sv = 2Pv \implies I + S = 2P \implies S = 2P - I$. Outra forma
    é fazer as tranformações dos vetores da base canônica.

2.  Considere 5 lâmpadas, cada uma com um botão. Cada botão muda o
    estado da lâmpada e das vizinhas. Todas estão apagadas. Como deixar
    a primeira, terceira e quinta acesas.

3.  Encontre os números $a,b,c,d$ de modo que o operador
    $A: \mathbb{R}^2 \to \mathbb{R}^2$, dado por
    $A(x,y) = (ax + by, cx + dy)$ tenha como núcleo a reta $y = 3x$.

4.  A transformação
    $A: \mathbb{R} \to \mathbb{R}^n; A(x) = (x,2x,...,nx)$ é uma
    transformação injetiva? E $B(x,y) = (x + 2y, x + y, x - y)$?

5.  Considere uma transformação $A: E \to F$ na base canônica. Considere
    $V$ uma base de vetores de $E$. Determine a matriz de transformação
    $A'$ nessa base. Ou seja, se $Av = w \to A'v_V = w_V$.

6.  Ache uma transformação $A: \mathbb{R}^2 \to \mathbb{R}^2$ tal que a
    imagem e o núcleo sejam o eixo x.


