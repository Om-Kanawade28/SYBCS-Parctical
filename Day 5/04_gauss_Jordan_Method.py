from sympy import *
A = Matrix([[2,1],[1,2]])
B = Matrix([5,7])
print(A.gauss_jordan_solve(B))