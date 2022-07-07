import sys
import Cucumber as C
import numpy as np

building_room = []
cucumbers = [[],[]]
for line in sys.stdin:
	line = line.strip('\n')
	
	to_add = []
	for c in line:
		new_space = C.Space()
		if c in ['v', '>']:
			new_space.Free = False
			if c == 'v':
				new_cucumber = C.Cucumber(new_space, 0)
				cucumbers[0].append(new_cucumber)
			elif c == '>':
				new_cucumber = C.Cucumber(new_space, 1)
				cucumbers[1].append(new_cucumber)
				
			new_space.Cucumber = new_cucumber
		
		to_add.append(new_space)
		
	building_room.append(to_add)
	
myRoom = C.Room(np.array(building_room), cucumbers)

print(myRoom.View())

steps = 0
while myRoom.Step():
	steps += 1
	#print()
	print('Step {}'.format(steps))
	#print(myRoom.View())

steps += 1
print("Completed after {} steps.".format(steps))
#print(myRoom.View())