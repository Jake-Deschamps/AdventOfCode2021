import sys

import numpy as np

def IsNeighboring(pos1, pos2):
        p1 = np.array(pos1)
        p2 = np.array(pos2)
        dists = (p1 - p2)
        if not(all(abs(dists) <= 1)):
                return False
        else:
                return True
        

class EnergyMatrix:
        def __init__(self, initialmatrix):
                self.Matrix = np.array(initialmatrix)
                self.IncrementMatrix = np.ones(np.shape(self.Matrix), dtype = 'int32')
                #print(self.IncrementMatrix)
                self.CheckMatrix = 9.*np.ones(np.shape(self.Matrix), dtype = 'int32')
                self.BurstsInStep = 0
                self.nRows, self.nCols = np.shape(self.Matrix)

        def BurstNCheck(self, pos):
                #print('burstin')
                #print(self.Matrix)
                self.Matrix[pos[0], pos[1]] = 0
                for r in range(self.nRows):
                       for c in range(self.nCols):
                               if IsNeighboring([r,c], pos) and not self.Matrix[r,c] == 0:
                                       #print(self.Matrix[r, c])
                                       self.Matrix[r, c] += 1
                                       #print(self.Matrix)
                for v in np.argwhere(self.Matrix > 9):
                        if self.Matrix[v[0], v[1]] > 9:
                                self.BurstsInStep += 1
                                self.BurstNCheck([v[0],v[1]])
                 
        def Step(self):
                self.BurstsInStep = 0
                self.Matrix += self.IncrementMatrix
                #print('just incremented')
                #print(self.Matrix)
                for v in np.argwhere(self.Matrix > 9):
                        #print(self.Matrix[v[0], v[1]])
                        if self.Matrix[v[0], v[1]] > 9:
                                self.BurstsInStep += 1
                                self.BurstNCheck(v)
                return self.BurstsInStep

# Hit 'em with the ol' burst n check

testpos1 = [0,0]
testpos2 = [1,1]
#print(IsNeighboring(testpos1, testpos2))

rows = []
for line in sys.stdin:
        line = line.strip('\n')
        row = [int(c) for c in line]
        rows.append(row)

myEnergyMatrix = EnergyMatrix(rows)
#print(CheckMatrix)
Steps = 100
bursts = 0
for s in range(Steps):
        bursts += myEnergyMatrix.Step()
        print(myEnergyMatrix.Matrix)
print(bursts)
