# Example in Markov Chains

# The Transition Matrix indicates that the element ij represents the probability of 
# a member in state j goes to state i.

# Consider an election with democrats, republicans and independents. Say that p = [D; R; I] 
# represents the proportion of voters in the three cenarios. 

import numpy as np

T = np.matrix('0.7 0.1 0.3; 0.2 0.8 0.3; 0.1 0.1 0.4')

# p represents the proportion of voters in the 2004 election.

p0 = np.matrix('0.48;0.51;0.01')

print(T[1,:])
print(p0[2])

#Now,let's calculate the first state. 

print(" p1 = Tp = {}".format(T*p0))
print(" p2 = Tp1 = {}".format((T**2)*p0))

# We know 1 is eigenvalue of this matrix. What is the associated eigenvector?  

evalues, evectors = np.linalg.eig(T)
print(evalues)
print(evectors)

# Now we know it, we want it has all entries has positive values and the sum up is 1. 
# So I take the inverse of each coordinate and divide by the norm 1. 

v = - evectors[:,0]/np.linalg.norm(evectors[:,0],1)

print(v)