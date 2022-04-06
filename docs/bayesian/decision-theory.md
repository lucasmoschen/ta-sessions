# Teoria da Decisão

Em geral, a estatística se preocupa em propor uma decisão frente a um problema apresentado. 
Nesse caso, a avaliação deve estar clara, como, por exemplo, com a descrição do procedimento e suas consequências. 
A Teoria da Decisão entra para axiomatizar a estrutura de avaliar um estimador para algum parâmetro. 
O critério para avaliar uma tomada de decisão é usualmente através de uma **função de perda**. 
Alguns estatísticos discordam de usá-la, justamente porque defini-la para um problema pode levar a resultados inesperados. 

Seja $\mathcal{D}$ o espaço das decisões (por exemplo, uma estimativa é uma decisão) e $\Omega$ o espaço dos parâmetros.
Uma função de perda é uma função $L : \Omega \times \mathcal{D} \to [0, +\infty]$ e avalia uma penalidade $L(\theta, d)$ em tomar a decisão $d$ com respeito a $\theta$. 
Quando $\mathcal{D} = h(\Omega)$, temos que $L(\theta, d)$ mede o erro em obter $h(\theta)$ por $d$.
Escolher uma função de perda de maneira a considerar o problema em questão não é uma tarefa fácil. 
A complexidade envolvida em defini-la a partir de conceitos subjetivos leva ao uso de perdas matematicamente tratáveis, como a perda quadrática ou absoluta, por exemplo.

Então, uma inferência bayesiana, do ponto de vista da Teoria da Decisão, os três fatores principais são: a família paramétrica de distribuições das observações, a distribuição a priori dos parâmetros, e a função de perda associada às decisões. Inclusive a subjetividade em definir a função de perda e a priori não pode ser separada, conforme destacado por [Lindley (1985)](https://scirp.org/reference/referencespapers.aspx?referenceid=1164705). 

---
``📝`` **Exemplo (Função de perda)**



---

## Função utilidade

## Relação entre utilidade e perda

## Maximalidade e admissibilidade

## Perdas clássicas

## Críticas
