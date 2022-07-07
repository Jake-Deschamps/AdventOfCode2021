import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])


			

for line in sys.stdin:
	print(line)
	initials = line.strip('\n').split(',')
	crab_inits = [int(i) for i in initials]

for i in range(max(crab_inits)+1):
	total_d = 0
	for c in crab_inits:
		total_d += abs(c - i)
	if i == 0:
		best_d = total_d
		best_i = i
	elif total_d <= best_d:
		best_d = total_d
		
print(best_d)