import sys

import matplotlib.pyplot as plt

template = []
Rules = {}
for line in sys.stdin:
	line = line.strip('\n')
	if '->' in line:
		line = line.split(' -> ')
		Rules[line[0]] = line[1]
	elif line:
		template = line
		
Steps = 40
# print(template)
for s in range(Steps):
	print("{} {}".format(s, len(template)))
	to_add = ''
	for i in range(len(template)-1):
		# print("looking up {}".format(Rules[template[i:i+2]]))
		to_add = to_add + Rules[template[i:i+2]]
		
	# print(to_add)
	temp_template = ''
	temp_template = temp_template + template[0]
	template = template[1:]
	while template:
		temp_template = temp_template + to_add[0]
		to_add = to_add[1:]
		temp_template = temp_template + template[0]
		template = template[1:]
	
	template = temp_template
	# print(template)
	
# output info on template
Character_Counts = {}
for c in template:
	if c not in Character_Counts.keys():
		Character_Counts[c] = 1
	else:
		Character_Counts[c] += 1

print(max(Character_Counts.values()) - min(Character_Counts.values()))