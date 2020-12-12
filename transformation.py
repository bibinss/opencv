import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

#1. translation
def translate(img, x, y):
    matx = np.float32([[1,0,x], [0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, matx, dimension)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


#2. rotation
def rotation(img, angle, rotPoint=None):
    (width,height) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMatx = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotMatx, dimension)

rotated = rotation(img, 45)
cv.imshow('Rotated', rotated)

#3. flip
flipped = cv.flip(img, -1)
cv.imshow('Flipped', flipped)

cv.waitKey(0)