# Monitoria 7

## Definições e Teoremas

-  Quando uma linha é substituída pela soma dela com um múltiplo de outra, a nova linha pertence ao mesmo subespaço gerado pelas primeiras. Mais do que isso, o subespaço gerado é o mesmo.
-  **Nulidade da Matriz:** Dimensão do espaço anulado da matriz $A$ ($anul(A)$). Você sabe encontrar a nulidade de uma matriz? **Teorema do Posto**! $anul(A) + posto(A) = n$.
-  Considere $Ax = v_E$. Então, $A$ é a matriz de passagem da base $B$ para a base $E$, canônica. Assim, $v_B = A^{-1}v_E$. 
-  Transformação Linear é uma função linear entre os espaços vetorias $E$ e $F$  com as propriedades de soma $T(u+v)=T(u)+T(v)$ e $T(\alpha u) = \alpha T(u)$.
-  Lembre que $T(v) = T(\alpha_1 e_1 + ... + \alpha_n e_n) = \alpha_1 T(e_1) + ... + \alpha_n T(e_n)$. Logo, a transformação linear está definida quando conhcemos as imagens dos elementos de uma base. Daí saí a matriz de transformação.
-  O escalonamento mantém a relação entre as colunas das matrizes. Para se ter a intuição, basta pensar que para resolver sistemas, escalonamos as matrizes, e as incógnitas permanecem as mesmas para o sistema escalonado.
-  Suponha que temos uma vetor $w_\beta = (a,b)_\beta$ e queremos reescrever $w_E = (a',b')$, na base canônica. Para isso, precisamos fazer uma mudança de bases que envolve uma matriz de tranformação. Essa matriz é simples, pois é composta pelos vetores da base $\beta$. 
-  **Teorema:** Seja uma transformação linear $A: E \to F$. A cada vetor $u \in \beta$ base de $E$, façamos corresponder um vetor $u' \in F$. Então essa tranformação, tal que $Au = u'$, é única. 

## Importante 

 -  Saber encontrar bases do espaço-coluna, do espaço-linha e do espaço-anulado (logo suas dimensões).
 -  Um funcional linear é $T: E \to \mathbb{R}$.
 -  Um operador linear é $T: E \to E$. 
 -  Lembrar de conjunto gerador. 

## Exercícios: 

1. Prove que os seguintes polinômios são linearmente independentes: $p(x) = x^3 - 5x^2 + 1, q(x) = 2x^4 + 5x - 6, r(x) = x^2 - 5x + 2$. *Considere a base $X = \{1, x, x^2, x^3, x^4\}$*
2. Seja $X$ um conjunto de polinômios.  Se dois polinômios quaisquer de $X$ têm graus diferentes, $X$ é LI.
3. Mostre que os vetores $u = (1,1)$ e $v = (-1,1)$ formam uma base de $\mathbb{R}^2$. 
4. Avalie as afirmações: 
   1. ( ) Seja $C = \{(x_1,x_2,x_3,x_4,x_5); x_i = 3\cdot x_{i-1}, i=2,...,5\}$. É um subespaço do $\mathbb{R}^5$. (Se verdadeiro, apresente uma base). 
   2. ( ) É possível encontrar dois planos do $\mathbb{R}^4$ que se interesectem em apenas um ponto. (*Pense em planos com dois parâmetos livres*).
   3. ( ) O conjunto de todas as matrizes cujo determinante é maior do que zero é um subespaço das matrizes. 
   4. ( ) A união de dois conjuntos LI é um conjunto LI, se  um deles é disjunto do subespaço gerado pelo outro. 
   5. ( ) Existe apenas uma transformação linear com $T(0,0,1) = (1,2)$, $T(0,1,0) = (2,3), T(1,0,0) = (4,7) $, onde $T: \mathbb{R}^3\to \mathbb{R}^2$. Isto é, não existem $x,y,z$, tal que $T(x,y,z) \neq T'(x,y,z)$ com essas propriedades. 
   6. ( ) Se $u, v, w \in E$ são colineares, então $Au,Av,Aw$ também são. 
   7. ( ) Se $Aw = Au + Av$, então $w = u + v$.
5. Encontre os espaços linha, coluna e anulado da matriz:

$$
A = \left[
\begin{array}{ccccc}
-1 & 2 & 0 & 4 & 5\\
3 & -7 & 2 & 0 & 1\\
2 & -5 & 2 & 4 & 6
\end{array}
\right]
$$

6. Seja $U = \{u_1,u_2,u_3\}$. Como representar o vetor $(a,b,c)$, como combinação linear dos vetores de $U$. 
7. Exiba uma base para o espaço vetorial formado pelos polinômios de grau $\leq n$ que se anulam em $x=2$ e $x=3$. Qual a dimensão dessa base? 
8. Tem-se uma transformação linear $A(-1,1) = (1,2,3)$ e $A(2,3) = (1,1,1)$. Qual a matriz de tranformação de $A$, em relação às bases canônicas. 



## Aplicação: Quadrados Mágicos

Na monitoria 6, observamos a imagem da Melancolia I, de Albrecht Durer de 1514, em que apareceia um quadrado mágico clássico.

*Para lembrar: definimos uma matriz $n\times n$ como quadrado mágico quando a soma de cada linha, coluna e diagonal é igual. Essa soma se chama peso. $Mag_n$ o conjunto de todos os quadrados mágicos de ordem $n$.O quadrado será clássico se usarmos os todos on números entre $1$ e $n^2$*. 

Considere $Mag_2$. Você conseguiria encontrar uma base para esse subespaço das matrizes 2 por 2 (provamos que é um subespaço na semana passada)? E $Mag_3$? 

**Exemplo:** $X = \{(1,1,1),(1,2,1)\}, Y = \{(1,0,0),(0,0,1)\}$
