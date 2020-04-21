#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:47:33 2020

@author: dsp
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('./images/tobago.jpg')
cv2.imshow('TOBAGO',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# =============================================================================
# calcHist function
# first parameter = [image]
# 2nd parameter = channels. For color images give channel [0],[1] or [2]
# for blue green and red channels respectively:
# 3rd parameter = scale. For full scale, use [256]
# 4th parameter = range of the histogram . Usually [0,256]
# =============================================================================

histogram=cv2.calcHist([image],[2],None,[256],[0,256])

# we now plot our histogram. ravel flattens the image array. Imagine
# taking a 2D array and making it a 1D array. That's exactly what 
# ravel does

plt.hist(image.ravel(),256,[0,256])
plt.show()

color = ('b','g','r')

for i,col in enumerate(color):
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2, color=col)
    plt.xlim([0,256])
    
plt.show()

"""
HISTOGRAM NAVIGATION

the peaks of blue on the left mean that there are darker colors
of blue but they are not very intense. The short red spikes means 
that dark red is more intense than other colors.

In case of a histogram where peaks are to the right of the screen,
it means that the bright colors are more in number. 
"""

