import numpy as np
from scipy import linalg as spl
import scipy as sp

def apply_circuit(t,a,b,c,d,alpha,applications):
    global H,x,psi
    # Generate x and psi
    beta = float((1 - (alpha**2))**(1/2))
    x = np.array([[1],[0]])
    psi = np.array([[alpha],[beta]])
    # Create the specified hamiltonian
    H = a*np.kron(np.transpose(x),x)
    H = np.add(H,b*np.kron(np.transpose(psi),psi))
    H = np.add(H,c*np.kron(np.transpose(x),psi))
    H = np.add(H,d*np.kron(np.transpose(psi),x))
    H = spl.expm(-1j*t*H)
    # Apply quantum search desired amount of times
    for j in range(applications):
        psi = np.dot(H,psi)
    # Return result
    return np.real(psi[0][0]*np.conj(psi[0][0]))
