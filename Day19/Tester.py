import numpy as np
import TCPE

testA = [np.array([-1, -1, 1]), np.array([-2, -3, 1]), np.array([5, 6, -4])]
testB = [np.array([1, -1, 1]), np.array([2, -1, 3]), np.array([-5, 4, -6])]
#testB = [np.array([2, -1, 1]), np.array([2, -1, 3]), np.array([-5, 4, -6])]

F = TCPE.GetF(testA, testB)

C = np.transpose(F)*F

print(F)

print(np.linalg.det(F))
print(F @ testA[2])
print(testB[2])
print('')
print(F.T @ testB[2])
print(testA[2])
print('')
print(TCPE.Gett(testA[1], testB[1], F))