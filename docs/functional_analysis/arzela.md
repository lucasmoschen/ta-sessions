# Teorema de Arzelà-Ascoli

Considere $(C[a,b], \rho)$ o conjunto das funções contínuas definidas no intervalo $[a,b]$ munido com a métrica 
$$
\rho(f,g) = \max_{x \in [a,b]} |f(x)-g(x)|, f,g \in C[a,b].
$$
Nós provamos que esta tupla é um espaço métrico completo na lista. 
Vamos estender esse espaço para as funções contínuas $f : X \to Y$, em que $(X, d_X)$ e $(Y, d_Y)$ são espaços métricos.
O teorema de Arzelà apresenta um critério de compacidade para subconjunto de $C(X,Y)$.

> Seja $f:X\to Y$ uma função. Ela é dita **função limitada** se $im(f)$ é um conjunto limitado em $Y$, isto é, $\exists M > 0$ tal que $\forall a,b \in X, d_Y(f(a), f(b)) \le M$.

**Teorema:** O conjunto de funções limitadas $f:X \to Y$ sob a métrica $d(f,g) = \sup_{x \in X} d_Y(f(x), g(x))$ é um espaço métrico. 
Além disso, se $Y$ é completo, então o espaço também será. 

- Mostrar que $d$ define uma métrica não é complicado pois ela herda as propriedades de $d_Y$. 
Além disso, ela é limitada, pois $d_Y(f(x), g(x)) \le d(im(f) \cup im(g)), \forall x$.

- A completude vem do fato de que a convergência ponto a ponto ocorre pela completude de $Y$ e do fato de que a convergência é uniforme, dado que o supremo é limitado.

Denotamos $C_b(X,Y)$ o conjunto das funções contínuas limitadas de $X$ a $Y$. Se $Y = \mathbb{C}$, denotamos por $C(X)$.
Se $f_n \to f$ em $C_b(X,Y)$, chamamos de **convergência uniforme**.

- página 80 - Muscat
- página 54 - Kolmogorov