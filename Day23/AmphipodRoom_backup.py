# can amphipods move simultaneously?

import sys
from time import sleep

def isNeighboring(s1, s2):
	c1 = s1.Coords
	c2 = s2.Coords
	if c1[0] == c2[0] and abs(c1[1] - c2[1]) == 1:
		return True
	elif c1[1] == c2[1] and abs(c1[0] - c2[0]) == 1:
		return True
	else:
		return False

class Room:
	def __init__(self):
		self.Spaces = []
		self.Amphipods = []
		self.Energy = 0
		self.Steps = 0
		self.SuccessfulEnergies = [999_999_999]
		
		self.States = {}
		
		self.StatusLogs = []
		
		self.AnalysisIndex = 0
	
	def AddSpaceDictionary(self, sd):
		self.SpaceDict = sd
		
	def DetermineAccessibleSpaces(self, amph):
		# fortunately for this configuration, we only need a combo move [u/d] then [l/r]
		space = amph.Space
		adj_space_list = []
		
		Working = True
		while Working:
			Working = False
			for a in [space] + adj_space_list:
				for s in self.Spaces:
					if isNeighboring(s, a) and s not in adj_space_list + [space]:
						if not s.Type == 'W' and not s.IsOccupied:
						
							adj_space_list.append(s)
							Working = True
						
		return adj_space_list
		
	def Step(self):
		
		self.Steps += 1
		
		#self.StatusLogs.append("Step: {} Energy: {}.".format(self.Steps, self.Energy))
		
		temp_state = self.GetState()
		try_it = False
		if temp_state not in self.States:
			try_it = True
		elif self.Energy < self.States[temp_state]:
			try_it = True
			
		if try_it:
			self.States[temp_state] = self.Energy
			
			
			
			#self.AnalysisIndex += 1
			#print(self.AnalysisIndex)
			#if len(self.SuccessfulEnergies) > 0:
			#	print("Current minimum energy {}".format(min(self.SuccessfulEnergies)))
			
			
			#print("Step: {} Energy: {}.".format(self.Steps, self.Energy))
			
			
			#if len(self.SuccessfulEnergies) > 0:
			#	print("Current minimum energy {}".format(min(self.SuccessfulEnergies)))
			#self.PrintRoom()
			#sleep(2)
			for a in self.Amphipods:
				#print(a.MovesLeft)
				if (not a.IsDone) and (a.MovesLeft > 0):
					#print("Type {} has {} moves left".format(a.Type, a.MovesLeft))
					for s in self.DetermineAccessibleSpaces(a):
						if s.Stoppable:
							if a.MovesLeft == 1: # make a thing so it doesnt step partway in?
								if s.Type == a.Type:
									prev_space = a.Space
									self.MoveTo(a, s) # do the energy check here?
									self.LogRoom()
									self.Step()
									#for _ in range(10):
									#	self.StatusLogs.pop(-1)
									self.UndoMove(a, prev_space)
							else:
								if s.Type == 'H':
									prev_space = a.Space
									self.MoveTo(a, s)
									self.LogRoom()
									self.Step()
									#for _ in range(10):
									#	self.StatusLogs.pop(-1)
									self.UndoMove(a, prev_space)
							
							
			if all([a.IsDone for a in self.Amphipods]):
				print("Im done! Energy used: {}".format(self.Energy))
				# sys.exit()
				#self.SuccessfulEnergies.append(self.Energy)
				#self.PrintRoom()
				#for l in self.StatusLogs:
				#	print(l)
				#sys.exit()
				
			
			
			#self.StatusLogs.pop(-1)
			
		if all([a.IsDone for a in self.Amphipods]):
			#self.PrintRoom()
			print("Im done! Energy used: {}".format(self.Energy))
			self.SuccessfulEnergies.append(self.Energy)
			
			#for l in self.StatusLogs:
			#	print(l)
			
			#if self.Energy == 12721: sys.exit()
		
		#self.StatusLogs.pop(-1)
		self.Steps -= 1	
		
	def MoveTo(self, amph, destination):
		amph.Space.IsOccupied = False
		destination.IsOccupied = True
		
		dx = abs(amph.Space.Coords[0] - destination.Coords[0])
		dy = abs(amph.Space.Coords[1] - destination.Coords[1])
		self.Energy += amph.Energy*(dx + dy)
		
		amph.Space = destination
		amph.Coords = destination.Coords
		destination.Amphipod = amph
		amph.MovesLeft -= 1
		amph.UpdateDone()
		
	def UndoMove(self, amph, destination):
		amph.Space.IsOccupied = False
		destination.IsOccupied = True
		
		dx = abs(amph.Space.Coords[0] - destination.Coords[0])
		dy = abs(amph.Space.Coords[1] - destination.Coords[1])
		self.Energy -= amph.Energy*(dx + dy)
		
		amph.Space = destination
		amph.Coords = destination.Coords
		destination.Amphipod = amph
		amph.MovesLeft += 1
		amph.UpdateDone()
		
	def PrintRoom(self):
		for y in range(10):
			line = ''
			for x in range(20):
				if str([x, y]) in self.SpaceDict:
					if not self.SpaceDict[str([x, y])].IsOccupied:
						#line += self.SpaceDict[str([x, y])].Type
						if self.SpaceDict[str([x, y])].Type == 'W': line += '#'
						else: line += '.'
					else:
						line += self.SpaceDict[str([x, y])].Amphipod.Type
				else:
					line += ' '
			print(line)
			
	def LogRoom(self):
		for y in range(10):
			line = ''
			for x in range(20):
				if str([x, y]) in self.SpaceDict:
					if not self.SpaceDict[str([x, y])].IsOccupied:
						#line += self.SpaceDict[str([x, y])].Type
						if self.SpaceDict[str([x, y])].Type == 'W': line += '#'
						else: line += '.'
					else:
						line += self.SpaceDict[str([x, y])].Amphipod.Type
				else:
					line += ' '
			self.StatusLogs.append(line)
		
	def GetState(self):
		message = ''
		for y in range(10):
			line = ''
			for x in range(20):
				if str([x, y]) in self.SpaceDict:
					if not self.SpaceDict[str([x, y])].IsOccupied:
						#line += self.SpaceDict[str([x, y])].Type
						if self.SpaceDict[str([x, y])].Type == 'W': line += '#'
						else: line += '.'
					else:
						line += self.SpaceDict[str([x, y])].Amphipod.Type
				else:
					line += ' '
			line += '\n'
			message += line
		return message
		
class Space:
	def __init__(self, coords, type):
		self.Coords = coords
		self.IsOccupied = False
		self.Amphipod = []
		self.Type = type
		if self.Type == 'H' and self.Coords[0] in [3, 5, 7, 9]:
			self.Stoppable = False
		else:
			self.Stoppable = True
			
		if self.Coords[1] == 3:
			self.Bottom = True
		else:
			self.Bottom = False
		
		
class Amphipod:
	def __init__(self, type, space):
		self.Space = space
		self.MovesLeft = 2
		self.Type = type
		
		if self.Type == 'A':
			self.Energy = 1
		elif self.Type == 'B':
			self.Energy = 10
		elif self.Type == 'C':
			self.Energy = 100
		elif self.Type == 'D':
			self.Energy = 1000
			
		self.IsDone = False
		
		self.UpdateDone()
		
	def UpdateDone(self):
		if (self.Type == self.Space.Type) and (self.Space.Bottom or self.MovesLeft == 0): # Currently does not detect if a hallway starts fully solved
			self.IsDone = True
			
		else:
			self.IsDone = False