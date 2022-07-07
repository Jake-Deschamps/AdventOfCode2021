import sys

import numpy as np

clues = []
outputs = []
for line in sys.stdin:
	line = line.strip('\n')
	[clue, output] = line.split(' | ')
	clues.append(clue.split(' '))
	outputs.append(output.split(' '))

	# ty kite again https://www.kite.com/python/answers/how-to-find-the-index-of-list-elements-that-meet-a-condition-in-python

bigsum = 0
for c, o in zip(clues, outputs):
	# sort all in c and o
	c_sorted = [sorted(d) for d in c]
	o_sorted = [sorted(d) for d in o]
	#print(c_sorted)
	digits = ['','','','','','','','','','']
	
	# get 1, 4, 7, 8
	digits[1] = c_sorted.pop([idx for idx, element in enumerate(c_sorted) if len(element) == 2][0])
	
	digits[4] = c_sorted.pop([idx for idx, element in enumerate(c_sorted) if len(element) == 4][0])
	
	digits[7] = c_sorted.pop([idx for idx, element in enumerate(c_sorted) if len(element) == 3][0])
	
	digits[8] = c_sorted.pop([idx for idx, element in enumerate(c_sorted) if len(element) == 7][0])
	
	# get 6, 9, 0
	digits[6] = c_sorted.pop([(not all(elim in c for elim in digits[1])) and len(c) == 6 for c in c_sorted].index(True))
	
	digits[9] = c_sorted.pop([(all(elim in c for elim in digits[4])) and len(c) == 6 for c in c_sorted].index(True))
	
	digits[0] = c_sorted.pop([len(c) == 6 for c in c_sorted].index(True))
	
	# get 3, 5, 2
	digits[3] = c_sorted.pop([(all(elim in c for elim in digits[1])) and len(c) == 5 for c in c_sorted].index(True))
	
	digits[5] = c_sorted.pop([(all(elim in digits[9] for elim in c)) and len(c) == 5 for c in c_sorted].index(True))
	#print(c_sorted)
	digits[2] = c_sorted.pop([len(c) == 5 for c in c_sorted].index(True))
	
	temp_out = ''
	
	#print(o_sorted[1])
	for d in o_sorted:
		temp_out = temp_out + str(digits.index(d))
		
	bigsum += int(temp_out)
	#print(c_sorted)
	#print('')
print(bigsum)