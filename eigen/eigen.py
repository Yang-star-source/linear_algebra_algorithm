import numpy as np
from scipy.linalg import det , eig

# Suppress scientific notation and round to 4 decimal places
np.set_printoptions(suppress=True, precision=4)

def get_determinant(A):
    return det(A)

def get_eigen(A):
    eigenvalues, eigenvectors = eig(A)
    eigenvalues = np.real(eigenvalues)
    eigenvectors = np.real(eigenvectors)
    return eigenvalues, eigenvectors

A = np.array([
    [1,2,3],
    [5,6,7],
    [9,10,11],
])

eigenvalues, eigenvectors = get_eigen(A)

print(get_determinant(A))
print("\n")
print(eigenvalues)
print("\n")
print(eigenvectors)