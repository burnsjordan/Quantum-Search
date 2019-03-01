import numpy as np
from scipy import linalg as spl
import scipy as sp
import matplotlib.pyplot as plt

# Adjustable Parameters
alpha = 1/(2**(1/2)) # Proportion of target solutions in the initial state
applications = 10 # Maximum number of times to apply quantum search
t = sp.pi*(2**(1/2))/2 # Time to measure at
a = 1.0 # Proportion of |x><x| in the hamiltonian
b = 1.0 # Proportion of |psi><psi| in the hamiltonian
c = 0 # Proportion of |x><psi| in the hamiltonian
d = 0 # Proportion of |psi><x| in the hamiltonian

# Create list to store results
results = []

for i in range(applications):
    # Generate x and psi
    beta = float((1 - (alpha**2))**(1/2))
    x = np.array([[1],[0]])
    psi = np.array([[alpha],[beta]])

    # Generate an empty hamiltonian
    H = np.array([[0,0],[0,0]])

    # Function that creates hamiltonian using the specified parameters
    def create_hamiltonian(a,b,c,d):
        global H
        H = np.add(H,a*np.kron(np.transpose(x),x))
        H = np.add(H,b*np.kron(np.transpose(psi),psi))
        H = np.add(H,c*np.kron(np.transpose(x),psi))
        H = np.add(H,d*np.kron(np.transpose(psi),x))
        H = spl.expm(-1j*t*H)

    # Function that applies quantum search using the specified hamiltonian
    def qsearch(input):
        global psi
        psi = np.dot(H,input)

    # Create the specified hamiltonian
    create_hamiltonian(a,b,c,d)

    # Apply quantum search desired amount of times
    for j in range(i):
        qsearch(psi)

    # Store result in results
    results.append(np.real(psi[0][0]*np.conj(psi[0][0])))

# Print result
plt.plot(results)
plt.ylim([0,1])
plt.show()
