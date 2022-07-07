import sys

import numpy as np
from statistics import median

CORRUPTSCORE_DICT = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
COMPLETESCORE_DICT = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

def MissingClosers(entry):
	closers = []
	CorruptionScore = 0
	isCorrupt = False
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
				CorruptionScore = CORRUPTSCORE_DICT[c]
		if CorruptionScore > 0:
			#print('corrupt')
			#print(CorruptionScore)
			isCorrupt = True
			return [isCorrupt, CorruptionScore]
	
	#print('notcorrupt')
	closers.reverse()
	#print(closers)
	CompletionScore = 0
	for c in closers:
		CompletionScore *= 5
		CompletionScore += COMPLETESCORE_DICT[c]
	#print(CompletionScore)
	return [isCorrupt, CompletionScore]
		
		
Scores = []
for line in sys.stdin:
	Corrupt, Score = MissingClosers(line)
	if not Corrupt:
		Scores.append(Score)

print(median(Scores))

