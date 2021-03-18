# Curvas Clássicas

Como uma forma de curiosidade, nessa página serão descritas algumas curvas que
consideradas clássicas na literatura, dada a história que fizeram na
matemática, porque são famosas ou só porque são bonitas. Aqui será fornecido
apenas um pequeno resumo sobre cada uma delas e ponteiros para referências
mais descritivas. Uma boa referência é o <a href="https://www.amazon.com/Catalog-Special-Plane-Curves-Mathematics/dp/0486602885"> livro de J. Dennis Lawrence </a>. 

## Contribuição voluntária

Quem quiser contribuir com esse texto, basta seguir o seguinte processo: 

1. Fork o repositório `ta-sessions`. 
2. Acesse o arquivo `docs/curvas/classic-curves.md`
3. Faça as modificações seguindo o padrão das outras curvas, inserindo seu
   nome, quem descobriu, sua equação ou parametrização e uma figura, caso
   possível. Também é necessário pelo menos uma referência exterior ao site. 
   
      - No caso de colocar imagem, coloque na pasta `classic-curves_files` e
        siga o padrão daquelas que já estão aqui. Procure fazer as curvas no
        geogebra. 
      - Para equações não use as expressões entre `$`, use `\(...\)`. 

<details>
  <summary>Astroide</summary>
  
  <table style="width:100%">
  <tr>
    <th>Descrição</th><th>Equação</th><th>Gráfico</th>
  </tr>
  <tr>
    <td  style="vertical-align:middle;">A astroide foi discutida primeiramente pelo matemático Roemer em 1674 como busca para a melhor forma do dente da engrenagem. Ela é chamada algumas vezes de <i> tetracúspide </i> devido às quatro cúspides (ponta). Ela ganhou esse nome apenas em 1838 em um livro de Vienna. A equação propriamente foi descrita em cartas de Leibniz. Ela é o lugar geométrico de um ponto em uma circunferência que rola em uma circunferência maior de raio \(a\). <a href="http://xahlee.info/SpecialPlaneCurves_dir/Astroid_dir/astroid.pdf">Referência</a>.
    </td>
    <td style="vertical-align:middle;">
    \(x^{2/3} + y^{2/3} = a^{2/3}\)
    </td>
    <td><img src="/ta-sessions/curvas/classic-curves_files/astroid.svg" width = 400></td>
  </tr> 
</table>
</details>

<details>
  <summary>Cissoide de Diocles</summary>
  
<table style="width:100%">
  <tr>
    <th>Descrição</th><th>Equação</th><th>Gráfico</th>
  </tr>
  <tr>
    <td  style="vertical-align:middle;">
    É uma curva cúbica planar que permite construir duas médias proporcionais a uma dada razão. Seu nome vem do grego "forma de Hera" e foi estuda por Diocles 2 séculos antes da Era Comum. Ela é o <a href="http://www2.mat.ufrgs.br/~mat01074/20072/grupos/genio/cisoide.html"> lugar geométrico </a> da interseção da reta tangente à parábola com a reta perpendicular a essa passando pela origem. <a href="https://mathshistory.st-andrews.ac.uk/Curves/Cissoid/"> Referência 1 </a>, <a href="https://mathcurve.com/courbes2d.gb/cissoiddroite/cissoiddroite.shtml"> Referência 2 </a>
    </td>
    <td style="vertical-align:middle;">
    \(2ay^3 - (x^2 + y^2)x = 0\)
    </td>
    <td><img src="/ta-sessions/curvas/classic-curves_files/cissoid.svg" width = 400></td>
  </tr> 
</table>

</details>

<details>

  <summary>Folium de Descartes</summary>
  
  <table style="width:100%">
    <tr>
      <th>Descrição</th><th>Equação</th><th>Gráfico</th>
    </tr>
    <tr>
      <td  style="vertical-align:middle;">
      Seu nome deriva do Latim que significa <i>folha</i>. Ela foi primeiro proposta por René Descartes em 1638. Ele desafiou o matemático Pierre de Fermat a encontrar a linha tangente a essa curva em um ponto qualquer. Podemos encontrá-la facilmente através da diferenciação implícita. <a href="https://encyclopediaofmath.org/wiki/Folium_of_Descartes">Referência 1</a><a href="https://www.jstor.org/stable/4145129?seq=1">Referência 2</a>
      </td>
      <td style="vertical-align:middle;">
      \(x^3 + y^3 = 3axy\)
      </td>
      <td><img src="/ta-sessions/curvas/classic-curves_files/folium.svg" width = 400></td>
    </tr> 
  </table>

</details>

<details>
  <summary>Espiral de Euler</summary>
  
<table style="width:100%">
  <tr>
    <th>Descrição</th><th>Equação</th><th>Gráfico</th>
  </tr>
  <tr>
    <td  style="vertical-align:middle;">
    É uma curva cuja curvatura varia linearmente conforme varia o comprimento de arco (veja o exemplo na página sobre curvatura). Ela tem outros nomes como clotoide ou espirais de Cornu. <a href="https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-111.pdf">Acredita-se</a> que tenha sido primeiramente estudada por James Bernoulli em 1694. Sua equação é através da integral de Fresnel. Ela foi proposta como a solução para o problema da elasticidade, mas hoje tem diversas aplicações como <a href="https://www.youtube.com/watch?v=D3tdW9l1690">projeção do de uma esfera.</a>
    </td>
    <td style="vertical-align:middle;">
    \(\alpha(s) = (\int_0^s \cos(t^2)dt, \int_0^s \sin(t^2)dt\)
    </td>
    <td><img src="/ta-sessions/curvas/classic-curves_files/euler.svg" width = 400></td>
  </tr> 
</table>

</details>

