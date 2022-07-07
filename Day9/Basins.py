import sys

import numpy as np

# Find all basins
# Find local mins first
# Spread out from local mins until reaching a 9

def Get_Neighbors(position,size, grid):
	r, c = position
	nrows, ncols = size
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
		
	return neighbors
	
def Get_Neighbors_wCoords(position, grid):
	r, c = position
	nrows, ncols = np.shape(grid)
	neighbors = []
	# we have a neighbor below if we are not the (nrow - 1th) row
	if r < nrows - 1:
		neighbors.append([grid[r+1,c], [r+1,c]])
	# we have a neighbor above if we are not the 0th row
	if r > 0:
		neighbors.append([grid[r-1, c], [r-1, c]])
	# we have a neighbor right if we are not the (ncol - 1th) column
	if c < ncols - 1:
		neighbors.append([grid[r, c+1], [r, c+1]])
	# we have a neighbor left if we are not the 0th column
	if c > 0:
		neighbors.append([grid[r, c-1], [r, c-1]])
		
	return neighbors

class Basin:
	def __init__(self, start_point, grid):
		self.start_point = start_point
		self.grid = grid
		self.size = 0
		self.Build(self.start_point)
		
	def Build(self, test_point):
		# make sure this hasn't been set anywhere else
		if self.grid[test_point[0], test_point[1]] < 9:
			self.size += 1
			self.grid[test_point[0], test_point[1]] = 9 # set 9 to the current location
			neighbors = Get_Neighbors_wCoords(test_point, self.grid)
			#print("Found neighbors {}".format(neighbors))
			#print(self.grid)
			for val, position in neighbors:
				if val < 9:
					self.Build(position)


	
def main():
	temp_array = []
	for line in sys.stdin:
		line = line.strip('\n')
		temp_array.append([int(char) for char in line])
	
	grid = np.array(temp_array)

	nrows, ncols = np.shape(grid)

	local_mins = []
	walls = []
	for r, row in enumerate(grid):
		for c, char in enumerate(row):
			neighbors = Get_Neighbors([r, c], [nrows, ncols], grid)
	
			# check to see if ours is lower than all of its neighbors
			if all([char < n for n in neighbors]):
				local_mins.append([char, [r, c]])
			#if all([char > n for n in neighbors]):
			#	walls.append([char, r, c])
	print(local_mins)
	
# build out basins until hitting a 9
	basin_sizes = []
	for val, position in local_mins:
		b_temp = Basin(position, grid)
		basin_sizes.append(b_temp.size)
	
	# get top 3
	top_mult = 1
	top_mult *= basin_sizes.pop(basin_sizes.index(max(basin_sizes)))
	top_mult *= basin_sizes.pop(basin_sizes.index(max(basin_sizes)))
	top_mult *= basin_sizes.pop(basin_sizes.index(max(basin_sizes)))
	print(top_mult)

main()
