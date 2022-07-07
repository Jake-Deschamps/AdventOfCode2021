import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])

# just identify the amount of times the simple digits (1 - 2 segs, 4 - 4 segs, 7 - 3 segs, 8 - 7 segs) appear in the output


digits = []
for line in sys.stdin:
	line = line.strip('\n')
	line = line.split(' | ')[1]
	digits.append(line.split(' '))

	
count = 0
for c in digits:
	for s in c:
		if len(s) in [2, 4, 3, 7]: count += 1

print(count)