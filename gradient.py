import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)
cv.imshow('Sobel combined', sobel_combined)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)