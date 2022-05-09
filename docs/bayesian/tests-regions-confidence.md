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

Jeffreys desenvolveu uma escala fora da uma configuração baseada em teoria da decisão para avaliar a evidência trazida por $x$ contra $H_0$, considerando o valor $\log_{10}(B_{10}^{\pi})$: 
$$0 < \text{ pobre } < 0.5 < \text{ substancial } < 1 < \text{ forte } < 2 < \text{ decisiva } < +\infty$$