import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])

numbers = sys.stdin.readline()
numbers = numbers.strip('\n')
numbers = [int(i) for i in numbers.split(',')]
boards = []
got_numbers = False

#print("numbers is {}".format(numbers))
temp_board = []
board_marks = []
for line in sys.stdin:
	if line.strip('\n \r'):
		temp_board.append([int(i) for i in (line).split()])
	if len(temp_board) >= 5:
		boards.append(np.array(temp_board))
		temp_board = []
		board_marks.append(np.zeros([5,5]))
		#print('made one')

# print(boards[0].shape)
#print('there are {} boards'.format(len(boards)))
winners = np.zeros([len(boards)])
# print(winners)
# winner = False
for n in numbers:
	for i, b in enumerate(boards):
		#print(b)
		#print(board_marks[i])
		board_marks[i][b == n] = 1
		#print(b == n)
		#print("marked {} on board".format(n))
		#print(board_marks[i])
		#print('')
		#break
	#break
	# check for winner
	for i, b in enumerate(boards):
		if (board_marks[i].sum(axis = 0) == 5).any() or (board_marks[i].sum(axis = 1) == 5).any():
			#print("winner obtained")
			if winners[i] == 0:
				winners[i] = 1
				recent_winner = i
	if winners.sum() == len(boards):
		winning_board = recent_winner
		break


print("board number {} has won last".format(winning_board+1))
print(boards[winning_board])
print(board_marks[winning_board])

# score the board
Score = boards[winning_board][board_marks[winning_board] == 0].sum().sum()*n
print(Score)