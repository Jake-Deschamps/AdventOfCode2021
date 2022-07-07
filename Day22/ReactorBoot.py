import sys
import numpy as np

Steps = []

for line in sys.stdin:
	line = line.strip('\n')
	toggle, rest = line.split(' ')
	xs, ys, zs = rest.split(',')
	xs = xs.strip('x=')
	x1, x2 = [int(c) for c in xs.split('..')]
	ys = ys.strip('y=')
	y1, y2 = [int(c) for c in ys.split('..')]
	zs = zs.strip('z=')
	z1, z2 = [int(c) for c in zs.split('..')]
	Steps.append([toggle, x1, x2, y1, y2, z1,z2])


Reactor = np.zeros([101,101,101])

for t, x1, x2, y1, y2, z1, z2 in Steps:
	if all([C>=-50 and C<=50 for C in [x1, x2, y1, y2, z1, z2]]):
		dx = x2 - x1 + 1
		dy = y2 - y1 + 1
		dz = z2 - z1 + 1
		
		if t == 'on':
			temp = np.ones([dx, dy, dz])
		else:
			temp = np.zeros([dx, dy, dz])
			
		Reactor[x1+50: x2+50+1, y1+50: y2+50+1, z1+50: z2+50+1] = temp
	
print(sum(sum(sum(Reactor))))