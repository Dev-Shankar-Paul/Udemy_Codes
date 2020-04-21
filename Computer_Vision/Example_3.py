#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:54:01 2020

@author: dsp
"""
import cv2
import numpy as np

image=cv2.imread('./images/input.jpg')

#first pixel color values 
B, G, R=image[0,0]
print(B,G,R)

#convert to grayscale
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray_image.shape)

# =============================================================================
# image has been converted from 3 dimensions to 2 dimensions. As a 
# result, what happens is that each pixel has only 2 units behind it 
# i.e. black and white. These values decide the color of the whole 
# pixel on the screen. As a result, we cannot obtain B,G,R values
# from the pixel (0,0) anymore. So, we need a different approach.
# =============================================================================

gray_image[0,0]

# get the r, g, b components of the image separately but all as 
# grayscale images

b,g,r=cv2.split(image)

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)

cv2.waitKey(0)
cv2.destroyAllWindows()

# merging the image to give back the original image. An interesting
# thing to do here is to do b+100 or g+100. These can help you to 
# add color filters to your image. b+100 will enhance blue in your
# image drastically...

merged=cv2.merge([b,g,r])
cv2.imshow('merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# to see images as actual color images as opposed to grayscale as
# done above... 

b,g,r=cv2.split(image)

# create a matrix of zeros having the same dimensions as the image 
# itself. Use numpy.

import numpy as np

zeros= np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow("red",cv2.merge([zeros,zeros,r]))
cv2.imshow("green",cv2.merge([zeros,g,zeros]))
cv2.imshow("blue",cv2.merge([b,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()
