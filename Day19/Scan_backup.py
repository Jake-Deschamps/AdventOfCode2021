import sys
import numpy as np
import re
from itertools import combinations, product, permutations
import TCPE

class Scanner:
	def __init__(self):
		self.Beacons = []
		
		self.Rs = []
		self.Os = []
		
		self.SharedBeacons = []
		
	def AddBeacon(self, beacon):
		self.Beacons.append(beacon)
	def AddShared(self, sensor, beacon):
		self.SharedBeacons.append([sensor, beacon])
	def AddR(self, sensor, R): # R that rotates from the given sensor to this one
		self.Rs.append([sensor, R])
	def AddO(self, sensor, O): # R that rotates from the given sensor to this one
		self.Os.append([sensor, O])

		
#reg = re.compile("l[0-9]+st")
#string = "l42st"
#match = bool(re.match(reg, string))
#print(match)


lines = []

Scanners = []

for line in sys.stdin:
	line = line.strip('\n')
	
	# if not empty
	if not line=='':
		# if it's a scanner intro line
		if 'scanner' in line:
			Scanners.append(Scanner())
		
		# it's a beacon line
		else:
			num_in = [int(c) for c in line.split(',')]
			Scanners[-1].AddBeacon(np.array(num_in))
			
		
		
#for i, s in enumerate(Scanners):
#	print("Scanner {} has beacons:".format(i))
#	for b in s.Beacons:
#		print(b)

# print(Scanners[0].Beacons[2][1])
mn = 0
combo_count = 0
# look for overlap
for s1, s2 in combinations(Scanners, 2):
	combo_count += 1
	print("analyzing combo {}".format(combo_count))
	valid_pairs = []
	Done = False
	for pairs in product(combinations(s1.Beacons,2), combinations(s2.Beacons,2)):
		#print(pairs)
		#print(pairs[0][0])
		#print(pairs[0][1])
		#print(pairs[1][0])
		#print(pairs[1][1])
		
		# get all successful pairs and then try to make tris of them all valid ones should be connected to each other. an errant one wont be. like connected nodes?
		
		if all(TCPE.GetAbsDists(pairs[0][0],pairs[0][1]) == TCPE.GetAbsDists(pairs[1][0],pairs[1][1])):
			# record this connected pair
			#valid_pairs.append([pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1]])
			valid_pairs.append([[id(pairs[0][0]) == id(b) for b in s1.Beacons].index(True), [id(pairs[0][1]) == id(b) for b in s1.Beacons].index(True), [id(pairs[1][0]) == id(b) for b in s2.Beacons].index(True), [id(pairs[1][1]) == id(b) for b in s2.Beacons].index(True)])
			
			#print(valid_pairs)
			# this will check permutations second group of three points
	for p1, p2, p3 in combinations(valid_pairs, 3):
		tri1_indices = []
		tri2_indices = []
		for i in p1[0:2]+p2[0:2]+p3[0:2]:
			if i not in tri1_indices: tri1_indices.append(i)
		for i in p1[2:]+p2[2:]+p3[2:]:
			if i not in tri2_indices: tri2_indices.append(i)
		
		if len(tri1_indices) == 3:
			#print(p1, p2, p3)
			#print(tri1_indices)
			# puzzle out which matches with which now:
			# goal is to have an ordered set of indices [1,2,3] [8,9,10]
			#for t1 in tri1_indices:
			#	if t1 in 
			for tis in [[tri1_indices, t2] for t2 in permutations(tri2_indices,3)]:
				#print(tis)
				tris = [[s1.Beacons[tis[0][0]], s1.Beacons[tis[0][1]], s1.Beacons[tis[0][2]]],[s2.Beacons[tis[1][0]], s2.Beacons[tis[1][1]], s2.Beacons[tis[1][2]]]]
				temp_F = TCPE.GetF(tris[0], tris[1])
				if np.linalg.det(temp_F) == 1:
					temp_t = TCPE.Gett(tris[0][0], tris[1][0], temp_F)
					#print(temp_t)
					#sys.exit()
					check_total = 0
			
					#print("Found a valid tri")
			
					for b2 in s2.Beacons: # get at least 12 of these
						B2 = temp_F.T @ b2 - temp_t # undo rotation and translation
						if any(np.array_equal(B2, B) for B in s1.Beacons):
							check_total += 1
							#print("Sensor match {}".format(check_total))
							#s1.AddShared(B2, s2)
							#s2.AddShared(b2, s1)
							if check_total >= 12:
								Done = True
								break
				if Done: break
		# breaks to here
		if Done:
			# F rotates from s1 to s2, so we'll give F to s1
			print('success!')
			for b2 in s2.Beacons:
				B2 = temp_F.T @ b2 - temp_t # undo rotation and translation
				if any(np.array_equal(B2, B) for B in s1.Beacons):
					#check_total += 1
					s1.AddShared(s2, B2)
					s1.AddR(s2, temp_F)
					s1.AddO(s2, temp_t)
					s2.AddShared(s1, b2)
					s2.AddR(s1, temp_F.T)
					s2.AddR(s1, -temp_t)
			break
		#for tri in combinations(s1.Beacons, 3):
		# find shared tri of beacons that overlap
		# define overlapping region
		# populate the region with beacons in the overlap
		# determine the position of s2's overlapping beacons in s1's frame, should be in s1's overlapping beacons
		# if fully successful, then it's all good
		# if any issues, give up on this tri and try (like, tri, heh, get it?) again
		
for i, s in enuemrate(Scanners):
	print("Scanner {}")
	for b in s.SharedBeacons:
		print(b[1])