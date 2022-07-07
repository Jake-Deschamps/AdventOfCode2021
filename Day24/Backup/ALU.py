class ALU:
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
				var_b = int(words[2])
		
		if words[0] == 'inp':
			var_a = int(input('Enter value for {}: '.format(words[1])))
			
		elif words[0] == 'add':
			var_a = var_a + var_b
			
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
		
	def Routine(self, Instructions):
		pass