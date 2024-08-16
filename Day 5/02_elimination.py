from sympy import *
x, y, z = symbols("x, y, z")
A = Matrix([[7,6,-8],[7,-2,2],[6,-1,-2]])
b = Matrix([3,0,9])
print(linesolve((A,b),[x, y, z]))