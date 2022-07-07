import sys

horizontal = 0
depth = 0
aim = 0
for line in sys.stdin:
	#print(line)
	[direction, distance] = line.split(' ')
	direction = str(direction)
	distance = int(distance)
	if direction == 'forward':
		horizontal += distance
		depth += aim*distance
	#elif direction == 'backward':
	#	horizontal -= distance
	elif direction == 'up':
		aim -= distance
	elif direction == 'down':
		aim += distance
	else:
		print('ERROR')

print(horizontal)
print(depth)

print(horizontal*depth)