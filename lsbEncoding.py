import skimage
from skimage import data
import numpy as np
import binascii
import csv
import cv2

# ENCODING

image = skimage.io.imread('resized_C0005.png') # read cover image

file = csv.reader(open('features.csv','r')) # read feature file
arr_encode = []
for lines in file:
	for val in lines:
		arr_encode.append(int(val))

# print(len(arr_encode))

str_encode = ''

for val in arr_encode:
	str_encode = str_encode + '{0:08b}'.format(val) # to encode each value as a 8-bit binary number
	# print(len(str_encode))

# print(len(str_encode))

str_encode = '{0:032b}'.format(105) + '{0:08b}'.format(32) + str_encode

# print(str_encode)
# print(type(str_encode))

Length = len(str_encode)
# print(Length)

encoded_image = []
count = 0
for row in image:
	temp1 = []
	for each in row:
		if(count < len(str_encode)):
			temp = ''
			temp_arr = []
			temp = '{0:08b}'.format(each)
			temp_arr = list(temp)
			temp_arr[7] = str_encode[count]
			count = count + 1
			
			''' Uncomment for LSB-1 encoding'''
			
			'''temp_arr[6] = str_encode[count]
			count = count + 1'''
			
			''' Uncomment for LSB-1 encoding'''

			'''
			temp_arr[5] = str_encode[count]
			count = count + 1'''
			
			temp = "".join(temp_arr)
			changed_pixel = int(temp,2)
			temp1.append(changed_pixel)
		else:
			temp1.append(each)
	encoded_image.append(temp1)

encoded_numpy = np.array(encoded_image)
cv2.imwrite("C0005_stego_0.png",encoded_numpy) # write stego image
