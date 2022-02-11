# Inferência Estatística

Procedimento que objetiva produzir uma proposição probabilísitca sobre um modelo estatístico. 

## Modelo Estatístico

Identificar variáveis aleatórias de interesse, especificar uma distribuição conjunta (ou família), parâmetros relevantes e uma especificação para uma distribuição para os parâmetros desconhecidos (baysianos adoram essa parte, $p \sim N(0,1)$)

## Espaço dos Parâmetros

Uma característica ou uma combinação de características para determinar uma distribuição conjunta para as variáveis aleatórias forma o parâmetro, que pertence a um espaço denominado $\Omega$.  

## Estatística

Função das variáveis aleatórias observáveis

## Problemas estudados

- Predição: Baseado na época do ano que estamos, fatores climatológicos dos últimos dias, entre outros fatores, qual a probabilidade de chuva amanhã?
- Problemas de decisão estatística: É relacionado ao risco e teste de hipóteses. 
[Resposta considerável](https://math.stackexchange.com/questions/2842793/what-is-meant-by-a-statistical-decision-problem)
- Desenho de experimentos: um psicólogo quer inferir quão avesso ao risco é uma determinada população. Ele pode determinar, desenhar o experimento para isso. 

[Inferência Estatística com Python](https://towardsdatascience.com/statistical-inference-in-pyhton-using-pandas-numpy-part-i-c2ac0320dffe)


```python
import numpy as np 
import pandas as pd 

from scipy.stats import poisson

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
```

### Importando os Dados

Este banco de dados inclui um registro para cada vazamento ou derramamento de oleoduto relatado à Administração de Segurança de Dutos e Materiais Perigosos desde 2010. Esses registros incluem a data e hora do incidente, operador e oleoduto, causa do incidente, tipo de líquido perigoso e quantidade perdida, ferimentos e fatalidades e custos associados.


```python
oil_accident_df = pd.read_csv('../data/oil_pipeline.csv')
oil_accident_df.sample()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Report Number</th>
      <th>Supplemental Number</th>
      <th>Accident Year</th>
      <th>Accident Date/Time</th>
      <th>Operator ID</th>
      <th>Operator Name</th>
      <th>Pipeline/Facility Name</th>
      <th>Pipeline Location</th>
      <th>Pipeline Type</th>
      <th>Liquid Type</th>
      <th>...</th>
      <th>Other Fatalities</th>
      <th>Public Fatalities</th>
      <th>All Fatalities</th>
      <th>Property Damage Costs</th>
      <th>Lost Commodity Costs</th>
      <th>Public/Private Property Damage Costs</th>
      <th>Emergency Response Costs</th>
      <th>Environmental Remediation Costs</th>
      <th>Other Costs</th>
      <th>All Costs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>871</th>
      <td>20120202</td>
      <td>17135</td>
      <td>2012</td>
      <td>6/15/2012 3:50 PM</td>
      <td>31476</td>
      <td>ROSE ROCK MIDSTREAM L.P.</td>
      <td>BURKETT DISCHARGE</td>
      <td>ONSHORE</td>
      <td>UNDERGROUND</td>
      <td>CRUDE OIL</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6020.0</td>
      <td>200.0</td>
      <td>2500.0</td>
      <td>10500.0</td>
      <td>8500.0</td>
      <td>16000.0</td>
      <td>43720</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 48 columns</p>
</div>




```python
cols_of_interest = ['Accident Date/Time','Accident State','Pipeline Location',
                    'Liquid Type','Net Loss (Barrels)','All Costs']
data = oil_accident_df[cols_of_interest]
data['All Costs'] = data['All Costs'] / 1000000    # unidade em milhão.
data.sample()
```

    /home/lucasmoschen/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      after removing the cwd from sys.path.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Accident Date/Time</th>
      <th>Accident State</th>
      <th>Pipeline Location</th>
      <th>Liquid Type</th>
      <th>Net Loss (Barrels)</th>
      <th>All Costs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>263</th>
      <td>10/11/2010 4:10 PM</td>
      <td>NJ</td>
      <td>ONSHORE</td>
      <td>REFINED AND/OR PETROLEUM PRODUCT (NON-HVL), LI...</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



Vamos entender um pouco como esta informação esta organizada. 


```python
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Net Loss (Barrels)</th>
      <th>All Costs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2795.000000</td>
      <td>2795.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>132.194050</td>
      <td>0.834033</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1185.019252</td>
      <td>16.578298</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>0.005040</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.023129</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.000000</td>
      <td>0.117232</td>
    </tr>
    <tr>
      <th>max</th>
      <td>30565.000000</td>
      <td>840.526118</td>
    </tr>
  </tbody>
</table>
</div>



Vamos analisar os dados utilizando leis da probabilidade para aprender sobre a população. Veja que não temos a informação completa, apenas a partir de 2010. 


```python
fig, ax = plt.subplots(1,2,figsize = (15,4))

sns.boxplot(data['All Costs'], data=data, ax = ax[0])
ax[0].set_title('Custos dos Acidentes por Milhão US$')

sns.boxplot(data['Net Loss (Barrels)'], data=data, ax = ax[1])
ax[1].set_title('Prejuízo Líquido (Barris)')

plt.show()
```


![svg](output_8_0.svg)


Mas esse não era para ser um boxplot? Cade a caixa? Isso indica que valores grandes nos dois dados são muito maiores relativamente aos outros dados. Poderíamos prever o custo de um acidente usando a mediana dos valores? É de fato um modelo, mas nesse caso, parece ser ruim dado os valores grandes. 

O que são esses valores grandes, afinal? Em alguns casos, podem realmente apresentar erros, mas nesse caso fica difícil de afirmar. 

Bom. Podemos, dados esses problemas, trabalhar com outra variável disponível: o tempo do acidente. Conhecemos uma família de distribuições de probabilidade que modela frequência de acidentes em um intervalo de tempo? 

**Distribuição de Poisson:** probabilidade de uma série de eventos ocorrer num certo período de tempo se estes eventos ocorrem independentemente de quando ocorreu o último evento.

De forma geral, podemos dizer que isso é verdade para acidentes de óleo. Assim, temos uma **variável aleatória** de interesser $X$, que indica o número de acidentes, já temos uma distribuição para essa variável (Poisson) e já temos o parâmetro $\lambda$ desconhecido. 




```python
data['Accident Date/Time'] = pd.to_datetime(data['Accident Date/Time'])
totaltimespan = np.max(data['Accident Date/Time']) - np.min(data['Accident Date/Time'])

totaltime_hour = (totaltimespan.days*24 + totaltimespan.seconds/(3600))
totaltime_month = (totaltimespan.days + totaltimespan.seconds/(3600*24)) *12/365

lmda_h = len(data) / totaltime_hour
lmda_m = len(data) / totaltime_month 

print('Número estimado de acidentes por hora: {}'.format(lmda_h)) 
print('Número estimado de acidentes por mês {}'.format(lmda_m))
```

    Número estimado de acidentes por hora: 0.04540255169379675
    Número estimado de acidentes por mês 33.14386273647162


    /home/lucasmoschen/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      """Entry point for launching an IPython kernel.


Poderíamos ter procedimentos para estimar $\lambda$, mas por hora, vamos tomar ele como a média das observações. Pela Lei dos Grandes Números, sabemos que a média da Poisson é $\lambda$ e a média amostral tende para ela.  


```python
lamda = 33
```


```python
X = poisson(lamda)
I = np.arange(0,60,1)  #intervalo(0,60), passo = 1

samples_poisson = np.sort(np.random.poisson(lamda,10000)) 
Y = X.cdf(samples_poisson)     #função de densidade acumulada 

fig, ax  = plt.subplots(1,2,figsize = (20,8))
ax[0].scatter(I,X.pmf(I) , color = 'purple')
ax[0].set_xlabel('Número de Acidentes por mês (n)')
ax[0].set_ylabel('P(X <= n)')
ax[0].set_title('Função de Massa de Probabilidade')

ax[1].scatter(samples_poisson, Y, color = 'purple')
ax[1].hlines(0.5, xmin = min(samples_poisson), xmax = max(samples_poisson), 
             linestyle = '--', color = 'black')
ax[1].set_xlabel('Número de acidentes por mês (n)')
ax[1].set_ylabel('P(X <= n)')
ax[1].set_title('Função de Distribuição Acumulada')

plt.show()
```


![png](output_13_0.png)


A partir de nosso modelo, já podemos fazer acertações probabilística!


```python
real_data = np.array(data['Accident Date/Time'].apply(lambda x: (x.year, x.month)))
accidents_count = {2010 + i: {m: 0 for m in range(1,13)} for i in range(8)}

for info in real_data:
    accidents_count[info[0]][info[1]] += 1

distribution = [accidents_count[y][m] for y in accidents_count.keys() for m in accidents_count[y].keys()]
distribution = distribution[:-12] #Tirando 2 observações de 2017 

fig, ax = plt.subplots()
sns.distplot(distribution, bins = 15, ax = ax, label = 'Original data', kde = False, norm_hist = True)
ax.scatter(I,X.pmf(I) , color = 'purple', label = 'Nosso modelo')
ax.legend()
ax.set_title('Comparando modelo com dados reais')
plt.show()
```


![png](output_15_0.png)

