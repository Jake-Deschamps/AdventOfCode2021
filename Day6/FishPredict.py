import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])


for line in sys.stdin:
	initials = line.strip('\n').split(',')
	fish = [int(i) for i in initials]

