from sympy import *

from ALU_Expression import IntegerModSymplify

x, y, z = symbols("x y z")

expr = (676*x + y/10 + z + 27) % 26

print(expr)

new_expr = IntegerModSymplify(expr)

print(new_expr)
print(type(new_expr))

expr = (676*x + 26*y + z - 27)

success = False
for term in Add.make_args(expr):
	try:
		var = list(term.free_symbols)[0]
		coeff = term.coeff(var)
		if coeff < 0:
			success = True
			break
	except:
		if term < 0:
			success = True
			break
			
if success:
	print("{} is a success".format(expr))
else:
	print("{} is a failure".format(expr))
	