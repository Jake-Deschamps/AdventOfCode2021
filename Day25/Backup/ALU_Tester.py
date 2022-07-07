import sys
from ALU import ALU

myALU = ALU()

InstructionsFilename = 'verify_model.txt'

Instructions = []
with open(InstructionsFilename) as f:
	for line in f.readlines():
		line = line.strip('\n')
		Instructions.append(line)
	
for l in Instructions:
	print(l)
	myALU.ParseLine(l)
	
print(myALU.View())