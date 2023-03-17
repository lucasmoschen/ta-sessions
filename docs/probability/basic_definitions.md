# Conceitos introdutórios

Chamamos de **espaço amostral** $\Omega$ o conjunto de todos os possíveis resultados de possíveis de um experimento.
Por exemplo, os resultados possíveis de uma jogada de dado de 6 lados é $\Omega = \{1,2,3,4,5,6\}$.
Já os **eventos** são os subconjuntos de $\Omega$.
Em geral, eles são uma afirmação do tipo *observa-se algo*.
Por definição, $\Omega$ é o evento *certo*, enquanto $\emptyset$ é o evento *impossível*.

Algumas notações clássicas para $A,B$ eventos:

- $A \cup B$: evento $A$ ou $B$;
- $A \cap B$: evento $A$ e $B$;
- $A^c$: evento não $A$;
- $A \cap B$: a ocorrência do evento $A$ implica a ocorrência de $B$;
- $A \cap B = \emptyset$: os eventos são **mutuamente exclusivos**.

A próxima questão é como atribuir probabilidades ao eventos, isto é, como definir uma função que a cada evento associe um valor numérico entre $0$ e $1$.
Um evento $A$ ao qual se atribui uma probabilidade é chamado de **evento aleatório**.
A Teoria da Medida é a ferramenta para formalizar esse conceito. 
Uma **álgebra** $\mathbb{A}$ de subconjuntos de $\Omega$ é um conjunto de subconjuntos de $\Omega$ que satisfaz as seguintes propriedades:

1. $\Omega \in \mathbb{A}$;
2. Se $A \in \mathbb{A}$, então $A^c \in \mathbb{A}$;
3. Se $A,B \in \mathbb{A}$, então $A \cup B \in \mathbb{A}$.

Com essas propriedades temos que, por consequência, $\emptyset \in \mathbb{A}$ e união e interseção finitas de conjuntos de $\mathbb{A}$ pertence a $\mathbb{A}$ (aplicação do princípio da indução e [lei de De Morgan](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)).

Estendemos uma álgebra para uma $\sigma$**-álgebra** com a seguinte propriedade:

3. 1 Se $A_1, A_2, A_3, \dots \in \mathbb{A}$, então $\cup_{i=1}^{\infty} A_i \in \mathbb{A}$.

Vale lembrar que esses são os axiomas que definem os eventos a que vamos atribuir probabilidades.
Além do mais, o Teorema da Extensão, que pode ser encontrado no primeiro livro [aqui](https://lucasmoschen.github.io/ta-sessions/probability/info/#sugestoes-adicionais), permite que primeiro definamos probabilidade em uma álgebra e isso automaticamente define na $\sigma$-álgebra correspondente de forma única. 
Probabilidade, no sentido que conhecemos hoje, tem uma construção axiomática e é dada por Kolmogorov:

1. $P(A) \ge 0$;
2. $P(\Sigma) = 1$;
3. Se $A_1, A_2, A_3. \dots \in \mathbb{A}$ são disjuntos, então 
$$
P\left(\cup_{i=1}^{\infty} A_n \right) = \sum_{i=1}^{\infty} P(A_n).
$$

O terceiro axioma é nomeado de propriedade $\sigma$-aditividade da probabilidade.
Alguns trabalhos teóricos substituem a união infinita de conjuntos pela finita, obtendo a aditividade como axioma apenas e, portanto, restringindo um pouco a sua aplicabilidade. 
Com as três propriedades acima, temos uma **medida de probabilidade**.

---
``📝`` **Exemplo de $\sigma$-álgebra**

Considere o experimento de selecionar um ponto em $[0,1]$ ao acaso.
Seja $\mathbb{A}$ a $\sigma$-álgebra formada por todos os subconjuntos cujo comprimento esteja definido.
Iniciamos com $\mathbb{A}_0 = \{A \subset [0,1] : A \text{ é união finita de intervalos}\}$. 
É fácil ver que $\mathbb{A}_0$ é álgebra, mas não é $\sigma$-álgebra.
Por exemplo, o conjunto 
$$
B = \cup_{i=0}^{\infty} \left(\frac{2^i-1}{2^i}, \frac{2^{i+1}-1}{2^{i+1}}\right).
$$
Esse conjunto não está em $\mathbb{A}_0$, mas podemos calcular seu comprimento usando séries. Assim,
$$
P(B) = 1
$$
é o comprimento de $B$.
Outro conjunto que não está em $\mathbb{A}_0$ são os dos números racionais, ou dos números irracionais.
De fato, temos que $P(\mathbb{Q} \cap [0,1]) = 0$ é o comprimento desse conjunto, pois temos uma união enumerável de intervalos degenerados $\{r_n\}$, que tem comprimento $0$.

Nesse caso, para os reais, usamos a $\sigma$-álgebra de Borel, cujos elementos são os **borelianos**.
Ele é a menor $\sigma$-álgebra que contém todos os intervalos abertos. 
Assim, uniões e intersecções enumeráveis e seus complementares estarão também na $\sigma$-álgebra.

---

---
``📝`` **Um conjunto sem probabilidade**

Considere o experimento anterior e tome $X \sim \operatorname{Unif}[0,1]$.
Podemos supor que 
$$
P([a,b]) = P((a,b)) = P((a,b]) = P([a,b)) = b - a,
$$
para $0 \le a \le b \le 1$.

Para manter a uniformidade, podemos supor que 
$$
P(A) = P(A \oplus r),
$$
em que $A \oplus r = \{a + r; a \in A, a+r \le 1\} \cup \{a+r-1; a \in A, a + r > 1\}$.

**Proposição:** Não existe uma definição de $P(A)$ para todos os subconjuntos $A \subseteq [0,1]$ que satisfaçam o conceito de probabilidade e a translação acima mencionada.

O resultado dessa proposição é por contradição é usa o famoso [Axioma da Escolha](https://en.wikipedia.org/wiki/Axiom_of_choice).
Defina a relação de equivalência em $[0,1]$ por $x \sim y$ se $y- x$ é racional.
Isso relação particiona o intervalo $[0,1]$ em subconjuntos disjuntos, visto que, se $x \sim y$ e $y \sim z$, então $x \sim z$ e $y \sim x$.
Defina $H$ como um conjunto que contenha exatamente um elemento de cada classe de equivalência, o que pode ser obtido pelo Axioma da Escolha.
Assuma que $0 \not \in H$ e, caso esteja, troque-o por $1/2$, visto que $0 \sim 1/2$.
Com isso, note que 
$$
(0,1] \subseteq \cup_{r\in[0,1)\cap\mathbb{Q}} (H \oplus r)\dots
$$
(para cada $p \in (0,1]$, seja $x$ seu representante de classe em $H$ e tome $r = |x-p|$).
Além do mais, $H \oplus r$ são disjuntos dois a dois. 
Caso contrário, $h_1 + r_1 = h_2 + r_2 \implies h_1 - h_2 = r_2 - r_1 \implies h_1 \sim h_2$ e, portanto, $h_1 = h_2$ e $r_1 = r_2, pois só um representante está na classe.
Portanto, pela aditividade contável, 
$$
1 = P((0,1]) = \sum_{r \in [0,1) \cap \mathbb{Q}} P(H \oplus r) = \sum_{r \in [0,1) \cap \mathbb{Q}} P(H) = 0 \text{ or } \infty,
$$
o que é um absurdo. 
Logo $P(H)$ não pode estar definido.

---

## Propriedades da probabilidade

Algumas propriedades da probabilidade são

1. $P(A^c) = 1 - P(A)$ para $A \in \mathbb{A}$;
2. $A_1 \subseteq A_2 \implies P(A_1) \le P(A_2)$;
3. $P(\cup A_i) \le \sum P(A_i)$ (para uniões enumeráveis não necessariamente disjuntas.);
4. Se $A_n \subseteq A_{n+1}$ para todo $n$ e $\cup A_n = A$, então $P(A_n) \to P(A)$.

Um **modelo probabilístico** inclui definir um espaço amostral, uma $\sigma$-álgebra e uma probabilidade, o que define um **espaço de probabilidade** $(\Sigma, \mathbb{A}, \mathbb{P})$.

## Probabilidade condicional

Seja $(\Sigma, \mathbb{A}, \mathbb{P})$ um espaço de probabilidade. 
Se $B \in \mathbb{A}$ e $P(B) > 0$, dizemos que a probabilidade de $A$ condicional em $B$ é definida por 
$$
P(A | B) := \frac{P(A \cap B)}{P(B)}.
$$
Podemos verificar que $P(\cdot | B)$ define uma medida de probabilidade também.

Com essa definição, é possível demonstrar (usando indução em $n$) que
$$
P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 | A_1) \cdot P(A_3 | A_1 \cap A_2) \cdots P(A_n | A_1 \cap \dots \cap A_{n-1}).
$$

*Observação: Se $P(B) = 0$, essa definição de probabilidade condicional não serve. Por exemplo, se condicionarmos num evento do tipo "sorteie um número entre $0$ e $1$ ao acaso", esse evento pode acontecer, mas tem probabilidade $0$. Nesse caso, uma definição mais precisa é necessária, apesar de ser um tanto mais complicada. Em particular ela vai envolver esperanças e condicionais em variáveis aleatórias.* 

**Teorema da Probabilidade Total:** Se a sequência $A_1, A_2, \dots$ forma uma partição de $\Omega$, isto é, são disjuntos dois a dois, mas a união deles forma $\Omega$, então
$$
P(B) = \sum_{i} P(A_i) P(B|A_i), \text{ para todo } B \in \mathbb{A}.
$$

A partir dela, podemos chegar na **Fórmula de Bayes**:

$$
P(A_i | B) = \frac{P(A_i) P(B | A_i)}{P(B)} = \frac{P(A_i) P(B | A_i)}{\sum_{i} P(A_i) P(B|A_i)}.
$$

## Independência

Dizemos que os eventos $A$ e $B$ são independentes se 
$$
P(A \cap B) = P(A) \cdot P(B).
$$
Uma consequência direta dessa definição é que se $A$ e $B$ são independentes, então $A^c$ e $B$ também o são.

Para uma coleção de eventos $A_i$, dizemos que eles são independentes 2 a 2 se satisfazem a propriedade acima 2 a 2.
Mas para dizermos que essa coleção é **independente**, temos que exigir que toda subfamília finita de eventos $A_{i_1}, \dots, A_{i_m}$ satisfaça
$$
P(A_{i_1} \cap \dots \cap A_{i_m}) = P(A_{i_1}) \cdots P(A_{i_m}).
$$
Alguns se referem a essa propriedade como **independência estatística**.