import sys

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
			print('added literal packet')
			self.ChunkIndex = i
			#self.ChunkIndex = i + 1
			#self.ChunkIndex = self.ChunkIndex + 4 #- self.ChunkIndex%4
			
		else:
			#print('operator')
			temp_IDType = int(self.InputString[self.ChunkIndex+6], 2)
			self.Packets.append(Packet(temp_version, temp_type))
			print('added operator packet')
			# self.OperatorIdTypes.append(IDType)
			if temp_IDType == 0:
				# next 15 bits give the number of bits of the sub-packets
				temp_length = int(self.InputString[self.ChunkIndex+7:self.ChunkIndex+7+15], 2)
				# save the type and the address of the last bit of the last sub-packet
				self.OperatorIDTypes.append([temp_IDType, temp_length+self.ChunkIndex+7+15])
				self.ChunkIndex = self.ChunkIndex+7+15
				
			if temp_IDType == 1:
				temp_subpacketnumber = int(self.InputString[self.ChunkIndex+7:self.ChunkIndex+7+11], 2)
				self.OperatorIDTypes.append([temp_IDType, temp_subpacketnumber])
				self.ChunkIndex = self.ChunkIndex+7+11
	

for line in sys.stdin:
	line = line.strip('\n')
	InputHex = line
	
InputBinary = ''

for c in InputHex:
	InputBinary += format(int(c, 16), "04b")
	
myParser = Parser(InputBinary)
for p in myParser.Packets:
	print("Version {}, Type {}".format(p.Version, p.Type))
	if p.Type == 4:
		print(p.Value)
		
print("Version Sum is {}".format(myParser.VersionSum))