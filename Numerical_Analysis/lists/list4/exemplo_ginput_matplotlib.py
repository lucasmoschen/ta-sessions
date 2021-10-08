"""
=====================
Funções interativas
=====================

Estes exemplos possuem funções interativas como ginput, waitforbuttonpress
e manual clabel. Esse script não funciona no Jupyter Notebook e precisa de 
uma interface gráfica. 

"""

# Importando os pacotes. 

import time

import numpy as np
import matplotlib.pyplot as plt

# A função a seguir re-resenha a figura que já existe. 

def drawing(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

##################################################
# Define o triângulo com os 3 pontos correspondentes. 

# Configura os eixos para não se escalarem com a mudança dos dados
plt.setp(plt.gca(), autoscale_on=False) 

drawing('Você definirá um triângulo marcando 3 pontos.')

# Tranca o código enquanto nada é pressionado. 
plt.waitforbuttonpress()

while True:
    pontos = []
    while len(pontos) < 3:
        drawing('Selecione três pontos no espaço.')
        pontos = np.asarray(plt.ginput(3, timeout=-1))
        if len(pontos) < 3:
            drawing('Poucos pontos, começando de novo...')
            time.sleep(1)

    ph = plt.fill(pontos[:, 0], pontos[:, 1], 'r', lw=2)

    drawing('Feliz? Clique no mouse se não, e no teclado se sim.')

    if plt.waitforbuttonpress():
        break

    # Remove tudo. 
    for p in ph:
        p.remove()

plt.show()