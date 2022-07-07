import sys
#import ast
import math

class SnailNumber:
	def __init__(self, numberin):
		self.number = numberin
		
	def ViewNumber(self):
		temp_str = ''
		for i, c in enumerate(self.number):
			if type(c) == int:
				if self.number[i-1] == ']':
					temp_str += ','
			temp_str += str(c)
			if type(c) == int and not (self.number[i+1] == ']'):
				temp_str += ','
				
		return temp_str
		
	def Simplify(self):
		while not self.Simplify_step():
			pass
			
	def Simplify_step(self):
	
		#print(self.number)
	
		depth = 0
		
		Mode = ''
		
		for i, c in enumerate(self.number):
			if type(c) == int:
				if type(self.number[i+1]) == int and depth >= 5:
					Mode = 'Explode'
					break
				if c >= 10:
					Mode = 'Split'
					break
		
			if c == '[': depth += 1
			if c == ']': depth -= 1
		
		if Mode == 'Explode':
			pair = [self.number[i], self.number[i+1]]
			#print('exploding with pair {}'.format(pair))
			j = i-1 # step backwards index
			k = i+2 # step forwards index
			while j >= 0:
				if type(self.number[j]) == int:
					#print('left adding successful, index {}'.format(j))
					self.number[j] += pair[0]
					break
				j -= 1
			while k < len(self.number):
				if type(self.number[k]) == int:
					#print('right adding successful, index {}'.format(k))
					self.number[k] += pair[1]
					break
				k += 1
			# remove section
			#  i-2  i-1, i  i+1 i+2  i+3
			# ..... '[','2','4',']'.....
			self.number = self.number[:i-1] +[0] +  self.number[i+3:]
			return False
					
			
		elif Mode == 'Split':
			n = self.number[i]
			n1 = math.floor(n/2)
			n2 = n-n1
			self.number = self.number[:i] + ['[',n1,n2,']'] + self.number[i+1:]
			return False
		else:
			#print('all done')
			return True

for line in sys.stdin:
	line = line.strip('\n')

#the_number = eval(line)
#I think it'll be easier as one giant list of characters and ints
the_number = []
LISTOFINTS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
building_int = ''
for i, c in enumerate(line):
	if c in LISTOFINTS:
		building_int += c
	else:
		if not building_int == '':
			the_number.append(int(building_int))
			building_int = ''
		if not c == ',':
			the_number.append(c)

sNumber = SnailNumber(the_number)
sNumber.Simplify()
print(sNumber.ViewNumber())