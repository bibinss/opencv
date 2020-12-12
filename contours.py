import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)

# ret, thresh = cv.threshold(img, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contour', blank)

cv.waitKey(0)