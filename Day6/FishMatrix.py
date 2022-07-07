import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])


			

for line in sys.stdin:
	initials = line.strip('\n').split(',')
	fish = [int(i) for i in initials]

fish = np.array(fish)


for time in range(256):
	print(time)
	fish = fish - np.ones(np.size(fish))
	new_fish = sum(fish == -1)
	#print(new_fish)
	fish[fish == -1] = 6
	fish = np.append(fish, 8*np.ones([1, new_fish]))
	#print("Day {}: {}".format(time+1, fish))

#print()
#for f in fish:
#	print(f.timer)

print(np.size(fish))