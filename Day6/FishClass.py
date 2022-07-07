import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])

class Lantern:
	def __init__(self, timer = 8):
		self.timer = timer
		
	def cycle(self):
		self.timer -= 1
		if  self.timer == -1:
			self.timer = 6
			return Lantern()
			

for line in sys.stdin:
	initials = line.strip('\n').split(',')
	fish = [Lantern(int(i)) for i in initials]




# https://www.kite.com/python/answers/how-to-append-elements-to-a-list-while-iterating-over-the-list-in-python
for time in range(256):
	print(time)
	print(len(fish))
	for i in range(len(fish)):
		#print(fish[i].timer)
		temp = fish[i].cycle()
		if temp:
			fish.append(temp)
	#print()
	#print("Day {}: {}".format(time+1, [fish[i].timer for i in range(len(fish))]))

#print()
#for f in fish:
#	print(f.timer)

print(len(fish))