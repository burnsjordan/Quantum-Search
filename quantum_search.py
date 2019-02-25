import numpy as np
from scipy import linalg as sp

alpha = 1/(2**(1/2))
beta = float((1 - (alpha**2))**(1/2))
applications = 1
t = 1/(2**(1/2))

x = np.array([[1],[0]])
psi = np.array([[alpha],[beta]])

H = np.array([[0,0],[0,0]])

def create_hamiltonian(a,b,c,d):
    global H
    H = np.add(H,a*np.kron(np.transpose(x),x))
    H = np.add(H,b*np.kron(np.transpose(psi),psi))
    H = np.add(H,c*np.kron(np.transpose(x),psi))
    H = np.add(H,d*np.kron(np.transpose(psi),x))
    H = H*(1/(np.linalg.det(H)**(1/2)))
    H = sp.expm(1j*t*H)

def qsearch(input):
    global psi
    psi = np.dot(H,input)

create_hamiltonian(1.0,1.0,0,0)

for i in range(applications):
    qsearch(psi)

print(psi)
