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

Podemos extender o espaço dos parâmetros para $\boldsymbol{\Theta} = \cup_{i\in I} \{i\}\times \Theta_i$, em que $\mu \in I$ é também um parâmetro.
Assim, podemos definir $p_{i}$ como a probabilidade a priori para o modelo $\mathcal{M}_i$. 
Com isso, o Teorema de Bayes diz que 
$$
p(\mathcal{M}_i | x) \propto p_i\int_{\Theta_i}  f_i(x|\theta_i) \pi_i(\theta_i) \, d\theta_i.
$$
Quando $I$ é infinito, a construção da priori $(\pi_i, p_i)$ para cada $i \in I$ é delicada. 
Além do mais, quando um modelo $i$ é submodelo de outro $j$, deveria haver uma coerência entre $\pi_i$ e $\pi_j$ e, talvez, entre $p_i$ e $p_j$. 
Um outro ponto importante é que parâmetros comuns a modelos diferentes devem ser tratados como entidades separadas.
Exceções devem ser consideradas caso a caso.

### Fator de Bayes

O fator de Bayes
$$
B_{12} = \frac{P(\mathcal{M}_1|x)}{P(\mathcal{M}_2|x)} \bigg/ \frac{P(\mathcal{M}_1)}{P(\mathcal{M}_2)}
$$
é usado para comparar os modelos $\mathcal{M}_1$ e $\mathcal{M}_2$. 
O problema acontece quando queremos comparar muitos modelos.

### Critério de Schwartz

Considere a *expansão de Laplace* 
$$
\int_{\Theta} \exp\{n h(\theta)\} \, d\theta = \exp\{n h(\hat\theta)\} (2\pi)^{p/2} n^{-p/2} |H^{-1}(\hat\theta)| + O(n^{-1}),
$$
em que $\hat{\theta}$ é o argumento máximo de $h$ e $H$é a Hessiana de $h$. 
Aplicando essa aproximação ao fator de Bayes, obtemos 
$$
B_{12} \approx \frac{L_{1,n}(\hat\theta_{1,n})}{L_{2,n}(\hat\theta_{2,n})}\bigg|\frac{H_1^{-1}(\hat\theta_{1,n})}{H_2^{-1}(\hat\theta_{2,n})}\bigg|\left(\frac{n}{2\pi}\right)^{(p_1-p_2)/2},
$$
em que $L_{i,n}$ é a verossimilhança do modelo $i$ para $n$ observações e $\hat{\theta}_{i,n}$ o respectivo argumento máximo.
Portanto, 
$$
\log(B_{12}) \approx \log\lambda_n + \frac{p_2-p_1}{2}\log(n) + K(\hat\theta_{1,2}, \hat\theta_{2,n}),
$$
em que $\lambda_n = L_{1,n}(\hat\theta_{1,n}) / L_{2,n}(\hat\theta_{2,n})$
O critério de Schwartz é dado por 
$$
S = -\log \lambda_n - \frac{p_2-p_1}{2}\log(n) 
$$
quando $\mathcal{M}_1 \subset \mathcal{M}_2$ e o termo restante é negligenciável.

Esse critério também é conhecido como *Critério de Informação de Bayes* (BIC). 
Substituindo $1/2$ por $\log(2)$, e temos o primeiro termo multiplicado por 2, temos o *Critério de Informação Akaike* (AIC). 
Apesar de ser uma aproximação de primeira ordem para o fator de Bayes, a dependência na priori desaparece, e a comparação só é válida para modelos regulares, logo a relevância em Inferência Bayesiana é menor. 

### Desvio bayesiano

Uma alternativa ao AIC e ao BIC é o *Critério de Informação de Desvio* (DIC), definido como 
$$
\mathbb{E}[D(\theta)|x] + p_D = \mathbb{E}[D(\theta)|x] + (\mathbb{E}[D(\theta)|x] - D(\mathbb{E}[\theta|x])),
$$
em que $D(\theta) = -2\log(f(x|\theta))$ é uma medida de desvio. e $p_D$é uma penalização. 
Assim, quanto menor o valor de $DIC$, melhor o modelo. 

## Ideias adicionais

> **Modelo médio:** Uma forma de lidar com a escolha de modelos é não escolher um de fato, mas sim, incluir todos os modelos para lidar com a incerteza do modelo propriamente.
Isso nem sempre é possível em questões científicas, já que a escolha de um modelo explicativo pode ser relevante.
Além do mais, essa maneira parece infringir a parcimônia.

> **Projeção de modelos:** essa abordagem é baseada na ideia de projetar um modelo $f(y|\theta)$ em submodelos através de restrições em $\theta$. Isso permite a construção de uma única priori para $\theta$ e, portanto, acomoda bem prioris impróprias. Dada uma restrição $\Theta_0$, uma ideia é considerar uma restrição aceitável se $d(f(\cdot|\theta). \Theta_0)< \epsilon$, em que $d$ é uma medida de divergência, tal como a pseudo-distância de Kullback-Leibler.
