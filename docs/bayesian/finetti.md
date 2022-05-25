# Teorema da Representação de De Finetti

Considere uma sequência $X_1, \dots, X_n$ de variáveis aleatórias indicadoras (assumem valor $0$ ou $1$). 
Em geral, assumimos que elas são independentes e identicamente distribuídas (IID), implicando em algo do tipo:
$$\Pr(X_n = x_n \mid X_1 = x_1, \dots, X_{n-1} = x_{n-1}) = \Pr(X_n = x_n).$$
Desta forma, assumindo essa propriedade e que $\Pr(X = 1) = \Pr(X = 0) = 1/2$, mesmo que eu visualizasse um milhão de variáveis sendo $1$, eu acreditaria que a milionésima primeira ainda teria a mesma probabilidade.
Logo, observar um experimento não traria informação para a moeda. 
Com isso, De Finetti introduziu um conceito mais fraco, o de permutabilidade.
Em particular, ele demonstrou, para esse caso de variáveis binárias, que existe uma variável $\theta$ com distribuição $\mu_{\theta}$ tal que 
$$\Pr(X_1 = x_1, \dots, X_n = x_n) = \int_0^1 \theta^s(1-\theta)^{n-s} d\mu_{\theta}(\theta),$$
com $s = x_1 + \cdots + x_n$.
Portanto, sob a hipótese de permutabilidade, existe um parâmetro $\theta$ tal que esse parâmetro é uma função do limite das distribuições empíricas e, em particular, as variáveis são IID condicionadas em $\theta$. 
Isso permite a introdução de modelos estatísticos bayesianos de uma forma natural.

## Permutabilidade

Em uma análise estatística, existem diversas quantidades sobre as quais somos incertos. 
Por exemplo, considere uma população e uma determinada doença. 
A priori, não sabemos se as pessoas têm ou não a doença.
E mesmo que testemos algumas das pessoas, ainda não saberemos as respostas daqueles que não foram testados. 
Além do mais, o próprio teste é uma quantidade incerta, visto que o seu resultado pode ser falso. 
Portanto, deveríamos conseguir escrever a distribuição de probabilidade conjunta de todas as variáveis de interesse.
Nesse caso, elas se resumem à indicação de doença de cada indivíduo. 

Outro exemplo é a de jogar uma moeda $n$ vezes. 
Não temos informação de que jogadas próximas tenham algum tipo de relação diferente da relação para jogadas distantes.
Por esse motivo, faz sentido assumirmos que as jogadas são simétricas, e em geral, assumimos que são independentes e identicamente distribuídas, imbuindo um modelo e um parâmetro $\theta$. 
Mas essa maquinaria pode ser simplificada para refletir a ideia de simetria que gostaríamos de atingir.
Por simetria, dizemos que para toda permutação de resultados $x_1, \dots, x_n$ leva aos mesmos resultados. 
Em particular, apenas essa hipótese vai implicar que existe uma medida para $\theta$ que satisfaz propriedades probabilísticas que almejamos.

> **Permutabilidade:** As variáveis aleatórias $X_1, \dots, X_n$ são permutáveis se toda permutação de $(X_1, \dots, X_n)$ tem a mesma distribuição conjunta. Para uma coleção infinita, essa propriedade é válida quando todo subconjunto finito é permutável. 

Um resultado direto é que distribuições marginais são iguais. Além disso, a distribuição conjunta de qualquer subconjunto de variáveis de tamanho $n$ só depende de $n$. 
Também podemos afirmar que **IID implica permutabilidade**. 
Todavia, a recíproca não é verdadeira. Se $X_1, X_2, \dots$ são (condicionalmente) IID dado $Y$, as variáveis são permutáveis, mas não IID necessariamente.
De forma simples, a permutabilidade é uma hipótese fraca quando se deseja simetria entre as variáveis, e que o índice delas seja "irrelevante". 

---
*Observação: probabilidade é vista como um limite de frequências por uma grande parte dos estatísticos. 
Em particular, isso exige a tomada de uma quantidade infinita de variáveis, o que é impossível.
O Teorema de Finetti a seguir esclarece que o limite de frequências de 1s na sequência Bernoulli, denominado $\theta$ é apenas uma probabilidade condicional dada informação desconhecida.
Essa probabilidade tem visão subjetiva. 
Mesmo que o cálculo de probabilidades seja diferente, se os indivíduos assumem permutabilidade das variáveis aleatórias, então eles acreditam na existência de $\theta$, de forma que condicionado em $\theta$, as variáveis são IID Bernoulli($\theta$).*

---

## Teorema de De Finetti

O teorema de De Finetti conecta os conceitos de permutabilidade com o de independência e distribuição idêntica condicionada em uma outra variável aleatória. 
Por fim, ele relaciona essa variável condicionadora com o que chamamos de parâmetro, cerne dos modelos estatísticos paramétricos.

### Variáveis aleatórias Bernoulli

Considere uma sequência de variáveis aleatórias $\{X_n\}_{n=1}^{+\infty}$ distribuídas conforme Bernoulli. 
A sequência é permutável se, e somente se, existe uma variável aleatória $\theta \in [0,1]$ tal que $\{X_n \mid \theta\}_{n=1}^{+\infty}$ é uma sequência IID Bernoulli($\theta$). 
Além do mais, se a sequência é permutável, a distribuição de $\theta$ é única e 
$$\frac{1}{n}\sum_{i=1}^n X_i \to \theta$$ 
quase certamente.

### Versão Finita

Suponha que $X_1, \dots, X_n$ são variáveis aleatórias em um espaço de Borel $(\mathcal{X}, \mathcal{B})$. 
Seja $X = (X_1, \dots, X_n)$ e para cada $B \in \mathcal{B}$, seja $P_n(B) = \sum_{i=1}^n 1_{X_i \in B}/n$ a distribuição empírica de $X$.
As variáveis aleatórias são permutáveis se, e somente se, para toda $k$-tupla de distintos elementos de $X$, a distribuição conjunta de $(X_{i_1}, \dots, X_{i_k})$, condicionadas em $P_n = P$ é a de uma amostra aleatória simples sem reposição da distribuição $P$. 
Nesse caso, tomamos $k$ amostras sem reposição de uma urna tal que cada bola tem a mesma probabilidade de ser retirada.

### Versão infinita

Seja $(S, \mathcal{A}, \mu)$ um espaço de probabilidade e $(\mathcal{X}, \mathcal{B})$ um espaço de Borel. Para cada $n$, seja $X_n : S \to \mathcal{X}$ mensurável.
A sequência $\{X_n\}_{n \in \mathbb{N}}$ é permutável se, e somente se, existe uma medida de probabilidade *aleatória* $P$ em $(\mathcal{X}, \mathcal{B})$ tal que, condicionada em $P$, a sequência é IID com distribuição $P$. 
Nesse caso, $P$ é única e $P_n(B)$ converge para $P(B)$ quase certamente para cada $B \in \mathcal{B}$.

Alguns pontos importantes: 

(1) Um espaço de Borel: Seja $(\mathcal{X}, \mathcal{B})$ um espaço mensurável. Se existe uma função bimensurável (mensurável bijetiva com inversa mensurável) $\phi : \mathcal{X} \to R \subseteq \mathbb{R}$ com $R$ Borel, então $(\mathcal{X}, \mathcal{B})$ é espaço de Borel.

(2) Medida de probabilidade aleatória: Seja $\mathcal{P}$ o conjunto de todas as medidas de probabilidade em $(\mathcal{X}, \mathcal{B})$ e $\mathcal{C}_{\mathcal{P}}$ uma $\sigma$-álgebra de subconjuntos $\mathcal{P}$ de forma que $g_B : \mathcal{P} \to \mathbb{R}$ sejam mensuráveis, com $g_B(P) = P(B)$. 
Em particular, a função $P : S \to \mathcal{S}$ é medida de probabilidade aleatória, em que $(S, \mathcal{A}, \mu)$ é espaço de probabilidade.

Esse teorema foi estendido para sequência de variáveis aleatórias não permutáveis.

A demonstração se encontra entre as páginas 33-49 do livro de Schervish.

## Links relevantes

- [What is so cool about de Finetti's representation theorem?](https://stats.stackexchange.com/questions/34465/what-is-so-cool-about-de-finettis-representation-theorem)

- [Exchangeability, Correlation, and Bayes' Effect, Ben O'Neill](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1751-5823.2008.00059.x): esse paper discute a diferença da estatística bayesiana e frequentista sobre os valores observados, relacionando com o conceito de permutabilidade.