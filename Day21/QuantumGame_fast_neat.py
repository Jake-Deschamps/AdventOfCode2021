import sys
import numpy as np
from itertools import product
# attempting to speed up runtime:
# - there are lots of instances where it iterates over the whole gamestate list to find a match. is there a faster way?
# - make the gamestates one gigantic 7-D numpy array so they can be addressed with their values?

# THIS SAVED SO MUCH TIME!

class GameState:
	def __init__(self, p1, Score1, p2, Score2, turn):
		self.p1 = p1
		self.Score1 = Score1
		self.p2 = p2
		self.Score2 = Score2
		
		self.Turn = turn
		
		self.Ways = 0
		
		self.Info = [self.p1, self.Score1, self.p2, self.Score2, self.Turn]
		
		self.DiceOptions = [[3,1],[4,3],[5,6],[6,7],[7,6],[8,3],[9,1]]
		
		self.Done = False
		
		

class QuantumGame:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
		self.GameStates = np.zeros([31, 31, 10, 10, 2])
		self.GameStates[0,0,p1,p2,0] = 1 # initial scores, initial player positions, initial turn is p1s
		self.FinalStates = []
		
		self.DiceOptions = [[3,1],[4,3],[5,6],[6,7],[7,6],[8,3],[9,1]]
		
		for s1, s2, p1, p2, turn in product(range(31), range(31), range(10), range(10), range(2)):
			e = self.GameStates[s1, s2, p1, p2, turn]
			if not e == 0: # dont evaluate if no ways
				if (s1 >= 21) or (s2 >= 21):
					self.FinalStates.append(GameState(p1, s1, p2, s2, turn))
					self.FinalStates[-1].Ways = int(e)
				else:
					if turn == 0: # p1s turn
						temp_p2 = p2
						temp_s2 = s2
						temp_turn = 1
						for dice_total, n in self.DiceOptions:
							temp_p1 = int((p1 + dice_total) % 10)
							temp_s1 = int(s1 + temp_p1 + 1)
							temp_ways = e * n
							self.GameStates[temp_s1, temp_s2, temp_p1, temp_p2, temp_turn] += temp_ways
					else: # p2s turn
						temp_p1 = p1
						temp_s1 = s1
						temp_turn = 0
						for d, n in self.DiceOptions:
							temp_p2 = int((p2 + d) % 10)
							temp_s2 = int(s2 + temp_p2 + 1)
							temp_ways = e * n
							self.GameStates[temp_s1, temp_s2, temp_p1, temp_p2, temp_turn] += temp_ways
								


gotP1 = False

for line in sys.stdin:
	line = line.strip('\n')
	print(line[-2:])
	if not gotP1:
		p1 = int(line[-2:])
		gotP1 = True
	else:
		p2 = int(line[-2:])
	
print("{} {}".format(p1, p2))
p1 -= 1
p2 -= 1
# consider a board 0 - 9 instead and just add 1 to each value
myQuantumGame = QuantumGame(p1, p2)
TotalUniverses1 = 0
TotalUniverses2 = 0
for fgs in myQuantumGame.FinalStates:
	print("{} to {}".format(fgs.Score1, fgs.Score2))
	if fgs.Score1 > fgs.Score2:
		TotalUniverses1 += fgs.Ways
	else:
		TotalUniverses2 += fgs.Ways
		
print('{} to {}'.format(TotalUniverses1, TotalUniverses2))