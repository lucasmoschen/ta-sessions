# Modelo estatístico

Uma descrição baseada no livro de Schervish de modelo paramétrico é dada [nesse link](/bayesian/intro). 
Nesse link, também é possível obter uma introdução bem geral à Estatística do ponto de vista do livro [The Bayesian Choice](https://link.springer.com/book/10.1007/0-387-71599-1) de Christian P. Robert. 
Uma obra de arte em forma de artigo sobre o tema é discorrido no artigo [What is a statistical model?](https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2Faos%2F1035844977&referringURL=https%3A%2F%2Fgithub.com%2Fmaxbiostat%2FStatistical_Inference_MSc&isResultClick=False) de Peter McCullagh.

De forma geral, um modelo estatístico é um conjunto de distribuições de probabilidade em um espaço amostral $\mathcal{X}$. 
Um **modelo estatístico paramétrico** é um conjunto de parâmetros $\Theta$ junto de uma função $P : \Theta \to \mathcal{F}(\mathcal{X})$ que para cada parâmetro $\theta \in \Theta$, define uma distribuição de probabilidade $P(\theta) = P_\theta$ definida em $\mathcal{X}$. 
No caso de um modelo bayesiano, exigimos uma distribuição de probabilidade em $\Theta$, a **distribuição a priori**.

Estamos interessados, em particular, em **modelos identificáveis**, isto é, quando uma família de distribuições de probabilidade satisfaz: $P_{\theta} = P_{\theta '} \implies \theta = \theta '$. 
Em outras palavras, a função $P$ é injetiva.

## Função de verossimilhança

Denote $f(\boldsymbol{x}|\theta)$ a densidade da distribuição de $\boldsymbol{X} = (X_1, \dots, X_n)$ com respeito à medida de Lebesgue em $\mathbb{R}^n$, pertence a uma família de distribuições parametrizada por $\theta$.
Dada a observação $\boldsymbol{X} = \boldsymbol{x}$, a **função de verossimilhança** é a função 
$$
L : \Theta \to \mathbb{R}_+
$$
definida como $L(\theta | \boldsymbol{x}) = f(\boldsymbol{x}|\theta)$. 
Note que se $L(\theta_1 | \boldsymbol{x}) > L(\theta_2 | \boldsymbol{x})$, queremos dizer que é mais provável que $\theta = \theta_1$ do que $\theta = \theta_2$ quando observamos $\boldsymbol{x}$.


