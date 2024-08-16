from sympy import *
x, y, z = symbols("x, y, z")
A = Matrix([[3,2,-1],[2,-2,4],[2,-1,2]])
b = Matrix([3,6,9])
print(linsolve((A,b),[x, y, z]))