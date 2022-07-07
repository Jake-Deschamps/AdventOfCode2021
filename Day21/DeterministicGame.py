import sys

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
Die = range(1,101,1)

Score1 = 0
Score2 = 0

Done = False
i = 0
while not Done:
	print("{} to {}".format(Score1, Score2))
	p1 += Die[i%100]
	i += 1
	p1 += Die[i%100]
	i += 1
	p1 += Die[i%100]
	i += 1
	p1 = p1 % 10
	Score1 += p1 + 1
	if Score1 >= 1000:
		print("P1 wins, {} to {}. {} rolls".format(Score1, Score2, i))
		print("Product {}".format(Score2*i))
		break
	
	
	p2 += Die[i%100]
	i += 1
	p2 += Die[i%100]
	i += 1
	p2 += Die[i%100]
	i += 1
	p2 = p2 % 10
	Score2 += p2 + 1
	if Score2 >= 1000:
		print("21 wins, {} to {}. {} rolls".format(Score2, Score1, i))
		print("Product {}".format(Score1*i))
		break
