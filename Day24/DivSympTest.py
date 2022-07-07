from sympy import *

from ALU_Expression import FloorDivSymplify

x, y, z = symbols("x y z")

#expr = 26*x + y/7 + z/11 + 12/5

expr = 8/7
print(expr)

new_expr = FloorDivSymplify(expr)

print(new_expr)