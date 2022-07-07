import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])



#print("numbers is {}".format(numbers))
vents = []
for line in sys.stdin:
	vents.append([int(i) for i in line.strip('\n').replace(' -> ', ',').split(',')])
		#print('made one')
#print(vents)
grid = np.zeros([max(max(vents))+1,max(max(vents))+1])
#print(grid)

for v in vents:
	if v[0] == v[2]:
		for p in range(min(v[1], v[3]),max(v[1], v[3])+1,1):
			grid[v[0], p] += 1
	
	elif v[1] == v[3]:
		for p in range(min(v[0], v[2]),max(v[0], v[2])+1,1):
			grid[p, v[1]] += 1
	else:
		#xs = np.linspace(v[0], v[2], abs(v[2]-v[0]+1))
		#ys = np.linspace(v[1], v[3], abs(v[1]-v[3]+1))
		for x, y in zip(np.linspace(v[0], v[2], abs(v[2]-v[0])+1), np.linspace(v[1], v[3], abs(v[1]-v[3])+1)):
			grid[int(x),int(y)] += 1

print(grid)
print(sum(sum(grid >= 2)))