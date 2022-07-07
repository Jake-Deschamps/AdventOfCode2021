import sys

import numpy as np

SCORE_DICT = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}

def CorruptionCheck(entry):
	closers = []
	CorruptionScore = 0
	for c in entry:
		if c == '(':
			closers.append(')')
		if c == '[':
			closers.append(']')
		if c == '{':
			closers.append('}')
		if c == '<':
			closers.append('>')
		if c in ['>', '}', ']', ')']:
			if c == closers[-1]:
				closers.pop(-1)
			else:
				CorruptionScore = SCORE_DICT[c]
		if CorruptionScore > 0:
			break
	# print(CorruptionScore)
	return CorruptionScore


scoretot = 0
for line in sys.stdin:
	line = line.strip('\n')
	scoretot += CorruptionCheck(line)
	
print(scoretot)