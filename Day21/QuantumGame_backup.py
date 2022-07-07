import sys

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
		
		self.GameStates = []
		self.GameStates.append(GameState(p1, 0, p2, 0, 'p1'))
		self.GameStates[0].Ways = 1
		
		self.FinalStates = []
		
		self.DiceOptions = [[3,1],[4,3],[5,6],[6,7],[7,6],[8,3],[9,1]]
		
		#print(self.GameStates[0])
		self.EvaluateState(self.GameStates[0])
		print(len(self.GameStates))
		acceptable_s1s = 0
		acceptable_s2s = 0
		while True:
			for gs in self.GameStates:
				if (gs.Score1 <= acceptable_s1s) and (gs.Score2 <= acceptable_s2s) and (not gs.Done):
					self.EvaluateState(gs)
			acceptable_s1s += 1
			
			for gs in self.GameStates:
				if (gs.Score1 <= acceptable_s1s) and (gs.Score2 <= acceptable_s2s) and (not gs.Done):
					self.EvaluateState(gs)
			acceptable_s2s += 1
			
			print('{} {}, {} gamestates, {} finished'.format(acceptable_s1s, acceptable_s2s, len(self.GameStates), len(self.FinalStates)))
			
			if not any([not gs.Done for gs in self.GameStates]):
				print('done')
				break
		
	def EvaluateState(self, gstate):
		if gstate.Done:
			print('ERROR: Returned to evaluated state')
			sys.exit()
		if (gstate.Score1 >= 21) or (gstate.Score2 >= 21):
			self.FinalStates.append(gstate)
		else:
			if gstate.Turn == 'p1':
				# stuff
				temp_p2 = gstate.p2
				temp_s2 = gstate.Score2
				for d, n in self.DiceOptions:
					temp_p1 = (gstate.p1 + d) % 10
					temp_s1 = gstate.Score1 + temp_p1 + 1
					temp_ways = gstate.Ways * n
					temp_turn = 'p2'
					
					match = [[temp_p1, temp_s1, temp_p2, temp_s2, temp_turn] == i.Info for i in self.GameStates]
					if any(match):
						#print("Found existing {}".format([temp_p1, temp_s1, temp_p2, temp_s2, temp_turn]))
						self.GameStates[match.index(True)].Ways += temp_ways
					else:
						#print("Made new {}".format([temp_p1, temp_s1, temp_p2, temp_s2, temp_turn]))
						self.GameStates.append(GameState(temp_p1, temp_s1, temp_p2, temp_s2, temp_turn))
						self.GameStates[-1].Ways = temp_ways
				#sys.exit()
					
			else:
				# stuff
				temp_p1 = gstate.p1
				temp_s1 = gstate.Score1
				for d, n in self.DiceOptions:
					temp_p2 = (gstate.p2 + d) % 10
					temp_s2 = gstate.Score2 + temp_p2 + 1
					temp_ways = gstate.Ways * n
					temp_turn = 'p1'
					
					match = [[temp_p1, temp_s1, temp_p2, temp_s2, temp_turn] == i.Info for i in self.GameStates]
					if any(match):
						self.GameStates[match.index(True)].Ways += temp_ways
					else:
						self.GameStates.append(GameState(temp_p1, temp_s1, temp_p2, temp_s2, temp_turn))
						self.GameStates[-1].Ways = temp_ways
		gstate.Done = True

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