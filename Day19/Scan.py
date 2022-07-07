import sys
import numpy as np
import re
from itertools import combinations, product, permutations
import TCPE

from matplotlib import pyplot as plt

class Scanner:
	def __init__(self):
		self.Beacons = []
		
		self.Rs = []
		self.Os = []
		
		self.SharedBeacons = []
		self.Pairs = []
		self.TruePositon = []
		
	def AddBeacon(self, beacon):
		self.Beacons.append(beacon)
	def AddShared(self, sensor, beacon):
		self.SharedBeacons.append([sensor, beacon])
	def AddR(self, sensor, R): # R that rotates from the given sensor to this one
		self.Rs.append([sensor, R])
	def AddO(self, sensor, O): # R that rotates from the given sensor to this one
		self.Os.append([sensor, O])
	def AddPair(self, b1, b2, d):
		self.Pairs.append([b1, b2, d])

		
		
class ScanSolver:
	def __init__(self, ScannerArray):
		self.UniqueBeacons = []
		self.ScannerArray = ScannerArray
		
		self.ToDo = ScannerArray
		self.Done = []
		self.Working = []
		
		self.RStack = []
		self.OStack = []
		
		self.ScannerPositions = []
		
		#self.Working.append(self.ScannerArray[3])
		#self.Working.append(self.ScannerArray[2])
		
		self.SolveIt(ScannerArray[0])
		
	def SolveIt(self, Scanner):
		print("Entered scanner {}".format(self.ScannerArray.index(Scanner)))
		self.Working.append(Scanner)
		for [s, r], [_, o] in zip(Scanner.Rs, Scanner.Os):
			if (s not in self.Working) and (s not in self.Done):
				self.RStack.append(r.T)
				self.OStack.append(-o)
				self.SolveIt(s)
				self.RStack.pop(-1)
				self.OStack.pop(-1)
				
		
		print("Solving in on scanner {}".format(self.ScannerArray.index(Scanner)))
		self.OStack.reverse()
		self.RStack.reverse()
		temp_p = np.array([0,0,0])
		for O, R in zip(self.OStack, self.RStack):
			#print("applying {} and {}".format(O, R))
			temp_p = R @ temp_p + O
		self.ScannerPositions.append([self.ScannerArray.index(Scanner), temp_p])
		Scanner.TruePositon = temp_p
		for b in Scanner.Beacons:
			B = b
			#print(type(B))
			#print(B)
			for O, R in zip(self.OStack, self.RStack):
				#print("applying {} and {}".format(O, R))
				B = R @ B + O
				#B = R @ ( B + O )
			#B = np.around(B, 1)
			if not any(np.array_equal(B, ub) for ub in self.UniqueBeacons):
				self.UniqueBeacons.append(B)
			#print("{} --> {}".format(b, B))
			#sys.exit()
				
		self.OStack.reverse()
		self.RStack.reverse()
		self.Working.pop(-1)
		self.Done.append(Scanner)
				
			
		
		
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

for s in Scanners:
	for pair in combinations(s.Beacons, 2):
		s.AddPair(pair[0], pair[1], TCPE.GetAbsDists(pair[0], pair[1]))
	

# print(Scanners[0].Beacons[2][1])
mn = 0
combo_count = 0
# look for overlap

for s1, s2 in combinations(Scanners, 2):
	combo_count += 1
	print("analyzing combo {}. {} and {}".format(combo_count, Scanners.index(s1), Scanners.index(s2)))
	valid_pairs = []
	Done = False
	for pairs in product(s1.Pairs, s2.Pairs):
		#print(pairs)
		#print(pairs[0][0])
		#print(pairs[0][1])
		#print(pairs[1][0])
		#print(pairs[1][1])
		
		# get all successful pairs and then try to make tris of them all valid ones should be connected to each other. an errant one wont be. like connected nodes?
		
		if all(pairs[0][2] == pairs[1][2]):
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
			#print('success!')
			s1.AddR(s2, temp_F)
			s1.AddO(s2, temp_t)
			s2.AddR(s1, temp_F.T)
			s2.AddO(s1, -(temp_F @ temp_t))
			#s2.AddR(s1, temp_F)
			#s2.AddO(s1, temp_t)
			#s1.AddR(s2, temp_F.T)
			#s1.AddO(s2, -(temp_F.T @ temp_t))
			for b2 in s2.Beacons:
				B2 = temp_F.T @ b2 - temp_t # undo rotation and translation
				for B in s1.Beacons:
					if np.array_equal(B2, B):
					#check_total += 1
						s1.AddShared(s2, B)
						s2.AddShared(s1, b2)
			break
		#for tri in combinations(s1.Beacons, 3):
		# find shared tri of beacons that overlap
		# define overlapping region
		# populate the region with beacons in the overlap
		# determine the position of s2's overlapping beacons in s1's frame, should be in s1's overlapping beacons
		# if fully successful, then it's all good
		# if any issues, give up on this tri and try (like, tri, heh, get it?) again
		
for i, s in enumerate(Scanners):
	#for j, r in enumerate(s.Rs):
	#	print("Scanner {} is linked to scanner {}".format(i, Scanners.index(r[0])))
	#	print("{} {}".format(s.Os[j][1], r[1]))
	# Check that all are linked properly
	for r, o in zip(s.Rs, s.Os):
		#print("{} = {}".format(Scanners.index(r[0]), Scanners.index(o[0])))
		if not Scanners.index(r[0]) == Scanners.index(o[0]):
			print("ERROR in scanner {}".format(i))
			sys.exit()

#Scanners.reverse()
			
mySolver = ScanSolver(Scanners)
out_done = []
for ub in (mySolver.Done):
	out_done.append(Scanners.index(ub))
out_done.sort()

print((out_done))
print(len(mySolver.UniqueBeacons))

for tp in mySolver.ScannerPositions:
	print(tp)
	
ScannerDistances = []
for s1, s2 in combinations(Scanners, 2):
	ScannerDistances.append(TCPE.GetAbsDist(s1.TruePositon, s2.TruePositon))
	
print("Max distance = {}".format(max(ScannerDistances)))



ScannerTruePosX = []
ScannerTruePosY = []
ScannerTruePosZ = []
for s in mySolver.ScannerPositions:
	ScannerTruePosX.append(s[1][0])
	ScannerTruePosY.append(s[1][1])
	ScannerTruePosZ.append(s[1][2])
	
UBTruePosX = []
UBTruePosY = []
UBTruePosZ = []
for b in mySolver.UniqueBeacons:
	UBTruePosX.append(b[0])
	UBTruePosY.append(b[1])
	UBTruePosZ.append(b[2])

ax = plt.axes(projection='3d')
ax.scatter3D(ScannerTruePosX, ScannerTruePosY, ScannerTruePosZ)
ax.scatter3D(UBTruePosX, UBTruePosY, UBTruePosZ)

plt.show()

#for ub in mySolver.UniqueBeacons:
#	print(ub)

# Get it another way - does not work for stray beacons
# BeaconTotal = 0
# for s in Scanners:
	# BeaconTotal += len(s.Beacons)
	# shared_beacon_overlap = []
	# shared_beacon_unique = []
	# for sb in s.SharedBeacons:
		# shared_beacon_overlap.append(sb[1])
		# if not any(np.array_equal(sb[1], B) for B in shared_beacon_unique):
			# shared_beacon_unique.append(sb[1])
	# #print(shared_beacon_unique)
	# #print(shared_beacon_unique)
	# #print(shared_beacon_overlap)
	# for sb in shared_beacon_unique:
		# count = 0
		# for sb2 in shared_beacon_overlap:
			# if np.array_equal(sb, sb2):
				# count += 1
		# #print(count)
		# BeaconTotal -= count/(1+count)
		
	# #sys.exit()
# print(BeaconTotal)