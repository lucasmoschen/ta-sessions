# Monitoria 6

## Definições e Teoremas

**Linearmente Independente:** Um cojunto $X \subset E$ é dito linearmente independente, quando nenhum vetor do conjunto é combinação linear dos outros vetores. O conjunto unitário é dito LI. Para isso, existe o teorema de que: $\alpha_1v_1 + ... + \alpha_nv_n = 0 \to \alpha_1 = ... = \alpha_n = 0$, se e só se, X é LI. A partir disso, conclue-se que a representação de um vetor como combinação de outros vetores é sempre única (se os vetores formarem um conjunto LI). Se um conjunto não é LI, ele é dito linearmente dependente.

**Teorema 1** Seja $X = \{x_1,x_2,...,x_m\}$. Se, $\forall k \leq m, v_k$ não é combinação linear de seus antecessores, então X é LI. 

**Observação** Considere $X = \{(1,2),(3,4),(2,4)\} \subset \mathbb{R}^2$, Note que $X$ é LD, porém $(3,4)$ não é combinação linear dos outros vetores (verifique!). Por que isso não é contraditório?

**Base:** É um conjunto linearmente independente que gera E. Os coeficientes são chamados de coordenadas do vetor nessa base. Como veremos a seguir, toda base de um espaço vetorial apresenta o mesmo número de elementos. Este número é chamado de \textit{dimensão}. 

**Lema 2.1:** Todo sistema homogêneo cujo número de incógnitas é maior que o número de equações admite solução não trivial (a prova é por indução em $m$, o número de equações. 

**Teorema 2.2:** Se um conjunto de n vetores gera o espaço E, então qualquer conjunto com mais de n elementos é LD.

**Corolário 2.3:** Assim, se os vetores $v_1,...,v_n$ geram o espaço vetorial $E$ e os vetores $u_1,...,u_m$ são LI, $m\leq n$. Daqui tiramos que se $E$ admite uma base $\beta = \{u_1,...,u_n\}$, qualquer outra base também possui n elementos.

**Teorema 3:** Considere um espaço vetorial de dimensão finita:

- Considere o conjunto de todos os geradores de E. Ele contém uma base.
- Todo conjunto LI está contido numa base.
- Todo subespaço vetorial tem dimensão finita. 
- Se a dimensão de um subespaço é $n$, então o subespaço é o próprio espaço. 

## Exercícios

1. Prove que os seguintes polinômios são linearmente independentes: $p(x) = x^3 - 5x^2 + 1, q(x) = 2x^4 + 5x - 6, r(x) = x^2 - 5x + 2$. *Dica: Considere a base $X = \{1, x, x^2, x^3, x^4\}$*
2. Seja $X$ um conjunto de polinômios.  Se dois polinômios quaisquer de $X$ têm graus diferentes, $X$ é LI.
3. Dado $X \subset E$, seja $Y$ o conjunto obtido de $X$ substituindo um dos seus elementos $v$ por $v + \alpha u$, onde $u \in X$ e $\alpha \in \mathbb{R} $. Prove que X e Y geram o mesmo subespaço vetorial de $E$. Conclua, então que $\{v_1,...,v_k\} \subset E$ e $\{v_1, v_2 - v_1, ..., v_k - v_1\} \subset E$ geram o mesmo subespaço vetorial de $E$.
4. Mostre que os vetores $u = (1,1)$ e $v = (-1,1)$ formam uma base de $\mathbb{R}^2$. 
5. Considere a afirmação: "A união de dois conjuntos subconjuntos LI do espaço
   vetorial E é ainda um conjunto LI". Assinale verdadeiro e falso: (  )
   Nunca; (  ) Quando um deles é disjunto do outro; (  ) Quanto um deles é
   parte do outro; (  ) Quando um deles é disjunto do subespaço gerado pelo
   outro; (  ) Quando o número de elementos de um deles mais o número de
   elementos do outro é igual à dimensão de E.
6. Encontre uma base para o espaço vetorial  
   
$$W = \{\begin{pmatrix} a \\ b \\ -b \\ a\end{pmatrix}, \forall a,b \in
\mathbb{R}^2\}$$
 
7.  Se $f$ e $g$ estão no espaço vetorial de todas as funções com derivadas
   contínuas, então o determinante de 
   
$$\begin{pmatrix} f(x) & g(x) \\
   f'(x) & g'(x) \end{pmatrix}
   $$ 

é conhecido como **Wronskiano** de $f$ e
   $g$. Prove que $f$ e $g$ são linearmente independentes, se seu Wronskiano
   não for identicamente nulo. Esse estudo é estremamente importante no estudo
   de soluções de sistemas de equações diferenciáveis, pois identifica se duas
   soluções são linearmente independentes.   

## Aplicação: Quadrados Mágicos

Observe a imagem da Melancolia I, de Albrecht Durer de 1514:
[Link da
obra](https://artsandculture.google.com/asset/melencolia-i-albrecht-d%C3%BCrer/aAGgEK-AKbn5eQ?hl=zh-tw&ms=%7B%22x%22%3A0.7518538853310617%2C%22y%22%3A0.2894316595268001%2C%22z%22%3A10%2C%22size%22%3A%7B%22width%22%3A0.4646606018194542%2C%22height%22%3A0.355444997236042%7D%7D)

Observa-se o quadrado mágico: 

$$\begin{pmatrix}
16 & 3  & 2 & 13 \\ 
5 & 10 & 11 & 8 \\
9 & 6 & 7 & 12 \\
4 & 15 & 14 & 1
\end{pmatrix}
$$

Primeira coisa interessante é ver $15$ e $14$ lado a lado. A soma de cada coluna, linha e diagoral é $34$. Podemos definir uma matriz $n\times n$ sendo quadrado mágico quando a soma de cada linha, coluna e diagonal é igual. Essa soma se chama peso. Considere $Mag_n$ o conjunto de todos os quadrados mágicos de ordem $n$. Prove que $Mag_3$ é um subespaço de $M_{3x3}$. 
