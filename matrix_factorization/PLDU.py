import numpy as np
from scipy.linalg import lu

def PLDU_factorization(A):
    P, L, U = lu(A)
    diagonal = np.diag(U).copy()

    diagonal[diagonal == 0] = 1.0

    D = np.diag(diagonal)
    D_inverse  = np.diag(1.0/diagonal)

    Unew = D_inverse @ U

    return P, L, D, Unew

A = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
])

P , L, D, Unew = PLDU_factorization(A)
print(P)
print("\n")
print(L)
print("\n")
print(D)
print("\n")
print(Unew)
print("\n")
print(P @ L @ D @ Unew)