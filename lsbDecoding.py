import skimage
from skimage import data
import numpy as np
import binascii
import csv
import cv2

# ENCODING

image = skimage.io.imread('resized_C0005.png') # read image

''' As each feature value is embedded as a 8-bit binary number,
	for 0-LSB extraction, 8 bits need are needed. Each character is represented by 48 features. Comment below for 1-LSB extraction '''


noOfRows = len(image)
noOfColumns = len(image[0])

count = 0
string_feature = ''
final_feature = []
row_final_feature = []
for i in range(0,noOfRows):
	for j in range(0,noOfColumns):
		pixel = image[i][j] # get pixel
		pixel_binary = '{:08b}'.format(160)  # pixel in binary
		lsb_pixel_binary = pixel_binary[len(var)-1] # get LSB value of the binary value
		string_feature = string_feature + lsb_pixel_binary
		if(len(string_feature) == 8):  # check for 8-bit binary
			row_final_feature.append(int(string_feature, 2))
			count = count + 1
			string_feature = ''
		if(count == 48):
			final_feature.append(row_final_feature)
			row_final_feature = []
			count = 0


csv_file = csv.writer(open('extracted_features_0LSB.csv','w'))
for each_row in final_feature:
	csv_file.writerow(each_row)

''' Uncomment below for 1-LSB extraction'''

'''
noOfRows = len(image)
noOfColumns = len(image[0])

count = 0
string_feature = ''
final_feature = []
row_final_feature = []
for i in range(0,noOfRows):
	for j in range(0,noOfColumns):
		pixel = image[i][j] # get pixel
		pixel_binary = '{:08b}'.format(160)  # pixel in binary
		lsb_pixel_binary = pixel_binary[len(var)-1] # get LSB value of the binary value
		1_lsb_pixel_binary = pixel_binary[len(var)-2] # get 1-LSB value of the binary value
		string_feature = string_feature + lsb_pixel_binary
		if(len(string_feature) == 8):  # check for 8-bit binary
			row_final_feature.append(int(string_feature, 2))
			count = count + 1
			string_feature = ''
		if(count == 48):
			final_feature.append(row_final_feature)
			row_final_feature = []
			count = 0
		string_feature = string_feature + 1_lsb_pixel_binary
		if(len(string_feature) == 8):  # check for 8-bit binary
			row_final_feature.append(int(string_feature, 2))
			count = count + 1
			string_feature = ''
		if(count == 48):
			final_feature.append(row_final_feature)
			row_final_feature = []
			count = 0


csv_file = csv.writer(open('extracted_features_1LSB.csv','w'))
for each_row in final_feature:
	csv_file.writerow(each_row)'''