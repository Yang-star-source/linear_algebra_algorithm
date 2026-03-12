import numpy as np
from scipy.linalg import lu

def LU_from_scipy(A):

    P, L, U = lu(A)
    return P, L, U

A=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
])

P, L, U = LU_from_scipy(A)

print(P)
print("\n")
print(L)
print("\n")
print(U)