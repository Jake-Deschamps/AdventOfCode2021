import sys
import numpy as np
from matplotlib import pyplot as plt

# 5617 was too high! note that padding with 0s is bad in the full case since it changes pure 0 grids to 1s!
# perhaps I should pad with 0s and the issue is that the 0s on the edge arent turned to 1s??
# or pad with a huge region and simply take only the middle portion??

class Image:
	def __init__(self, Pixels, Algorithm):
		self.Pixels = Pixels # the array of binary image bits
		self.Border = 0 # if algorithm[0] is a #, then the infinite sea of pixels will change colors
		self.Algorithm = Algorithm
		
	def Enhance(self):
		self.PadImage()
		self.PadImage()
		
		temp_image = np.zeros(self.Pixels.shape)
		h, w = self.Pixels.shape
		for i, r in enumerate(self.Pixels[1:-1]):
		#print(r)
			for j, c in enumerate(r[1:-1]):
			# coordinates character c at indices i+1,j+1
				#print('{} {}'.format(i,j))
				#print(Image[i+1-1:i+1+2, j+1-1:j+1+2])
				temp = np.reshape(self.Pixels[i+1-1:i+1+2, j+1-1:j+1+2], 9)
				#temp = [0,0,0,0,0,0,0,0,0]
				replacement_index = int(sum(d * 2 **k for k, d in enumerate(temp[::-1])))
				#print(replacement_index)
				temp_image[i+1, j+1] = Algorithm[replacement_index]
		
		
		# replace border as appropriate: ignore outermost layer
		temp_image = temp_image[1:-1, 1:-1]
		
		self.Pixels = temp_image
		if self.Border == 0:
			self.Border = self.Algorithm[0]
		else:
			self.Border = self.Algorithm[-1]
	
	def PadImage(self):
		h, w = self.Pixels.shape
		temp = self.Border * np.ones([h+2, w+2])
		
		temp[1:1+h, 1:1+w] = self.Pixels
		self.Pixels = temp
		

	
GettingAlgorithm = True
temp_Algorithm = ''
Image_Binary = []

for line in sys.stdin:
	line = line.strip('\n')
	
	
	# if not empty
	if line=='':
		GettingAlgorithm = False
	
	elif GettingAlgorithm:
		temp_Algorithm += line
	
	else:
		image_line = []
		for c in line:
			if c == '.': image_line.append(0)
			else: image_line.append(1)
		Image_Binary.append(image_line)
		
		
Image_Binary = np.array(Image_Binary)

Algorithm = []
for c in temp_Algorithm:
	if c == '#':
		Algorithm.append(1)
	else:
		Algorithm.append(0)

myImage = Image(Image_Binary, Algorithm)

print(myImage.Pixels)

EnhanceCount = 50
for i in range(EnhanceCount):
	print("Conducting Enhance {} of {}".format(i+1, EnhanceCount))
	myImage.Enhance()

print(sum(sum(myImage.Pixels)))
plt.imshow(myImage.Pixels)
plt.show()