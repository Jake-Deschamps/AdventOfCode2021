import numpy as np
from Cuboid import Cuboid

C1 = Cuboid([0,2], [0,2], [0,2]) # cuboid with volume 27
print("Cuboid 1 has volume {}".format(C1.GetVolume()))
C2 = Cuboid([1,1], [1,1], [1,1]) # cuboid with volume 1
print("Cuboid 2 has volume {}".format(C2.GetVolume()))

C3 = Cuboid([0,3], [1,2], [1,2]) # cuboid with volume 16
print("Cuboid 3 has volume {}".format(C3.GetVolume()))
C4 = Cuboid([1,2], [0,1], [0,1]) # cuboid with volume 8
print("Cuboid 4 has volume {}".format(C4.GetVolume()))

C5 = Cuboid([-3,0], [-2,-1], [-2,-1]) # cuboid with volume 16
print("Cuboid 5 has volume {}".format(C3.GetVolume()))
C6 = Cuboid([-2,-1], [-1,0], [-1,0]) # cuboid with volume 8
print("Cuboid 6 has volume {}".format(C4.GetVolume()))

C7 = Cuboid([-1,-1],[1,1],[3,3]) # good for all variations

C8 = Cuboid([12, 12], [10, 12], [10, 10])
print("Cuboid 8 has volume {}".format(C8.GetVolume()))
C9 = Cuboid([10, 10], [10, 10], [10, 10])
print("Cuboid 9 has volume {}".format(C9.GetVolume()))

# Case 1: C2 fully inside C1. Should give volume = 27-1 = 26
test = C1.Collision(C2)
print("Case 1: This should be 26: {}".format(sum([c.GetVolume() for c in test])))

# Case 2: C2 fully inside C1. Should give 0
test = C2.Collision(C1)
print("Case 2: This should be 0: {}".format(sum([c.GetVolume() for c in test])))

# Case 3: C4 takes a bite out of C3. Should give 14
test = C3.Collision(C4)
print([c.GetVolume() for c in test])
#print("{} {} {}".format(test[-1].xs, test[-1].ys, test[-1].zs))
print("Case 3: This should be 14: {}".format(sum([c.GetVolume() for c in test])))

# Case 4: C3 takes a bite out of C4. Should give 6
test = C4.Collision(C3)
print([c.GetVolume() for c in test])
print("Case 4: This should be 6: {}".format(sum([c.GetVolume() for c in test])))

# Case 5: C6 takes a bite out of C5. Should give 14
test = C5.Collision(C6)
print([c.GetVolume() for c in test])
#print("{} {} {}".format(test[-1].xs, test[-1].ys, test[-1].zs))
print("Case 5: This should be 14: {}".format(sum([c.GetVolume() for c in test])))

# Case 6: C3 takes a bite out of C4. Should give 6
test = C6.Collision(C5)
print([c.GetVolume() for c in test])
print("Case 6: This should be 6: {}".format(sum([c.GetVolume() for c in test])))

# Case 7: C7 takes a bite out of C1. Should give 27
test = C1.Collision(C7)
print([c.GetVolume() for c in test])
print("Case 7: This should be 27: {}".format(sum([c.GetVolume() for c in test])))

# Case 8: C9 takes a 'bite' out of C8. Should give 3
test = C8.Collision(C9)
print([c.GetVolume() for c in test])
print("Case 8: This should be 3: {}".format(sum([c.GetVolume() for c in test])))

