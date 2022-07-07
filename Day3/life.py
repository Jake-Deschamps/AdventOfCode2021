import sys

import numpy as np

#bcounts = np.zeros([2, 12])
#bcounts = np.zeros([2, 5])

nlist = []
for line in sys.stdin:
	nlist.append(line.strip('\n'))

# get oxygen candidates
done = False
oxy_cands = nlist
on_bit = 0
while not done:
	ones = 0
	zeros = 0
	for line in oxy_cands:
		if line[on_bit] == '0':
			zeros += 1
		else:
			ones += 1
	
	if ones >= zeros:
		winner = '1'
	else:
		winner = '0'
		
	# keep only those with most common (or 1 on tie)
	temp_oxy_cands = []
	for line in oxy_cands:
		if line[on_bit] == winner:
			temp_oxy_cands.append(line)

	oxy_cands = temp_oxy_cands
	if len(oxy_cands) == 1:
		done = True
	else:
		on_bit += 1
			
oxy_winner = []
for c in oxy_cands[0]:
	oxy_winner.append(int(c))

oxy_val = sum(d * 2**i for i, d in enumerate(oxy_winner[::-1]))
print(oxy_val)

# get co2 candidates
done = False
co2_cands = nlist
on_bit = 0
while not done:
	ones = 0
	zeros = 0
	for line in co2_cands:
		if line[on_bit] == '0':
			zeros += 1
		else:
			ones += 1
	
	if ones >= zeros:
		winner = '0'
	else:
		winner = '1'
		
	# keep only those with most common (or 1 on tie)
	temp_co2_cands = []
	for line in co2_cands:
		if line[on_bit] == winner:
			temp_co2_cands.append(line)

	co2_cands = temp_co2_cands
	if len(co2_cands) == 1:
		done = True
	else:
		on_bit += 1
			
co2_winner = []
for c in co2_cands[0]:
	co2_winner.append(int(c))

co2_val = sum(d * 2**i for i, d in enumerate(co2_winner[::-1]))
print(co2_val)

print("Life rating: {}".format(oxy_val*co2_val))