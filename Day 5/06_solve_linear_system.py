from sympy import *
from sympy .abc import x,y,z
AB = Matrix([[6,18,3,3],[2,12,1,19],[4,15,1,0]])
print(solve_linear_system_LU(AB,[x,y,z]))
