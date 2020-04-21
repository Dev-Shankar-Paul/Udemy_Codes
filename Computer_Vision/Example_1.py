#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 02:13:29 2020

@author: dsp
"""

import cv2
import numpy as np

"""
Stating the location of the image...
The function imread() enables cv2 to open that particular image
and ready it for analysis
"""
input=cv2.imread('./images/input.jpg')  

"""
Displaying the image in a frame/window of its own...
The function imshow() enables cv2 to display that particular image
on a new and separate frame/window
"""
cv2.imshow('hello world',input)    

"""
waitKey() is used to wait for a key press from the keyboard. It can 
also be used as a delay. If we mention the time in miliseconds in 
the paranthesis, then we'll be able to stop and display the frame
for that amount of time
"""
cv2.waitKey()       

"""
The function destroyAllWindows() is used to close all the current
frames automatically
"""
cv2.destroyAllWindows()

"""
(Height, width)
"""
print(input.shape)

"""
save the image
"""
cv2.imwrite('output.jpg',input)    
