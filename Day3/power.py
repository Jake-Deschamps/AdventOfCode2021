import sys

import numpy as np

bcounts = np.zeros([2, 12])

for line in sys.stdin:
	for i, b in enumerate(line[:-1]):
		#print("{} {}".format(i, b))
		if b == '0':
			bcounts[0,i] += 1
		else:
			bcounts[1,i] += 1
	

gamma = np.argmax(bcounts, axis=0)
gamma_val = sum(d * 2**i for i, d in enumerate(gamma[::-1]))

epsilon = np.argmin(bcounts, axis=0)
epsilon_val = sum(d * 2**i for i, d in enumerate(epsilon[::-1]))

#print(gamma_val)
#print(epsilon_val)

print("The product is {}".format(epsilon_val * gamma_val))