import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

# converting to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)

#dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

#cropping
cropped = resized[100:300, 200:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)