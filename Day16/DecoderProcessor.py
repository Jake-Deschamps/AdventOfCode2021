import sys
from functools import reduce
import operator

class Packet:
	def __init__(self, Version, Type, Value = 0):
		self.Version = Version
		self.Type = Type
		if Type == 4:
			self.Value = Value
		else:
			self.Subpackets = []
		
		
		
	def AddSubpacket(self, Subpacket):
		self.Subpackets.append(Subpacket)
		
		
class Parser:
	def __init__(self, InputString):
		self.InputString = InputString
		self.Packets = []
		
		self.ChunkIndex = 0
		self.VersionSum = 0
		
		self.OperatorIDTypes = []
		self.Parents=[]
		
		self.ParseString(InputString)
		
		self.FinalValue = self.Solve(self.Packets[0])
		
	def ParseString(self, InputString):
		while (not self.ChunkIndex >= len(self.InputString)) and not int(self.InputString[self.ChunkIndex:],2) == 0:
			#print(self.ChunkIndex)
			#print(len(self.InputString))
			self.ParsePacket()
	
	def ParsePacket(self):
		temp_version = int(self.InputString[self.ChunkIndex:self.ChunkIndex+3], 2)
		self.VersionSum += temp_version
		temp_type = int(self.InputString[self.ChunkIndex+3:self.ChunkIndex+6], 2)
		#print(temp_type)
		
		if self.OperatorIDTypes:
			print('ID Chain {}'.format(self.OperatorIDTypes))
			popping = True
			while popping:
				if self.OperatorIDTypes[-1][1] <= 0:
					self.OperatorIDTypes.pop(-1)
					self.Parents.pop(-1)
				else:
					popping = False
		
		if temp_type == 4:
			#print('literal')
			i = self.ChunkIndex + 6
			temp_literal = ''
			DoneProcessing = False
			while not DoneProcessing:
				temp_literal += self.InputString[i+1:i+5]
				if int(self.InputString[i], 2) == 0:
					DoneProcessing = True
				i += 5
			temp_value = int(temp_literal, 2)
			self.Packets.append(Packet(temp_version, temp_type, temp_value))
			#print('added literal packet')
			#self.ChunkIndex = i + 1
			#self.ChunkIndex = self.ChunkIndex + 4 #- self.ChunkIndex%4
			
			if self.OperatorIDTypes:
				self.Parents[-1].AddSubpacket(self.Packets[-1])
				for id in self.OperatorIDTypes:
					if id[0] == 0:
						id[1] -= (i-self.ChunkIndex)
			
			#if self.OperatorIDTypes:
			#	self.Parents[-1].AddSubpacket(self.Packets[-1])
			#	if self.OperatorIDTypes[-1][0] == 0:
			#		self.OperatorIDTypes[-1][1] -= (i-self.ChunkIndex)

				if self.OperatorIDTypes[-1][0] == 1:
					self.OperatorIDTypes[-1][1] -= 1
					
				#if self.OperatorIDTypes[-1][1] <= 0:
					#self.OperatorIDTypes.pop(-1)
					#self.Parents.pop(-1)
			print('Packet no. {} Version {} Type {} Value {}'.format(len(self.Packets), self.Packets[-1].Version, self.Packets[-1].Type, self.Packets[-1].Value))
			#print('ID Chain {}'.format(self.OperatorIDTypes))
			self.ChunkIndex = i
			
		else:
			#print('operator')
			temp_IDType = int(self.InputString[self.ChunkIndex+6], 2)
			self.Packets.append(Packet(temp_version, temp_type))
			if self.OperatorIDTypes:
				self.Parents[-1].AddSubpacket(self.Packets[-1])
				
			#print('added operator packet')
			if temp_IDType == 0:
				# next 15 bits give the number of bits of the sub-packets
				temp_length = int(self.InputString[self.ChunkIndex+7:self.ChunkIndex+7+15], 2)
				print("packet string {} gives size {}".format(self.InputString[self.ChunkIndex:self.ChunkIndex+7+15], temp_length))
				# Interact with IDTypes
				if self.OperatorIDTypes:
					for id in self.OperatorIDTypes:
						if id[0] == 0:
							id[1] -= 22
			
				
					#if self.OperatorIDTypes[-1][0] == 0:
					#	self.OperatorIDTypes[-1][1] -= 22

					if self.OperatorIDTypes[-1][0] == 1:
						self.OperatorIDTypes[-1][1] -= 1
					
					#if self.OperatorIDTypes[-1][1] <= 0:
						#self.OperatorIDTypes.pop(-1)
						#self.Parents.pop(-1)
				
				
				# save the type and the address of the last bit of the last sub-packet
				#print('Packet no. {} Version {} Type {}'.format(len(self.Packets), self.Packets[-1].Version, self.Packets[-1].Type))
				#print('ID Chain {}'.format(self.OperatorIDTypes))
				# OLD WAY THAT ENDS AT LAST BIT INSTEAD OF ITERATING self.OperatorIDTypes.append([temp_IDType, temp_length+self.ChunkIndex+7+15])
				self.OperatorIDTypes.append([temp_IDType, temp_length])
				self.Parents.append(self.Packets[-1])
				self.ChunkIndex = self.ChunkIndex+7+15
				
			if temp_IDType == 1:
				# next 11 bits give the number of the subpackets
				temp_subpacketnumber = int(self.InputString[self.ChunkIndex+7:self.ChunkIndex+7+11], 2)
				
				if self.OperatorIDTypes:
					for id in self.OperatorIDTypes:
						if id[0] == 0:
							id[1] -= 18
					#if self.OperatorIDTypes[-1][0] == 0:
					#	self.OperatorIDTypes[-1][1] -= 18

					if self.OperatorIDTypes[-1][0] == 1:
						#print('reduced {}'.format(self.OperatorIDTypes[-1]))
						self.OperatorIDTypes[-1][1] -= 1
						#print('to {}'.format(self.OperatorIDTypes[-1]))
					
					#if self.OperatorIDTypes[-1][1] <= 0:
						#self.OperatorIDTypes.pop(-1)
						#self.Parents.pop(-1)
				print('Packet no. {} Version {} Type {}'.format(len(self.Packets), self.Packets[-1].Version, self.Packets[-1].Type))
				#print('ID Chain {}'.format(self.OperatorIDTypes))
				self.OperatorIDTypes.append([temp_IDType, temp_subpacketnumber])
				self.Parents.append(self.Packets[-1])
				self.ChunkIndex = self.ChunkIndex+7+11
				
		
				
				
	def Solve(self, Packet):
		print('Analyzing packet version: {} type: {}'.format(Packet.Version, Packet.Type))
		if Packet.Type == 4:
			return Packet.Value
		
		else:
			temp_values = []
			for s in Packet.Subpackets:
				temp_values.append(self.Solve(s))
		
			# Sum
			if Packet.Type == 0:
				return sum(temp_values)
			
			# Product
			if Packet.Type == 1:
				return reduce(operator.mul, temp_values, 1) #https://stackoverflow.com/questions/63727929/pycharm-module-math-has-no-attribute-prod
	
			# Minimum
			if Packet.Type == 2:
				return min(temp_values)
				
			# Maximum
			if Packet.Type == 3:
				return max(temp_values)

			# Greater Than
			if Packet.Type == 5:
				#print(temp_values)
				print('Comparison for packet version: {} type: {}'.format(Packet.Version, Packet.Type))
				if temp_values[0] > temp_values[1]:
					return 1
				else:
					return 0
					
			# Less Than
			if Packet.Type == 6:
				if temp_values[0] < temp_values[1]:
					return 1
				else:
					return 0
					
			# Equal To
			if Packet.Type == 7:
				if temp_values[0] == temp_values[1]:
					return 1
				else:
					return 0
					
			
				
				
				
for line in sys.stdin:
	line = line.strip('\n')
	InputHex = line
	
InputBinary = ''

for c in InputHex:
	InputBinary += format(int(c, 16), "04b")
	
myParser = Parser(InputBinary)

#print(len(myParser.Packets))

#for p in myParser.Packets:
	#print("Version {}, Type {}".format(p.Version, p.Type))
	#if p.Type == 4:
		#print(p.Value)
	
		
print("Version Sum is {}".format(myParser.VersionSum))

print("Final Value is {}".format(myParser.FinalValue))