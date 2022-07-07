from itertools import product
import numpy as np

class Cuboid:
	def __init__(self, xs, ys, zs, type):
		self.xs = xs
		self.ys = ys
		self.zs = zs
		#vs = product(xs, ys, zs)
		#print(vs)
		self.vs = [np.array(list(v)) for v in product(self.xs, self.ys, self.zs)] # create all vertices
		
		self.type = type
		
		
	def GetVolume(self):
		l = self.xs[1] + 1 - self.xs[0]
		w = self.ys[1] + 1 - self.ys[0]
		h = self.zs[1] + 1 - self.zs[0]
		return l*w*h

	def IsInside(self, point):
		# True if point [x, y, z] is inside this cuboid
		if all(self.vs[0] <= point) and all(point <= self.vs[-1]):
			return True
		else:
			return False
		
	def CheckNSolveCollision(self, C2): # Use this to remove. This can be repurposed when adding
		# check if c2 consumes c1, just return c2 and destroy c1. if c1 consumes c2 its more complicated.
		
		if C2.IsInside(self.vs[0]):#all(C2.vs[0] <= self.vs[0]) and all(self.vs[0] <= C2.vs[-1]): # if first vertex is within C2
			# this is the tough bit, what do I try instead?
			# go in the +x direction until you are out of C2
				# once you leave, mark the xyz location.
				# continue in the +x until you reach the boundary of the original cuboid. mark this position
				# go from each point in the +y until you reach the boundary of the original cuboid c1 OR until you reach the edge of c2
				# if you reached the end of c1
					# repeat the process for the z direction (+z until you reach the end of c1 or c2)
				# if you reached the edge c2
					# go back to the original x but with this new y
					# draw rectangle from there
					
				
				
				# if you never leave C2 this method, try the +y from the original location
			
			pass
		else: # if first vertex is not inside C2
			V1 = self.vs[0]
			# try to extend along first dimension what do we hit? The boundary of c2 or the far edge of c1?
			if all(C2.vs[0] <= V1) and all(self.vs[0] <= C2.vs[-1]): # if the extension of x is in C2
				pass