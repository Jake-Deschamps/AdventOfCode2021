import sys

from math import floor

template = []
Rules = {}
for line in sys.stdin:
	line = line.strip('\n')
	if '->' in line:
		line = line.split(' -> ')
		Rules[line[0]] = line[1]
	elif line:
		template = line
		
PairCounts = {}
for i in range(len(template)-1):
	pair = template[i:i+2]
	if not pair in PairCounts.keys():
		PairCounts[pair] = 1
	else:
		PairCounts[pair] += 1

FirstChar = template[0]
LastChar = template[-1]


Steps = 40
# print(template)
for s in range(Steps):
	temp_PairCounts = {}
	for p in PairCounts.keys():
		newpairA = p[0] + Rules[p]
		newpairB = Rules[p] + p[1]
		
		if not newpairA in temp_PairCounts.keys():
			temp_PairCounts[newpairA] = PairCounts[p]
		else:
			temp_PairCounts[newpairA] += PairCounts[p]
			
		if not newpairB in temp_PairCounts.keys():
			temp_PairCounts[newpairB] = PairCounts[p]
		else:
			temp_PairCounts[newpairB] += PairCounts[p]
			
	PairCounts = temp_PairCounts
	
# total it all up
LetterCounts = {}
for p in PairCounts.keys():
	if not p[0] in LetterCounts.keys():
		LetterCounts[p[0]] = PairCounts[p]
	else:
		LetterCounts[p[0]] += PairCounts[p]
		
	if not p[1] in LetterCounts.keys():
		LetterCounts[p[1]] = PairCounts[p]
	else:
		LetterCounts[p[1]] += PairCounts[p]
		
for l in LetterCounts.keys():
	fcbonus = 0
	lcbonus = 0
	if FirstChar == l:
		fcbonus = 1
	if LastChar == l:
		lcbonus = 1
		
	LetterCounts[l] = floor((LetterCounts[l] + fcbonus + lcbonus)/2)
		
print(max(LetterCounts.values()) - min(LetterCounts.values()))