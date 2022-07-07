from sympy import *

from ALU_Expression import IntegerModSymplify, EqualityTest

x, y, z = symbols("x y z")

expr = (2*x + z + 10) % 26

new_expr = IntegerModSymplify(expr) + 10 - z

print(new_expr)
print(EqualityTest(new_expr, 8))
