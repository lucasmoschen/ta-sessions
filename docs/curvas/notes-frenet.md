# Fórmulas de Frenet de Curvas Regulares 

Seja $\alpha : I \to \mathbb{R}^3$ uma curva regular, isto é, tal que
$||\alpha'(t)||$ nunca se anula. Por esse motivo, existe uma reparametrização
de $\alpha$ pelo comprimento de arco. Defina 
$$
h : I \to J \\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ t \mapsto h(t) = \int_{t_0}^t ||\alpha'(r)||dr
$$
e $\phi(s) := h^{-1}(s)$. Assim, seja $\beta$ a reparametrização pelo comprimento de arco, 
$$
\beta = \alpha \circ \phi : J \to \mathbb{R}^3 
$$
Observe que $\dfrac{d}{dt}h(c) = ||\alpha'(c)||$ e que $\dfrac{d}{ds}\phi(d) = \dfrac{1}{\frac{dh}{dt}(\phi(d))}$ pelo Teorema da Função Inversa na reta. Diremos que $\phi(s) = t$ e que $h(t) = s$. 

Sejam $T_{\beta}, N_{\beta}, B_{\beta}$ o triedro de Frenet de $\beta$ (que é parametrizada pelo comprimento de arco) e $\kappa_{\beta}$ e $\tau_{\beta}$ a curvatura e a torção, respectivamente. Então, definimos o triedro de Frenet para $\alpha$ da seguinte forma:
$$
T_{\alpha} : I \to \mathbb{R}^3 \\
~~~~~~~~~~~~~~~~~~ t \mapsto T_{\beta}(h(t))
$$
$$
N_{\alpha} : I \to \mathbb{R}^3 \\
~~~~~~~~~~~~~~~~~~ t \mapsto N_{\beta}(h(t))
$$
$$
B_{\alpha} : I \to \mathbb{R}^3 \\
~~~~~~~~~~~~~~~~~~ t \mapsto B_{\beta}(h(t))
$$
$$
\kappa_{\alpha} : I \to \mathbb{R}^3 \\
~~~~~~~~~~~~~~~~~~ t \mapsto \kappa_{\beta}(h(t))
$$
$$
\tau_{\alpha} : I \to \mathbb{R}^3 \\
~~~~~~~~~~~~~~~~~~ t \mapsto \tau_{\beta}(h(t))
$$
Como $h(t) \in J$, tudo está bem definido acima. Nesse caso, vamos provar que $T_{\alpha}(t) = \dfrac{\dot\alpha(t)}{||\dot\alpha(t)||}$. 

Veja que $T_{\alpha}(t) = T_{\beta}(h(t)) = \dot\beta(h(t))$ por definição. Além disso, $\dot\beta(h(t)) = \dfrac{d}{ds}\alpha(\phi(h(t)))$ (lembrando que $s = h(t)$).Pela regra da cadeia, 
$$
\dot\beta(h(t)) = \dot{\alpha}(\phi(h(t)))\dot\phi(h(t)) = \dot\alpha(t)\dot{\phi}(h(t)),
$$
pois $\phi(h(t)) = \phi(s) = t$. Por fim, usando o Teorema da Função Inversa, 
$$
 \dot\alpha(t)\dot{\phi}(h(t)) = \frac{\dot\alpha(t)}{\dot{h}(\phi(h(t)))} = \frac{\dot\alpha(t)}{||\dot{\alpha}(t)||} 
$$
o que prova nosso resultado inicial. Esse texto foi feito para deixar mais claro como fazer o exercício 6 da lista 4 e como calcular os vetores normal e binormal para uma curva regular qualquer. 