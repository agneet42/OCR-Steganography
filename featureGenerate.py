import numpy as numpy
import cv2
from PIL import Image
import os
import skimage
from skimage import data
import matplotlib.pyplot as plt
import csv


feature_file = csv.writer(open('feature.csv','w')) # file to write features in
contents = os.listdir()
for files in contents:
	if(files != 'RunLength.py' and files != 'feature.csv'):
		file_path = '/media/agneet42/Sony_8GR/Final/%s'%(files) # Loading dataset
		contents1 = os.listdir(file_path)
		for imagename in contents1:
			img = cv2.imread('/media/agneet42/Sony_8GR/Final/%s/%s'%(files,imagename),0)
			res = cv2.resize(img,(32,32))
			cv2.imwrite('resized.png',res)
			img = skimage.io.imread('resized.png')
			final_arr = []
			'''
				Calculate Run Length Feature
			'''
			modified_arr = []
			for rows in img:
				temp_row = []
				for val in rows:
					if(val == 255):
						temp_row.append(0)
					else:
						temp_row.append(1)
				modified_arr.append(temp_row)
				temp_row = []
			
			max_one_array = []
			for rows in modified_arr:
				max_length = 0
				length = 0
				for val in rows:
					if(val == 0):
						length = 0
					else:
						length = length + 1
						max_length = max(max_length,length)
				max_one_array.append(max_length)

			# print(len(max_one_array))
			final_arr.append(max_one_array)
			
			'''
				Calculate Shadow Feature
			'''
			modified_arr = []
			for rows in img:
				temp_row = []
				for val in rows:
					if(val == 255):
						temp_row.append(0)
					else:
						temp_row.append(1)
				modified_arr.append(temp_row)
				temp_row = []

			Matrix = numpy.array(modified_arr)
			temp_a, temp_b = numpy.vsplit(Matrix,2)
			one_a, two_a = numpy.hsplit(temp_a,2)
			three_a, four_a = numpy.hsplit(temp_b,2)

			sub_matrices = [one_a,two_a,three_a,four_a]
			shadow_vector = []
			for val in sub_matrices:
				length_LR = 0
				length_TB = 0
				flag = 0
				for row in range(0,16):
					for col in range(0,16):
						if(val[row][col] == 1 and flag == 0):
							start = row
							flag = 1
							break
						elif(val[row][col] == 1):
							end = row
							break
				length_LR = end - start
				flag = 0
				shadow_vector.append(length_LR)
				for col in range(0,16):
					for row in range(0,16):
						if(val[row][col] == 1 and flag == 0):
							start = col
							flag = 1
							break
						elif(val[row][col] == 1):
							end = col
							break
				length_TB = end - start
				shadow_vector.append(length_TB)

			final_arr.append(shadow_vector)
			# print(len(shadow_vector))


			'''
				Calculate Centre of Mass Feature
			'''

			modified_arr = []
			for rows in img:
				temp_row = []
				for val in rows:
					if(val == 255):
						temp_row.append(0)
					else:
						temp_row.append(1)
				modified_arr.append(temp_row)
				temp_row = []

			Matrix = numpy.array(modified_arr)
			temp_a, temp_b = numpy.vsplit(Matrix,2)
			one_a, two_a = numpy.hsplit(temp_a,2)
			three_a, four_a = numpy.hsplit(temp_b,2)

			arr = [one_a,two_a,three_a,four_a]
			CM_vector = []
			for val in arr:
				Cx = 0
				Cy = 0
				temp_X = 0
				temp_Y = 0
				for row in range(15,-1,-1):
					row_count = 0
					for col in range(0,16):
						if(val[row][col] == 1):
							temp_X = temp_X + row_count # needs division by some factor
						row_count = row_count + 1
				CM_vector.append(round(temp_X/32)) # division to normalise
 
				for col in range(0,16):
					col_count = 0
					for row in range(15,-1,-1):
						if(val[row][col] == 1):
							temp_Y = temp_Y + col_count # needs division by some factor
						col_count = col_count + 1
	
				CM_vector.append(round(temp_Y/32))   # division to normalise

			final_arr.append(CM_vector)
			# print(len(CM_vector))
			flat_final = [item for sublist in final_arr for item in sublist]
			flat_final.append("%s"%(files))
			feature_file.writerow(flat_final) # write to feature file
	print(files)	
