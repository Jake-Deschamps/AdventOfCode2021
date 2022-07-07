import sys
import numpy as np
from math import ceil

def SendIt(vs, target):
	vx, vy = vs
	[[xmin, xmax], [ymin, ymax]] = target
	#print([xmin, xmax, ymin, ymax])
	step = 0
	xpos = 0
	ypos = 0
	maxh = ypos
	HitTarget = False
	
	while (xpos <= xmax) and (ypos >= ymin):
		xpos += vx
		ypos += vy
		#print([xpos, ypos])
		maxh = max([ypos, maxh]) # is this faster than 'if greater then replace'? ... looks nice tho
		if (xpos >= xmin) and (xpos <= xmax) and (ypos >= ymin) and (ypos <= ymax):
			#print('hit it')
			HitTarget = True
			break
			
		# new vs
		if not vx == 0:
			vx = np.sign(vx)*(abs(vx)-1)
		vy -= 1
			
	return [HitTarget, maxh, [xpos, ypos]]
		

for line in sys.stdin:
	line = line.strip('\n')
	line = line.strip('target area: x=')
	temp = line.split(', y=')
	temp = [d.split('..') for d in temp]
	#theres definitely a tidier way to do this, but hardcoding is aight since inputs are limited...?
	zone = [[int(temp[0][0]), int(temp[0][1])],[int(temp[1][0]), int(temp[1][1])]]
	

#print(SendIt([6, 9], zone))
print(zone)

# find valid vys for going up
v_test = 1
vys = []
Working = True
while Working:
	#print('testing {}'.format(v_test))
	temp_sum = 0
	i = 1
	while temp_sum <= abs(zone[1][0]):
		temp_sum += v_test + i
		#print(temp_sum)
		i += 1
		if(temp_sum <= abs(zone[1][0]) and temp_sum >= abs(zone[1][1])):
			#print([v_test])
			vys.append(v_test)
			break
	v_test += 1
	if v_test > abs(zone[1][0]):
		break

# now for going down
v_test = 0
Working = True
while Working:
	#print('testing {}'.format(v_test))
	temp_sum = 0
	i = 0
	while temp_sum <= abs(zone[1][0]):
		temp_sum += v_test + i
		#print(temp_sum)
		i += 1
		if(temp_sum <= abs(zone[1][0]) and temp_sum >= abs(zone[1][1])):
			#print([v_test])
			vys.append(-v_test)
			break
	v_test += 1
	if v_test > abs(zone[1][0]):
		break
		
print(vys)	
	
valid_combos = []
# now get vxs for all vys
for vy in vys:
	for vx in range(zone[0][1]+1):
		if SendIt([vx, vy], zone)[0]: valid_combos.append([vx, vy])
	
print(valid_combos)
print(len(valid_combos))

#print(SendIt([12,6], zone))