# Teste de Hipóteses II 

Nesse notebook veremos:

1. Teste de Hipóteses Simples 
2. Hipótese Alternativa Bilateral 
3. Teste T

## Teste de Hipótese Simples: 

O objetivo é considerar se um vetor de observações vem de uma entre duas observações. Nesse caso o espaço $\Omega$ é formado por dois pontos, e não é um espaço de parâmetros, mas espaço de distribuições, em particular dessas duas distribuições. 

Isto é, vamos assumir que $X = (X_1, ..., X_n)$ vem de $f_0(x)$ ou $f_1(x)$. Assim $\Omega = \{\theta_0, \theta_1\}$ e $\theta = \theta_i$ se os dados tem distribuição $f_i(x), i = 0,1$. 

Vamos denotar:

$
\alpha(\delta) = P(\text{Rejeitar} H_0|\theta = \theta_0) = P(\text{Erro I})
$

$
\beta(\delta) = P(\text{Não rejeitar} H_0|\theta = \theta_1) = P(\text{Erro II})
$

### Teorema 

Seja $\delta^*$ o procedimento de teste que não rejeita $H_0$ se $af_0(x) > bf_1(x)$ e rejeita se $af_0(x) < bf_1(x)$. Então, para todo outro procedimento de teste $\delta$, 
$$
a\alpha(\delta^*) + b\beta(\delta^*) \le a\alpha(\delta) + b\beta(\delta) 
$$

### Corolário

### Lema Nayman-Pearson


```python

```
