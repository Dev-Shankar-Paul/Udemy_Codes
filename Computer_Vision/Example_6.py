#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:11:50 2020

@author: dsp
"""
# Shiftimg images from one place to another using cv2's warpAffine

import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

#get height and width of the image

height ,  width = image.shape[:2]
quarter_width , quarter_height = width/4 , height/4

#       | 1 0 Tx |
#   T=  | 0 1 Ty |     {Translation matrix}

T= np.float32([[1,0,quarter_width],[0,1,quarter_height]])

# we use warpAffine to transform the image using the matrix T

img_translation=cv2.warpAffine(image, T , (width,height))
cv2.imshow('Translation',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()