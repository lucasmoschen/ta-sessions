# Teorema de Arzelà-Ascoli

Considere $(C[a,b], \rho)$ o conjunto das funções contínuas definidas no intervalo $[a,b]$ munido com a métrica 
$$
\rho(f,g) = \max_{x \in [a,b]} |f(x)-g(x)|, f,g \in C[a,b].
$$
Nós provamos que esta tupla é um espaço métrico completo na lista. 
Vamos estender esse espaço para as funções contínuas $f : X \to Y$, em que $(X, d_X)$ e $(Y, d_Y)$ são espaços métricos.
O teorema de Arzelà apresenta um critério de compacidade para subconjuntos de $C(X,Y)$.

> Seja $f:X\to Y$ uma função. Ela é dita **função limitada** se $im(f)$ é um conjunto limitado em $Y$, isto é, $\exists M > 0$ tal que $\forall a,b \in X, d_Y(f(a), f(b)) \le M$.

**Teorema:** O conjunto de funções limitadas $f:X \to Y$ sob a métrica $d(f,g) = \sup_{x \in X} d_Y(f(x), g(x))$ é um espaço métrico. 
Além disso, se $Y$ é completo, então o espaço também será. 

- Mostrar que $d$ define uma métrica não é complicado pois ela herda as propriedades de $d_Y$. 
Além disso, ela é limitada, pois $d_Y(f(x), g(x)) \le \operatorname{diam}(im(f) \cup im(g)), \forall x$.

- A completude vem do fato de que a convergência ponto a ponto ocorre pela completude de $Y$ e do fato de que a convergência é uniforme, dado que se o supremo é limitado e, todo ponto é.

Denotamos $C_b(X,Y)$ o conjunto das funções contínuas limitadas de $X$ a $Y$. Se $Y = \mathbb{C}$, denotamos por $C(X)$.
Se $f_n \to f$ em $C_b(X,Y)$, chamamos de **convergência uniforme**.

**Teorema (Stone-Weierstra**$\beta$**):** Os polinôomios (em $z$ e $\bar{z}$) são densos em $C(K)$ quando $K \subseteq \mathbb{C}$ é compacto.

---
A demonstração dada no livro do Muscat consiste em cinco etapas:

**(I)** Existe uma sequência de polinômios que aproxima $|x|$ em $x \in [-1,1]$. Defina $q_{n+1}(x) = q_n(x) + (x^2 - q_n(x)^2)$ e $q_0(x) = 0$. Primeiro mostra-se a convergência ponto a ponto, depois a uniforme.

**(II)** Seja $f \in C(K, \mathbb{R})$ com $c = \max_{x \in K} |f(x)| > 0$. Então $|f/c|$ pode ser aproximado por $q_n \circ f/c$. 
Além do mais, se $p_n \to f$, então $cq_n \circ (p_n/c) \to |f|$.

**(III)** Se $f$ e $g$ podem ser aproximados por polinômios, então $f+g$ e $f-g$ também podem. Portanto $|f-g|$, $\max\{f,g\}$ e $\min\{f,g\}$ também podem ser aproximados.

**(IV)** Polinômios reais são densos em $C(K, \mathbb{R})$. Para isso, tome uma função $f \in C(K, \mathbb{R})$ e $z \neq w$. Seja $p_{w,z}$ a a reta que passa por $f(w)$ e $f(z)$ e defina $U_{z,w}$ como o conjunto dos pontos $a \in K$ que satisfazem $p_{w,z}(a) < f(a) + \epsilon$, claramente aberto e não-vazio, cuja união sobre $w \neq z$ cobre $K$ (que é compacto e, portanto, admite subcobertura finita). Assim $g_{z} := \min\{p_{z,w_1}, \dots, p_{z,w_M}\} < f + \epsilon$ pode ser aproximada por polinômios ($w_1, \dots, w_M$ é a subcobertura finita). 
Faz-se o mesmo com os conjuntos $V_z = \{a \in K : g_z(a) > f(a) - \epsilon\}$. 

**(V)** Para $f \in C(K)$, basta escrever $f = u + iv$, em que $u$ e $v$ tem imagem nos reais.

---

> Um conjunto $F \subseteq C(X,Y)$ é **equicontínuo** se para todo $\epsilon > 0$, existe $\delta > 0$ tal que para toda função $f \in F$, se $x, x' \in X$ satisfazem $d_X(x,x') < \delta$, então $d(f(x), f(x')) < \epsilon$.  

Com isso, um conjunto desses contém funções uniformemente contínuas e, além disso, o valor de $\delta$ é selecionado independente da função escolhida.

**Teorema de Arzelà-Ascoli:** Seja $K$ compacto. Então $F \subseteq C(K,Y)$ é totalmente limitado se, e somente se, $F K = \{f(x) : f \in F, x \in K\}$ é totalmente limitado em $Y$ e $F$ é equicontínuo.

Uma versão um pouco simplificada que pode ser encontrada na literatura:

Uma condição suficiente e necessária para que $F \subseteq C([a,b], \mathbb{R})$ seja compacto em $C[a,b]$ é que $F$ seja equicontínuo e *uniformemente limitado*, isto é, existe um $M$ tal que $|f(x)| < M$ para todo $x \in [a,b]$ e para todo $f \in F$.