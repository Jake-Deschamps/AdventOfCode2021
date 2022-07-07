import sys
from ALU import ALU
from time import sleep

myALU = ALU()

InstructionsFilename = 'verify_model.txt'
#InstructionsFilename = 'test_binary.txt'

Instructions = []
with open(InstructionsFilename) as f:
	for line in f.readlines():
		line = line.strip('\n')
		Instructions.append(line)
	

# maybe try tweaking a digit and see if the change moves z_f closer of further from 0
# the issue is that these functions are not necessarily continuous, particularly mod and eql
# might be worth a shot considering
	
trying = 99999999999999
#trying = 99999999944441 # a 14-digit prime number
#trying = 13579246899999
#trying = 1

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
			#print(l)
			myALU.ParseLine(l)
			print(myALU.View())
			
		if myALU.View()[-1] == 0:
			print('success! ' + chars)
			sys.exit()
			
	trying -= 1
	myALU.Reset()
	sys.exit()