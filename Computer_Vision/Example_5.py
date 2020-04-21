#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:04:25 2020

@author: dsp
"""
# DRAWING SHAPES USING OPENCV

import cv2
import numpy as np

# creating a black square 
# 512 by 512 square image with 3 array pixels for RGB
# second one is for black and white images only. 2 array pixels
image = np.zeros((512,512,3),np.uint8)
image_bw=np.zeros((512,512), np.uint8)

#cv2.imshow('Black Rectangle (color)',image)
#cv2.imshow('Black Rectangle (black and white)',image_bw)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

# to create a line across our image
#        image,start,stop,     (b,g,r) val,thickness in pixels 
cv2.line(image,(0,0),(511,511),(255,127,0),5)
cv2.imshow('Blue line',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# get black screen again to prevent overlapping 
image = np.zeros((512,512,3),np.uint8)

# draw rectangles
cv2.rectangle(image,(100,100),(300,250),(127,50,127),5)
cv2.imshow('Rectangle',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw circles
image = np.zeros((512,512,3),np.uint8)
cv2.circle(image,(350,350),100,(15,75,50),-1)
cv2.imshow('circle',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw polygons
image = np.zeros((512,512,3),np.uint8)
pts= np.array([[10,50],[400,50],[90,200],[50,500]], np.int32)

#need to reshape array for polylines function
pts=pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True ,(0,0,255), 3)
cv2.imshow('polygon', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#writing on image
image = np.zeros((512,512,3),np.uint8)

cv2.putText(image,'helo world',(75,290),cv2.FONT_HERSHEY_COMPLEX,
            2,(100,170,0),3)
cv2.imshow('text',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

