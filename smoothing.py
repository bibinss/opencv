import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

blur = cv.blur(img, (7,7))
cv.imshow('Blurred', blur)

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gauss', gauss)

median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

cv.waitKey(0)