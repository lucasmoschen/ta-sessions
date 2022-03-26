# Introdução

- **Teoria Estatística**: objetiva obter uma inferência sobre a distribuição de probabilidade de um fenômeno a partir de observações. 

- A base teórica do livro *The Bayesian Choice* é construída sob o ponto de vista da Teoria da Decisão. Isso se deve a dois fatores: $(I)$ a inferência tem algum objetivo, isto é, alguma decisão é tomada baseada em uma previsão ou análise, e ela tem consequências mensuráveis; e $(II)$ a decisão clarifica a preferência do estatístico.

- Estatística é mais sobre a interpretação de fenômenos naturais do que a explicação sobre eles. Além disso, ela tem um passo de *formalização redutiva*. 

- A modelagem estatística, através probabilidade, possibilita incluir a informação disponível sobre o fenômeno e a incerteza sobre essa informação. Uma crítica à abordagem probabilística é a dificuldade em saber exatamente a distribuição de probabilidade do fenômeno. 

---
``📝`` **Exemplo (modelo capture-recapture)**

Suponha que queremos estimar o número de ônibus $N$ em uma cidade. Uma forma de fazer isso é a seguinte: contamos a quantidade vista de ônibus em um dia ($q_1$) e armazenamos a identificação de cada um. No dia seguinte, fazemos a mesma coisa e obtemos ($q_2$). Seja $n$ o número de ônibus que vimos nos dois dias. Qual a distribuição de $n$? Olhando para o segundo dia, em uma população de tamanho $N$, tínhamos $q_1$ ônibus de interesse para recontar. Nossa amostra é de tamanho $q_2$. Isso define a [distribuição hipergeométrica](https://en.wikipedia.org/wiki/Hypergeometric_distribution), pois a amostragem do segundo dia é sem reposição (note que simplificamos que só podemos ver o mesmo ônibus uma vez). Logo

$$n \sim Hypergeometric(N, q_1, q_2).$$

Sabemos que $\mathbb{E}[n] = (q_1/N) \cdot q_2 \implies \hat{N} = q_1 \cdot q_2 / n$ é um possível estimador para $N$. Note que esse estimador não é necessariamente não enviesado, pois $\mathbb{E}[1/n] \neq 1/\mathbb{E}[n]$.

---

- Para aproximar uma distribuição de probabilidade de um fenômeno, duas abordagens estatísticas são usadas: **não paramétrica** e **paramétrica**. Na primeira, a estimativa procura assumir o mínimo de hipóteses possível, procurando uma estimação funcional. Já a segunda vem de uma densidade parametrizada, em que o parâmetro de dimensão finita é desconhecido.

- Um modelo estatístico paramétrico consiste de observações de uma variável aleatória $x \in \mathcal{X}$ (espaço de estados) com distribuição cuja densidade é $f(x | \theta)$ e $\theta \in \Omega$ (espaço dos parâmetros) é desconhecido com dimensão finita. 

- Logo, métodos estatísticos permitem fazer inferência sobre $\theta$ a partir de $x$, enquanto a modelagem probabilística caracteriza o comportamento de observações futuras condicionadas em $\theta$. 

## Modelo paramétrico 

Schervish apresenta uma definição formalizada de modelo paramétrico, a qual eu apresento a seguir. 

> Seja $(S, \mathcal{A}, \mu)$ um espaço de probabilidade, e $(\mathcal{X}, \mathcal{B})$ e $(\Omega, \tau)$ espaços de Borel (espaço mensurável isomorfo a um subconjunto mensurável dos reais. Em geral, veremos que esses espaços são subconjuntos mensuráveis dos reais). Seja $X : S \to \mathcal{X}$ e $\Theta : S \to \Omega$ funções mensuráveis. Chamamos $\Theta$ de parâmetro e $\Omega$ de espaço de parâmetros. A distribuição de $X | \Theta = \theta$ é família paramétrica de distribuições de $X$ dada por $P_{\theta}$. A medida de probabilidade $\mu_{\Theta}$ sobre $(\Omega, \tau)$ induzida por $\Theta$ a partir de $\mu$ é chamada de distribuição a priori ($\mu_{\Theta}(B) = \mu(\Theta \in B), B \in \tau$). A densidade de $P_{\theta}$ (que é absolutamente contínua) com respeito à uma medida $\nu$ é dada por
> $$f_{X|\Theta}(x|\theta) = \frac{dP_{\theta}}{d\nu}(x),$$
> a derivada de Radon-Nikodym. 

## Paradigma bayesiano

No paradigma bayesiano, as quantidades desconhecidas são tratadas como variáveis aleatórias, incluindo o parâmetro $\theta$. Na página 12 de seu livro, Shervish apresenta uma justificativa matemática para esse fato. Assim, se temos um modelo $P_{\theta}$ para $x$, precisamos de uma distribuição para $\theta$, a qual chamamos de **distribuição a priori**. Com elas, construímos uma distribuição em $\mathcal{X} \times \Omega$. Em particular, 

$$\Pr((x,\theta) \in B) = \int_{\Omega} \int_{\mathcal{X}} I_B(u, v) f_{x | \theta}(u|v)f_{\theta}(v) \, du \, dv,$$

se $f_{\theta}$ for a densidade da distribuição de $\theta$. Para isso, basta exigir que $f_{X | \Theta}$ seja mensurável em $\mathcal{B} \otimes \tau$.Matematicamente, probabilidades podem representar crenças numericamente, relacionando informação com probabilidade. A Regra de Bayes provê um método racional para atualizar essas crenças frente a novas informações. O processo indutivo de atualizar crenças com Bayes é chamada de inferência bayesiana. 

### Teorema de Bayes

Se $E$ é um evento com probabilidade positiva e $A$ é um outro evento, temos que 
$$\Pr(A | E) = \frac{\Pr(E |A) \Pr(A)}{\Pr(E)}.$$
Podemos expressar através de densidades, com 
$$p(\theta | x) = \frac{f(x|\theta)\pi(\theta)}{\int_{\Omega} f(x|t)\pi(t) \, dt},$$
em que $\pi(\theta)$ é a densidade da priori do parâmetro $\theta$ e $p(\theta | x)$ é chamada de **distribuição a posteriori** de $\theta$ (para uma demonstração detalhada do Teorema de Bayes, vale conferir a página 16 do livro de Schervish). Além disso, como o parâmetro $\theta$ é desconhecido, também denotamos a densidade de $x$ condicionada em $\theta$ como uma função de $\theta$, após observar $x$. Nesse caso, chamamos de **função de verossimilhança** $l(\theta | x) = f(x | \theta)$ para cada $\theta \in \Omega$ e $x$ observado. O denominador da expressão acima é chamada de **densidade preditiva a priori** e não depende de $\theta$. É a marginal no espaço de estados. 

A distribuição a priori encapsula a informação disponível sobre o parâmetro $\theta$ antes do experimento, incluindo a incerteza residual. Se a distribuição a priori e a distribuição dos dados representam crenças racionais, [a regra de Bayes é o método ótimo para atualizar essas crenças](https://books.google.com.br/books?id=V8jT2SimGR0C&pg=PA2&lpg=PA2&dq=%22Bayes%E2%80%99+rule+is+an+optimal+method%22&source=bl&ots=X6NYVjaGMG&sig=ACfU3U35KV7iPBPmwMc8lNcupnc5zrEysg&hl=en&sa=X&ved=2ahUKEwiH7PmO0uT2AhWQVt8KHTpsBCgQ6AF6BAgcEAM#v=onepage&q=%22Bayes%E2%80%99%20rule%20is%20an%20optimal%20method%22&f=false) sobre o parâmetro dada nova informação. Claro que, em geral, não conseguimos explorar as crenças de modo perfeito e a posteriori não vai ser ótima, nesse sentido. 

---
``📝`` **Exemplo (Bayes, 1974)**

Uma bola de sinuca $O$ é rolada em uma linha de comprimento 1. É natural assumir que ela tem uma distribuição uniforme de parar em qualquer lugar, só dependendo da força exercida sobre ela. Seja $p$ o ponto de parada. Em seguida, rolamos uma outra bola $n$ vezes e contamos a quantidade de vezes ($X$) que ela parou antes de $B$. Nesse caso, observado $X=x$, queremos inferir $p$. Se $p$ fosse conhecido, qual seria distribuição de $X$? Veja que temos $n$ experimentos independentes e idênticos de sucesso ou falha, com probabilidade de sucesso $p$ (lembrando da distribuição uniforme!). Nesse caso $X|p \sim Bernoulli(n, p)$. Com essas configurações, podemos verificar que 
$$\Pr(a < p < b | X=x) = \frac{\int_a^b p^x(1-p)^{n-x} \, dp}{B(x+1, n-x+1)},$$
em que $B$ é a [função Beta](https://en.wikipedia.org/wiki/Beta_function).

---

Enquanto a estatística clássica é dirigida por princípios justificados axiomaticamente, a abordagem bayesiana incorpora esses princípios sem a restrição sobre os procedimentos e também rejeita outros princípios. Por exemplo, o conceito de estimadores não enviesados, em geral preferidos na estatística clássica, impõe restrições fortes sobre os procedimentos adotados e leva a performances ineficientes (ver [exemplo de Stein](https://en.wikipedia.org/wiki/Stein%27s_example)). Isso acontece, pois a justificativa é assintótica, já que em média o estimador é correto. 

Por fim, em estatística bayesiana, **TODAS AS INFERÊNCIAS SÃO BASEADAS NA DISTRIBUIÇÃO A POSTERIORI**.

## Um pouco de história

Em 1763, é publicado [An Essay towards Solving a Problem in the Doctrine of Chances](https://www.jstor.org/stable/105741?seq=1), paper atribuído a Thomas Bayes e publicado por Richard Price. O principal objeto desse trabalho, além do exemplo acima, é o que conhecemos como Teorema de Bayes, mas com a priori sendo uniforme. Laplace, em [Memoir on the Probability of the Causes of Events](https://www.york.ac.uk/depts/maths/histstat/memoir1774.pdf) foi quem descreveu em uma forma mais geral, apesar de ainda ser discreta. Do ponto de vista probabilístico, o Teorema de Bayes é apenas uma forma de mensurar a incerteza. A controvérsia advém da interpretação da probabilidade e se ele deveria ser considerado ponto central no processo de aprendizado. 

## Visão subjetiva da probabilidade

A visão de que o mundo é determinístico ou não, como a discussão do [Demônio de Laplace](https://en.wikipedia.org/wiki/Laplace%27s_demon), é pouco importante na verdade para a estatística. O que importa é a incerteza que temos sobre as quantidades. No prefácio de seu livro [Theory of Probability](https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781119286387.fmatter), Bruno de Finetti argumenta que "probabilidade não existe" no sentido *objetivo*. A única exigência é que exista consistência em nossas crenças e na relação com dados objetivos. Basicamente, a definição de probabilidade é subjetiva: a taxa em que o indivíduo está disposto a apostar na ocorrência de um evento.

Considere um dado normal de seis lados. Um frequentista afirmaria que, por simetria, cada lado tem igual chance de ocorrer. Evidência empírica passada suportaria sua afirmação. Um subjetivista ouviria os argumentos, mas o que realmente iria considerar seria sua crença sobre o que acontecerá em uma jogada de dados, isto é, quanto seria apostado em cada lado, dada a informação presente. Logo, no trabalho de De Finetti, Probabilidade e Preço são equivalentes. Para uma discussão mais detalhada, consulte [esse trabalho](https://faculty.fuqua.duke.edu/~rnau/definettiwasright.pdf).

## Princípio da Verossimilhança e Princípio da Suficiência

### Suficiência

Seja $x \sim f(x | \theta)$. Uma função/estatística $T: \mathcal{X} \to \mathbb{R}^k$ (a imagem de $T$, juntamente com o conjunto de seus singletons, pode ser qualquer espaço mensurável) é **suficiente** se a distribuição de $x$ condicionada em $T(x)$ não depende de $\theta$. Para mais detalhes, ver [aqui](/ta-sessions/infestatistica/SufficientStatistics/). De forma simplificada, $T(x)$ traz toda a informação sobre $\theta$ advinda de $x$. Schervish (página 84) adiciona o fato de que para qualquer priori $\pi(theta)$, a distribuição a posteriori de $\theta$ condicionada em $x$ e a posteriori condicionada em $T(x)$ são iguais quase certamente. Como demonstrado no Teorema 2.14 do mesmo livro, essas definições são equivalentes dadas algumas hipóteses de regularidade.

O **Teorema da fatoração Fisher-Neyman** mostra que se a densidade de $x$ é a derivada de Radon-Nikodym para alguma medida de probabilidade ($\sigma$ - finita) cuja distribuição seja absolutamente contínua, então vale que $T(x)$ é suficiente para $\theta$ se, e somente se, existem funções $g$ e $h$ não-negativas tal que 

$$f(x|\theta) = g(T(x)|\theta)h(x|T(x)).$$

O conceito de suficiência foi introduzido por Fisher e está associado com o seguinte princípio:

> **Princípio da Suficiência (PS):** Se duas observações $x$ e $y$ são tais que $T(x) = T(y)$ para alguma estatística suficiente $T$, então elas devem levar à mesma inferência sobre o parâmetro.

---
``📝`` **Exemplo**

Suponha que observamos $x = (x_1, \dots, x_n) \overset{iid}{\sim} Exponential(\lambda)$. Uma estatística suficiente para $\lambda$ é a média amostral $T(x) = \bar{x}$, em particular, 
$$f(x | \lambda) = \lambda^n e^{-\lambda n \bar{x}}.$$
Logo, inferências sobre $\lambda$ só devem se basear em $\bar{x}$, segundo o Princípio da suficiência.

---

### Princípio da Verossimilhança 

Esse conceito é também atribuído a [Fisher](https://www.amazon.com/Statistical-Methods-Scientific-Inference-Ronald/dp/0050008706), mas a sua formalização se deve a [Birnbaum (1962)](https://www.jstor.org/stable/pdf/2281640.pdf).

> **Princípio da Verossimilhança (PV):** a informação trazida por uma observação $x$ sobre $\theta$ é inteiramente contida na função de verossimilhança $l(\theta|x)$. Além do mais, se duas observações $x$ e $y$ dependem de $\theta$, de forma que $l_1(\theta|x) = cl_2(\theta|y), \, \forall \theta \in \Omega$ para alguma constante $c$, então elas levam à mesma inferência sobre $\theta$. 

Uma outra forma de expressar esse princípio é o seguinte: Se $E$ e $E'$ são experimentos definidos em $\Omega$, representados pelas densidades $f(x, \theta)$ e $g(y, \theta)$, e $x$ e $y$ são observações determinando a mesma função de verossimilhança, então a evidência trazida por ambos os experimentos é a mesma vista a partir dessas observações, isto é, o resultado $x$ de qualquer experimento $E$ é caracterizado somente pela verossimilhança até uma constante. 

---
``📝`` **Exemplo**

Seja $\theta \in [0,1]$ a proporção de doentes em uma população. Um examinador encontrou nove pessoas saudáveis e três doentes. Se nenhuma informação adicional é obtida, podemos propor dois modelos diferentes para esse fenômeno:

(1) O examinador testou 12 pessoas e observou $x \sim Binomial(12, \theta)$ com $x = 3$.

(2) Ele questionou $N = 12$ pessoas até encontrar $3$ doentes. Nesse caso, $N \sim NegativeBinomial(3, \theta)$

Apesar do dado ser diferente em ambos os experimentos, as verossimilhanças são proporcionais. Portanto, as inferências devem ser as mesmas sobre $\theta$.

---

Como as inferências são baseadas na posteriori, a abordagem bayesiana satisfaz o Princípio da Verossimilhança. Porém, na abordagem frequentista, isso não é verdade, já que é baseada no comportamento médio dos procedimentos. O estimador de máxima verossimilhança também satisfaz.

### Derivando o princípio da verossimilhança

> **Princípio da Condicionalidade (PC):** Se dois experimentos $E$ e $E'$ sobre $\Omega$ estão disponíveis e um deles é selecionado com probabilidade $p$, a inferência resultante sobre $\theta$ só deveria depender do experimento selecionado.
 
O fato que Birnbaum demonstrou é que PS + PC = PL. Isso é interessante, pois, para muitos estatísticos, PS e PC são aceitáveis, mais PL não. Isso faz com que os resultados científicos, para serem coerentes, devessem ser descritos através da função de verossimilhança, e não por níveis de significância e estimativas intervalares. [Evans, 2013](https://projecteuclid.org/journals/electronic-journal-of-statistics/volume-7/issue-none/What-does-the-proof-of-Birnbaums-theorem-prove/10.1214/13-EJS857.full) utiliza teoria dos conjuntos para mostrar que a demonstração de Birnbaum tem falhas, já que ignora uma hipótese chave. [Gandenberger, 2015](https://www.journals.uchicago.edu/doi/abs/10.1093/bjps/axt039?journalCode=bjps) ofereceu uma nova demonstração para o Princípio da Verossimilhança, mas com hipóteses diferentes. [Aqui](https://vicpena.github.io/isba2016.pdf) temos um breve resumo em formato de slides.

## Distribuições a priori e a posteriori

Dada a distribuição de $x$ dada por $f(x|\theta)$ e a distribuição a priori $\pi(\theta)$, podemos derivar as seguintes distribuições:

(a) a distribuição conjunta
$$ \varphi(x, \theta) = f(x |\theta) \pi(\theta);$$

(b) a distribuição marginal de $x$
$$m(x) = \int f(x|\theta) \pi(\theta) \, d\theta;$$

(c) a distribuição a posteriori de $\theta$
$$p(\theta|x) = \frac{f(x|\theta)\pi(\theta)}{m(x)};$$

(d) a distribuição preditiva de $y$, quando $y \sim g(y|x, \theta),$
$$g(y|x) = \int g(y|\theta, x) \pi(\theta | x) \, d\theta.$$

### Distribuições a priori impróprias

Para a especificação de um modelo (paramétrico) segundo o preceito bayesiano, é preciso definir uma família paramétrica para as observações $X$ e uma distribuição a priori para $\theta$. É importante destacar que ambas são escolhas que introduzem subjetividade. Para especificar uma priori, traduzimos conhecimento prévio em uma distribuição de probabilidade. Nem sempre, temos uma informação suficiente para tal. Uma maneira usual de contornar essa situação é construir uma sequência de distribuições no espaço de parâmetros e tomar $\pi$ como a distribuição limite. Todavia, ela poderá sofrer com a propriedade que 
$$ \int_{\Omega} \pi(\theta) \, d\theta = + \infty.$$
Nesse caso temos uma **distribuição imprópria** ou generalizada. 

