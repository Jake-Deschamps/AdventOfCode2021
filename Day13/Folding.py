import sys

import numpy as np
from string import ascii_uppercase
from time import sleep

class Paper:
	def __init__(self):
		self.dots = []
	
	def add_dot(self, dot):
		self.dots.append(dot)
		
	def fold(self, fold_line):
		if fold_line[0] == 'x':
			for d in self.dots:
				if d[0] > fold_line[1]:
					#print("adjusting {} by fold {}".format(d, fold_line))
					d[0] = 2*fold_line[1] - d[0]
					#print("now its {}".foramt(d))
		if fold_line[0] == 'y':
			#print('foldingalongy {}'.format(fold_line))
			for d in self.dots:
				#print(d[1])
				if d[1] > fold_line[1]:
					#print("adjusting {} by fold {}".format(d, fold_line))
					d[1] = 2*fold_line[1] - d[1]
					#print("now its {}".format(d))
		#final scan: remove overlap
		temp = []
		for d in self.dots:
			if d not in temp:
				temp.append(d)
				
		self.dots = temp
	
	
dots = []
folds = []
for line in sys.stdin:
	line = line.strip('\n')
	if ',' in line:
		# print("got dot {}".format(line))
		dots.append([int(x) for x in line.split(',')])
	elif 'fold' in line:
		# print("got fold {}".format(line))
		line = line.replace('fold along ', '')
		line = line.split('=')
		line[1] = int(line[1])
		folds.append(line)
		
myPaper = Paper()

for d in dots:
	myPaper.add_dot(d)
		
myPaper.fold(folds[0])

for d in myPaper.dots:
	print(d)
	
print(len(myPaper.dots))