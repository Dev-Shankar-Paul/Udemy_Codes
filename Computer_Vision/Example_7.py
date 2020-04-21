#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:29:45 2020

@author: dsp
"""
# rotating images

import cv2
import numpy as np

image=cv2.imread('./images/input.jpg')
height , width = image.shape[:2]

#create a transformation matrix i.e. the rotation matrix
#                                       pivot point, by how much, scale
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
rotated_image=cv2.warpAffine(image, rotation_matrix, (width,height))

cv2.imshow('rotated image',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# to remove all the black space around the image use transpose 
img=cv2.imread('./images/input.jpg')
rotated_image=cv2.transpose(img)
cv2.imshow('rotated image 2',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
