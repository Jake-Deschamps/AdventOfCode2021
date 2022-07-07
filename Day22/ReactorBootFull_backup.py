import sys
import numpy as np

class Cuboid:
	def __init__(self, xs, ys, zs, type):
		self.xs = xs
		self.ys = ys
		self.zs = zs
		
		self.type = type
		
		
	def GetVolume(self):
		l = self.xs[1] + 1 - self.xs[0]
		w = self.ys[1] + 1 - self.ys[0]
		h = self.zs[1] + 1 - self.zs[0]
		return l*w*h
		
	def CheckNSolveCollision(self, C2): # Use this to remove. This can be repurposed when adding
		# detect collision
		x_int = False
		if (C2.xs[0] <= self.xs[0]) and (self.xs[0] <= C2.xs[1] <= self.xs[1]): #Case 1
			x_int = True
			xCase = 1
			
		elif (C2.xs[0] <= self.xs[0]) and (self.xs[1] <= C2.xs[1]): #Case 2
			x_int = True
			xCase = 2
			
		elif (self.xs[0] <= C2.xs[0] <= self.xs[1]) and (self.xs[1] <= C2.xs[1]) #Case 3
			x_int = True
			xCase = 3
			
		elif (self.xs[0] <= C2.xs[0] <= self.xs[1]) and (self.xs[0] <= C2.xs[1] <= self.xs[1]) #Case 4
			x_int = True
			xCase = 4
			
		# Is there a way to just make the algorithm so that nothing happens if there is no intersection
		# return a new set of cuboids if intersecting, return 
		
		

Steps = []

for line in sys.stdin:
	line = line.strip('\n')
	toggle, rest = line.split(' ')
	xs, ys, zs = rest.split(',')
	xs = xs.strip('x=')
	x1, x2 = [int(c) for c in xs.split('..')]
	ys = ys.strip('y=')
	y1, y2 = [int(c) for c in ys.split('..')]
	zs = zs.strip('z=')
	z1, z2 = [int(c) for c in zs.split('..')]
	Steps.append([toggle, x1, x2, y1, y2, z1,z2])


Reactor = np.zeros([101,101,101])

for t, x1, x2, y1, y2, z1, z2 in Steps:
	if all([C>=-50 and C<=50 for C in [x1, x2, y1, y2, z1, z2]]):
		dx = x2 - x1 + 1
		dy = y2 - y1 + 1
		dz = z2 - z1 + 1
		
		if t == 'on':
			temp = np.ones([dx, dy, dz])
		else:
			temp = np.zeros([dx, dy, dz])
			
		Reactor[x1+50: x2+50+1, y1+50: y2+50+1, z1+50: z2+50+1] = temp
	
print(sum(sum(sum(Reactor))))