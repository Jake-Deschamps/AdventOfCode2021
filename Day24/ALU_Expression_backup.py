from sympy import *
from itertools import product
import sys

class ALU_Solver:
	def __init__(self, Instructions):
		self.ALU = ALU_Ex()
		
		self.Instructions = Instructions
		self.FinalExpressions = []
		self.TruthHistory = []
		self.Analyze(Instructions)
		
		
	def Analyze(self, Inst_In):
		index = 0
		for index, inst in enumerate(Inst_In):
			out = self.ALU.ParseLine(inst)
			#print(type(out))
			#print(out)
			if not type(out) == type(1): # if its an eql where we got two outcomes
				StateT, StateF = out# out is then two different states to continue with
				self.ALU.SetState(StateT)
				self.TruthHistory.append(1)
				self.Analyze(Inst_In[index+1:])
				self.ALU.SetState(StateF)
				self.TruthHistory.pop(-1)
				self.TruthHistory.append(0)
				self.Analyze(Inst_In[index+1:])
				self.TruthHistory.pop(-1)
				break
			
		if index == len(Inst_In)-1: # if we analyzed the last instruction here
			# see if the final value for z is achievable, then store it
			final_expr = self.ALU.View()[-1]
			print("{} gives {}".format(self.TruthHistory,final_expr))
			if PolyHasSolution(final_expr):
				self.FinalExpressions.append(final_expr)
			pass

			
# Simplify an integer mod expression
def IntegerModSymplify(Expression):
	# The idea is this: if you have a linear polynomial plugged into mod m
	# and the coefficients of some terms are powers of m, those terms can be removed
	#print(Expression.args)
	Polynomial, mod_m = Expression.args
	new_expression = 0
	powers = []
	for ind in range(1, 7):
		powers.append(mod_m**ind)
	
	for term in Add.make_args(Polynomial):
		try:
			var = list(term.free_symbols)[0]
			#print(var)
			coeff = term.coeff(var)
			#print(coeff)
			if (coeff not in powers) and (not abs(coeff) < 1/9):
				new_expression += term
		except:
			new_expression += term % mod_m
			
	return new_expression % mod_m
	
	
def PolyHasSolution(Expression):
	success = False
	for term in Add.make_args(Expression):
		try:
			var = list(term.free_symbols)[0]
			coeff = term.coeff(var)
			if coeff < 0:
				success = True
				break
		except:
			if term < 0:
				success = True
				break
				
	return success



# simplify polynomials such that any coeffs that /10 or more result in 0
	

def EqualityTest(LHS, RHS):
	# return true if it is possible for the LHS to equal the RHS for some value
	#print(LHS)
	try:
		variables = list(LHS.free_symbols)
		success = false
		for values in product(range(1,10), repeat = len(variables)):
			Subs_Array = []
			for var, val in zip(variables, values):
				Subs_Array.append((var, val))
				
			#print("{} >{}".format(Subs_Array, LHS.subs(Subs_Array)))
			#print(str(values))
			plugged_in = LHS.subs(Subs_Array)
			if 1 <= plugged_in and plugged_in <= 9:
				success = True
				break
				
		return(success)
	except:
		return False
	

class ALU_Ex:
	def __init__(self):
		self.w = 0
		self.x = 0
		self.y = 0
		self.z = 0
	
	def ParseLine(self, Line):
		words = Line.split()
		
		var_a = getattr(self, words[1])
		
		if len(words) == 3:
			if words[2] in ['w', 'x', 'y', 'z']:
				var_b = getattr(self, words[2])
			else:
				try:
					var_b = int(words[2])
				except:
					var_b = symbols(words[2])
		
		
		if words[0] == 'inp':
			var_a = var_b
			setattr(self, words[1], var_a)
			return 0
			
		elif words[0] == 'add':
			var_a += var_b
			setattr(self, words[1], var_a)
			return 0
			
		elif words[0] == 'mul':
			var_a = var_a * var_b
			setattr(self, words[1], var_a)
			return 0
			
		elif words[0] == 'div':
			var_a = var_a/var_b
			setattr(self, words[1], var_a)
			return 0
			#var_a = floor(var_a / var_b)
			#var_a = (var_a-var_a%var_b)/var_b
		
		elif words[0] == 'mod':
			var_a = var_a % var_b
			
			if not type(var_a) == type(1):
				var_a = IntegerModSymplify(var_a)
			
			setattr(self, words[1], var_a)
			return 0
			
		elif words[0] == 'eql': # try plugging in combos of stuff to see if possible? lets just try saying things all things are possible and using the resulting 2^28 equations. if not, 
			# expr.subs(list(expr.free_symbols)[0],1)
			#input("parsing...")
			if type(var_a) == type(1) and type(var_b) == type(1):
				if var_a == var_b:
					var_a = 1
				else:
					var_a = 0
				setattr(self, words[1], var_a)
				return 0
			else: # create option for both
				#var_a=1
				#print("{} == {}?".format(var_a, var_b))
				if False: EqualityTest(var_a, var_b):
					State_Array = []
					setattr(self, words[1], 0)
					State_Array.append(self.View())
					setattr(self, words[1], 1)
					State_Array.append(self.View())
					#print(State_Array)
					return State_Array
					
				elif False: #else:
					setattr(self, words[1], 0)
					return 0
					
				
				
				# It should technically never get here so I ought not to have to comment it out
				# simply ask user to decide
				UserDecision = input("{} == {}?".format(var_a, var_b))
				if UserDecision == 1:
					var_a = 1
				else:
					var_a = 0
				setattr(self, words[1], var_a)
				return 0
				
				# For all possible sets of values in the relevant expressions
					# Test if it creates equality
					# If equal:
						# Append the set to the true_if array.
					# If not equal:
						# Append set to false_if array
				# If only one array has values
					# var_a = #Relevant values
					# done
				# If both arrays have values
					# create copy for false
					# set current version for true
					# return copy
					
		
	def View(self):
		return([self.w, self.x, self.y, self.z])
		
	def Reset(self):
		self.w = 0
		self.x = 0
		self.y = 0
		self.z = 0
		
	def SetState(self, State):
		self.w = State[0]
		self.x = State[1]
		self.y = State[2]
		self.z = State[3]