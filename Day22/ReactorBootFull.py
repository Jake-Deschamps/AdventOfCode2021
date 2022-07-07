import sys
import numpy as np
from Cuboid import Cuboid
		

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

Cuboids = []
GotFirst = False
s = 0
for t, x1, x2, y1, y2, z1, z2 in Steps:
	s += 1
	print("Step {}".format(s))
	new_cuboid = Cuboid([x1,x2], [y1, y2], [z1, z2])
	if GotFirst:
		temp_cuboids = []
		#print(Cuboids)
		for c in Cuboids:
			for c_new in c.Collision(new_cuboid):
			
				# why are some of these negative?
				if c_new.GetVolume() < 0:
					print("Got a negative volume. Cuboid {} cut by {} to create {}".format([c.vs[0], c.vs[-1]], [new_cuboid.vs[0], new_cuboid.vs[-1]], [c_new.vs[0],c_new.vs[-1]]))
					sys.exit()
			
				temp_cuboids.append(c_new)
				
			#if not sum([c_new.GetVolume() for c_new in c.Collision(new_cuboid)]) == c.GetVolume():
			#	print('Volume changed by temp cuboid {} to {}'.format(new_cuboid.vs[0],new_cuboid.vs[-1]))
			#	print('{} to {}'.format(c.vs[0], c.vs[-1]))
			#	print('{} became {}'.format(c.GetVolume(), sum([c_new.GetVolume() for c_new in c.Collision(new_cuboid)])))
			
		Cuboids = temp_cuboids
		if t == 'on':
			Cuboids.append(new_cuboid)
	else:
		GotFirst = True
		Cuboids.append(new_cuboid)
	
	
	print(sum([c.GetVolume() for c in Cuboids]))
		
		
print("Final {}.".format(sum([c.GetVolume() for c in Cuboids])))