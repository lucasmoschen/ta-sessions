# Escolha de modelos

Podemos considerar a **escolha de modelos** como um caso especial de testagem, afinal estamos testando qual modelo usar.
Todavia, cuidado adicional deve ser tomado porque estamos lidando com modelos potencialmente bastante diferentes, diferente de apenas verificarmos se o parâmetro de um modelo específico mora em uma região do espaço de parâmetros.

Estamos agora considerando que a distribuição dos dados $f$ é desconhecida, o que torna mais difícil condicionar em $x$.
Isso também levanta a pergunta se $f$ pertence mesmo à família considerada $\{f_{\theta} : \theta \in \Theta\}$ e, de forma mais pronfunda, se um modelo verdadeiro de fato existe. 
Considere inicialmente uma situação que temos modelos paramétricos competindo:
$$
\mathcal{M}_i : x \sim f_i(x|\theta_i). \theta_i \in \Theta_i,  i \in I. 
$$
Do ponto de vista bayesiano, poderíamos contruir uma distribuição a priori para $I$, e todas as inferências deveriam ser baseadas na posteriori definida em $I$.
Em geral, $I$ é um conjunto pequeno, com distribuições conhecidas.

---
``📝`` **Exemplo**

Em problemas de contagem, por exemplo o número de acidentes de carro em uma rodovia em um período de tempo, estamos modelando $N$. Podemos atribuir duas distribuições distitas: $\mathcal{M}_1 : N \sim \operatorname{Poi}(\lambda)$ ou $\mathcal{M}_2 : N \sim \operatorname{NegBin}(m,p)$. 
Note que a dimensão dos parâmetros é completamente diferente e cada distribuição tem suas particularidades.

---

Podemos também atribuir modelos não paramétricos, quando pouca informação sobre o processo gerador é obtido. 
Nesse caso, $I$ é infinito e possivelmente não enumerável.
Outro problema que precisamos enfrentar, é que modelos diferentes podem ter resultados similares e serem apropriados, mesmo que não sejam os verdadeiros (se é que isso existe!).
Por fim, existe a situação de compararmos modelos em que um é submodelo do outro. 
Nesse caso, em geral o modelo maior vai apresentar uma perda quadrática menor, por exemplo, mas mais parâmetros são estimados a partir da mesma amostra. 
O clássico exemplo dessa situação é a escolha das variáveis que vão compor uma regressão linear. 

## Framework padrão 

### Modelagem a priori 

### Fator de Bayes

### Critério de Schwartz

### Desvio bayesiano

## Modelo médio

## Projeção de modelos

## Goodness-of-fit