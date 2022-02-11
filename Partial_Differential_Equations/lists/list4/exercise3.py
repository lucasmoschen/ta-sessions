import numpy as np
import matplotlib.pyplot as plt

numero_pontos_tempo = 20
numero_pontos_espaco = 20

c = 0.8 #velocidade da onda

t = np.linspace(0,1,numero_pontos_tempo, endpoint=True)
x = np.linspace(0,1,numero_pontos_espaco,endpoint=False)

dt = t[1]-t[0]
dx = x[1]-x[0]

f = np.sin(2*np.pi*x) # valor inicial - você pode trocar essa funcao
g = np.zeros([numero_pontos_espaco]) # valor inicial

u = np.zeros([numero_pontos_espaco, numero_pontos_tempo])
ut = np.zeros([numero_pontos_espaco, numero_pontos_tempo])

u[:,0] = f #valor inicial
ut[:,0] = g # valor inicial
for tk in range(0,numero_pontos_tempo-1):
    for xk in range(numero_pontos_espaco):
        # ---  vizinhos do ponto xk: cuidado para garantir a periodicidade da funcao ---------
        xk_esquerda = xk-1
        if xk_esquerda < 0:
            xk_esquerda = numero_pontos_espaco-1
        xk_direita = xk+1
        if xk_direita >= numero_pontos_espaco:
            xk_direita = 0
        #--------
        
        # aproximacao de uxx 
        uxx = (u[xk_esquerda, tk] - 2 * u[xk,tk] + u[xk_direita, tk])/dx**2
        
        # calcular ut
        ut[xk, tk+1] = ut[xk, tk] + dt * (c**2 * uxx)
        
        # calcular a funcao u
        u[xk, tk+1] = u[xk, tk] + dt * ut[xk, tk+1]

fig, ax = plt.subplots(2,2)
        
ax[0][0].plot(x, u[:,0])
ax[0][1].plot(x, u[:,4])
ax[1][0].plot(x, u[:,10])
ax[1][1].plot(x, u[:,19])

plt.show()