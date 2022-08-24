# Testes Uniformemente mais Poderosos

Estamos lidando com um teste de hipóteses com as variáveis aleatórias $X_1, ..., X_n$ de uma distribuição parametrizada em $\theta$ desconhecido. 
$$
H_0: \theta \in \Omega_0
$$
$$
H_1: \theta \in \Omega_1
$$
Assumiremos que $\Omega_1$ não é conjunto unitário. Também suponha que o nível de significância do teste seja $\alpha$, isto é $\pi(\theta|\delta) \le \alpha, \forall \theta \in \Omega_0$. 
Segundo essas condições, queremos encontrar o procedimento de teste $\delta$ que tem a menor probabilidade de erro do tipo II. 

> **Definição:** Uma família de densidades $p_{\theta}(x)$ tem razões de verossimilhanças monótonas se existe uma estatística $T$ tal que se $\theta_1 < \theta_2$, a razão de verossimilhança $p_{\theta_2}(x)/p_{\theta_1}(x)$ é função não decrescente de $T$.

---
``📝`` **Família exponencial**

Considere a família exponencial 
$$
p_{\theta}(x) = h(x) \exp\{\pi(\theta) T(x) - A(\theta)\}.
$$
Assim, 
$$
\log \frac{p_{\theta_2}(x)}{p_{\theta_1}(x)} = T(x) (\pi(\theta_2)  - \pi(\theta_1)) - (A(\theta_2) - A(\theta_1)).
$$
Se $\pi$ é uma função crescente, teremos que essa família astisfaz a propriedade de monotonicidade das razões de verossimilhança, visto que essa razão não descresce monotonicamente com $T(x)$.

---

**Teorema:** Suponha que a família de densidades tenha razões de verossimilhança monótonas. 
Então o teste
$$
\delta^*(x) = \begin{cases}
    1, &T(x) > c, \\
    \gamma, &T(x) = c, \\
    0, &T(x) < c.
\end{cases}
$$
é **uniformemente mais poderoso** ao testar $H_0 : \theta \le \theta_0$ contra $H_1 : \theta > \theta_0$.
As constantes $\gamma$ e $c$ são definidas a fim do teste ter nível $\alpha$.