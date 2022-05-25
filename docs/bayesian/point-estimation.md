# Estimação pontual em inferência bayesiana

Inferência bayesiana sobre um parâmetro de interesse $\theta$ após observar os dados nos dá uma distribuição de probabilidade $p(\theta | x)$, a distribuição a posteriori.
Resumir essa informação pontualmente em um estimador é de interesse do agente tomador de decisão. 
Por exemplo, se a quantidade de interesse é $h(\theta)$, a média a posteriori de $h(\theta)$ sob a distribuição a posteriori $p(\cdot|x)$ é um possível estimador.

Sem definir uma perda, não há como selecionar um melhor estimador. 
Um possível estimador é o **máximo a posteriori** (MAP) que é definido como a moda da distribuição a posteriori, isto é, o valor de $\theta$ cuja densidade é a mais alta.
Se $\theta \in \{0,1\}$, a perda associada a esse estimador é a 0-1. 
Para o caso contínuo, defina $L_{\epsilon}(\theta, d) = 1_{\|\theta - d\| \ge \epsilon}$. 
O estimador que minimizar $L_{\epsilon}$ quando $\epsilon \to 0$ é o MAP.

Como maximizar $p(\theta | x)$ em $\theta$ é equivalente a maximizar $\log l(\theta|x) + \log\pi(\theta)$, o MAP pode ser visto como um estimador de máxima verossimilhança com penalização.
Além do mais, sob algumas condições de regularidade, as propriedades assintóticas do MLE clássico são preservadas, o que faz sentido dado que quando $n$ aumenta, a informação da verossimilhança é predominante se comparada com a informação da priori, que é fixa.

Quando atribuímos um estimador $\delta^{\pi}(x)$ para $h(\theta)$, também podemos medir sua **precisão** através de alguma esperança, por exemplo o erro quadrado a posteriori
$$
\mathbb{E}^{p}[(\delta^{\pi}(x) - h(\theta))^2 | x],
$$
que é, em particular, a variância sob $p$ de $h(\theta)$ condicionada em $x$ quando o estimador é a média a posteriori de $h(\theta)$.

## Teoria da decisão em inferência bayesiana

Lembramos que dada uma perda $L(\theta, \delta)$ e uma distribuição a priori $\pi$, o estimador de Bayes $\delta^{\pi}(x)$ é solução de 
$$
\min \mathbb{E}^p[L(\theta, \delta)|x]
$$

**Lema:** Seja $f(x|\theta) = h(x)e^{\theta\cdot x - \psi(\theta)}$ uma distribuição da família exponencial. 
Assim, a média a posteriori de $\theta$ é dada por
$$
\delta^{\pi}(x) = \nabla \log m(x) - \nabla \log h(x),
$$
em que $m(x)$ é a distribuição marginal do dado. 
Esse resultado é como se fosse o dual da relação dos momentos de $f$ com $\psi$.

Dada uma perda $L(\theta, \delta)$ e o estimador de Bayes associado $\delta^{\pi}(x)$, podemos estimar a performance dele através da estimativa da perda $L(\theta, \delta^{\pi}(x))$ através de 
$$
\tilde{L}(\theta,  \delta^{\pi}, \gamma) = [\gamma(x) - L(\theta, \delta^{\pi}(x))]^2.
$$
O estimador de Bayes para $L(\theta, \delta^{\pi}(x))$ segundo essa perda é 
$$
\gamma^{\pi}(x) = \mathbb{E}[L(\theta, \delta^{\pi}(x))|x].
$$
Quando $L$ é a perda quadrática, note que $\gamma^{\pi}(x) = \operatorname{Var}^{\pi}(\theta | x)$.