import numpy as np

# Get F, each entry rounded to 10 decimal places
def GetF(Xs, xs):
	# Xs: list of 3 1x3 numpy arrays for reference positions of three points
	# xs: same, but for present positions
	
	D1 = Xs[0] - Xs[2]
	D2 = Xs[1] - Xs[2]
	D_12 = np.linalg.norm(np.cross(D1, D2)) # may get a divide by 0 thing for one of these if no diff or trying a bad setup
	#print(D_12)
	D3 = np.cross(D1, D2)/D_12
	
	# if(D_12 == 0): print('ERROR, D_12 = 0')
	
	Dup1 = np.cross(D2, D3)/D_12
	Dup2 = np.cross(D3, D1)/D_12
	Dup3 = np.cross(D1, D2)/D_12
	Dups = [Dup1, Dup2, Dup3]
	
	d1 = xs[0] - xs[2]
	d2 = xs[1] - xs[2]
	d_12 = np.linalg.norm(np.cross(d1, d2))
	# if(d_12 == 0): print('ERROR, d_12 = 0')
	d3 = np.cross(d1, d2)/d_12
	ds = [d1, d2 ,d3]
	
	#dup1 = np.cross(d2, d3)/D_12
	#dup2 = np.cross(d3, d1)/D_12
	#dup3 = np.cross(d1, d2)/D_12
	
	
	return np.around(sum([np.outer(d, Dup) for d, Dup in zip(ds, Dups)]),10)
	
def GetO(X1, x1, F):
	return X1 - F.T @ x1
	
def Gett(X1, x1, F):
	return F.T @ x1 - X1
	
def GetAbsDist(x1, x2):
	return sum(abs(x1 - x2))

def GetAbsDists(x1, x2):
	return np.sort(abs(x1 - x2))