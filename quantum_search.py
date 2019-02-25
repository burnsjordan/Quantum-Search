import numpy as np
from scipy import linalg as sp

# Adjustable Parameters
alpha = 1/(2**(1/2)) # Proportion of target solutions in the initial state
applications = 1 # Number of times to apply quantum search
t = 1/(2**(1/2)) # Time to measure at
a = 1.0 # Proportion of |x><x| in the hamiltonian
b = 1.0 # Proportion of |psi><psi| in the hamiltonian
c = 0 # Proportion of |x><psi| in the hamiltonian
d = 0 # Proportion of |psi><x| in the hamiltonian

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
    H = H*(1/(np.linalg.det(H)**(1/2)))
    H = sp.expm(1j*t*H)

# Function that applies quantum search using the specified hamiltonian
def qsearch(input):
    global psi
    psi = np.dot(H,input)

# Create the specified hamiltonian
create_hamiltonian(1.0,1.0,0,0)

# Apply quantum search desired amount of times
for i in range(applications):
    qsearch(psi)

# Print result
print(psi)
