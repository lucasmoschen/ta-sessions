# Testes e regiões de confiança

Com a abordagem bayesiana, podemos fazer afirmações do tipo $\pi(\theta \in \Theta_0 | x)$, o que é difere da proposta frequentista, já que lá o parâmetro é fixo, apesar de desconhecido. 
Alguns bayesianos acreditam que o teste, em especial o teste com hipótese nula pontual, não deveria ser realizado por diversos motivos: representação redutiva do modelo; priori modificada de forma não natural para representar a questão pontual; falta de estrutura baseada em teoria da decisão; impossibilidade do uso de prioris impróprias.

## Uma primeira abordagem

Considere um modelo $f(x|\theta)$ com $\theta \in \Theta$. 
Queremos verificar $H_0 : \theta \in \Theta_0$ com $\Theta_0 \subseteq \Theta$ sendo um subconjunto de interesse.
Chamamos $H_0$ de **hipótese nula**. 
Em contrapartida, temos a **hipótese alternativa** $H_1 : \theta \in \Theta_1$ com $\Theta_0 \cap \Theta_1 = \emptyset$ e $\theta$ pertencendo a um dos dois conjuntos.

A perda proposta por Neyman e Pearson é 
$$
L(\theta, \varphi) = \begin{cases}
    1 &\text{se } \varphi \neq 1_{\Theta_0}(\theta), \\
    0 &\text{c.c.}
\end{cases}
$$
Para essa perda, o estimador de Bayes é 
$$
\varphi^{\pi}(x) = \begin{cases}
    1 &\text{se } \Pr(\theta \in \Theta_0 | x) > \Pr(\theta \in \Theta_1 | x), \\
    0 &\text{c.c.}
\end{cases}
$$
Podemos generalizar essa perda para
$$
L(\theta, \varphi) = \begin{cases}
    0 &\text{se } \varphi = 1_{\Theta_0}(\theta), \\
    a_0 &\text{se } \theta \in \Theta_0 \text{ e } \varphi = 0, \\
    a_1 &\text{se } \theta \in \Theta_1 \text{ e } \varphi = 1, 
\end{cases}
$$
cujo estimador de Bayes é $\varphi^{\pi}(x) = 1$ se $\Pr(\theta \in \Theta_0 | x) > a_1/(a_0 + a_1)$, sendo essa fração o **level de aceitação**.

### Fator de Bayes

Definimos o fator de Bayes como a razão das razões da posteriori e da priori:
$$
B_{01}^{\pi}(x) = \frac{\Pr(\theta \in \Theta_0 | x)}{\Pr(\theta \in \Theta_1 | x)}\Big /\frac{\Pr(\theta \in \Theta_0)}{\Pr(\theta \in \Theta_1)} = \frac{\int_{\Theta_0} f(x|\theta)\pi_0(\theta) \, d\theta}{\int_{\Theta_1} f(x|\theta)\pi_1(\theta) \, d\theta},
$$
que avalia a modificação das chances de $\Theta_0$ contra $\Theta_1$. 
Observe que $\pi_i$ é a distribuição a priori sob $H_i$.

Jeffreys desenvolveu uma escala (fora da uma configuração baseada em teoria da decisão) para avaliar a evidência trazida por $x$ contra $H_0$, considerando o valor $\log_{10}(B_{10}^{\pi})$: 
$$0 < \text{ pobre } < 0.5 < \text{ substancial } < 1 < \text{ forte } < 2 < \text{ decisiva } < +\infty.$$

---
``📝`` **Exemplo (Basquete)**

Um jogador de basquete tem "mão quente" quando tem bons e maus dias, ao invés de uma probabilidade fixa de vencer em um lançamento.
O modelo base é $H_0: y_i \sim B(n_i, p)$ para cada jogo $i=1,\dots, G$ ($p$ é fixo). 
A Alternativa é que $p$ varia com o dia.
Considere a priori $p_i \sim Beta(\xi/\omega, (1-\xi)/\omega)$, de forma que $\xi = \mathbb{E}[p_i|\xi] \sim Unif(0,1)$. 
Isto é, estamos fixando as médias das jogadas dos dias e afirmando que alguns dias teremos $p_i > \xi$ e outros $p_i < \xi$, é claro com alguma probabilidade. 
Além do mais, consideramos $p \sim Unif(0,1)$. 
O fator de Bayes é 
$$
B_{10} = \frac{\int_0^1 \left\{\prod_{i=1}^G \int_0^1 p_i^{y_i}(1-p_i)^{n_i-y_i}p_i^{\alpha-1}(1-p_i)^{\beta-1} \, dp_i \right\}\left(\Gamma(1/\omega)/\Gamma(\xi/\omega)\Gamma((1-\xi)/\omega)\right)^G \, d\xi}{\int_0^1 p^{\sum y_i}(1-p)^{\sum (n_i-y_i)} \, dp}
$$

No paper [Kass, Raftery (1995)](https://sites.stat.washington.edu/raftery/Research/PDF/kass1995.pdf), verificou-se que para $\omega = 0.005$, temos $B_{10} = 0.16$, que dá baixa evidência a favor de $H_1$, isto é, que existem bons e maus dias. Escolhemos $\omega$ olhando para $Var(p_i | \xi) = \xi(1-\xi)/(1+\omega^{-1}) \implies \omega^{-1} = \xi(1-\xi)/Var(p_i) - 1.$

---

Note que se $H_0$ for pontual, não conseguimos usar o Fator de Bayes. Para esses casos, precisamos definir 
$$
\pi(\theta) = \Pr(\theta \in \Theta_0) \pi_{0}(\theta) + \Pr(\theta \in \Theta_1) \pi_{1}(\theta) = \varrho_0 \pi_0(\theta) + \varrho_1 \pi_1(\theta).
$$
Apesar de hipóteses pontuais serem problemáticas, elas têm muita utilidade na prática. 

Assim, teremos a priori $\pi(\theta) = \varrho_0 1_{\theta = \theta_0} + (1-\varrho_0)g_1(\theta)$ com posteriori
$$
\pi(\Theta_0 | x) = \frac{f(x|\theta_0) \varrho_0}{f(x|\theta_0\varrho_0 + (1-\varrho_0)m_1(x))},
$$
em que $m_1$ é a marginal dos dados sob $H_1$. Em particular, o Fator de Bayes é 
$$
B_{01}^{\pi}(x) = \frac{f(x|\theta_0)}{m_1(x)},
$$
levando à relação
$$
\pi(\Theta_0 | x) = \left[1 + \frac{1-\varrho_0}{\varrho_0} \frac{1}{B_{01}(x)}\right]^{-1}.
$$

---
``📝`` **Exemplo (Distribuição normal)**

Considere $x \sim \operatorname{Normal}(\theta, 1)$ e $H_0: \theta = 0$. 
Se usarmos a priori imprópria $\pi(\theta) = \frac{1}{2}1_{\theta = 0} + \frac{1}{2}$, teremos que a posteriori de $H_0$ será 
$$
\pi(\theta = 0 | x) = \frac{e^{-x^2/2}}{e^{-x^2/2} + \int e^{-(x-\theta)^2/2} \, d\theta} = \frac{1}{1 + \sqrt{2\pi}e^{x^2/2}} \le 0.285,
$$
isto é, a posteriori é limitada superiormente por um valor baixo. Fenômeno parecido acontece quando $\Theta_0$ é um conjunto compacto. 

Uma questão interessante é que para os níveis tradicionais, que ocorrem quando $x = 1.65, 1.96$ e $2.58$ (respectivamente níveis $0.1, 0.05, 0.01$), a posteriori de $H_0$ é próxima a esses valores (quando a priori é a medida de Lebesgue).

Em particular, quando $H_0 : \theta \le 0$ para $\pi(\theta) = 1$, temos que 
$$
\pi(\theta \le 0 | x) = \Phi(-x),
$$
que é o **p-valor** desse mesmo teste.

---

## Comparação com a abordagem clássica

### Testes UMP

### Prioris menos favoráveis

### p-valores

### Respostas bayesianas menos favoráveis

### Caso unilateral

## Uma segunda abordagem

## Regiões de confiança

### Intervalos de credibilidade

### Intervalos de confiança clássicos

### Avaliação baseada em teoria da decisão