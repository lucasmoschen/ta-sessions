import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class OptimalControl:
    
    def __init__(self, H, X, Adj, U, fU, sConst, const, T, initial, final, N = 100):

        self.dX = list()
        self.dAdj = list()

        self.symbX = X
        self.symbAdj = Adj
        self.symbU = U
        
        self.Const = dict(zip(sConst, const)) 

        for i in range(len(X)):
            self.dX.append(H.diff(Adj[i]))
            self.dAdj.append(- H.diff(X[i]))

        self.U = list()
        for u in fU:
            self.U.append(u)

        self.T = T
        self.initial = initial
        self.final = final
        self.N = N

    def runge_kutta_state(self, X, U, Adj, N, h):

        for i in range(N):

            values = list()
            for k in range(len(X)):
                values.append(X[k][i])

            values2 = list()
            for k in range(len(U)):
                values2.append(U[k][i])

            K = [[None]*len(X) for k in range(4)]
            for j in range(4):

                for k in range(len(K[j])):               
                    
                    D = dict(zip(self.symbX, values))
                    D.update(self.Const)
                    D.update(dict(zip(self.symbU, values2)))

                    Old = D[self.symbX[k]]

                    if j > 0:
                        tmp = h*K[j-1][k]
                        if j == 1 or j == 2: 
                            tmp = tmp/2
                        D[self.symbX[k]] = D[self.symbX[k]] + tmp

                    K[j][k] = self.dX[k].subs(D)                    
                    D[self.symbX[k]] = Old

            for j in range(len(X)):
                X[j][i+1] = X[j][i] + h/6*(K[0][j] + 2*K[1][j] + 2*K[2][j] + K[3][j])
            
        return X

    def runge_kutta_adj(self, X, U, Adj, N, h):

        for i in range(N, 0, -1):

            values = list()
            for k in range(len(X)):
                values.append(X[k][i])

            values2 = list()
            for k in range(len(U)):
                values2.append(U[k][i])
            
            values3 = list()
            for k in range(len(Adj)):
                values3.append(Adj[k][i])
            
            K = [[None]*len(Adj) for k in range(4)]
            for j in range(4):

                for k in range(len(K[j])):               
                    
                    D = dict(zip(self.symbX, values))
                    D.update(self.Const)
                    D.update(dict(zip(self.symbU, values2)))
                    D.update(dict(zip(self.symbAdj, values3)))

                    Old = D[self.symbAdj[k]]
                    
                    if j > 0:
                        tmp = h*K[j-1][k]
                        if j == 1 or j == 2: 
                            tmp = tmp/2
                        D[self.symbAdj[k]] = D[self.symbAdj[k]] + tmp                
                    K[j][k] = self.dAdj[k].subs(D)
                    
                    D[self.symbAdj[k]] = Old

            for j in range(len(X)):
                Adj[j][i-1] = Adj[j][i] - h/6*(K[0][j] + 2*K[1][j] + 2*K[2][j] + K[3][j])
            
        return Adj

    def solve(self):


        #parameters
        h = 1/self.N
        N = int(self.N*self.T)
        p = 0.001
        test = -1
        
        #variables
        X = np.array([np.zeros(N + 1) for i in range(len(self.symbX))])
        Adj = np.array([np.zeros(N + 1) for i in range(len(self.symbAdj))])
        U = np.array([np.zeros(N + 1) for i in range(len(self.symbU))])

        for x in range(len(X)):
            X[x][0] = self.initial[x]
        
        for x in range(len(Adj)):
            Adj[x][-1] = self.final[x]

        it = 0

        while test < 0:

            it += 1 
            print('Iteration {}'.format(it))
            print
        
            old_U = U.copy()
            old_X = X.copy()
            old_Adj = Adj.copy()
            
            X = self.runge_kutta_state(X, U, Adj, N, h)

            Adj = self.runge_kutta_adj(X, U, Adj, N, h)


            D = dict()
            D.update(self.Const)

            for u in range(len(U)):
                for i in range(len(U[u])):
                    for k in range(len(X)):
                        D[self.symbX[k]] = X[k][i]
                        D[self.symbAdj[k]] = Adj[k][i]
                    U[u][i] = 0.5*(self.U[u].subs(D) + old_U[u][i])

            test = p*sum(abs(U[0])) - sum(abs(old_U[0] - U[0]))

            for i in range(1,len(U)):
                test = min(test, p*sum(abs(U[i])) - sum(abs(old_U[i] - U[i])))
            
            for i in range(len(X)):
                test = min(test, p*sum(abs(X[i])) - sum(abs(old_X[i] - X[i])))
                test = min(test, p*sum(abs(Adj[i])) - sum(abs(old_Adj[i] - Adj[i])))
            print("The minimum is {}".format(test))
        return X, U

    def plot(self, *args):

        X,U = self.solve()
    
        t = np.linspace(0,self.T,self.N*self.T + 1)

        fig = plt.figure(figsize=(12,24))
        
        for i in range(len(self.symbX)): 
            plt.subplot(len(self.symbX) + len(self.symbU),1,i+1)
            plt.plot(t, X[i])
            plt.title(args[i])
        for i in range(len(self.symbU)):
            plt.subplot(len(self.symbX) + len(self.symbU),1,len(self.symbX) + i + 1)
            plt.plot(t, U[i])
            plt.title('Control ' + str(i+1))
        
        plt.show()

        return t, X, U
