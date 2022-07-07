import sys

class Submarine:
	def __init__(self, horizontal = 0, depth = 0, aim = 0):
		self.horizontal = horizontal
		self.depth = depth
		self.aim = aim
		
	def move(self, direction, distance):
		if direction == 'forward':
			self.horizontal += distance
			self.depth += self.aim*distance
		#elif direction == 'backward':
			#	horizontal -= distance
		elif direction == 'up':
			self.aim -= distance
		elif direction == 'down':
			self.aim += distance
		else:
			print('ERROR, INVALID DIRECTION')
			
	def get_mult(self):
		return self.horizontal*self.depth

		

santa_sub = Submarine()

for line in sys.stdin:
	[direction, distance] = line.split(' ')
	direction = str(direction)
	distance = int(distance)
	
	santa_sub.move(direction, distance)

print(santa_sub.horizontal)
print(santa_sub.depth)

print(santa_sub.get_mult())