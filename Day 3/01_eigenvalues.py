from sympy import *
A = Matrix([[1,2,2],[2,1,2],[2,2,1]])
print(A.eigenvals())

B = Matrix([[1,1,1],[0,1,1],[0,0,1]])
print(B.eigenvals())