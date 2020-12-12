import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)