import sys

class Room:
	def __init__(self, Spaces, Cucumbers):
		
		self.Spaces = Spaces # numpy array of Spaces (don't know if it needs to be a numpy)
		self.Cucumbers = Cucumbers
		
		self.AcuireNeighbours()
		
	def AcuireNeighbours(self):
		Limits = self.Spaces.shape
		for r, Row in enumerate(self.Spaces):
			for c, space in enumerate(Row):
				space.Neighbours.append(self.Spaces[(r+1)%Limits[0], c])
				space.Neighbours.append(self.Spaces[r, (c+1)%Limits[1]])
			
		
		
	def Step(self):
		Movement = False
		to_move = []
		for C in self.Cucumbers[1]:
			if C.CanIMove():
				to_move.append(C)
		for C in to_move:
			C.Move()
			Movement = True
		
		to_move = []
		for C in self.Cucumbers[0]:
			if C.CanIMove():
				to_move.append(C)
		for C in to_move:
			C.Move()
			Movement = True
			
		return Movement
		
		
		
		
	def View(self):
		output = ''
		for row in self.Spaces:
			for space in row:
				if space.Free:
					output += '.'
				elif space.Cucumber.Type == 0:
					output += 'v'
				elif space.Cucumber.Type == 1:
					output += '>'
			output += '\n'
			
		return output
		
		

class Cucumber:
	def __init__(self, Space, Type):
		self.Space = Space
		self.Type = Type
		
	def CanIMove(self):
		return self.Space.Neighbours[self.Type].Free
		
	def Move(self):
		self.Space.Cucumber = []
		self.Space.Free = True
		
		self.Space = self.Space.Neighbours[self.Type]
		
		self.Space.Cucumber = self
		self.Space.Free = False

class Space:
	def __init__(self):
		self.Free = True
		self.Neighbours = []
		self.Cucumber = []