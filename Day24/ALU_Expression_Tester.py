import sys
from ALU_Expression import ALU_Ex
from time import sleep

myALU = ALU_Ex()

InstructionsFilename = 'verify_model.txt'
#InstructionsFilename = 'test_binary.txt'
#InstructionsFilename = 'test_Input.txt'

Instructions = []
with open(InstructionsFilename) as f:
	for line in f.readlines():
		line = line.strip('\n')
		Instructions.append(line)
	

trying = 'abcdefghijklmn'

Working = True
while Working:

	chars = str(trying)
	if not '0' in chars:
		print(chars)
		char_index = 0
		for l in Instructions:
			
			if 'inp' in l:
				l += ' ' + chars[char_index]
				#print(chars[char_index])
				#print(l)
				char_index += 1
			print(l)
			myALU.ParseLine(l)
			print(myALU.View())
			
	print(type(myALU.View()[-1]))
	myALU.Reset()
	sys.exit()