import sys
import ALU_Expression_backup as ALU
from time import sleep


InstructionsFilename = 'verify_model.txt'
#InstructionsFilename = 'test_binary.txt'
#InstructionsFilename = 'test_Input.txt'

Instructions = []
with open(InstructionsFilename) as f:
	for line in f.readlines():
		line = line.strip('\n')
		Instructions.append(line)
	

trying = 'abcdefghijklmn'


char_index = 0
for i, l in enumerate(Instructions):
	
	if 'inp' in l:
		Instructions[i] += ' ' + trying[char_index]
		char_index += 1

myAnalyzer = ALU.ALU_Solver(Instructions)
print()
print("Final Results")
print(myAnalyzer.FinalExpressions)