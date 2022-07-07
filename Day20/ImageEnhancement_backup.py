import sys
import numpy as np

# 5617 was too high! note that padding with 0s is bad in the full case since it changes pure 0 grids to 1s!

# if a binary image does not have a complete ring of 0's around it, add one
# ty: https://stackoverflow.com/questions/7115437/how-to-embed-a-small-numpy-array-into-a-predefined-block-of-a-large-numpy-arra
def PadImage(Image, Algorithm):
	h, w = Image.shape
	if Algorithm[0] == '#': #pad with 1s
	else:
		border = np.zeros([h+2, w+2])
		border[1:1+h, 1:1+w] = Image
	return(border)
	
def SmartPad(Image):
	# make function that only Pads where needed
	pass
	
def Enhance(Image, Algorithm):
	temp_image = np.zeros(Image.shape)
	h, w = Image.shape
	for i, r in enumerate(Image[1:-1]):
		#print(r)
		for j, c in enumerate(r[1:-1]):
			# coordinates character c at indices i+1,j+1
				#print('{} {}'.format(i,j))
				#print(Image[i+1-1:i+1+2, j+1-1:j+1+2])
				temp = np.reshape(Image[i+1-1:i+1+2, j+1-1:j+1+2], 9)
				#temp = [0,0,0,0,0,0,0,0,0]
				replacement_index = int(sum(d * 2 **k for k, d in enumerate(temp[::-1])))
				#print(replacement_index)
				if Algorithm[replacement_index] == '#':
					temp_image[i+1, j+1] = 1
	return(temp_image)
				#print(temp)
				#sys.exit()
				#for 
	
GettingAlgorithm = True
Algorithm = ''
Image_Binary = []

for line in sys.stdin:
	line = line.strip('\n')
	
	
	# if not empty
	if line=='':
		GettingAlgorithm = False
	
	elif GettingAlgorithm:
		Algorithm += line
	
	else:
		image_line = []
		for c in line:
			if c == '.': image_line.append(0)
			else: image_line.append(1)
		Image_Binary.append(image_line)
		
Image_Binary = np.array(Image_Binary)

Image_Binary = PadImage(Image_Binary)
Image_Binary = PadImage(Image_Binary)
Image_Binary = Enhance(Image_Binary, Algorithm)
print(Image_Binary)

Image_Binary = PadImage(Image_Binary)
Image_Binary = PadImage(Image_Binary)
Image_Binary = PadImage(Image_Binary)
Image_Binary = Enhance(Image_Binary, Algorithm)

print(Image_Binary)
print(sum(sum(Image_Binary)))