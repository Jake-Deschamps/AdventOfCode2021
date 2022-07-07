from itertools import product
import numpy as np

class Cuboid:
	def __init__(self, xs, ys, zs):
		self.xs = xs
		self.ys = ys
		self.zs = zs
		#vs = product(xs, ys, zs)
		#print(vs)
		self.vs = [np.array(list(v)) for v in product(self.xs, self.ys, self.zs)] # create all vertices
		
		#self.type = type
		
		
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
		
	def Collision(self, c2): # Use this to remove. This can be repurposed when adding
		# make sure there is collision first

		# test simple cases first!
		
		# if there *is* collision
		temp_cuboid_array = []
		if self.zs[0] < c2.zs[0]: # if self exists above c2
			temp_cuboid_array.append(Cuboid(self.xs, self.ys, [self.zs[0], c2.zs[0]-1]))# c1.xs, c1.ys, [c1.z1[0] c2.zs[0]]-1 # the full floor
		if c2.zs[1] < self.zs[1]:# if self exists below
			temp_cuboid_array.append(Cuboid(self.xs, self.ys, [c2.zs[1]+1, self.zs[1]]))# c1.xs, c1.ys, [c2.zs[1]+1, c1.zs[1]] # the full ceiling
		if max(self.zs[0], c2.zs[0]) <= min(self.zs[1], c2.zs[1]):
			if (self.xs[0] < c2.xs[0]): # and (SELF_WITHIN_C2 Z SPANS):# if self exists strictly left of c2 AND w/in it's z spans
				# use the max of c2.zs[0] and self.zs[0] and the min of c2.zs[1] and self.zs[1]
				temp_cuboid_array.append(Cuboid([self.xs[0], c2.xs[0]-1], self.ys, [max(self.zs[0], c2.zs[0]), min(self.zs[1], c2.zs[1])]))# [c1.xs[0], c2.xs[0]-1], c1.ys, c2.zs # the left hall
			if c2.xs[1] < self.xs[1]:# for c1 right of c2
				temp_cuboid_array.append(Cuboid([c2.xs[1]+1, self.xs[1]], self.ys, [max(self.zs[0], c2.zs[0]), min(self.zs[1], c2.zs[1])]))# [c2.xs[1]+1, c1.xs[1]], c1.ys, c2.zs # the right hall
			if max(self.xs[0], c2.xs[0]) <= min(self.xs[1], c2.xs[1]):
				if self.ys[0] < c2.ys[0]:# for c1 in front of c2
					temp_cuboid_array.append(Cuboid([max(self.xs[0], c2.xs[0]), min(self.xs[1], c2.xs[1])], [self.ys[0], c2.ys[0]-1], [max(self.zs[0], c2.zs[0]), min(self.zs[1], c2.zs[1])]))# c2.xs, [c1.ys[0], c2.ys[0]-1], c2.zs # the little front bit
				if c2.ys[1] < self.ys[1]:# for c1 in back of c2
					temp_cuboid_array.append(Cuboid([max(self.xs[0], c2.xs[0]), min(self.xs[1], c2.xs[1])], [c2.ys[1]+1, self.ys[1]], [max(self.zs[0], c2.zs[0]), min(self.zs[1], c2.zs[1])]))# c2.xs, [c2.ys[1]+1, c1.ys[1]], c2.zs # the little back bit

		return temp_cuboid_array