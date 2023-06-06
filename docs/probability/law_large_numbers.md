# Lei dos grandes números 

Considere $X$ uma variável aleatória e um experimento que seja repetido seguidas vezes para se obter valores característicos de $X$, que são os valores **observados**.
A lei dos grandes números afirma que a média aritmética dos $n$ valores observados converge para a média real dada pelo valor esperado de $X$ quando $n$ vai para o infinito.

Aqui, quando temos $n$ experimentos, o espaço amostral é 
$$
\Omega_n = \{(w_1, \dots, w_n) > w_i \in \Omega_0, i=1,\dots,n\},
$$
que aumenta com $n$.
Em particular, consideramos $\Omega = \Omega_0^{\infty}$.
Assim estamos observando em um sequencial de experimentos:
$$
X(w_0), x(w_1), X(w_2), \dots.
$$
Denota-se $X_n(w) := X(w_n)$.
Como os experimentos são independentes e todos advém de $X$ e são identicamente distribuídos, dizemos que $X_1, \dots, X_n$ são i.i.d. (independentes e identicamente distribuídos).

## Convergências

**Definição:** A sequência $\{Y_n\}$ converge para a variável aleatória $Y$ em **probabilidade** se, para todo $\epsilon > 0, 
$$
P(|Y_n - Y| > \epsilon) \to 0, n \to \infty.
$$
Dizemos que $Y_n \overset{P}{\to} Y$.

**Definição:** A sequência $\{Y_n\}$ converge quase certamente (q.c.) para a variável aleatória $Y$ se
$$
P(\{\omega : Y_n(\omega) \to Y(\omega) \}) = 1.
$$
Dizemos que $Y_n \overset{q.c.}{\to} Y$.

A relação é que $Y_n \overset{q.c.}{\to} Y \implies Y_n \overset{P}{\to} Y$, mas não o contrário.

## Lei dos grandes números

Sejam $X_1, X_2, \dots$ variáveis aleatórias integráveis e defina $S_n  = X_1 + \cdots + X_n$.
A **Lei fraca dos grandes números** diz que 
$$
\frac{S_n - E[S_n]}{n} \overset{P}{\to} 0.
$$
Se essa convergência é quase certamente, temos a **lei forte dos grandes números**.

O resultado de **Chebyshev** pede que as variáveis $X_1, X_2, \dots$ sejam 2 a 2 independentes com variância finita e uniformemente limitadas, isto é, a variância é uniformemente limitada.

O resultado de **Khintchin** não pede unif. limitada, mas pede integrabilidade e iid.

## Sequências de eventos

Sejam $A_1, A_2, \dots \subseteq \Omega$.
Assim
$$
\lim\sup_{n \to \infty} A_n = \cap_{n=1}^{\infty} \cup_{k=n}^{\infty} A_k,
$$
$$
\lim\inf_{n \to \infty} A_n = \cup_{n=1}^{\infty} \cap_{k=n}^{\infty} A_k.
$$
Dizemos que $\lim\sup A_n$ é a **ocorrência de um número infinito dos $A_n$**, enquanto $\lim\sup A_n$ é a **ocorrência para $n$ suficientemente grande**.

Se $\lim\sup A_n = \lim\inf A_n$, o limite existe e $A = \lim A_n$.
Nesse caso $P(A_n) \to P(A)$.

**Borel-Cantelli:** Sejam $A_1, A_2,\cdots$ eventos aleatórios, tal que 

(a) Se $\sum_{n=1} P(A_n) < \infty$, então $P(\lim\sup A_n) = 0$.
(B) Se $\sum_{n=1} P(A_n) = \infty$ e $A_n$ são independentes, então $P(\lim\sup A_n) = 1$.