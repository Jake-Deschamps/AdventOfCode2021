import sys

import numpy as np
from string import ascii_uppercase

class CaveNode:
	def __init__(self, name):
		if name == 'start':
			self.IsStart = True
			self.IsEnd = False
		elif name == 'end':
			self.IsEnd = True
			self.IsStart = False
		else:
			self.IsEnd = False
			self.IsStart = False

		if name[0] in ascii_uppercase:
			self.IsBig = True
		else:
			self.IsBig = False
		
		self.Name = name
		self.ConnectedNodes = [] # a list of the names of nodes to which this is connected
		
	def AddNode(self, newnode):
		self.ConnectedNodes.append(newnode)
		
	def IsIsolated(self):
		Isolated = True
		for n in self.ConnectedNodes:
			if n[0] in ascii_uppercase:
				Isolated = False
		if len(self.ConnectedNodes) > 1:
			Isolated = False
		return Isolated

		
class CaveSolver:
	def __init__(self, CaveSystem):
		self.CaveSystem = CaveSystem
		self.LegalNodes = [n for n in CaveSystem]
		self.ValidPaths = []
		self.CurrentBuiltPath = []
		# print(self.LegalNodes)
		self.SolveFromNode('start')
		self.HasRevisit = True
		
	def SolveFromNode(self, node):
		#print(self.CurrentBuiltPath)
		self.CurrentBuiltPath.append(node)
		# if it is not big, remove from legal nodes after visiting
		if not self.CaveSystem[node].IsBig and node in self.LegalNodes:
			self.LegalNodes.pop(self.LegalNodes.index(node))
		for n in self.CaveSystem[node].ConnectedNodes:
			if n == 'end':
				#print("GOT ONE {}".format(self.CurrentBuiltPath))
				self.CurrentBuiltPath.append('end')
				self.ValidPaths.append(self.CurrentBuiltPath.copy())
				self.CurrentBuiltPath.pop(-1)
			elif n in self.LegalNodes:
				self.SolveFromNode(n)
			elif self.HasRevisit and not n == 'start':
				self.HasRevisit = False
				self.SolveFromNode(n)
				self.HasRevisit = True
				
				
		self.LegalNodes.append(node)
		self.CurrentBuiltPath.pop(-1)
		#reappend at end?
				
	
		
links = []
Nodes = {}
for line in sys.stdin:
	line = line.strip('\n')
	link = line.split('-')
	links.append(link)

for l in links:
	# print(l)
	if not l[0] in Nodes:
		Nodes[l[0]] = CaveNode(l[0])
	Nodes[l[0]].AddNode(l[1])
	
	if not l[1] in Nodes:
		Nodes[l[1]] = CaveNode(l[1])
	Nodes[l[1]].AddNode(l[0])

#for n in Nodes:
#	print("{} is connected to {}".format(n, Nodes[n].ConnectedNodes))
#	print("Is {} isolated: {}".format(n, Nodes[n].IsIsolated()))
	
Solution = CaveSolver(Nodes)
# find paths

for vs in Solution.ValidPaths:
	print(vs)
	
print(len(Solution.ValidPaths))