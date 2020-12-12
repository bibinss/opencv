import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#1. paint the image to a color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)   

#2. paint a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)

#3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 0), thickness=-1)
cv.imshow('Circle', blank)

#4. draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 0), thickness=3)
cv.imshow('Line', blank)

#5. Add text
cv.putText(blank, 'Feedback', (250, 250), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)
cv.imshow('Text', blank)

cv.waitKey(0)
