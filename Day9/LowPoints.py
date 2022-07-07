import sys

import numpy as np

# find low points in a grid of numbers (locations lower than all bordering via up/down/left/right locations)

temp_array = []
for line in sys.stdin:
	line = line.strip('\n')
	temp_array.append([int(char) for char in line])
	
grid = np.array(temp_array)

nrows, ncols = np.shape(grid)

local_mins = []
for r, row in enumerate(grid):
	for c, char in enumerate(row):
		neighbors = []
		# we have a neighbor below if we are not the (nrow - 1th) row
		if r < nrows - 1:
			neighbors.append(grid[r+1,c])
		# we have a neighbor above if we are not the 0th row
		if r > 0:
			neighbors.append(grid[r-1, c])
		# we have a neighbor right if we are not the (ncol - 1th) column
		if c < ncols - 1:
			neighbors.append(grid[r, c+1])
		# we have a neighbor left if we are not the 0th column
		if c > 0:
			neighbors.append(grid[r, c-1])

		# check to see if ours is lower than all of its neighbors
		if all([char < n for n in neighbors]):
			local_mins.append([char, r, c])
			
print(local_mins)

# get sum of risk
risksum = 0
for val, r, c in local_mins:
	risksum += val+1
	
print(risksum)