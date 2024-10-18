from sympy import *
A = Matrix([[1,2,2],[2,1,2],[2,2,1]])
print(A.diagonalize())
P,D = A.diagonalize()
print(P)
print(D)