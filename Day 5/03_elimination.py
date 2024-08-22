from sympy import *
x, y, z = symbols("x, y, z")
A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
b = Matrix([3,6,9])
print(linsolve((A,b),[x, y, z]))