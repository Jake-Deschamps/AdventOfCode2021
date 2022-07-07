from sympy import *

class ALU_Ex:
	def __init__(self):
		self.w = 0
		self.x = 0
		self.y = 0
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
					var_b = words[2]
		
		
		if type(var_a) == type(1) and type(var_b) == type(1):
			IS = 'int-int'
		elif type(var_a) == type(1) and type(var_b) == type('a'):
			IS = 'int-str'
		elif type(var_a) == type('a') and type(var_b) == type(1):
			IS = 'str-int'
		elif type(var_a) == type('a') and type(var_b) == type('a'):
			IS = 'str-str'
		
		
		if words[0] == 'inp':
			var_a = var_b
			
		elif words[0] == 'add':
			if IS == 'int-int': # both are ints
				var_a = var_a + var_b
			elif IS == 'int-str':
				if var_a == 0:
					var_a = var_b
				else:
					var_a = var_b + ' + ' + str(var_a)
			elif IS == 'str-int':
				if var_b == 0:
					var_a = var_a
				else:
					var_a = var_a + ' + ' + str(var_b)
			elif IS == 'str-str':
				var_a = var_a + ' + ' + var_b
			
		elif words[0] == 'mul':
			var_a = var_a * var_b
			
		elif words[0] == 'div':
			var_a = int(var_a / var_b)
		
		elif words[0] == 'mod':
			var_a = var_a % var_b
			
		elif words[0] == 'eql':
			if var_a == var_b:
				var_a = 1
			else:
				var_a = 0
				
		setattr(self, words[1], var_a)		
		
	def View(self):
		return([self.w, self.x, self.y, self.z])
		
	def Reset(self):
		self.w = 0
		self.x = 0
		self.y = 0
		self.z = 0