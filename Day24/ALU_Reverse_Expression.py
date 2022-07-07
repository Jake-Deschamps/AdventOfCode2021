from sympy import *

class ALU_Ex:
	def __init__(self):
		w1, x1, y1 = symbols('w1 x1 y1')
		self.w = w1
		self.x = x1
		self.y = y1
		self.z = 0
	
	def ParseLine(self, Line):
		words = Line.split()
		
		var_a = getattr(self, words[1])
		
		if len(words) == 3:
			if words[2] in ['w', 'x', 'y', 'z']:
				var_b = getattr(self, words[2])
			else:
				try:
					var_b = int(words[2])
				except:
					var_b = symbols(words[2])
		
		
		if words[0] == 'inp':
			var_a = var_b
			
		elif words[0] == 'add': # current value of var_a is old value of var_a + var_b
			# replace var_a with var_a - var_b
			var_a += var_a - var_b
			
		elif words[0] == 'mul':
			var_a = var_a * var_b
			
		elif words[0] == 'div':
			var_a = int(var_a / var_b)
		
		elif words[0] == 'mod':
			var_a = var_a % var_b
			
		elif words[0] == 'eql': # try plugging in combos of stuff to see if possible? lets just try saying things all things are possible and using the resulting 2^28 equations. if not, 
			# expr.subs(list(expr.free_symbols)[0],1)
			if type(var_a) == type(1) and type(var_b) == type(1):
				if var_a == var_b:
					var_a = 1
				else:
					var_a = 0
			else: # create option for both
				# create version with equal:
					# set var_a to 1, add restriction that var_a = var_b
				# create version with not equal to:
					# set var_a to 0, add restriction that var_a != var_b
				
		setattr(self, words[1], var_a)		
		
	def View(self):
		return([self.w, self.x, self.y, self.z])
		
	def Reset(self):
		self.w = 0
		self.x = 0
		self.y = 0
		self.z = 0