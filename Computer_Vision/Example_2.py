#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:16:40 2020

@author: dsp
"""
# GRAYSCALING

import cv2

#load our input image 
image=cv2.imread('./images/input.jpg')
cv2.imshow('Original',image)
cv2.waitKey(0)

#use cvtColor to convert image to grayscale
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




