import sys

old_1 = 0
old_2 = 0
old_3 = 0
inc_count = -1
meas_num = 0
for line in sys.stdin:
	current = int(line)
	meas_num += 1
	if meas_num >= 3:
		#if current + old_1 + old_2 > old_1 + old_2 + old_3:
		if current > old_3: #lmao
			inc_count += 1
		#print(current + old_1 + old_2 )
	
	old_3 = old_2
	old_2 = old_1
	old_1 = current

print(inc_count)