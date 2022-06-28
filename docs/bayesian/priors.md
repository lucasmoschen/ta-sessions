# Distribuições a priori

A determinação da distribuição a priori para a quantidade de interesse é um ponto-chave da inferência bayesiana e, simultaneamente, é alvo de críticas. 
De forma geral, queremos codificar a informação sobre um parâmetro $\theta$ antes de realizarmos um determinado experimento. 
Dessa forma, a partir de uma informação a priori, queremos definir uma distribuição a priori. 
É claro que raramente conseguimos fazer esse processo de forma exata e única. 
Quando a informação é insuficiente para definir uma distribuição de probabilidade, o estatístico deve colocar informação subjetiva para, então, obter uma priori que faça sentido.
Como a distribuição a priori influencia as inferências a posteriori o tanto quanto se queira (no limite, podemos colocar a massa de probabilidade em um único ponto), análises de robustez e de sensibilidade são essenciais no dia-a-dia bayesiano.

## Determinação de uma priori

Queremos que a priori $\pi$ resuma a informação disponível sobre o fenômeno e a incerteza que temos sobre essa informação, mesmo quando $\theta$ não advém de um processo aleatório.
Usando o conceito de George Box de que [todos os modelos são errados](https://en.wikipedia.org/wiki/All_models_are_wrong), não existe uma priori verdadeira e, portanto, buscamos aproximações para representar $\pi$.

---
``📝`` **Exemplo (Distribuição normal)**

Suponha que observamos $x_1, \dots, x_n \sim N(\theta, 1)$ e assumimos que $\theta \sim N(\mu, \tau)$. A média a posteriori de $\theta$ é dada por 
$$
\mathbb{E}[\theta|x] = \frac{\bar{x}\tau + \mu/n}{\tau + 1/n}. 
$$
Nesse caso, note que estamos fazendo uma média ponderada de $\bar{x}$ e $\mu$ com pesos $\tau$ e $1/n$, respectivamente. Dessa forma, poderíamos pensar que a priori, teríamos virtualmente uma amostra de tamanho $\tau^{-1}$ e média $\mu$. 

---

Podemos construir uma medida de probabilidade para $\theta$ através de uma relação $\preceq$ que ordena o quão provável é um evento definido pela variável aleatória $\theta$, como resumido [aqui](https://lucasmoschen.github.io/files/disciplines/bayesian-statistics/probabilidade-subjetiva-resumo.pdf).

Quando não existe uma informação direta sobre $\theta$, uma alternativa é usar a distribuição marginal de $x$ dada por 
$$m(x) = \int_{\Theta} f(x|\theta) \pi(\theta) \, d\theta.$$
Por exemplo, se $\theta$ é a produção diária média de leite, informação sobre $\theta$ pode ser obtida a partir da informação que já temos sobre o rebanho, o que é informação sobre a marginal de $x$.

### Prioris de entropia máxima

Assuma que temos $\mathbb{E}^{\pi}[g_k(\theta)] = \omega_k$ para $k=1,\dots, K$. Podemos selecionar $\pi$ que satisfaça essas $K$ relações e maximize a entropia, que mede o nível de desordem em um sistema. Se $\Theta$ é finito, temos que 
$$
\mathcal{E}(\pi) = \sum_{\theta_i \in \Theta} \pi(\theta_i) \log(\pi(\theta_i))
$$
é a **entropia** de $\pi$. 
Essa quantidade é uma medida de incerteza dada por $\pi$. 
Dessa forma, estamos minimizando a informação de $\pi$ trazida a priori. 
Sendo $\lambda_k$ o multiplicador de Lagrange associado a $\mathbb{E}^{\pi}[g_k(\theta)] = \omega_k$, temos que a definição da priori é 
$$
\pi^*(\theta_i) \propto \exp\left\{\sum_{k=1}^K \lambda_k g_k(\theta_i)\right\}.
$$
No caso contínuo, as contas se complicam um pouco e precisamos de uma medida de referência $\pi_0$,
que pode ser vista como a distribuição a priori sem restrição de momentos. 
Quando existe uma estrutura de grupo, a medida de Haar invariante à direita é a escolha natural para $\pi_0$. 
Nesse caso, a entropia é definida como
$$
\mathcal{E}(\pi) = \int \log\left(\frac{\pi(\theta)}{\pi_0(\theta)}\right) \, \pi_0(d\theta),
$$
que é a distância de Kullback-Leibler entre $\pi$ e $\pi_0$ e a distribuição a priori que maximiza $\mathcal{E}$ é 
$$
\pi^*(\theta) \propto \exp\left\{\sum_{k=1}^K \lambda_k g_k(\theta_i)\right\}\pi_0(\theta)
$$

### Aproximações paramétricas

A forma mais utilizada é provavelmente essa. Definimos uma família paramétrica para a distribuição a priori e buscamos definir os parâmetros através dos momentos ou quartis da distribuição. 
A base é mais a tratabilidade matemática do que a subjetividade. 
Outro ponto é que distribuições com caudas muito diferentes para $\Theta$ infinito levam a inferências bastante distintas.

## Prioris conjugadas

Prioris conjugadas são baseadas na verossimilhança e, portanto, já definem a família paramétrica da distribuição a priori, restando a definição dos parâmetros. 
Isso limita a informação a priori que deve ser obtida a fim de definir uma distribuição de probabilidade. 
Ela também auxilia na computação, como veremos na definição:

**Família conjugada:** Uma família de distribuições $\mathcal{F}$ sobre $\Theta$ é conjugada para a verossimilhança $f(x|\theta)$ se para toda priori $\pi \in \mathcal{F}$, a posteriori $p(\cdot \mid x) \in \mathcal{F}$. 

Essa família se torna interessante quando ela é a menor possível (é impossível encontrar uma mínima propriamente dita, mas a ideia é que ela tenha dimensão de parâmetros baixa) e parametrizada. Logo, atualizar a informação por $f(x|\theta)$ é equivalente a atualizar os parâmetros da distribuição. 
Nas famílias conjugadas, podemos interpretar os hiperparâmetros como observações passadas virtuais, o que é considerado um ponto positivo.

### Família exponencial e distribuições conjugadas

Seja $\mu$ uma medida $\sigma$-finita em $\mathcal{X}$ e $\Theta$ o espaço dos parâmetros. 
Sejam $C : \mathcal{X} \to \mathbb{R}_+$, $h : \mathcal{X} \to \mathbb{R}_+$, $R : \Theta \to \mathbb{R}^k$ e $T : \mathcal{X} \to \mathbb{R}^k$ funções. A família de distribuições com densidade com respeito a $\mu$
$$
f(x|\theta) = C(\theta) h(x) \exp\{R(\theta) \cdot T(x)\}
$$
é chamada de **família exponencial** de dimensão $k$. Quando $R(\theta) = \theta$ e $T(x) = x$, a família é dita **natural**.

> **Lema de Pitman–Koopman**: Se uma família de distribuições $f(\cdot | \theta)$ é tal que para $n$ suficientemente grande, existe uma estatística suficiente de dimensão constante, ela é exponencial se o suporte não depende de $\theta$ (essa condição final exclui a distribuição $U[-\theta, \theta]$, por exemplo). 

Além disso, para toda amostra de $f$, existe uma estatística suficiente de dimensão constante.

O **espaço natural** de parâmetros é denotado por 
$$
N = \left\{\theta \in \Theta \mid \int_{\mathcal{X}} e^{\theta\cdot x} h(x) \, d\mu(x) < +\infty \right\}.
$$
Ela é regular se $N$ é aberto e mínimo se $dim(N) = dim(C(\mu)) = K$ em que $C(\mu)$ é o menor conjunto convexo fechado que contém o suporte de $\mu$.

Reescreva a densidade como 
$$
f(x|\theta) = h(x) e^{\theta \cdot x - \psi(\theta)},
$$
em que $\psi$ é a **função geradora cumulativa**, pois
$$
\mathbb{E}_{\theta}[X] = \nabla \psi(\theta), \operatorname{Cov}(X_i, X_j) = \psi_{\theta_i \theta_j}(\theta),
$$
supondo $\psi$ de classe $C^2$ e $\theta \in int(N)$.

**Priori conjugada:** Uma família conjugada para $f$ é dada pela densidade
$$
\pi(\theta | \mu, \lambda) = K(\mu, \lambda) e^{\theta\cdot \mu - \lambda \psi(\theta)},
$$
cuja posteriori é dada por $\pi(\theta | \mu + x, \lambda + 1)$. Se $\lambda > 0$ e $\mu/\lambda$ pertence ao interior de $C(\mu)$, $\pi$ define uma distribuição de probabilidade [[Diaconis, Ylvisaker; 1978]](https://statweb.stanford.edu/~cgates/PERSI/papers/conjprior.pdf). Para uma tabela completa, consulte [aqui](https://en.wikipedia.org/wiki/Conjugate_prior#Table_of_conjugate_distributions).

Outro resultado verificado no artigo acima é que a esperança a posteriori de $\theta$ é dada por 
$$
\frac{\mu + n\bar{x}}{\lambda + n}, 
$$
quando $\mu \in \mathcal{X}$.

### Extensões

Considere o seguinte exemplo

---
``📝`` **Exemplo [[Diaconis, Ylvisaker; 1985]](https://statistics.stanford.edu/technical-reports/quantifying-prior-opinion)**

Quando a moeda é girada pela borda e observamos o resultado quando ela cai, temos um viés maior para um lado do que para o outro devido a irregularidades. Seja $x \sim Binomial(n, p)$ o número de caras nesse experimento após $n$ jogadas. 
Como sabemos que existe uma irregularidade, poderíamos pensar em uma priori para $p$ que tivesse uma cara bimodal, dado peso para as duas possibilidades. Isso não é possível com a família conjugada beta. 
Uma forma de fazer isso é, portanto, através de misturas de distribuições beta.

---

Com esse exemplo, podemos ver que misturas de distribuições conjugadas definem uma família conjugada maior que dá maior flexibilidade para o formato de uma distribuição a priori. 
Além disso, podemos verificar que a mistura de distribuições pode aproximar qualquer distribuição a priori sob a [distância de Prokhorov](https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Prokhorov_metric).


## Distribuições a priori não informativas

Quando pouca (ou nenhuma) informação sobre $\theta$ está disponível, é difícil justificar a escolha com base subjetiva.
Nesse caso, uma alternativa é usar a distribuição dos dados para, a partir dela, definir uma distribuição a priori.
Chamamos essas prioris de **não informativas**. 
Mas devemos que lembrar que uma distribuição ser não informativa não significa que ignorância total está sendo representada probabilisticamente.
Elas podem ser usadas como prioris de referência, todavia.

### Priori de Laplace

Laplace sugeriu construir a distribuição a priori baseado no **Princípio da Razão Insuficiente**, em que eventos elementares são equiprováveis. 
Nesse caso, adotamos a priori uniforme.
Se o espaço de parâmetros não for compacto, isso nos leva à uma distribuição imprópria, por consequência. 
Além disso, se fizermos uma transformação biunívoca $\eta = g(\theta)$, a priori para $\eta$ não será uniforme pela Fórmula da Mudança de Variáveis, isto é, a informação sobre $\theta$ não foi criada a partir dessa transformação, mas a distribuição não é uniforme.

### Prioris invariantes

O conceito de invariância é bem profundo na matemática e, com base nesse conceito, podemos construir distribuições invariantes a reparametrização. Por exemplo, a família $f(x - \theta)$ é invariante à translação, isto é, $y = x - x_0$ tem distribuição da mesma família para todo $x_0$, $f(x - (\theta - x_0))$. Chamamos $\theta$ de *parâmetro de locação*.

### Priori de Jeffreys

A Priori de Jeffreys é baseada na [Informação de Fisher](https://lucasmoschen.github.io/ta-sessions/infestatistica_BSc/FisherInformation/FisherInformation/) dada pela expressão:
$$
I(\theta) = \mathbb{E}_{\theta}\left[\left(\frac{\partial \log f(X|\theta)}{\partial \theta}\right)^2\right],
$$
no caso unidimensional. A distribuição de Jeffreys é definida por 
$$
\pi^*(\theta) \propto I^{1/2}(\theta).
$$
Note que $I(\theta) = I(h(\theta))(h'(\theta))^2$ se $h$ é uma transformação biunívoca. 
Nesse caso, $\pi^*(h(\theta)) \propto I^{1/2}(h(\theta)) = I^{1/2}(\theta)/|h'(\theta)|$, exatamente o que esperávamos usando a mudança de variáveis. 
Logo, essa priori é invariante à reparametrização.
Além disso, $I(\theta)$ é uma medida da quantidade de informação trazida pelo modelo sobre $\theta$.
Na prática, prioris de Jeffreys são usualmente impróprias.
No caso multidimensional, 
$$
\pi^*(\theta) \propto [det(I(\theta))]^{1/2}
$$
é a priori de Jeffreys. 
Todavia, usar esse procedimento para construir prioris leva a paradoxos e incoerências.

**Observação:** A priori de Jeffreys para família de locação é constante.

---
``📝`` **Exemplo (caso normal)**

Suponha que $x \sim N(\mu, \sigma^2)$ com $\theta = (\mu, \sigma^2)$ desconhecido. Nesse caso, podemos calcular que 
$$
I(\theta) = \begin{bmatrix}
1/\sigma^2 & 0 \\ 0 & 2/\sigma^2
\end{bmatrix},
$$
e, portanto, $\pi(\theta) \propto 1/\sigma^2$. Se assumirmos que $\mu$ e $\sigma$ são independentes a priori, todavia, teremos que $\pi(\mu, \sigma) = 1/\sigma$ como priori não informativa e também a medida de Haar invariante ao modelo locação-scala.

---

Essa priori, todavia, não obedece ao Princípio da Verossimilhança, dado que a informação de Fisher de dois modelos diferentes podem ser diferentes, mesmo que as verossimilhanças sejam proporcionais. [Confira essa resposta.](https://stats.stackexchange.com/questions/194448/do-you-have-to-adhere-to-the-likelihood-principle-to-be-a-bayesian).

### Prioris de referência 

[[Bernardo; 1979]](https://people.eecs.berkeley.edu/~jordan/sail/readings/bernardo-1979.pdf) propôs um procedimento para construir prioris não informativas, ou como ele destaca, um procedimento para obter prioris de forma que a posteriori aproxime aquela que adviria de uma informação a priori vaga.
Seja $x \sim f(x | \theta)$ e $\theta = (\theta_1, \theta_2)$, em que $\theta_1$ é o parâmetro de interesse. A priori de referência primeiro define $\pi(\theta_2 | \theta_1)$ usando a priori de Jeffreys através $f(x|\theta)$ quando $\theta_1$ é fixado. 
Depois, ele calcula 
$$
\tilde{f}(x|\theta_1) = \int f(x|\theta) \pi(\theta_2|\theta_1) \, d\theta_2
$$
e calcula a priori de Jeffreys para $\theta_1$ baseando-se em $\tilde{f}$. 
Assim, o processo elimina os parâmetros que não são de interesse.
O algoritmo se generaliza para mais camadas de parâmetros.

### Prioris matching 

Uma forma, no mínimo curiosa, de construir prioris não informativas é baseada em propriedades frequentistas, isto é, em que propriedades funcionem em média considerando $x$.
Seja $C_x$ um conjunto de confiança a posteriori nível $\alpha$, isto é, 
$$
p(g(\theta) \in C_x | x) = 1-\alpha.
$$
Esse conjunto define tem cobertura frequentista $\Pr_{\theta}(g(\theta) \in C_x)$, em que nesse caso $C_x$ é a variável aleatória. 
Em geral, quando $C_x = (-\infty, k_{\alpha}(x))$, então $\Pr_{\theta}(\theta \le k_{\alpha}(x)) = 1 - \alpha + O(n^{-1/2})$. No caso da priori de Jeffreys, isso se torna $O(n^{-1})$ que decresce mais rapidamente. 
Para mais detalhes, [consulte esse link](https://projecteuclid.org/ebook/Download?urlid=10.1214/lnms/1215091929&isFullBook=false).

## Pontuações finais

- Informação a priori não consegue ser traduzida em uma distribuição de probabilidade única. Além disso, ela é bastante complicada, principalmente em se tratando de definir caudas de forma subjetiva. 

- Se alguma informação é disponível, usá-la favorece inferências quando comparado a abordagens não informativas.

- Análise de sensibilidade é um tópico importante, que verifica a influência da escolha da priori nas inferências. Para essa análise, assumimos que a priori $\pi$ mora em alguma classe de distribuições, que mensura a incerteza sobre $\pi$. Essas classes podem ser: (i) prioris conjugadas: convenientes matematicamente; (ii) momentos definidos: a classe de distribuições que tem determinados momentos limitados impõe condições fortes sobre a cauda e inclui muitas distribuições impossíveis; (iii) classes de vizinhança: pondera por um $\epsilon$ uma outra classe de distribuições $Q$ a ser escolhida; entre outras.