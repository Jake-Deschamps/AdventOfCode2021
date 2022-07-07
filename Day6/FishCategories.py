import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])


			

for line in sys.stdin:
	initials = line.strip('\n').split(',')
	fish_inits = [int(i) for i in initials]

# fish array, fish with each timer size, 0 to 8
fish = [0,0,0,0,0,0,0,0,0]
for i in fish_inits:
	fish[i] += 1

#sort fish by day number each day the numbers cycledown

for time in range(256):
	newfish = fish[0]
	fish[0] = fish[1]
	fish[1] = fish[2]
	fish[2] = fish[3]
	fish[3] = fish[4]
	fish[4] = fish[5]
	fish[5] = fish[6]
	fish[6] = fish[7]
	fish[7] = fish[8]
	fish[8] = newfish
	fish[6] += newfish
	#print("Day {}: {}".format(time+1, fish))

#print()
#for f in fish:
#	print(f.timer)

print(sum(fish))