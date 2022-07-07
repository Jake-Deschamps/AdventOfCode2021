import sys
import numpy as np
import AmphipodRoom as ar

myRoom = ar.Room()

SpaceDictionary = {}

y = 0
# class
for line in sys.stdin:
	line = line.strip('\n')
	for x, s in enumerate(line):
		if s == '#':
			myRoom.Spaces.append(ar.Space([x, y], 'W'))
		elif s == '.':
			myRoom.Spaces.append(ar.Space([x, y], 'H'))
		elif s in ['A', 'B', 'C', 'D']:
			if x == 3:
				myRoom.Spaces.append(ar.Space([x,y], 'A'))
			elif x == 5:
				myRoom.Spaces.append(ar.Space([x,y], 'B'))
			elif x == 7:
				myRoom.Spaces.append(ar.Space([x,y], 'C'))
			elif x == 9:
				myRoom.Spaces.append(ar.Space([x,y], 'D'))
			myRoom.Spaces[-1].IsOccupied = True
				
			myRoom.Amphipods.append(ar.Amphipod(s, myRoom.Spaces[-1]))
			myRoom.Spaces[-1].Amphipod = myRoom.Amphipods[-1]
		
		
		if s in ['#', 'A', 'B', 'C', 'D', '.']:
			SpaceDictionary[str([x, y])] = myRoom.Spaces[-1]
		
	y += 1

myRoom.AddSpaceDictionary(SpaceDictionary)
	
# giant numpy array version: easier to get what is at a new ??

myRoom.PrintRoom()

myRoom.Step()

print("Finished! Minimum energy is: {}".format(min(myRoom.SuccessfulEnergies)))