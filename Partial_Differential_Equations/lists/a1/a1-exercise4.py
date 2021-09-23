#!usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import time 


def exact_solution(t, f, c = 1, numero_pontos_espaco = 100): 
    """
    Describe the exact solution of the transport equation 
    for wave speed c, time t, and initial curve f, that is a 
    vectorial function. 
    """
    x = np.linspace(0,1,numero_pontos_espaco)
    return x, f(x - c*t)

def euler_method_transport(f = lambda x: np.sin(np.pi*x), position = 'Direita',
                           c = 1, numero_pontos_tempo = 100, numero_pontos_espaco = 100): 
    
    # t com endpoint = False para ter o tempo exato para 0.2 e 0.6
    # f tem período 2pi, então x de 0 a 2 para tornar a função periódica no intevalo
    # endpoint = False para os intervalos serem igualmente espaçados em [0, 2)
    # pois f(0) = f(2) => derivada nula em um intervalinho
    t = np.linspace(0,1,numero_pontos_tempo,endpoint=False)
    x = np.linspace(0,2,numero_pontos_espaco,endpoint=False)

    # Discretização
    dt = t[1]-t[0]
    dx = x[1]-x[0]

    u = np.zeros([numero_pontos_tempo, numero_pontos_espaco])
    u[0,:] = f(x)

    for tk in range(0,numero_pontos_espaco-1):
        for xk in range(numero_pontos_espaco):
            xk_esquerda = xk-1
            if xk_esquerda < 0:
                xk_esquerda = numero_pontos_espaco-1
            xk_direita = xk+1
            if xk_direita >= numero_pontos_espaco:
                xk_direita = 0

            # Passo de euler 
            if position == 'Direita': 
                u[tk+1,xk] = u[tk, xk] - c*dt*(u[tk, xk_direita] - u[tk,xk])/dx
            else: 
                u[tk+1,xk] = u[tk, xk] - c*dt*(u[tk, xk] - u[tk,xk_esquerda])/dx

    return t,x,u


if __name__ == '__main__': 

    print("Olá! Esta é uma solução para a Questão 4 da A1 de EDP!")
    print("\n")
    time.sleep(1)
    print("Sinta-se a vontade para fazer correções!")
    print('\n')
    time.sleep(1)
    print('Primeiro, vamos ver a solução exata!')
    print('\n')

    x, u1_e = exact_solution(0, f = lambda x: np.sin(np.pi*x))
    _, u2_e = exact_solution(0.2, f = lambda x: np.sin(np.pi*x))
    _, u3_e = exact_solution(0.6, f = lambda x: np.sin(np.pi*x))

    fig, ax = plt.subplots(figsize = (12,12))
    ax.plot(x,u1_e, label = 't = 0')
    ax.plot(x,u2_e, label = 't = 0.2')
    ax.plot(x,u3_e, label = 't = 0.6')
    ax.set_title('Exact solution u(x,t) for fixed t')
    ax.legend()
    plt.show()

    print('Agora olhe para a discretização à direita.')
    print('\n')

    _, x, u1_d = euler_method_transport()

    fig, ax = plt.subplots(figsize = (12,12))
    ax.plot(x,u1_d[0,:], label = 't = 0')
    ax.plot(x,u1_d[20,:], label = 't = 0.2')
    ax.plot(x,u1_d[60,:], label = 't = 0.6')
    ax.set_title('Discretização à direita de u(x,t) para t fixo')
    ax.legend()
    plt.show()

    print('Agora olhe para a discretização à esquerda.')
    print('\n')
    time.sleep(1)

    t, x, u1_l = euler_method_transport(position='Esquerda')

    fig, ax = plt.subplots(figsize = (12,12))
    ax.plot(x,u1_l[0,:], label = 't = 0')
    ax.plot(x,u1_l[20,:], label = 't = 0.2')
    ax.plot(x,u1_l[60,:], label = 't = 0.6')
    ax.set_title('Discretização à esquerda de u(x,t) para t fixo')
    ax.legend()
    plt.show()

    print('Por fim, vamos compara-las.')
    print('\n')
    time.sleep(1)

    fig, ax = plt.subplots(2,2,sharex = True, figsize = (12,12))
    ax[0][0].plot(x,u1_e, label = 'exact')
    ax[0][0].plot(x,u1_d[0,:], label = 'right')
    ax[0][0].plot(x,u1_l[0,:], label = 'left')
    ax[0][0].set_title('t = 0')
    ax[0][0].legend()

    ax[0][1].plot(x,u2_e, label = 'exact')
    ax[0][1].plot(x,u1_d[20,:], label = 'right')
    ax[0][1].plot(x,u1_l[20,:], label = 'left')
    ax[0][1].set_title('t = 0.2')
    ax[0][1].legend()

    ax[1][0].plot(x,u3_e, label = 'exact')
    ax[1][0].plot(x,u1_d[60,:], label = 'right')
    ax[1][0].plot(x,u1_l[60,:], label = 'left')
    ax[1][0].set_title('t = 0.6')
    ax[1][0].legend()

    plt.show()
