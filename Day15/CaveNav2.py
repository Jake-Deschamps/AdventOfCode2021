import sys
import numpy as np

rows = []
for line in sys.stdin:
	line = line.strip('\n')
	rows.append([int(c) for c in line])
	
MazeTile = np.array(rows)
tx, ty = MazeTile.shape
Maze = np.zeros([MazeTile.shape[0]*5,MazeTile.shape[1]*5])
MazeDims = np.shape(Maze)

for r in range(9):
	temp_MazeTile = (MazeTile - 1 + r) % 9 + 1
	space = np.array([0, ty*r])
	while(space[1] >= 0):
		sx, sy = space
		if all(space < MazeDims):
			Maze[sx:sx+tx, sy:sy+ty] = temp_MazeTile
		space += np.array([tx, -ty])
	

#print(Maze)
MazeSums = np.zeros(np.shape(Maze))
running_total = 0

# print(Maze)
# lap 1
for r in range(1,(MazeDims[0]-1)+(MazeDims[1]-1)+1,1):
	space = np.array([0, r])
	while(space[1] >= 0):
		sx, sy = space
		if all(space < MazeDims):
			#print("{} has value {}".format(space, Maze[sx, sy]))
			#print('neighbors')
			if space[0] == 0:
				#print(Maze[sx, sy-1])
				MazeSums[sx, sy] = Maze[sx, sy] + MazeSums[sx, sy-1]
			elif space[1] == 0:
				#print(Maze[sx-1, sy])
				MazeSums[sx, sy] = Maze[sx, sy] + MazeSums[sx-1, sy]
			else:
				#print(Maze[sx-1, sy])
				#print(Maze[sx, sy-1])
				MazeSums[sx, sy] = Maze[sx, sy] + min(MazeSums[sx, sy-1], MazeSums[sx-1, sy])
			
		space += np.array([1,-1])
print(MazeSums)	

	
#make more laps checking all neighbors
Done = False
s = 1
while not Done:
	s += 1
	temp_MazeSums = MazeSums.copy()
	for r in range(1,(MazeDims[0]-1)+(MazeDims[1]-1)+1,1):
		space = np.array([0, r])
		while(space[1] >= 0):
			sx, sy = space
			if all(space < MazeDims):
				#print("{} has value {}".format(space, Maze[sx, sy]))
				#print('neighbors')
				# print(space)
				options = []
				if not space[0] == 0: options.append(MazeSums[sx-1, sy])
				if not space[1] == 0: options.append(MazeSums[sx, sy-1])
				if not space[0] >= MazeDims[0]-1: options.append(MazeSums[sx+1, sy])
				if not space[1] >= MazeDims[1]-1: options.append(MazeSums[sx, sy+1])

				MazeSums[sx, sy] = Maze[sx, sy] + min(options)
			
			space += np.array([1,-1])
	print("Lap {}".format(s))
	print(MazeSums)
	#print(MazeSums == temp_MazeSums)
	if (MazeSums == temp_MazeSums).all():
		Done = True

print("Minimal risk is {}".format(MazeSums[MazeDims[0]-1, MazeDims[1]-1]))

#print(Maze[test_mask>0])
#print(Maze)
# pick path thinking always forward and one move ahead
#while not Solver == Goal:
#	temp_dist = Goal - Solver
#	option_tots = []
#	if temp_dist[0] > 0:
#		if temp_dist[0] > 1 and temp_dist[1] > 0:
#			option_tots.append(Maze[Solver[0]+1, Solver[1]] + min(Maze[Solver[0]+2, Solver[1]], Maze[Solver[0]+1, Solver[1]+1]))
#			# this seems like an if then nightmare.

# Perhaps a backtracking algorithm: too massive

# for each square, find the smallest sum of all of the ways to reach that path?
# inspired by https://www.youtube.com/watch?v=k82-JehAQD8 i think