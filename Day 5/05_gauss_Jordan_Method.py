from sympy import *
A = Matrix([[1,2,3],[4,5,6],[7,8,10]])
B = Matrix([3,6,9])
sol,parms = A.gauss_jordan_solve(B)
print("solution:-",sol)
print("\nparms:-",parms)