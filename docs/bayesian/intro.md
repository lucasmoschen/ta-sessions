# Introdução

- **Teoria Estatística**: objetiva obter uma inferência sobre a distribuição de probabilidade de um fenômeno a partir de observações. 

- A base teórica do livro *The Bayesian Choice* é construída sob o ponto de vista da Teoria da Decisão. Isso se deve a dois fatos: (i) a inferência tem algum objetivo, isto é, alguma decisão deve ser tomada baseada em uma previsão ou análise, e ela tem consequências mensuráveis; e (ii) a decisão clarifica a preferência do estatístico.

- Estatística é mais sobre a interpretação de fenômenos naturais do que a explicação sobre eles. Ela tem um passo de *formalicação redutiva*. 

- A modelagem estatítica através probabilidade possibilita incluir informação disponível sobre o fenômeno e a incerteza sobre essa informação. Uma crítica à abordagem probabilística é a dificuldade em saber a distribuição de probabilidade do fenômeno exatamente. 

---
``📝`` **Exemplo (modelo capture-recapture)**

Suponha que queremos estimar o número de ônibus $N$ em uma cidade. Uma forma de fazer isso é a seguinte: contamos a quantidade vista de ônibus em um dia ($q_1$) e armazenamos a identificação de cada um. No dia seguinte, fazemos a mesma coisa e obtemos ($q_2$). Seja $n$ o número de ônibus que vimos nos dois dias. Qual a distribuição de $n$? Olhando para o segundo dia, em uma população de tamanho $N$, tínhamos $q_1$ ônibus de interesse para recontar. Nossa amostra é de tamanho $q_2$. Isso define a [distribuição hipergeométrica](https://en.wikipedia.org/wiki/Hypergeometric_distribution), pois a amostragem do segundo dia é sem reposição (note que simplificamos que só podemos ver o mesmo ônibus uma vez). Logo

$$n \sim Hypergeometric(N, q_1, q_2).$$

Sabemos que $\mathbb{E}[n] = (q_1/N) \cdot q_2 \implies \hat{N} = q_1 \cdot q_2 / n$ é um possível estimador para $N$. Note que esse estimador não é necessariamente não enviesado, pois $\mathbb{E}[1/n] \neq 1/\mathbb{E}[n]$.

---

- Para aproximar uma distribuição de probabilidade de um fenômeno, duas abordagens estatíticas são usadas: **não paramétrica** e **paramétrica**. Na primeira, a estimativa procura assumir o mínimo possível, procurando uma estimação funcional. Já a segunda, representa através de uma densidade parametrizada, em que o parâmetro de dimensão finita é desconhecido.

- Um modelo estatístico paramétrico consiste de observações de uma variável aleatória $x \in \mathcal{}$ (espaço de estados) com distribuição cuja densidade é $f(x | \theta)$ e $\theta \in \Omega$ (espaço dos parâmetros) é desconhecido com dimensão finita. 

- Logo, métodos estatísticos permitem fazer inferência sobre $\theta$ a partir de $x$, enquanto a modelagem probabilística caracteriza o comportamento de observações futuras condicionadas em $\theta$. 

## Paradigma bayesiano

No paradigma bayesiano, as quantidades desconhecidas são tratadas como variável aleatória, incluindo o parâmetro $\theta$. Assim, se temos um modelo $P_{\theta}$ para $x$, precisamos de uma distribuição para $\theta$, a qual chamamos de **distribuição a priori**. Com elas, construímos uma distribuição em $\mathcal{X} \times \Omega$. Em particular, 

$$\Pr((x,\theta) \in B) = \int_{\Omega} \int_{\mathcal{X}} I_B(u, v) f_{x | \theta}(u|v)f_{\theta}(v) \, du \, dv,$$

se $f_{\theta}$ for a densidade da distribuição de $\theta$. 

Matematicamente, probabilidades podem representar crenças numericamente, relacionando informação com probabilidade. A Regra de Bayes provê um método racional para atualizar crenças frente a novas informações. O processo indutivo de atualizar crenças com Bayes é chamada de inferência bayesiana. 

### Teorema de Bayes

Se $E$ é um evento com probabilidade positiva e $A$ é um outro evento, temos que 
$$\Pr(A | E) = \frac{\Pr(E |A) \Pr(A)}{\Pr(E)}.$$
Podemos expressar através de densidades, com 
$$p(\theta | x) = \frac{f(x|\theta)\pi(\theta)}{\int_{\Omega} f(x|t)\pi(t) \, dt},$$
em que $\pi(\theta)$ é a densidade da priori do parâmetro $\theta$ e $p(\theta | x)$ é chamada de **distribuição a posteriori** de $\theta$. Além disso, como o parâmetro $\theta$ é desconhecido, também denotamos a densidade de $x$ condicionada em $\theta$ como uma função de $\theta$, após observar $x$. Nesse caso, chamamos de **função de verossimilhança** $l(\theta | x) = f(x | \theta)$ para cada $\theta \in \Omega$ e $x$ observado. O denominador da expressão acima é chamada de **densidade preditiva a priori** e não depende de $\theta$. É a marginal no espaço de estados.

A distribuição a priori encapsula a informação disponível sobre o parâmetro $\theta$ antes do experimento, incluindo a incerteza residual. Cox (1946, 1961) and Savage (1954, 1972) provaram que se priori e verossimilhança representam crenças racionais, a regra de Bayes é o método ótimo de atualizar essas crenças sobre o parâmetro dada nova informação. Claro que, em geral, não conseguimos exploxar as crenças de modo perfeito e a posteriori não vai ser ótima, nesse sentido. 

---
``📝`` **Exemplo (Bayes, 1974)**

Uma bola de sinuca $O$ é rolada em uma linha de comprimento 1. É natural assumir que ela tem uma distribuição uniforme de parar em qualquer lugar, só dependendo da força exercida sobre ela. Seja $p$ o ponto de parada. Em seguida, rolamos uma outra bola $n$ vezes e contamos a quantidade de vezes ($X$) que ela parou antes de $B$. Nesse caso, observado $X=x$, queremos inferir $p$. Se $p$ fosse conhecido, qual seria distribuição de $X$? Veja que temos $n$ experimentos independentes e idênticos de sucesso ou falha, com probabilidade de sucesso $p$ (lembrando da distribuição uniforme!). Nesse caso $X|p \sim Bernoulli(n, p)$. Com essas configurações, podemos verificar que 
$$\Pr(a < p < b | X=x) = \frac{\int_a^b p^x(1-p)^{n-x} \, dp}{B(x+1, n-x+1)},$$
em que $B$ é a [função Beta](https://en.wikipedia.org/wiki/Beta_function).

---

Enquanto a estatística clássica é dirigida por princípios justificados axiomaticamente, a abordagem bayesiana incorpora esses princípios sem a restrição sobre os procedimentos e também rejeita outros pincípios. Por exemplo, o conceito de estimadores não enviesados, em geral preferidos na estatística clássica, impõe restrições fortes sobre os procedimentos adotados e leva a performances ineficientes (ver [exemplo de Stein](https://en.wikipedia.org/wiki/Stein%27s_example)). Isso acontece, pois a justificativa é assintótica, já que em média o estimador é correto. 

## Princípio da Verossimilhança e Princípio da Suficiência

### Suficiência

Se $x \sim f(x | \theta)$, uma função $T: \mathcal{X} \to \mathbb{R}^k$ (estatística) é **suficiente** se a distribuição de $x$ condicionada em $T(x)$ não depende em $\theta$. Para mais detalhes, ver [aqui](/ta-sessions/infestatistica/SufficientStatistics/). De forma simplificada, $T(x)$ traz toda a informação sobre $\theta$ advinda de $x$.

