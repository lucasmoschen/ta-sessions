# Introdução a grandes amostras

## Consistência

- Cap 10.1.1 Cassela (467 - 470)
- Cap 8.1 Keener

## Propriedades assintóticas MLE

- KN, Cap 8 e 9;
- SV, Cap 7.3.

### Distribuição assintótica de um estimador eficiente 

Assuma as hipóteses do teorema de Cramér-Rao. Seja $T$ um estimador eficiente para a sua média $m(\theta)$ e $m'(\theta) \neq 0$. Então: 

$$
\frac{[nI(\theta)]^{1/2}}{m'(\theta)}[T - m(\theta)] \overset{d}{\to} N(0,1)
$$

### Distribuição assintótica do MLE

Suponha que obtemos $\hat{\theta}_n$ resolvendo a equação $\lambda_n'(x|\theta) = 0$, isto é, maximizando a log-verossimilhança (MLE). E suponha que $\lambda_n''$ e $\lambda_n'''$ existem e satisfazem certas condições de regularidade. Então 

$$
[nI(\theta)]^{1/2}(\hat{\theta}_n - \theta) \overset{d}{\to} N(0,1)
$$

Como o MLE é não enviesado, então se ele for Eficiente, já sabemos que esse teorema é verdade pelo anterior. (se ele é não enviesado)

